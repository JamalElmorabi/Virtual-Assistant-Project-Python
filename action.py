import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather

def action(data):
    user_data = data.lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is virtual assistant")
        return "My name is virtual assistant"

    elif "hello" in user_data or "hi" in user_data:
        text_to_speech.text_to_speech("Hello, how can I help you?")
        return "Hello, how can I help you?"

    elif "good morning" in user_data:
        text_to_speech.text_to_speech("Good morning")
        return "Good morning"

    elif "time" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time.hour) + " : " + (str)(current_time.minute)
        text_to_speech.text_to_speech(Time)
        return Time

    elif "shut down" in user_data:
        text_to_speech.text_to_speech("Ok sir, shutting down")
        return "Ok sir, shutting down"

    elif "spotify" in user_data:
        webbrowser.open("https://open.spotify.com")
        text_to_speech.text_to_speech("Opening spotify for you")
        return "Opening spotify for you"

    elif "youtube" in user_data:
        webbrowser.open("https://youtube.com")
        text_to_speech.text_to_speech("Opening youtube for you")
        return "Opening youtube for you"

    elif "google" in user_data:
        webbrowser.open("https://google.com")
        text_to_speech.text_to_speech("Opening google for you")
        return "Opening google for you"

    elif "weather" in user_data:
        ans = weather.weather()
        text_to_speech.text_to_speech(ans)
        return ans

    else:
        text_to_speech.text_to_speech("I'm not able to understand")
        return "I'm not able to understand"