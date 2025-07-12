# 🤖 Voice & Text ChatBot with GUI

A simple Python chatbot that supports both **text input** and **voice interaction** using a Tkinter GUI. It recognizes basic commands, replies with text, and also speaks responses aloud.

---

## 📌 Features

- 🗨️ Text-based chat interface
- 🎤 Voice input via microphone (Speech Recognition)
- 🔊 Voice output (Text-to-Speech)
- 💬 Simple rule-based response logic
- 🧱 Clean, resizable GUI using Tkinter

---

## 🛠️ Tech Stack

- Python 3.x
- Tkinter (GUI)
- `speech_recognition` (Voice input)
- `pyttsx3` (Text-to-Speech)

---

## 📁 Project Structure

```
chatbot-project/
├── gui.py             # GUI logic and interaction
├── bot_logic.py       # Basic rule-based chatbot logic
├── audio.py           # Voice input/output functionality
├── send.png           # Send button icon
├── mic_icon.png       # Microphone icon
├── requirements.txt   # Dependencies list
└── README.md          # Project documentation
```

---

## ▶️ How to Run

1. **Install dependencies**

```bash
pip install -r requirements.txt
```

> ⚠️ Note: If you face errors installing `pyaudio`, run:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

2. **Run the application**

```bash
python main.py
```

3. **Interact with the chatbot** via:
- Typing a message and pressing **Enter**
- Clicking the **Send** button
- Clicking the **Mic** button to speak

---

## 💬 Sample Responses

| User Says            | Bot Replies                                        |
|----------------------|----------------------------------------------------|
| `Hello`              | Hi there! How can I assist you?                    |
| `What's the weather` | I can't fetch weather right now, but I'm here to chat! |
| `Exit`               | Goodbye!                                           |
| Anything else        | Working on it!                                     |

---

## 🧠 Features to Add

- NLP-based intent detection (using spaCy or transformers)
- Scrollable chat area
- Theme toggle (dark/light mode)
- Integration with real-time APIs (weather, news, etc.)
- Context-aware conversation memory

---

## 📦 requirements.txt

```txt
SpeechRecognition
pyttsx3~=2.98
pyaudio
tkinter
```

---


## 👤 Author

**Pratyaksh Agrawal**

---

## 📄 License

This project is open-source and free to use.

