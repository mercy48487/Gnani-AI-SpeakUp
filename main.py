import os
import json
import time
import requests
from dotenv import load_dotenv
from google import genai

load_dotenv()
GNANI_KEY = os.getenv("GNANI_API_KEY")
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODELS = ["gemini-3.5-flash-lite", "gemini-3.5-flash"]
MODEL = MODELS[0]


def generate_json(prompt):
    """Call Gemini with retries, then fall back to a second model."""
    last_error = None
    for model in MODELS:
        for attempt in range(3):
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt,
                    config={"response_mime_type": "application/json"},
                )
                return json.loads(response.text)
            except Exception as e:
                last_error = e
                time.sleep(1.5 * (attempt + 1))
    raise last_error


def transcribe(audio_path):
    url = "https://api.vachana.ai/stt/v3"
    headers = {"X-API-Key-ID": GNANI_KEY}
    with open(audio_path, "rb") as f:
        r = requests.post(
            url,
            headers=headers,
            files={"audio_file": f},
            data={"language_code": "en-IN"},
        )
    r.raise_for_status()
    return r.json()["transcript"]


def correct_sentence(sentence, target=None):
    goal = f'\nThe sentence they were trying to say: "{target}"' if target else ""
    prompt = f"""You are a friendly English speaking coach for Indian learners.
The learner said: "{sentence}"{goal}

Reply ONLY with JSON in this format:
{{"corrected": "the corrected English sentence, with proper capitalization and punctuation",
  "explanation": "one short, friendly explanation in simple Hinglish (Hindi written in English letters) of the main mistake(s). Cover every word that differs from the correct sentence, and for each one give the reason in one short phrase (for example the tense rule), not just the swap. Do not mention commas or punctuation."}}

If the sentence is already correct, return it unchanged and say so in the explanation."""
    return generate_json(prompt)


def speak(text, out_path="feedback.wav"):
    url = "https://api.vachana.ai/api/v1/tts/inference"
    headers = {"Content-Type": "application/json", "X-API-Key-ID": GNANI_KEY}
    body = {
        "text": text,
        "voice": "Kaveri",
        "model": "timbre-v2.5",
        "language": "en-IN",
        "speed": 1.0,
        "audio_config": {
            "sample_rate": 48000,
            "num_channels": 1,
            "sample_width": 2,
            "encoding": "linear_pcm",
            "container": "wav",
        },
    }
    r = requests.post(url, headers=headers, json=body)
    r.raise_for_status()
    with open(out_path, "wb") as f:
        f.write(r.content)


if __name__ == "__main__":
    heard = transcribe("test4.ogg")
    print("You said:", heard)

    result = correct_sentence(heard)
    print("Correct:", result["corrected"])
    print("Why:", result["explanation"])

    speak(result["corrected"])
    print("Saved feedback.wav")