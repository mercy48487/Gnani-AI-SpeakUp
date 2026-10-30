import os
import re
import difflib
import hashlib
import streamlit as st
from main import transcribe, speak
from progress import complete_lesson, lesson_done, sidebar
from grammar_content import LESSONS, EXCEPTIONS, PASS_MARK, LESSON_XP

st.set_page_config(page_title="SpeakUp Grammar Book", page_icon="📘")


def clean(text):
    return re.sub(r"[^a-z' ]", "", text.lower()).strip()


def audio_for(key, text):
    """Make the Timbre audio once, then reuse the saved file."""
    os.makedirs("grammar_audio", exist_ok=True)
    path = os.path.join("grammar_audio", f"{key}.wav")
    if not os.path.exists(path):
        with st.spinner("Getting the voice ready..."):
            speak(text, path)
    return path


def retry_quiz(lesson_id):
    """Runs when 'Try again' is clicked: gives the quiz a fresh set of empty answers."""
    key = f"qa_{lesson_id}"
    st.session_state[key] = st.session_state.get(key, 0) + 1


def topic_text(t):
    """All the searchable text of an exception topic."""
    parts = [t["title"], t["rule"], t.get("note", "")]
    if t.get("table"):
        parts += t["table"]["headers"]
        for row in t["table"]["rows"]:
            parts += row
    for wrong, right in t.get("mistakes", []):
        parts += [wrong, right]
    for en, hi in t["examples"]:
        parts += [en, hi]
    return " ".join(parts).lower()


