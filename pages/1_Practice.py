import os
import re
import difflib
import hashlib
import streamlit as st
from main import transcribe, speak, correct_sentence
from progress import add_xp, sidebar

st.set_page_config(page_title="SpeakUp Practice", page_icon="🎯")

SENTENCES = [
    "I am going to the market tomorrow morning.",
    "She doesn't like tea.",
    "Yesterday I went to school.",
    "Can you help me with my homework?",
    "I have been learning English for two years.",
]


def clean(text):
    return re.sub(r"[^a-z' ]", "", text.lower()).strip()


def clear_attempt():
    st.session_state.pr_hash = None
    st.session_state.pr_result = None


st.markdown(
    """
    <div style="text-align:center; padding: 0.5rem 0 1rem 0;">
        <h1 style="margin-bottom:0;">🎯 Practice</h1>
        <p style="margin-top:0; opacity:0.8;">
            Say it. See exactly what to fix. Hear why in Hinglish.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

if "i" not in st.session_state:
    st.session_state.i = 0
    st.session_state.tries = 0
if "pr_hash" not in st.session_state:
    clear_attempt()

i = st.session_state.i

# ---------- Finished screen ----------
if i >= len(SENTENCES):
    st.balloons()
    st.success("You finished all the sentences! 🎉")
    if st.button("Start again"):
        st.session_state.i = 0
        st.session_state.tries = 0
        clear_attempt()
        st.rerun()
    sidebar()
    st.stop()

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
        data = audio.getvalue()
        h = hashlib.md5(data).hexdigest()

        # Only call the APIs once per new recording
        if h != st.session_state.pr_hash:
            with open("recording.wav", "wb") as f:
                f.write(data)

            with st.spinner("Listening..."):
                heard = transcribe("recording.wav")

            heard_words = clean(heard).split()
            target_words = clean(target).split()
            matcher = difflib.SequenceMatcher(None, heard_words, target_words)
            score = matcher.ratio()

            mistakes = []
            for tag, i1, i2, j1, j2 in matcher.get_opcodes():
                if tag != "equal":
                    said = " ".join(heard_words[i1:i2]) or "(nothing)"
                    expected = " ".join(target_words[j1:j2]) or "(nothing)"
                    mistakes.append((said, expected))

            tip = None
            if mistakes:
                with st.spinner("Thinking..."):
                    tip = correct_sentence(heard, target)["explanation"]

            add_xp(25 if not mistakes else 5)
            st.session_state.pr_result = {
                "heard": heard, "score": score, "mistakes": mistakes, "tip": tip,
            }
            st.session_state.pr_hash = h

        r = st.session_state.pr_result
        if r:
            st.write(f"**You said:** {r['heard']}")
            st.progress(r["score"], text=f"Match: {int(r['score'] * 100)}%")

            if not r["mistakes"]:
                st.success("Perfect! 🔥  +25 XP")
                if st.button("Next sentence ➡️"):
                    st.session_state.i += 1
                    st.session_state.tries = 0
                    clear_attempt()
                    st.rerun()
            else:
                st.warning("Almost there! Check these parts:  (+5 XP for trying)")
                for said, expected in r["mistakes"]:
                    st.write(f"- You said **{said}**, try **{expected}**")
                st.info(f"💡 {r['tip']}")
                if st.button("Try again 🔁"):
                    st.session_state.tries += 1
                    clear_attempt()
                    st.rerun()

st.divider()
if st.button("Skip this sentence"):
    st.session_state.i += 1
    st.session_state.tries = 0
    clear_attempt()
    st.rerun()

sidebar()