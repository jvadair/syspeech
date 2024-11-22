# Syspeech
Syspeech is a system-wide speech-to-text application for Linux-based operating systems based on Whisper, primarily targeting Ubuntu 24.
It is (to my knowledge), the first and only system-wide speech-to-text program to work with Wayland.
### Roadmap
Syspeech is currently in an early development stage. In the future, I would like to:
- Run the event listener as a systemd service (and maybe also use something other than Flask to listen for events)
- Provide a proper and unified method of installation
- Create an appindicator (This has proven to be incredibly challenging on Ubuntu 24)
### "Installing"
1. Clone this repo
2. Set allow_downloads to `true` in the config.yaml
3. Run main.py
4. Set allow_downloads to `false` in the config.yaml, unless you want to allow Hugging Face models to be downloaded sometimes.
5. "Install" `transcribe.py` in your preferred manner. You can modify my sample `syspeech.desktop` file and move it to
`~/.local/share/applications` or similar, or you can add a hashbang to the top of the file and put in on PATH somewhere - it's up to you.