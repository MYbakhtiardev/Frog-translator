import random
import os
import speech_recognition as sr

FROG_NOISES = ["ribbit", "croak", "boing", "gribbit", "bloop"]

def frogify_word(word):
    if random.random() < 0.3:
        return random.choice(FROG_NOISES)
    return word

def frogify_sentence(sentence):
    words = sentence.split()
    frog_words = [frogify_word(word) for word in words]
    return ' '.join(frog_words)

def generate_gibberish(length):
    """Generates fake frog speech of about the same length."""
    return ' '.join(random.choice(FROG_NOISES) for _ in range(length))

def translate_audio(file_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
            print("🐸 Recognized speech:", text)
            return frogify_sentence(text)
    except Exception as e:
        print("⚠️ Could not understand audio, generating frog gibberish instead.")
        return generate_gibberish(10)

def main():
    print("🐸 Welcome to Frog Translator (Text or Audio Edition)! 🐸")

    while True:
        mode = input("\nEnter mode ('text', 'audio', or 'exit'): ").lower()

        if mode == 'exit':
            print("Bye bye 🐸")
            break

        elif mode == 'text':
            text = input("Enter your text: ")
            print("Frogified 🐸:", frogify_sentence(text))

        elif mode == 'audio':
            file_path = input("Enter the path to your audio file: ")
            if not os.path.exists(file_path):
                print("❌ File not found.")
                continue
            print("Frogified from audio 🐸:", translate_audio(file_path))

        else:
            print("Invalid option. Please type 'text', 'audio', or 'exit'.")

if __name__ == "__main__":
    main()
