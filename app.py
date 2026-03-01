import tkinter as tk
from tkinter import scrolledtext
import threading
import speech_recognition as sr
import pyttsx3
import pyaudio  
from commands import process_command

# Initialize recognizer & TTS
listener = sr.Recognizer()
engine = pyttsx3.init()

# Voice setup
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    """Speak text and show in GUI."""
    text_area.insert(tk.END, "Assistant: " + text + "\n")
    text_area.see(tk.END)
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    """Recognize voice and process command."""
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source)
        talk("Listening...")
        try:
            audio = listener.listen(source, timeout=5, phrase_time_limit=8)
            command = listener.recognize_google(audio).lower()
            text_area.insert(tk.END, "You: " + command + "\n")
            process_command(command, talk)
        except sr.UnknownValueError:
            talk("Sorry, I could not understand.")
        except sr.RequestError:
            talk("Please check your internet connection.")
        except Exception as e:
            talk(f"Error: {str(e)}")

def start_listening():
    """Run speech recognition in a thread."""
    threading.Thread(target=recognize_speech, daemon=True).start()

# Tkinter UI
window = tk.Tk()
window.title("Voice Assistant")

text_area = scrolledtext.ScrolledText(window, width=50, height=15, wrap=tk.WORD)
text_area.pack(padx=10, pady=10)

button = tk.Button(window, text="🎤 Start Listening", command=start_listening)
button.pack(pady=5)

window.mainloop()