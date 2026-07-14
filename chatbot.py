# Function for chatbot
def chatbot():

    user = input("You: ")

    if user == "hello":
        print("Bot: Hi!")

    elif user == "how are you":
        print("Bot: I'm fine, thanks!")

    elif user == "what is your name":
        print("Bot: My name is Python Chatbot.")

    elif user == "bye":
        print("Bot: Goodbye!")
        return False

    else:
        print("Bot: Sorry, I don't understand.")

    return True


# Loop to keep chatbot running
while True:

    result = chatbot()

    if result == False:
        break
