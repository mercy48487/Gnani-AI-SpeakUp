import streamlit as st

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

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader("🎯 Practice")
        st.write("Hear a sentence, say it back, and see exactly which words to fix.")
        st.page_link("pages/1_Practice.py", label="Start practicing", icon="➡️")

with col2:
    with st.container(border=True):
        st.subheader("🗣️ Hinglish to English")
        st.write("Say it your way and hear how to say it in English.")
        st.page_link("pages/2_Hinglish.py", label="Try it", icon="➡️")

st.divider()
st.caption(
    "Voice powered by Gnani Prisma (speech-to-text) and Gnani Timbre (text-to-speech). "
    "Feedback generated with Gemini."
)