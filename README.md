# 🐸 Frog Translator: Text & Audio Edition

A completely serious and extremely necessary tool that translates human language into Frog Speak™. Whether you type it or yell it into a mic, this frog is ready to ribbit, croak, or boing on command.

---

## 💡 Features

- 📝 **Text Translation**: Converts your input text into delightful frog gibberish.
- 🎧 **Audio Translation**: Takes `.wav` or `.mp3` files, deciphers your speech, and frogifies it.
- 🐸 **Frog Noises**: Randomized and emotion-mapped frog noises like `ribbit`, `croak`, and more.
- 🎲 **Frog Facts**: Learn something weirdly frog-related when you exit.
- 🏷️ **No guarantee to correctly translate it**: Maybe one day this could work. Who knows.

---

## 📦 Requirements

Install required packages:
```bash
pip install SpeechRecognition pygame
```
> **Note**: `pygame` is used for reliable cross-platform audio playback.

---

## 🚀 Usage

```bash
python frog_translator.py
```

### Modes
- `text` – Enter a sentence to frogify.
- `audio` – Give the path to a `.wav` or `.mp3` audio file and hear frog magic.
- `exit` – Quit the translator (a frog fact will reward you).

---

## 🐸 Examples

### Text Mode
```
Enter mode ('text', 'audio', or 'exit'): text
Enter your text: Hello, how are you today?
Frogified 🐸: Hello, ribbit croak you croak?
```

### Audio Mode
```
Enter mode ('text', 'audio', or 'exit'): audio
Enter the path to your audio file: myvoice.wav
🐸 Recognized speech: this is a test
Frogified from audio 🐸: this ribbit a gribbit
```

If recognition fails:
```
⚠️ Could not understand audio, generating frog gibberish instead.
Frogified from audio 🐸: ribbit boing croak gribbit bloop ribbit
```

---

## 🧪 Dev Tip
To preview audio before translating, install `pygame` for playback support. WAV/MP3 only.

---

## 🐸 Frog Out!
