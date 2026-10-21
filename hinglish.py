import json
import hashlib
import streamlit as st
from main import client, MODEL, transcribe, speak

st.set_page_config(page_title="SpeakUp Hinglish", page_icon="🗣️")


def to_english(text):
    prompt = f"""You help Indian learners say things in English.
The learner said this in Hinglish or Hindi: "{text}"

Reply ONLY with JSON in this format:
{{"english": "natural, correct English version with proper capitalization and punctuation",
  "tip": "one short, friendly tip in simple Hinglish (Hindi written in English letters) about how to say it in English"}}"""
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config={"response_mime_type": "application/json"},
    )
    return json.loads(response.text)


# ---------- State ----------
if "n" not in st.session_state:
    st.session_state.n = 0
    st.session_state.last_hash = None
    st.session_state.result = None
    st.session_state.history = []

# ---------- Header ----------
st.markdown(
    """
    <div style="text-align:center; padding: 0.5rem 0 1rem 0;">
        <h1 style="margin-bottom:0;">🗣️ Hinglish to English</h1>
        <p style="margin-top:0; opacity:0.8;">
            Say it your way. Hear how to say it in English.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- Recorder card ----------
with st.container(border=True):
    st.caption("🎤 Say anything in Hinglish")
    audio = st.audio_input(
        "Tap the mic, speak, tap again to stop",
        key=f"hing_audio_{st.session_state.n}",
    )

    if audio:
        data = audio.getvalue()
        h = hashlib.md5(data).hexdigest()

        # Only call the APIs once per new recording
        if h != st.session_state.last_hash:
            with open("hinglish_recording.wav", "wb") as f:
                f.write(data)

            with st.spinner("Listening..."):
                heard = transcribe("hinglish_recording.wav")

            with st.spinner("Finding the English..."):
                out = to_english(heard)

            out_path = f"hinglish_feedback_{len(st.session_state.history)}.wav"
            with st.spinner("Getting the voice ready..."):
                speak(out["english"], out_path)

            st.session_state.result = {
                "heard": heard,
                "english": out["english"],
                "tip": out["tip"],
                "audio_path": out_path,
            }
            st.session_state.history.append(st.session_state.result)
            st.session_state.last_hash = h

        r = st.session_state.result
        if r:
            st.write(f"**You said:** {r['heard']}")
            st.success(f"**In English:** {r['english']}")
            st.info(f"💡 {r['tip']}")
            st.audio(r["audio_path"])

            if st.button("🎤 Speak again"):
                st.session_state.n += 1
                st.session_state.last_hash = None
                st.session_state.result = None
                st.rerun()

# ---------- History ----------
if st.session_state.history:
    with st.expander(f"📜 Your sentences so far ({len(st.session_state.history)})"):
        for item in reversed(st.session_state.history):
            st.write(f"**{item['heard']}**  →  {item['english']}")