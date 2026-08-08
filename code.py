import os
import sys
from google import genai
from google.genai import types


# ==========================================
# 1. GET API KEY FROM ENVIRONMENT VARIABLE
# ==========================================

api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY environment variable is not set.")
    print("Run:")
    print("export GEMINI_API_KEY='your_api_key'")
    sys.exit(1)


# ==========================================
# 2. INITIALIZE GEMINI CLIENT
# ==========================================

client = genai.Client(api_key=api_key)


# ==========================================
# 3. SYSTEM PROMPT
# ==========================================

SYSTEM_PROMPT = """
You are Alex, a friendly and empathetic IT Helpdesk Specialist at Neurofive Solutions.

RULES:

1. Tone:
   - Be friendly, professional, clear, and reassuring.

2. Responsibilities:
   - Help users with IT-related problems such as:
     passwords, software, networks, email, computers, and device setup.

3. Explanations:
   - Explain technical solutions in simple language.
   - Give step-by-step instructions when appropriate.

4. Brevity:
   - Keep responses concise and focused.

5. Off-topic questions:
   - If the user asks something unrelated to IT, politely decline.
   - Redirect the user toward IT-related assistance.

6. Stay in character:
   - Always respond as Alex, the IT Helpdesk Specialist.
"""


# ==========================================
# 4. FUNCTION TO GET BOT RESPONSE
# ==========================================

def get_bot_reply(user_message):
    """Send a user message to Gemini and return the response."""

    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=user_message,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0.3
            )
        )

        return response.text.strip()

    except Exception as e:
        return f"Error connecting to Gemini API: {e}"


# ==========================================
# 5. AUTOMATED 5 TESTS
# ==========================================

def run_automated_tests():

    test_messages = [
        "I forgot my password and now I'm locked out of my email. What should I do?",

        "Can you help me install Python on my Ubuntu system?",

        "My second monitor stopped displaying anything after a system update.",

        "Can you give me a good recipe for chocolate chip cookies?",

        "I received a suspicious email asking me to verify my payroll information. Is this safe?"
    ]

    print("=" * 60)
    print("RUNNING 5 AUTOMATED TESTS")
    print("=" * 60)

    for index, message in enumerate(test_messages, 1):

        print(f"\n[Test {index}]")
        print(f"User: {message}")

        reply = get_bot_reply(message)

        print(f"Alex: {reply}")
        print("-" * 60)

    print("\nAll 5 tests completed.")


# ==========================================
# 6. INTERACTIVE CHAT
# ==========================================

def start_interactive_chat():

    print("\n" + "=" * 60)
    print("ALEX - IT HELPDESK ASSISTANT")
    print("=" * 60)
    print("Ask me an IT-related question.")
    print("Type 'exit' or 'quit' to end the conversation.\n")

    while True:

        try:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ["exit", "quit", "q"]:
                print("\nAlex: Goodbye! Have a great day.")
                break

            reply = get_bot_reply(user_input)

            print(f"\nAlex: {reply}\n")

        except KeyboardInterrupt:
            print("\n\nAlex: Goodbye!")
            break


# ==========================================
# 7. MAIN PROGRAM
# ==========================================

if __name__ == "__main__":

    print("\nSelect Mode:")
    print("1. Run 5 Automated Tests")
    print("2. Start Interactive Chat")
    print("3. Run Both")

    choice = input("\nEnter choice (1, 2, or 3): ").strip()

    if choice == "1":

        run_automated_tests()

    elif choice == "2":

        start_interactive_chat()

    elif choice == "3":

        run_automated_tests()
        start_interactive_chat()

    else:

        print("\nInvalid choice. Starting interactive chat...")
        start_interactive_chat()
