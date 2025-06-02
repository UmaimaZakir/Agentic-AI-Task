import os
import requests
import json

API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "deepseek/deepseek-r1-0528-qwen3-8b:free" 

if not API_KEY:
    raise ValueError("No API key found. Please set the OPENROUTER_API_KEY environment variable.")

response = requests.post(
    url=f"{BASE_URL}/chat/completions",
    headers={
        "Authorization": f"Bearer {API_KEY}",
    },
    data=json.dumps({
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": "What is the meaning of life?"
            }
        ]
    })
)

print(response.json())
