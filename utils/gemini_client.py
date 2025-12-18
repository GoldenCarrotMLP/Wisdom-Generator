import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
import yaml

load_dotenv()

# Configure Gemini client
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

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

    model = genai.GenerativeModel(model_name="gemini-3-flash-preview")
    response = model.generate_content(prompt)

    try:
        quotes = json.loads(response.text)
        if isinstance(quotes, list) and all(isinstance(q, str) for q in quotes):
            return quotes
        else:
            raise ValueError("Response was not a valid JSON array of strings.")
    except Exception as e:
        raise RuntimeError(f"Failed to parse Gemini response: {e}")
