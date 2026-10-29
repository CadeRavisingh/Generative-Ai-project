
print("Chatbot: Hello! I am your chatbot.")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("Chatbot: Goodbye!")
        break
    elif "hello" in user or "hi" in user:
        print("Chatbot: Hello! How can I help you?")
    elif "name" in user:
        print("Chatbot: My name is PyBot.")
    elif "help" in user:
        print("Chatbot: Sure! What do you need help with?")
    else:
        print("Chatbot: Sorry, I don't understand that yet.")
