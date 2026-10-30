import streamlit as st
from progress import sidebar

st.set_page_config(page_title="SpeakUp", page_icon="🎙️")

st.markdown(
    """
    <div style="text-align:center; padding: 1rem 0 0.5rem 0;">
        <h1 style="font-size:3rem; margin-bottom:0;">🎙️ SpeakUp</h1>
        <p style="font-size:1.2rem; opacity:0.8;">
            Your Hinglish-friendly English speaking coach
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

MODES = [
    ("🎯 Practice", "Repeat a sentence. See exactly which words to fix, and why, in Hinglish.", "pages/1_Practice.py", "Start practicing"),
    ("🗣️ Hinglish to English", "Say it your way. Hear it in clear English.", "pages/2_Hinglish.py", "Try it"),
    ("🎭 Tone Switch", "One message, three tones: casual, polite and professional.", "pages/3_Tone_Switch.py", "Switch tones"),
    ("🌀 Tongue Twisters", "Say it fast and right. Collect stars.", "pages/4_Tongue_Twister.py", "Take the challenge"),
    ("📘 Grammar Book", "Short Hinglish lessons, quizzes, and a section of common exceptions.", "pages/5_Grammar_Book.py", "Open the book"),
    ("🪜 Stages", "Start with a word. Build up to phrases and sentences, step by step.", "pages/6_Stages.py", "Start Stage 1"),
]

for i in range(0, len(MODES), 2):
    cols = st.columns(2)
    for col, (title, desc, page, label) in zip(cols, MODES[i:i + 2]):
        with col:
            with st.container(border=True):
                st.subheader(title)
                st.write(desc)
                st.page_link(page, label=label, icon="➡️")

st.divider()
st.caption(
    "Voice powered by Gnani Prisma (speech-to-text) and Gnani Timbre (text-to-speech). "
    "Feedback generated with Gemini."
)

sidebar()
