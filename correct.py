import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Use the same model name you used in your RAG project
MODEL = "gemini-3.5-flash-lite"

def correct_sentence(sentence):
    prompt = f"""You are a friendly English speaking coach for Indian learners.
The learner said: "{sentence}"

Reply ONLY with JSON in this format:
{{"corrected": "the corrected English sentence",
  "explanation": "one short, friendly explanation in simple Hinglish (Hindi written in English letters) of what was wrong"}}

If the sentence is already correct, return it unchanged and say so in the explanation."""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config={"response_mime_type": "application/json"},
    )
    return json.loads(response.text)

if __name__ == "__main__":
    result = correct_sentence("i not go school")
    print(result)