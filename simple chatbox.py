class Chatbot:
    def __init__(self):
        self.responses = {
            "hi": "Hello! How can I help you today?",
            "how are you?": "I'm just a program, but thanks for asking!",
            "bye": "Goodbye! Have a great day!",
        }

    def get_response(self, user_input):
        return self.responses.get(user_input.lower(), "I am not sure how to respond to that.")

chatbot = Chatbot()
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot:", chatbot.get_response(user_input))
        break
    print("Chatbot:", chatbot.get_response(user_input))