st.markdown(
    """
    <div style="text-align:center; padding: 0.5rem 0 1rem 0;">
        <h1 style="margin-bottom:0;">📘 Grammar Book</h1>
        <p style="margin-top:0; opacity:0.8;">
            Short lessons. Hinglish explanations. Say it out loud.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

section_lessons, section_exceptions = st.tabs(["📖 Lessons", "⚠️ Exceptions"])

# =====================================================================
# LESSONS
# =====================================================================
with section_lessons:
    ids = list(LESSONS.keys())
    lid = st.selectbox(
        "Choose a lesson",
        ids,
        format_func=lambda i: LESSONS[i]["title"],
        key="gb_lesson",
    )
    L = LESSONS[lid]
    done_count = sum(1 for i in ids if lesson_done(i))
    st.caption(
        f"✅ {done_count} of {len(ids)} lessons completed"
        + ("  |  This lesson: ✅ done" if lesson_done(lid) else "")
    )

    tab_learn, tab_say, tab_quiz = st.tabs(["📖 Learn", "🎤 Say it yourself", "📝 Quiz"])

    # ---------------- Learn ----------------
    with tab_learn:
        with st.container(border=True):
            st.subheader(L["title"])
            st.write(L["rule"])
            for point in L["points"]:
                st.markdown(f"- {point}")

        st.markdown("#### Examples")
        for n, (english, hinglish) in enumerate(L["examples"]):
            with st.container(border=True):
                c1, c2 = st.columns([4, 1])
                c1.markdown(f"**{english}**")
                c1.caption(hinglish)
                if c2.button("▶ Play", key=f"play_{lid}_{n}"):
                    st.session_state[f"aud_{lid}_{n}"] = audio_for(f"{lid}_ex{n}", english)
                path = st.session_state.get(f"aud_{lid}_{n}")
                if path:
                    st.audio(path)

        st.markdown("#### Common mistakes")
        for wrong, right in L["mistakes"]:
            st.write(f"❌ {wrong}   →   ✅ **{right}**")

    # ---------------- Say it yourself ----------------
    with tab_say:
        sentences = L["say_it"]
        pick = st.selectbox(
            "Pick a sentence",
            range(len(sentences)),
            format_func=lambda i: sentences[i],
            key=f"pick_{lid}",
        )
        target = sentences[pick]

        with st.container(border=True):
            st.caption("🎯 Listen, then say it")
            st.subheader(target)
            st.audio(audio_for(f"{lid}_say{pick}", target))

        audio = st.audio_input(
            "Tap the mic, say it, tap again to stop",
            key=f"say_audio_{lid}_{pick}",
        )

        if audio:
            data = audio.getvalue()
            h = hashlib.md5(data).hexdigest()
            res_key = f"say_res_{lid}_{pick}"

            # Only call Prisma once per new recording
            if st.session_state.get(res_key + "_hash") != h:
                with open("grammar_recording.wav", "wb") as f:
                    f.write(data)
                with st.spinner("Listening..."):
                    heard = transcribe("grammar_recording.wav")

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
                st.session_state[res_key] = {"heard": heard, "score": matcher.ratio(), "diffs": diffs}
                st.session_state[res_key + "_hash"] = h

            r = st.session_state.get(res_key)
            if r:
                st.write(f"**You said:** {r['heard']}")
                st.progress(r["score"], text=f"Match: {int(r['score'] * 100)}%")
                if not r["diffs"]:
                    st.success("Perfect! 🔥")
                else:
                    st.warning("Almost! Check these parts:")
                    for said, expected in r["diffs"]:
                        st.write(f"- You said **{said}**, try **{expected}**")

    # ---------------- Quiz ----------------
    with tab_quiz:
        if lesson_done(lid):
            st.success("You've completed this lesson ✅  You can retake the quiz any time (XP is given once).")

        # Each retry gets a new number, which gives the quiz fresh, empty answers
        attempt = st.session_state.get(f"qa_{lid}", 0)

        with st.form(f"quiz_{lid}_{attempt}"):
            answers = []
            for q_i, q in enumerate(L["quiz"]):
                answers.append(
                    st.radio(
                        f"{q_i + 1}. {q['q']}",
                        q["options"],
                        index=None,
                        key=f"q_{lid}_{attempt}_{q_i}",
                    )
                )
            submitted = st.form_submit_button("Check answers")

        if submitted:
            if any(a is None for a in answers):
                st.warning("Please answer every question first.")
            else:
                score = 0
                for q_i, (q, a) in enumerate(zip(L["quiz"], answers)):
                    correct = q["options"][q["answer"]]
                    if a == correct:
                        score += 1
                        st.success(f"{q_i + 1}. Correct ✅  {q['why']}")
                    else:
                        st.error(f"{q_i + 1}. Not quite ❌  Correct answer: **{correct}**. {q['why']}")

                st.markdown(f"### Score: {score} / {len(L['quiz'])}")
                if score >= PASS_MARK:
                    if complete_lesson(lid, LESSON_XP):
                        st.balloons()
                        st.success(f"Lesson complete! +{LESSON_XP} XP 🎉")
                    else:
                        st.success("Great work! (You already earned XP for this lesson.)")
                else:
                    st.info(f"You need {PASS_MARK} correct to complete the lesson. Read it once more and try again.")

                st.button(
                    "🔁 Try again",
                    key=f"retry_{lid}_{attempt}",
                    on_click=retry_quiz,
                    args=(lid,),
                )

# =====================================================================
# EXCEPTIONS
# =====================================================================
with section_exceptions:
    st.markdown("English mein rules ke saath kuch exceptions bhi hote hain. Yahan sabse common exceptions ek jagah hain.")
    query = st.text_input("🔎 Search (for example: hour, plural, went)", key="exc_search").strip().lower()

    matches = [t for t in EXCEPTIONS if not query or query in topic_text(t)]
    st.caption(f"Showing {len(matches)} of {len(EXCEPTIONS)} topics")

    if not matches:
        st.info("Nothing found. Try another word, like 'verb', 'plural' or 'article'.")

    for t in matches:
        with st.expander(t["title"], expanded=bool(query) and len(matches) <= 3):
            st.write(t["rule"])
            if t.get("note"):
                st.info(t["note"])

            tb = t.get("table")
            if tb:
                rows = [dict(zip(tb["headers"], row)) for row in tb["rows"]]
                st.dataframe(rows, hide_index=True, height=min(38 * (len(rows) + 1), 420))

            if t.get("mistakes"):
                st.markdown("**Common mistakes**")
                for wrong, right in t["mistakes"]:
                    st.write(f"❌ {wrong}   →   ✅ **{right}**")

            st.markdown("**Examples**")
            for n, (english, hinglish) in enumerate(t["examples"]):
                c1, c2 = st.columns([4, 1])
                c1.markdown(f"**{english}**")
                c1.caption(hinglish)
                if c2.button("▶ Play", key=f"excplay_{t['id']}_{n}"):
                    st.session_state[f"excaud_{t['id']}_{n}"] = audio_for(f"exc_{t['id']}_{n}", english)
                path = st.session_state.get(f"excaud_{t['id']}_{n}")
                if path:
                    st.audio(path)

sidebar()
