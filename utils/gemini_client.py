import os
import json
import yaml
from dotenv import load_dotenv
import google.genai as genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

def generate_batch():
    config = load_config()
    batch_size = config.get("batch_size", 30)
    system_prompt = config["system_prompt"]

    prompt = f"""{system_prompt}
Return exactly {batch_size} quotes as a valid JSON array of strings.
Do not include any explanations or text outside the array."""

    # Correct usage: keyword args
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    # ✅ Use .text instead of .output_text
    text_output = response.text.strip()

    try:
        quotes = json.loads(text_output)
        if isinstance(quotes, list) and all(isinstance(q, str) for q in quotes):
            return quotes
        else:
            raise ValueError("Response was not a valid JSON array of strings.")
    except Exception as e:
        raise RuntimeError(f"Failed to parse Gemini response: {e}")