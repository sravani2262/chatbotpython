import re
patterns_responses = {
    r'.*your name.*': "My name is ChatBot.",
    r'.*how are you.*': "I'm doing well, thank you!",
    r'.*what can you do.*': "I can answer questions and have simple conversations.",
    r'.*who created you.*': "I was created by a team of developers.",
    r'.*thanks for your information.*': "welcome!have a nice dayth",
    r'.*weather.*': "I'm sorry, I can't provide real-time weather information.",
    r'.*capital of France.*': "The capital of France is Paris."
}
def get_response(query):
    for pattern, response in patterns_responses.items():
        if re.match(pattern, query, re.IGNORECASE):
            return response
    return "I'm sorry, I don't understand that question."
print("Bot: Hi there! How can I help you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Bot: Bye!")
        break
    response = get_response(user_input)
    print("Bot:", response)
