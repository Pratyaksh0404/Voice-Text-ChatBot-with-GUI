def get_response(user_input):
    if "hello" in user_input.lower():
        return "Hi there! How can I assist you?"
    elif "weather" in user_input.lower():
        return "I can't fetch weather right now, but I'm here to chat!"
    elif "exit" in user_input.lower():
        return "Goodbye!"
    else:
        return "Working on it!"
