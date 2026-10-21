import streamlit as st
from main import transcribe, correct_sentence, speak

st.title("SpeakUp 🎙️")
st.write("Speak an English sentence. Get it corrected, explained in Hinglish, and hear the right version.")

audio = st.audio_input("Tap the mic and speak")

if audio:
    with open("recording.wav", "wb") as f:
        f.write(audio.getvalue())

    with st.spinner("Listening..."):
        heard = transcribe("recording.wav")
    st.subheader("You said")
    st.write(heard)

    with st.spinner("Checking your English..."):
        result = correct_sentence(heard)
    st.subheader("Better way to say it")
    st.write(result["corrected"])
    st.info(result["explanation"])

    speak(result["corrected"])
    st.audio("feedback.wav")