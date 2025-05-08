# Multilingual AI Voice Assistant 🤖🌐

A Python-based multilingual personal assistant that combines voice recognition, language translation, AI response generation (using Gemini), and task execution to deliver a smooth, interactive experience for users in various languages.

---

## 🔧 Features

* 🎤 Voice-to-Text using Google Speech Recognition
* 🌍 Multilingual support (English, Hindi, Marathi, Spanish, French, German, etc.)
* 🤖 AI-powered responses using Gemini (Generative AI)
* 🔄 Auto language detection & translation (via Google Translate)
* 📢 Text-to-Speech with gTTS
* 🔧 Task automation: open apps, search Wikipedia, get weather, play music, take screenshots, system control
* 🌐 Real-time interaction through a Streamlit web interface

---

## 🛠 Technologies Used

* **Frontend/UI**: Streamlit
* **Backend**: Python
* **APIs & Libraries**:

  * Google Speech Recognition
  * Google Translate (via Deep Translator)
  * Gemini API (via `google.generativeai`)
  * gTTS (Google Text-to-Speech)
  * Wikipedia API, PyAutoGUI, NLTK
* **Environment Management**: dotenv
* **Voice Playback**: playsound

---

## 🚀 Installation & Setup



1. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file and add your Gemini API key:

   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

4. Run the app:

   ```bash
   streamlit run app.py
   ```

---

## 🧪 Testing

* Unit testing for core modules
* Manual testing of voice input/output, multilingual translation, and task execution
* Cross-platform and browser compatibility checked

---

## 📌 Future Scope

* Add GUI desktop app version
* Offline speech recognition
* More natural dialog flow using advanced NLP
* Integrate calendar, mail, and smart device control
* Extend support to more languages and accents

---


## 🙋‍♂️ Author

Developed by \[Shravani Chavan] 

---

