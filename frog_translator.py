import random
import os
import speech_recognition as sr
from pydub import AudioSegment

try:
    import pygame
    pygame.init()
    PLAY_SOUND = True
except ImportError:
    PLAY_SOUND = False

FROG_NOISES = ["ribbit", "croak", "boing", "gribbit", "bloop"]
FROG_EMOTIONS = {
    "hello": "ribbit",
    "hi": "croak",
    "yes": "boing",
    "no": "gribbit",
    "wow": "bloop"
}
FROG_FACTS = [
    "A group of frogs is called an army.",
    "Frogs absorb water through their skin.",
    "There are over 7,000 frog species!",
    "Some frogs can jump over 20 times their own body length!",
    "Frogs don’t drink water, they soak it in through their skin!"
]

def convert_to_wav(path):
    audio = AudioSegment.from_file(path)
    wav_path = "temp_converted.wav"
    audio = audio.set_frame_rate(16000).set_channels(1).set_sample_width(2)
    audio.export(wav_path, format="wav")
    return wav_path

def play_audio(path):
    try:
        if not path.lower().endswith((".wav", ".mp3")):
            print("⚠️ Only .wav or .mp3 files are supported for playback.")
            return
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
    except Exception as e:
        print("⚠️ Could not play sound:", e)

def frogify_word(word):
    lw = word.lower()
    if lw in FROG_EMOTIONS:
        return FROG_EMOTIONS[lw]
    if random.random() < 0.3:
        return random.choice(FROG_NOISES)
    return word

def frogify_sentence(sentence):
    words = sentence.split()
    frog_words = [frogify_word(word) for word in words]
    count = sum(1 for a, b in zip(words, frog_words) if a != b)
    print(f"🐸 Frog noises inserted: {count}")
    return ' '.join(frog_words)

def generate_gibberish(length):
    return ' '.join(random.choice(FROG_NOISES) for _ in range(length))

def translate_audio(file_path):
    recognizer = sr.Recognizer()
    try:
        wav_file = convert_to_wav(file_path)
        with sr.AudioFile(wav_file) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
            print("🐸 Recognized speech:", text)
            return frogify_sentence(text)
    except Exception:
        print("⚠️ Could not understand audio, generating frog gibberish instead.")
        return generate_gibberish(10)


def main():
    print("🐸 Welcome to Frog Translator (Text or Audio Edition)! 🐸")

    while True:
        mode = input("\nEnter mode ('text', 'audio', or 'exit'): ").lower()

        if mode == 'exit' or mode == '0':
            print("Bye bye 🐸 Did you know? " + random.choice(FROG_FACTS))
            break

        elif mode == 'text':
            text = input("Enter your text: ")
            print("Frogified 🐸:", frogify_sentence(text))

        elif mode == 'audio':
            file_path = input("Enter the path to your audio file: ")
            if not os.path.exists(file_path):
                print("❌ File not found.")
                continue
            if PLAY_SOUND:
                play_audio(file_path)
            print("Frogified from audio 🐸:", translate_audio(file_path))

        else:
            print("Invalid option. Please type 'text', 'audio', or 'exit'.")

if __name__ == "__main__":
    main()
