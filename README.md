# Wisdom Quotes Generator

A lightweight Python program that generates batches of wisdom quotes using Gemini and integrates with Roblox (or any app) via simulated keypresses. Quotes are copied to your clipboard and pasted automatically when you double‑tap **Alt**.

---

## 🚀 Features
- Generates **30 quotes at a time** to reduce API traffic.
- Ensures Gemini outputs a **valid JSON array of strings** (no extra text).
- Cycles through quotes on each trigger.
- Double‑tap **Alt** within 200ms to:
  - Copy the next quote to clipboard
  - Send `/`
  - Paste (`Ctrl+V`)
  - Press `Enter`
- Configurable system prompt and batch size via `config.yaml`.
- Dev mode supported (use `.env.example` → rename to `.env` with your own API key).

---

## 📂 Project Structure