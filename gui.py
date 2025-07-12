import tkinter as tk
from bot_logic import get_response
from audio import listen, speak


def send_message(event=None):
    user_message = user_input.get()
    chat_history.insert(tk.END, f"You: {user_message}\n")
    response = get_response(user_message)
    chat_history.insert(tk.END, f"Bot: {response}\n")
    user_input.delete(0, tk.END)


def on_voice_button_click():
    user_message = listen()
    chat_history.insert(tk.END, f"You: {user_message}\n")
    response = get_response(user_message)
    chat_history.insert(tk.END, f"Bot: {response}\n")
    speak(response)


root = tk.Tk()
root.title("ChatBot")
root.geometry("600x400")  # Set initial size

# Configure grid layout
root.grid_rowconfigure(0, weight=1)  # Chat history resizes vertically
root.grid_columnconfigure(0, weight=1)  # Chat history resizes horizontally

# Chat history display
chat_history = tk.Text(root, height=20, wrap=tk.WORD)
chat_history.grid(row=0, column=0, columnspan=3, sticky="nsew")  # Expand in all directions

# Input field
user_input = tk.Entry(root)
user_input.grid(row=1, column=0, sticky="ew", padx=5, pady=5)  # Stretch horizontally

# Bind the Enter key to the send_message function
user_input.bind("<Return>", send_message)
user_input.focus_set()

send_icon = tk.PhotoImage(file="send.png")
send_button = tk.Button(root, image=send_icon, command=send_message, borderwidth=0)
send_button.grid(row=1, column=1, padx=5, pady=5)

mic_icon = tk.PhotoImage(file="mic_icon.png")
voice_button = tk.Button(root, image=mic_icon, command=on_voice_button_click, borderwidth=0)
voice_button.grid(row=1, column=2, padx=5, pady=5)

root.mainloop()
