
def simple_chatbot():
    """
    A simple rule-based chatbot that responds to predefined greetings and farewells.
    """
    print("Chatbot: Hi there! Type 'bye' to exit.")

    # Main loop for the chatbot conversation
    while True:
        user_input = input("You: ").strip().lower() # Get user input, remove whitespace, convert to lowercase

        if user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break # Exit the loop when the user says 'bye'
        else:
            print("Chatbot: I'm sorry, I don't understand that.")

# Call the chatbot function to start the conversation
if __name__ == "__main__":
    simple_chatbot()