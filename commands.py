import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

def process_command(command, talk):
    """Handle recognized commands."""
    command = command.lower().strip()

    if command.startswith('play '):
        song = command.replace('play', '', 1).strip()
        if song:
            talk(f"Playing {song}")
            pywhatkit.playonyt(song)
        else:
            talk("Please tell me what to play.")

    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The time is {current_time}")

    elif command.startswith('who is'):
        try:
            person = command.replace('who is', '', 1).strip()
            if person:
                info = wikipedia.summary(person, 1)
                talk(info)
            else:
                talk("Please tell me who you want to know about.")
        except:
            talk("Sorry, I couldn't find information.")

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)

    elif command.startswith('google '):
        query = command.replace('google', '', 1).strip()
        talk(f"Searching Google for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif command.startswith('youtube '):
        query = command.replace('youtube', '', 1).strip()
        talk(f"Searching YouTube for {query}")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

    elif 'bye' in command or 'exit' in command:
        talk("Goodbye! Have a nice day.")
        quit()

    else:
        talk("I didn't understand that. Please try again.")