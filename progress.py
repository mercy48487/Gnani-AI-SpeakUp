import json
from datetime import date, timedelta
import streamlit as st

FILE = "progress.json"
DEFAULT = {"xp": 0, "streak": 0, "best_streak": 0, "last_day": "", "lessons": [], "stages": []}


def load():
    try:
        with open(FILE) as f:
            d = {**DEFAULT, **json.load(f)}
    except Exception:
        d = dict(DEFAULT)
    d["lessons"] = list(d.get("lessons", []))
    d["stages"] = list(d.get("stages", []))
    return d


def save(d):
    try:
        with open(FILE, "w") as f:
            json.dump(d, f)
    except Exception:
        pass


def add_xp(amount):
    d = load()
    today = date.today()
    if d["last_day"] != today.isoformat():
        yesterday = (today - timedelta(days=1)).isoformat()
        d["streak"] = d["streak"] + 1 if d["last_day"] == yesterday else 1
        d["last_day"] = today.isoformat()
        d["best_streak"] = max(d["best_streak"], d["streak"])
    d["xp"] += amount
    save(d)


def lesson_done(lesson_id):
    return lesson_id in load()["lessons"]


def complete_lesson(lesson_id, xp):
    """Give XP the first time a lesson is passed. Returns True if XP was given."""
    d = load()
    if lesson_id in d["lessons"]:
        return False
    d["lessons"].append(lesson_id)
    save(d)
    add_xp(xp)
    return True


def stage_done(n):
    return n in load()["stages"]


def complete_stage(n, xp):
    """Give XP the first time a stage is passed. Returns True if XP was given."""
    d = load()
    if n in d["stages"]:
        return False
    d["stages"].append(n)
    save(d)
    add_xp(xp)
    return True


def sidebar():
    d = load()
    level = d["xp"] // 100 + 1
    into = d["xp"] % 100
    with st.sidebar:
        st.markdown("### 🏅 Your progress")
        st.write(f"**Level {level}**  |  {d['xp']} XP")
        st.progress(into / 100, text=f"{into} / 100 XP to next level")
        st.write(f"🔥 Streak: **{d['streak']}** day(s)")
        st.write(f"📘 Lessons completed: **{len(d['lessons'])}**")
        st.write(f"🪜 Stages completed: **{len(d['stages'])}** of 7")
        with st.expander("Reset progress"):
            if st.button("Reset to zero"):
                save(dict(DEFAULT))
                st.rerun()
