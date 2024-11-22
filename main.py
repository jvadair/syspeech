import speech_recognition as sr
import os
from faster_whisper import WhisperModel
from io import BytesIO
from pyntree import Node
from kbwriter import keywrite
from fastapi import FastAPI
config = Node("config.yaml")

r = sr.Recognizer()
print(sr.Microphone.list_microphone_names())
mic = sr.Microphone()
app = FastAPI()

whisper = WhisperModel(
    config.speech_recognition.model_size(),
    device=config.speech_recognition.device(),
    cpu_threads=config.speech_recognition.cpu_threads(),
    num_workers=config.speech_recognition.num_workers(),
    download_root=os.path.abspath("whisper_models"),
    local_files_only=False if config.speech_recognition.allow_downloads() else True
)


def listen():
    with mic as source:
        print("Listening...")
        recorded = r.listen(source)
        print("Recognizing...")
        segments, info = whisper.transcribe(BytesIO(recorded.get_wav_data()), beam_size=5, language="en",
                                            condition_on_previous_text=False)
        text = " ".join([segment.text for segment in segments]).replace("  ", " ")
        return text


@app.get("/transcribe")
async def transcribe():
    output = listen().lstrip()
    keywrite(output)

