# 🎙️ SpeakUp

**A Hinglish-friendly English speaking coach for Indian learners.**

Built for the Great Indian AI Internship Challenge by Gnani AI.
#GnaniAI #GreatIndianAIInternshipChallenge

## The problem

Many Indian learners understand English but freeze when they have to speak it.
Most apps correct them in English only and never show *why* a sentence was wrong.

## What SpeakUp does

**🎯 Practice mode**
The app speaks a sentence. The learner repeats it, and SpeakUp transcribes what
they actually said, shows a match score, points out the exact words that were wrong,
and explains the mistake in simple Hinglish.

**🗣️ Hinglish to English mode**
The learner says something in Hinglish. SpeakUp gives the natural English version,
a short Hinglish tip, and speaks the English sentence back.

## Models and APIs used

| Part | What it uses |
| --- | --- |
| Speech to text | **Gnani Prisma v2.5** (language code `en-IN`, handles Hinglish) |
| Text to speech | **Gnani Timbre v2.5** |
| Feedback and explanations | **Google Gemini** (general-purpose LLM) |

Evon is open-weights only and has no hosted API, so the feedback step uses Gemini.

## How it works

1. The learner records audio in the browser.
2. Prisma transcribes it exactly as spoken, mistakes included.
3. Gemini compares it with the target and explains the mistake in Hinglish.
4. Timbre speaks the corrected sentence back.

## Run it yourself

1. Install Python 3.10 or newer, then:
2. Create a `.env` file in the project folder:
3. Start the app:

Get a Gnani key at app.gnani.ai and a Gemini key at aistudio.google.com.

## Limitations

- Speech recognition can occasionally mishear a word, so there is a Skip button in Practice mode.
- The practice sentence list is short and hand-written.
- Feedback quality depends on the LLM, and explanations can vary between runs.

## Built by

Mercy Mochary, solo. Engineering student.

## Demo
