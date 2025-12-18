import time
import keyboard
import pyperclip
import pydirectinput
from utils.clipboard import set_clipboard
from utils.quote_buffer import QuoteBuffer
from utils.gemini_client import load_config

pydirectinput.PAUSE = 0.02

def main():
    config = load_config()
    buffer = QuoteBuffer(batch_size=config.get("batch_size", 30))

    # Generate first batch and copy first quote
    first_quote = buffer.next_quote()
    set_clipboard(first_quote)
    print(f"First quote ready: {first_quote}")

    last_alt_time = 0.0

    def alt_double_tap():
        nonlocal last_alt_time
        now = time.time()
        if now - last_alt_time < 0.2:  # 200ms threshold
            # Get next quote into clipboard
            quote = buffer.next_quote()
            set_clipboard(quote)
            print(f"Quote ready: {quote}")

            # Sequence: / → Ctrl+V → Enter (no delays)
            pydirectinput.press("/")          # press slash
            pydirectinput.keyDown("ctrl")
            pydirectinput.press("v")
            pydirectinput.keyUp("ctrl")
            pydirectinput.press("enter")
        last_alt_time = now

    # Bind Alt key
    keyboard.on_press_key("alt", lambda e: alt_double_tap())

    print("Listening... Double‑tap Alt to trigger sequence. Press Ctrl+C to exit.")
    keyboard.wait()

if __name__ == "__main__":
    main()