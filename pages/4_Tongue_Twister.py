import os
import re
import hashlib
import difflib
import streamlit as st
from main import transcribe, speak
from progress import add_xp, sidebar

st.set_page_config(page_title="SpeakUp Tongue Twisters", page_icon="🌀")

TWISTERS = [
    ("Easy", "She sells seashells by the seashore."),
    ("Easy", "Red lorry, yellow lorry."),
    ("Medium", "Fresh fried fish, fresh fried fish."),
    ("Medium", "Peter Piper picked a peck of pickled peppers."),
    ("Hard", "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"),
]


def clean(text):
    return re.sub(r"[^a-z' ]", "", text.lower()).strip()


def stars(score):
    if score >= 0.9:
        return 3
    if score >= 0.7:
        return 2
    if score >= 0.5:
        return 1
    return 0


# ---------- State ----------
if "tt_i" not in st.session_state:
    st.session_state.tt_i = 0
    st.session_state.tt_tries = 0
    st.session_state.tt_last_hash = None
    st.session_state.tt_result = None
    st.session_state.tt_best = {}

i = st.session_state.tt_i

# ---------- Header ----------
st.markdown(
    """
    <div style="text-align:center; padding: 0.5rem 0 1rem 0;">
        <h1 style="margin-bottom:0;">🌀 Tongue Twister Challenge</h1>
        <p style="margin-top:0; opacity:0.8;">
            Say it fast. Say it right. Collect the stars.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

total_stars = sum(st.session_state.tt_best.values())
st.progress(
    min(i, len(TWISTERS)) / len(TWISTERS),
    text=f"Twister {min(i + 1, len(TWISTERS))} of {len(TWISTERS)}   |   ⭐ {total_stars} / {3 * len(TWISTERS)}",
)

# ---------- Finished ----------
if i >= len(TWISTERS):
    st.balloons()
    st.success(f"All done! You collected ⭐ {total_stars} out of {3 * len(TWISTERS)} stars.")
    if st.button("Play again"):
        st.session_state.tt_i = 0
        st.session_state.tt_tries = 0
        st.session_state.tt_last_hash = None
        st.session_state.tt_result = None
        st.session_state.tt_best = {}
        st.rerun()
    st.stop()

level, target = TWISTERS[i]

# ---------- Twister card ----------
with st.container(border=True):
    st.caption(f"🎯 Level: {level}")
    st.subheader(target)
    path = f"twister_{i}.wav"
    if not os.path.exists(path):
        with st.spinner("Getting the voice ready..."):
            speak(target, path)
    st.audio(path)

# ---------- Your turn ----------
with st.container(border=True):
    st.caption("🎤 Your turn")
    audio = st.audio_input(
        "Tap the mic, say it, tap again to stop",
        key=f"tt_audio_{i}_{st.session_state.tt_tries}",
    )

    if audio:
        data = audio.getvalue()
        h = hashlib.md5(data).hexdigest()
        if h != st.session_state.tt_last_hash:
            with open("twister_recording.wav", "wb") as f:
                f.write(data)
            with st.spinner("Listening..."):
                heard = transcribe("twister_recording.wav")

            heard_words = clean(heard).split()
            target_words = clean(target).split()
            matcher = difflib.SequenceMatcher(None, heard_words, target_words)
            score = matcher.ratio()

            missed = []
            for tag, i1, i2, j1, j2 in matcher.get_opcodes():
                if tag != "equal":
                    missed.append((
                        " ".join(heard_words[i1:i2]) or "(nothing)",
                        " ".join(target_words[j1:j2]) or "(nothing)",
                    ))

            s = stars(score)
            best = st.session_state.tt_best.get(i, 0)
            st.session_state.tt_best[i] = max(best, s)
            if s > best:
                add_xp((s - best) * 10)
            st.session_state.tt_result = {
                "heard": heard, "score": score, "stars": s, "missed": missed,
            }
            st.session_state.tt_last_hash = h

        r = st.session_state.tt_result
        if r:
            st.write(f"**You said:** {r['heard']}")
            st.progress(r["score"], text=f"Match: {int(r['score'] * 100)}%")
            st.markdown(f"### {'⭐' * r['stars']}{'☆' * (3 - r['stars'])}")

            if r["stars"] == 3:
                st.balloons()
                st.success("Flawless! 🔥")
            elif r["missed"]:
                st.warning("Almost! Check these parts:")
                for said, expected in r["missed"]:
                    st.write(f"- You said **{said}**, try **{expected}**")

            c1, c2 = st.columns(2)
            with c1:
                if st.button("🔁 Try again"):
                    st.session_state.tt_tries += 1
                    st.session_state.tt_last_hash = None
                    st.session_state.tt_result = None
                    st.rerun()
            with c2:
                if st.button("Next twister ➡️"):
                    st.session_state.tt_i += 1
                    st.session_state.tt_tries = 0
                    st.session_state.tt_last_hash = None
                    st.session_state.tt_result = None
                    st.rerun()

st.divider()
if st.button("Skip this one"):
    st.session_state.tt_i += 1
    st.session_state.tt_tries = 0
    st.session_state.tt_last_hash = None
    st.session_state.tt_result = None
    st.rerun()