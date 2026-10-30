import os
import re
import difflib
import hashlib
import streamlit as st
from main import transcribe, speak
from progress import complete_stage, stage_done, sidebar
from stages_content import STAGES, COMING_SOON, STAGE_XP, PASS_MARK, heard_has_word

st.set_page_config(page_title="SpeakUp Stages", page_icon="🪜")

TOTAL_STAGES = len(STAGES) + len(COMING_SOON)


def clean(text):
    return re.sub(r"[^a-z' ]", "", text.lower()).strip()


def audio_for(key, text):
    """Make the Timbre audio once, then reuse the saved file."""
    os.makedirs("stage_audio", exist_ok=True)
    path = os.path.join("stage_audio", f"{key}.wav")
    if not os.path.exists(path):
        with st.spinner("Getting the voice ready..."):
            speak(text, path)
    return path


def unlocked(n):
    return n == 1 or stage_done(n - 1)


def retry_quiz(n):
    """Runs when 'Try again' is clicked: gives the quiz a fresh set of empty answers."""
    key = f"stage_qa_{n}"
    st.session_state[key] = st.session_state.get(key, 0) + 1


st.markdown(
    """
    <div style="text-align:center; padding: 0.5rem 0 1rem 0;">
        <h1 style="margin-bottom:0;">🪜 Stages</h1>
        <p style="margin-top:0; opacity:0.8;">
            Start with a word. Build up to sentences, stories and emails.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------- The path ----------------
done_n = sum(1 for n in STAGES if stage_done(n))
st.progress(done_n / TOTAL_STAGES, text=f"{done_n} of {TOTAL_STAGES} stages completed")

with st.container(border=True):
    for n, S in STAGES.items():
        if stage_done(n):
            icon, note = "✅", "completed"
        elif unlocked(n):
            icon, note = "🔓", "open"
        else:
            icon, note = "🔒", f"finish Stage {n - 1} first"
        st.markdown(f"{icon} **Stage {n}: {S['title']}**  ({note})")
    for n, title in COMING_SOON:
        st.markdown(f"⏳ **Stage {n}: {title}**  (coming soon)")

# ---------------- Pick a stage ----------------
n = st.radio(
    "Choose a stage",
    list(STAGES.keys()),
    format_func=lambda i: f"Stage {i}: {STAGES[i]['title']}",
    horizontal=True,
    key="stage_pick",
)
S = STAGES[n]

if not unlocked(n):
    st.info(f"🔒 Stage {n} is locked. Pass the Stage {n - 1} quiz first to unlock it.")
else:
    st.caption(S["goal"] + ("  |  This stage: ✅ done" if stage_done(n) else ""))
    tab_learn, tab_say, tab_quiz = st.tabs(["📖 Learn", "🎤 Say it yourself", "📝 Quiz"])

    # ---------------- Learn ----------------
    with tab_learn:
        with st.container(border=True):
            st.subheader(f"Stage {n}: {S['title']}")
            st.write(S["rule"])
            for point in S["points"]:
                st.markdown(f"- {point}")

        st.markdown("#### Listen and learn")
        for i, item in enumerate(S["items"]):
            with st.container(border=True):
                c1, c2 = st.columns([4, 1])
                c1.markdown(f"**{item['en']}**")
                c1.caption(item["hi"])
                if item["ex"]:
                    c1.write(f"_{item['ex']}_")
                    c1.caption(item["ex_hi"])
                if c2.button("▶ Play", key=f"stplay_{n}_{i}"):
                    st.session_state[f"staud_{n}_{i}"] = audio_for(f"s{n}_item{i}", item["en"])
                path = st.session_state.get(f"staud_{n}_{i}")
                if path:
                    st.audio(path)

        if S.get("mistakes"):
            st.markdown("#### Common mistakes")
            for wrong, right in S["mistakes"]:
                st.write(f"❌ {wrong}   →   ✅ **{right}**")

    # ---------------- Say it yourself ----------------
    with tab_say:
        targets = S["say_it"]
        pick = st.selectbox(
            "Pick one to say",
            range(len(targets)),
            format_func=lambda i: targets[i],
            key=f"stpick_{n}",
        )
        target = targets[pick]

        with st.container(border=True):
            st.caption("🎯 Listen, then say it")
            st.subheader(target)
            st.audio(audio_for(f"s{n}_say{pick}", target))

        audio = st.audio_input(
            "Tap the mic, say it, tap again to stop",
            key=f"stsay_{n}_{pick}",
        )

        if audio:
            data = audio.getvalue()
            h = hashlib.md5(data).hexdigest()
            res_key = f"stres_{n}_{pick}"

            # Only call Prisma once per new recording
            if st.session_state.get(res_key + "_hash") != h:
                with open("stage_recording.wav", "wb") as f:
                    f.write(data)
                with st.spinner("Listening..."):
                    heard = transcribe("stage_recording.wav")

                if S["mode"] == "word":
                    ok = heard_has_word(heard, target)
                    result = {"heard": heard, "score": 1.0 if ok else 0.0, "diffs": [], "ok": ok}
                else:
                    heard_words = clean(heard).split()
                    target_words = clean(target).split()
                    matcher = difflib.SequenceMatcher(None, heard_words, target_words)
                    diffs = []
                    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
                        if tag != "equal":
                            diffs.append((
                                " ".join(heard_words[i1:i2]) or "(nothing)",
                                " ".join(target_words[j1:j2]) or "(nothing)",
                            ))
                    result = {"heard": heard, "score": matcher.ratio(), "diffs": diffs, "ok": not diffs}
                st.session_state[res_key] = result
                st.session_state[res_key + "_hash"] = h

            r = st.session_state.get(res_key)
            if r:
                st.write(f"**You said:** {r['heard']}")
                if S["mode"] != "word":
                    st.progress(r["score"], text=f"Match: {int(r['score'] * 100)}%")
                if r["ok"]:
                    st.success("Perfect! 🔥")
                else:
                    st.warning("Almost! Listen once more and try again.")
                    for said, expected in r["diffs"]:
                        st.write(f"- You said **{said}**, try **{expected}**")

    # ---------------- Quiz ----------------
    with tab_quiz:
        if stage_done(n):
            st.success("You've completed this stage ✅  You can retake the quiz any time (XP is given once).")

        attempt = st.session_state.get(f"stage_qa_{n}", 0)

        with st.form(f"stquiz_{n}_{attempt}"):
            answers = []
            for q_i, q in enumerate(S["quiz"]):
                answers.append(
                    st.radio(
                        f"{q_i + 1}. {q['q']}",
                        q["options"],
                        index=None,
                        key=f"stq_{n}_{attempt}_{q_i}",
                    )
                )
            submitted = st.form_submit_button("Check answers")

        if submitted:
            if any(a is None for a in answers):
                st.warning("Please answer every question first.")
            else:
                score = 0
                for q_i, (q, a) in enumerate(zip(S["quiz"], answers)):
                    correct = q["options"][q["answer"]]
                    if a == correct:
                        score += 1
                        st.success(f"{q_i + 1}. Correct ✅  {q['why']}")
                    else:
                        st.error(f"{q_i + 1}. Not quite ❌  Correct answer: **{correct}**. {q['why']}")

                st.markdown(f"### Score: {score} / {len(S['quiz'])}")
                if score >= PASS_MARK:
                    if complete_stage(n, STAGE_XP):
                        st.balloons()
                        msg = f"Stage {n} complete! +{STAGE_XP} XP 🎉"
                        if n + 1 in STAGES:
                            msg += f"  Stage {n + 1} is now unlocked."
                        st.success(msg)
                    else:
                        st.success("Great work! (You already earned XP for this stage.)")
                else:
                    st.info(f"You need {PASS_MARK} correct to finish the stage. Go back to Learn and try again.")

                st.button(
                    "🔁 Try again",
                    key=f"stretry_{n}_{attempt}",
                    on_click=retry_quiz,
                    args=(n,),
                )

sidebar()
