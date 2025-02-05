import requests
import os
from config.settings import OPENROUTER_API_KEY

API_URL = "https://openrouter.ai/api/v1/chat/completions"

def generate_summary(topic, detail, format):
    prompt = f"Summarize '{topic}' in {detail} detail. Format: {format}."

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-3.5-turbo",  # Use the working model
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.5
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        response.raise_for_status()  # Raises an error for bad responses (4xx, 5xx)

        # Extract the generated summary
        return response.json()["choices"][0]["message"]["content"]

    except requests.exceptions.RequestException as e:
        return f"⚠️ API Error: {str(e)}"
    except KeyError:
        return "⚠️ Unexpected response format. Please check API response."
