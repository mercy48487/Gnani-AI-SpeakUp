import streamlit as st
from main import generate_json, transcribe, speak
from progress import add_xp, sidebar

st.set_page_config(page_title="SpeakUp Tone Switch", page_icon="🎭")

TONES = [
    ("casual", "😎 Casual", "To a friend"),
    ("polite", "🙏 Polite", "To a teacher or elder"),
    ("professional", "💼 Professional", "To a manager or in an email"),
]


def tone_versions(text):
    prompt = f"""You help Indian learners sound right in every situation.
The learner said: "{text}"

Write the same message in English in three tones, keeping the meaning:
- casual: how you would say it to a friend
- polite: how you would say it to a teacher or an elder
- professional: how you would say it to a manager or in a work email

Reply ONLY with JSON in this format:
{{"casual": "...", "polite": "...", "professional": "...",
  "tip": "one short, friendly line in simple Hinglish (Hindi written in English letters) on when to use each tone"}}"""
    return generate_json(prompt)


# ---------- State ----------
if "tn" not in st.session_state:
    st.session_state.tn = 0
    st.session_state.last_hash = None
    st.session_state.data = None
    st.session_state.audio = {}

# ---------- Header ----------
st.markdown(
    """
    <div style="text-align:center; padding: 0.5rem 0 1rem 0;">
        <h1 style="margin-bottom:0;">🎭 Tone Switch</h1>
        <p style="margin-top:0; opacity:0.8;">
            Same message. Three ways to say it.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- Recorder ----------
with st.container(border=True):
    st.caption("🎤 Say something in Hinglish or English")
    audio = st.audio_input(
        "Tap the mic, speak, tap again to stop",
        key=f"tone_audio_{st.session_state.tn}",
    )

    if audio:
        data = audio.getvalue()
        h = hash(data)
        if h != st.session_state.last_hash:
            with open("tone_recording.wav", "wb") as f:
                f.write(data)
            with st.spinner("Listening..."):
                heard = transcribe("tone_recording.wav")
            with st.spinner("Finding the right tones..."):
                versions = tone_versions(heard)
            st.session_state.data = {"heard": heard, **versions}
            st.session_state.audio = {}
            st.session_state.last_hash = h
            add_xp(10)

# ---------- Results ----------
d = st.session_state.data
if d:
    st.write(f"**You said:** {d['heard']}")
    cols = st.columns(3)
    for col, (key, label, who) in zip(cols, TONES):
        with col:
            with st.container(border=True):
                st.markdown(f"**{label}**")
                st.caption(who)
                st.write(d[key])
                if st.button("▶ Play", key=f"play_{key}_{st.session_state.tn}"):
                    path = f"tone_{st.session_state.tn}_{key}.wav"
                    with st.spinner("Preparing the voice..."):
                        speak(d[key], path)
                    st.session_state.audio[key] = path
                if key in st.session_state.audio:
                    st.audio(st.session_state.audio[key])

    st.info(f"💡 {d['tip']}")

    if st.button("🎤 Speak again"):
        st.session_state.tn += 1
        st.session_state.last_hash = None
        st.session_state.data = None
        st.session_state.audio = {}
        st.rerun()
        sidebar()