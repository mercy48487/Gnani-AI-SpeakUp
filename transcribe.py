import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GNANI_API_KEY")

url = "https://api.vachana.ai/stt/v3"
headers = {"X-API-Key-ID": api_key}

with open("test3.ogg", "rb") as f:
    files = {"audio_file": f}
    data = {"language_code": "en-IN"}
    response = requests.post(url, headers=headers, files=files, data=data)

print(response.status_code)
print(response.json())