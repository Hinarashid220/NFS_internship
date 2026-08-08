# Neurofive Support Bot — Custom AI Chatbot with a System Prompt

A small Python script that connects to Google's Gemini API and gives it a custom
system prompt, turning it into **Nova**, a Neurofive Solutions IT helpdesk assistant
that stays in character and redirects off-topic questions back to support.

This project was built as part of the **AI & Prompt Engineering Internship at Neurofive**,
covering: LLM APIs, system prompts, API key management, and basic API calls in Python.

## Features

- Connects to the Gemini API (`gemini-2.5-flash`) using the official `google-genai` SDK
- Custom system prompt that gives the bot a fixed persona and behavior rules
- Stays in character and redirects off-topic user messages back to support topics
- Tested against 5 sample user messages, including one off-topic message, to confirm
  the persona holds

## Tech Stack

- Python 3
- [`google-genai`](https://pypi.org/project/google-genai/) SDK
- Gemini API (free tier)

## Setup

### 1. Install Required Packages

```bash
pip install google-genai
```

### 2. Set Up Your API Key

Get a free-tier API key from [Google AI Studio](https://aistudio.google.com/), then
export it as an environment variable — **never hardcode it in your source code**:

```bash
export GEMINI_API_KEY="your_api_key_here"
```

> ⚠️ **Security note:** An API key is a secret, same as a password. If it's committed
> to a public repo, anyone can use it on your account and run up your usage. Always
> load it from an environment variable (or a `.env` file that's excluded via
> `.gitignore`), never as a literal string in `.py` files.

### 3. Run the Application

```bash
python3 chatbot.py
```

## Project Structure

```
.
├── chatbot.py        # Main script — connects to Gemini, applies the system prompt, runs test messages
├── .gitignore         # Keeps secrets and system files out of version control
└── README.md
```

## `.gitignore`

To make sure secrets and local clutter never get pushed to GitHub, create a
`.gitignore` file:

```bash
nano .gitignore
```

Add the following:

```
# Environment variables / Secrets
.env
*.env

# Python cache files
__pycache__/
*.pyc

# OS generated files
.DS_Store
```

## Example Interaction

```
User: My laptop won't connect to the office Wi-Fi, what should I try?
Nova: Let's get you back online! First, try toggling Wi-Fi off and on...

User: Can you recommend a good pizza place nearby?
Nova: That's outside what I can help with here — I'm focused on Neurofive
      Solutions support. Is there an IT issue I can help you with instead?
```

## Notes

- This repo intentionally does **not** include a real API key anywhere. If you fork
  or clone this project, you'll need your own free-tier Gemini key.
- If a key was ever committed to this repo's history, treat it as compromised and
  regenerate it immediately in Google AI Studio.
