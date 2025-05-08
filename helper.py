import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
import tempfile
import playsound
import pyautogui
import datetime
import subprocess
import wikipedia
import requests
from deep_translator import GoogleTranslator
from gtts import gTTS
from nltk.tokenize import word_tokenize
import nltk

nltk.download("punkt")
nltk.download("punkt_tab")

print("perfect!!")
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# Define supported languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Marathi": "mr",
}

task_keywords = {
    "open browser": ["browser", "chrome", "firefox", "internet"],
    "open youtube": ["youtube", "video", "watch"],
    "open google": ["google", "search"],
    "take screenshot": ["screenshot", "capture", "screen"],
    "open calculator": ["calculator", "calc"],
    "current time": ["time", "clock"],
    "current date": ["date", "day"],
    "weather": ["weather", "temperature", "forecast", "hawamaan", "tapman"],
    "shutdown": ["shutdown", "turn off"],
    "restart": ["restart", "reboot"],
    "log off": ["log off", "sign out"],
    "wikipedia": ["wikipedia", "wiki", "information"],
    "play music": ["music", "song", "play"],
}

def speak(text, lang="en"):
    """Convert text to speech and play it."""
    try:
        tts = gTTS(text=text, lang=lang)
        temp_audio_path = os.path.join(tempfile.gettempdir(), "temp_speech.mp3")
        tts.save(temp_audio_path)
        playsound.playsound(temp_audio_path, block=True)
        os.remove(temp_audio_path)
    except Exception as e:
        print(f"Error in speech synthesis: {e}")

def voice_input():
    """Capture voice input and return text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            return "Sorry, could not understand the audio."
        except sr.RequestError as e:
            return f"Could not request results: {e}"

def text_to_speech(text, lang="en"):
    """Convert text to speech and save it."""
    tts = gTTS(text=text, lang=lang)
    tts.save("speech.mp3")

def get_weather(city, target_lang="en"):
    """Fetch weather information for a given city and return it in the desired language."""
    
    API_KEY = "api-key"  # Replace with a valid API key
    url = f"your-url "
    
    try:
        # Translate city name to English if needed
        city_in_english = GoogleTranslator(source="auto", target="en").translate(city)
        
        # Fetch weather data
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_in_english}&appid={API_KEY}&units=metric").json()
        
        if response.get("main"):
            temp = response["main"]["temp"]
            weather_desc = response["weather"][0]["description"]
            weather_info = f"The temperature in {city} is {temp}°C with {weather_desc}."
            
            # Translate the weather response back to the user's language
            translated_response = GoogleTranslator(source="auto", target=target_lang).translate(weather_info)
            
            return translated_response
        else:
            return GoogleTranslator(source="auto", target=target_lang).translate("Sorry, I couldn't fetch the weather details.")
    
    except Exception as e:
        return GoogleTranslator(source="auto", target=target_lang).translate(f"Error fetching weather: {e}")

def detect_intent(command):
    """Detect user intent based on keywords."""
    words = word_tokenize(command)
    for task, keywords in task_keywords.items():
        if any(word in words for word in keywords):
            return task
    return None

def execute_task(intent, command):
    """Execute a specific command based on intent."""
    if intent == "open browser":
        subprocess.run("start chrome", shell=True)
        return "Opening browser..."
    
    elif intent == "open youtube":
        subprocess.run("start https://www.youtube.com", shell=True)
        return "Opening YouTube..."
    
    elif intent == "open google":
        subprocess.run("start https://www.google.com", shell=True)
        return "Opening Google..."
    
    elif intent == "take screenshot":
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        return "Screenshot taken."
    
    elif intent == "open calculator":
        subprocess.run("calc.exe", shell=True)
        return "Opening Calculator..."
    
    elif intent == "current time":
        return f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}."
    
    elif intent == "current date":
        return f"Today's date is {datetime.datetime.now().strftime('%A, %B %d, %Y')}."
    
    elif intent == "weather":
        city = command.split()[-1]  # Assume last word is the city name
        return get_weather(city)
    
    elif intent == "shutdown":
        os.system("shutdown /s /t 10")
        return "Shutting down in 10 seconds."
    
    elif intent == "restart":
        os.system("shutdown /r /t 10")
        return "Restarting in 10 seconds."
    
    elif intent == "log off":
        os.system("shutdown /l")
        return "Logging off."
    
    elif intent == "wikipedia":
        topic = command.replace("wikipedia", "").strip()
        if topic:
            try:
                summary = wikipedia.summary(topic, sentences=2)
                return f"According to Wikipedia: {summary}"
            except wikipedia.exceptions.PageError:
                return "Sorry, no results found."
        else:
            return "Please specify a topic."

    elif intent == "play music":
        os.startfile("C:/Users/Public/Music/Sample Music/song.mp3")  # Adjust path
        return "Playing music."

    else:
        return "I don't understand that command."

def llm_model_object(user_text, target_lang="en"):
    """Process text through LLM and return translated response."""
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-2.0-flash')
    
    translated_input = GoogleTranslator(source="auto", target="en").translate(user_text)
    
    response = model.generate_content(translated_input)
    result = response.text

    translated_output = GoogleTranslator(source="auto", target=target_lang).translate(result)
    
    return translated_output
