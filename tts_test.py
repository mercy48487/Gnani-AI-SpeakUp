import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GNANI_API_KEY")

url = "https://api.vachana.ai/api/v1/tts/inference"
headers = {
    "Content-Type": "application/json",
    "X-API-Key-ID": api_key,
}
body = {
    "text": "I did not go to school.",
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

response = requests.post(url, headers=headers, json=body)
print(response.status_code)

if response.status_code == 200:
    with open("output.wav", "wb") as f:
        f.write(response.content)
    print("Saved output.wav")
else:
    print(response.text)