
# from google import genai

# client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# response = client.models.generate_content(
#     model="gemini-3.6-flash",
#     contents="Explain what an API is in 2 sentences."
# )

# print(response.text)



from google import genai
import os
import time

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def call_with_retry(prompt, retries=3, delay=5):
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

result = call_with_retry("Explain what an API is in 2 sentences.")
print(result)