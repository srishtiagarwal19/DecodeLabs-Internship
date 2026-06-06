from datetime import datetime
print("🤖 ChatBot: Hello! Type 'bye' to exit.")

responses = {
    "hello": "Hi there!",
    "hi": "Hello!",
    "how are you": "I am doing great!",
    "what is your name": "I am a Rule-Based ChatBot.",
     "what's your name": "I am a Rule-Based ChatBot.",
    "help": "Ask me simple questions.",
    "thanks": "You're welcome!"
}

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "bye":
        print("🤖 ChatBot: Goodbye!")
        break
    if user_input == "time":
        print("🤖 ChatBot:", datetime.now().strftime("%H:%M:%S"))
        continue

    reply = responses.get(
        user_input,
        "Sorry, I don't understand that."
    )

    print("🤖 ChatBot:", reply)