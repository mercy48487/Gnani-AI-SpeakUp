# 🎙️ SpeakUp

**A Hinglish-friendly English speaking coach for Indian learners.**

Built solo for the Great Indian AI Internship Challenge by Gnani AI.
#GnaniAI #GreatIndianAIInternshipChallenge

## The problem

Many Indian learners understand English but freeze when they have to speak it, are unsure of basics like "a" or "an" and the past tense, and get feedback only in English.
SpeakUp listens to what the learner really says, shows exactly what to fix, and explains why in simple Hinglish (Hindi written in English letters).

## What SpeakUp does

| Mode | What it does |
| --- | --- |
| 🎯 **Practice** | The app speaks a target sentence and the learner repeats it. It shows what they actually said, a match score, the exact words to fix, and a Hinglish explanation of the rule. |
| 🗣️ **Hinglish to English** | Say something in Hinglish, get the natural English version and a Hinglish tip, spoken aloud. Keeps a history of past sentences. |
| 🎭 **Tone Switch** | One spoken message comes back in three English versions: casual (to a friend), polite (to a teacher or elder) and professional (to a manager or in an email). Each can be played aloud. |
| 🌀 **Tongue Twisters** | Say a tongue twister and earn one to three stars based on how closely the words match. Missed words are listed, and you can retry. |
| 📘 **Grammar Book** | Short Hinglish lessons (currently "A or An" and "Past tense") with spoken examples, a "say it yourself" check and a quiz. A separate **Exceptions** section lists 12 topics of common exceptions, such as irregular verbs, plurals and uncountable nouns, with search. |
| 🪜 **Stages** | A step-by-step path from words to sentences. **Stages 1 to 3 are built** (Words, Phrases, Simple sentences). Passing a quiz unlocks the next stage. |

**Progress:** XP for every attempt, a level for every 100 XP, a daily streak, and counts of completed lessons and stages. Progress is saved locally in `progress.json`.

**Not built yet:** Stages 4 to 7 (joining ideas, storytelling, emails and essays) are planned and shown in the app as "coming soon".

## Models and APIs used

| Part | What it uses |
| --- | --- |
| Speech to text | **Gnani Prisma v2.5** (language code `en-IN`; keeps grammar mistakes instead of silently fixing them, and writes Hinglish in Roman letters) |
| Text to speech | **Gnani Timbre v2.5** (voice: Kaveri) |
| Feedback and Hinglish explanations | **Google Gemini** (general-purpose LLM), with automatic retries and a fallback model when the server is busy |

Evon is open-weights only and has no hosted API, so the feedback step uses Gemini.
The Grammar Book and Stages lessons are fixed, reviewed content, not generated live.

## How it works

1. The learner records audio in the browser.
2. Prisma transcribes it exactly as spoken, mistakes included.
3. The app compares it with the target sentence word by word, and Gemini explains the mistake in Hinglish.
4. Timbre speaks the corrected sentence, the tones or the lesson examples aloud.

Each recording is processed only once, so clicking buttons does not repeat API calls.

## Project structure

```
Home.py                  home page with all the modes
main.py                  Prisma, Timbre and Gemini helper functions
progress.py              XP, levels, streak, completed lessons and stages
grammar_content.py       Grammar Book lessons and the Exceptions section
stages_content.py        Stages 1 to 3 content
pages/                   one file per mode (Practice, Hinglish, Tone Switch, Tongue Twister, Grammar Book, Stages)
.streamlit/config.toml   theme
```

## Run it yourself

1. Install Python 3.10 or newer, then:
   ```
   pip install streamlit requests python-dotenv google-genai
   ```
2. Create a `.env` file in the project folder:
   ```
   GNANI_API_KEY=your_gnani_key
   GEMINI_API_KEY=your_gemini_key
   ```
3. Start the app:
   ```
   python -m streamlit run Home.py
   ```

Get a Gnani key at app.gnani.ai and a Gemini key at aistudio.google.com.
The app runs locally and is not deployed publicly, which keeps API credits safe.

## Limitations

- Speech recognition can occasionally mishear a word. Practice mode has a Skip button, and single-word checks in Stage 1 are deliberately lenient.
- The practice sentences, tongue twisters and lessons are hand-written and few in number.
- Gemini's explanations can vary between runs.
- Progress is stored in a local file and the app is built for one user at a time.
- Stages 4 to 7 are not built yet.

## Built by

Mercy Mochary, solo. Engineering student.

## Demo

[Add your LinkedIn or X demo link here after posting]
