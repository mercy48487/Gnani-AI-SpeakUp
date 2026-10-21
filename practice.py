import os
import re
import difflib
import streamlit as st
from main import transcribe, speak, correct_sentence

st.set_page_config(page_title="SpeakUp", page_icon="🎙️")

SENTENCES = [
    "I am going to the market tomorrow morning.",
    "She doesn't like tea.",
    "Yesterday I went to school.",
    "Can you help me with my homework?",
    "I have been learning English for two years.",
]


def clean(text):
    return re.sub(r"[^a-z' ]", "", text.lower()).strip()


# ---------- Header ----------
st.markdown(
    """
    <div style="text-align:center; padding: 0.5rem 0 1rem 0;">
        <h1 style="margin-bottom:0;">🎙️ SpeakUp</h1>
        <p style="margin-top:0; opacity:0.8;">
            Speak English with confidence. Get feedback in Hinglish.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

if "i" not in st.session_state:
    st.session_state.i = 0
    st.session_state.tries = 0

i = st.session_state.i

# ---------- Finished screen ----------
if i >= len(SENTENCES):
    st.balloons()
    st.success("You finished all the sentences! 🎉")
    if st.button("Start again"):
        st.session_state.i = 0
        st.session_state.tries = 0
        st.rerun()
    st.stop()

# ---------- Progress ----------
st.progress(i / len(SENTENCES), text=f"Sentence {i + 1} of {len(SENTENCES)}")

target = SENTENCES[i]

# ---------- Target sentence card ----------
with st.container(border=True):
    st.caption("🎯 Say this sentence")
    st.subheader(target)
    target_path = f"target_{i}.wav"
    if not os.path.exists(target_path):
        speak(target, target_path)
    st.audio(target_path)

# ---------- Your turn card ----------
with st.container(border=True):
    st.caption("🎤 Your turn")
    audio = st.audio_input(
        "Tap the mic, say it, tap again to stop",
        key=f"audio_{i}_{st.session_state.tries}",
    )

    if audio:
        with open("recording.wav", "wb") as f:
            f.write(audio.getvalue())

        with st.spinner("Listening..."):
            heard = transcribe("recording.wav")

        heard_words = clean(heard).split()
        target_words = clean(target).split()
        matcher = difflib.SequenceMatcher(None, heard_words, target_words)
        score = matcher.ratio()

        st.write(f"**You said:** {heard}")
        st.progress(score, text=f"Match: {int(score * 100)}%")

        mistakes = []
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag != "equal":
                said = " ".join(heard_words[i1:i2]) or "(nothing)"
                expected = " ".join(target_words[j1:j2]) or "(nothing)"
                mistakes.append((said, expected))

        if not mistakes:
            st.balloons()
            st.success("Perfect! 🔥")
            if st.button("Next sentence ➡️"):
                st.session_state.i += 1
                st.session_state.tries = 0
                st.rerun()
        else:
            st.warning("Almost there! Check these parts:")
            for said, expected in mistakes:
                st.write(f"- You said **{said}**, try **{expected}**")
            with st.spinner("Thinking..."):
                tip = correct_sentence(heard, target)
            st.info(f"💡 {tip['explanation']}")
            if st.button("Try again 🔁"):
                st.session_state.tries += 1
                st.rerun()

st.divider()
if st.button("Skip this sentence"):
    st.session_state.i += 1
    st.session_state.tries = 0
    st.rerun()