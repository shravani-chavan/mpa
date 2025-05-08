import streamlit as st
from src.helper import voice_input, llm_model_object, text_to_speech, detect_intent, execute_task, languages

def main():
    st.title("Multilingual AI Assistant 🤖")

    lang = st.selectbox("Select Language", list(languages.keys()))
    target_lang = languages[lang]

    if st.button("Ask me anything"):
        with st.spinner("Listening..."):
            text = voice_input()
            
            if text:
                st.text_area("Your Input:", value=text, height=100, disabled=True)

                intent = detect_intent(text)
                if intent:
                    response = execute_task(intent, text)
                else:
                    response = llm_model_object(text, target_lang)

                text_to_speech(response, target_lang)

                audio_file = "speech.mp3"
                audio_bytes = open(audio_file, "rb").read()

                st.text_area(label="Response:", value=response, height=350, disabled=True)

                # Automatically play audio
                st.audio(audio_bytes, format="audio/mp3", autoplay=True)

                st.download_button("Download Speech", data=audio_bytes, file_name="speech.mp3", mime="audio/mp3")

if __name__ == '__main__':
    main()
