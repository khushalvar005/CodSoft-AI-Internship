import re
from datetime import datetime

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if re.search(r"\b(hi|hello|hey)\b", user_input):
        return "Hello! How can I help you?"

    elif re.search(r"\b(your name|who are you)\b", user_input):
        return "I am RuleBot, a simple rule-based chatbot."

    elif re.search(r"\bhow are you\b", user_input):
        return "I'm doing great! Thanks for asking."

    elif re.search(r"\b(time|current time)\b", user_input):
        return "Current time: " + datetime.now().strftime("%I:%M %p")

    elif re.search(r"\b(date|today)\b", user_input):
        return "Today's date: " + datetime.now().strftime("%d-%m-%Y")

    elif re.search(r"\b(help|commands)\b", user_input):
        return "I can greet you, tell you the date and time, and answer basic questions."

    elif re.search(r"\b(thank you|thanks)\b", user_input):
        return "You're welcome!"

    elif re.search(r"\b(joke|funny)\b", user_input):
        return "Why do programmers prefer dark mode? Because light attracts bugs!"

    elif re.search(r"\b(bye|goodbye|exit|quit)\b", user_input):
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I don't understand that. Could you rephrase?"


print("RuleBot: Hello! I am RuleBot.")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("RuleBot:", response)

    if re.search(r"\b(bye|goodbye|exit|quit)\b", user_input.lower()):
        break