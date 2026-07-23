# 🤖 Jarvis - Python Voice Assistant

A simple voice-controlled virtual assistant built with Python that can recognize voice commands, respond using text-to-speech, open websites, play music from a predefined playlist, open spotify and perform websearch on google.

---

## ✨ Features

- 🎙️ Wake word detection ("Hello")
- 🔊 Text-to-Speech responses using `pyttsx3`
- 🌐 Open popular websites using voice commands
- 🔍 Search anything on Google
- 🎵 Play music from a custom `music.txt` playlist
- 🎤 Speech recognition using Google's Speech Recognition API
- ⚡ Lightweight and beginner-friendly project

---

## 🛠️ Technologies Used

- Python 3.12+
- SpeechRecognition
- PyAudio
- pyttsx3
- Webbrowser (built-in)
- Setuptools

---

## 📂 Project Structure

```
Jarvis/
│
├── main.py              # Main voice assistant
├── music.txt            # Music playlist (song names & links)
├── requirements.txt     # Python dependencies
└── README.md
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Jarvis.git
cd Jarvis
```

### 2. Create a virtual environment (Recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install SpeechRecognition
pip install PyAudio
pip install pyttsx3
pip install setuptools
```

Or

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

```bash
python main.py
```

Jarvis will initialize and begin listening for the wake word.

---

## 🎤 Voice Commands

### Wake Word

```
Hello
```

After detecting the wake word, Jarvis waits for your command.

---

### Open Websites

```
Open Google
Open YouTube
Open GitHub
Open Wikipedia
Open instagram
```

Jarvis automatically opens the requested website in your default browser.

---

### Play Music

Example:

```
Play Believer

Play Shape of You

Play Faded
```

Jarvis reads the song link from `music.txt` and opens it in your browser.

---

## 🎵 music.txt Format

Store songs in the following format:

```
Believer=https://youtu.be/7wtfhZwyrcc

Faded=https://youtu.be/60ItHLz5WEA

Shape of You=https://youtu.be/JGwWNGJdvx8
```

Jarvis matches the spoken song name with the corresponding link.

---

### Google Search

Examples:

```
Search Python decorators

Search weather today

Search IIIT Sonipat
```

Jarvis opens Google with the search query.

---

## 📋 Example Session

```
You: Hello

Jarvis: Yes

You: Open GitHub

➡ Opens https://github.com
```

```
You: Hello

Jarvis: Yes

You: Play Believer

➡ Opens the song from music.txt
```

---

## 🔮 Future Improvements

- Weather updates
- News headlines
- ChatGPT integration
- AI conversation mode
- System controls (shutdown, restart, sleep)
- Email sending
- WhatsApp messaging
- Notes and reminders
- Application launcher
- Volume and brightness controls
- Face recognition login
- Offline speech recognition
- Better natural language understanding

---

## ⚠️ Limitations

- Requires an active internet connection for speech recognition.
- Website opening works best for supported website names.
- Speech recognition accuracy depends on microphone quality and background noise.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a Pull Request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Arpit Singh Chauhan**

B.Tech CSE (Data Science & Analytics)

Indian Institute of Information Technology (IIIT) Sonipat

---

⭐ If you found this project useful, consider giving it a star on GitHub!
