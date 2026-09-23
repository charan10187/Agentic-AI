from google import genai
import os
import time

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def call_with_retry(prompt, retries=5, delay=10):
    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )
            return response.text
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(delay)
    return "Failed after retries."

questions = [
    "What is a variable in programming?",
    "What is a list in Python?",
    "What is an API in one sentence?"
]

for q in questions:
    answer = call_with_retry(q)
    print(f"Q: {q}")
    print(f"A: {answer}\n")