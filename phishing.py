import tkinter as tk
from tkinter import messagebox

# List of sample questions and answers for the quiz
questions = [
    {
        "question": "What is a common indicator of a phishing email?",
        "options": ["Unexpected attachments", "Personalized greeting", "Proper spelling"],
        "answer": "Unexpected attachments"
    },
    {
        "question": "Which of these websites is most likely a phishing site?",
        "options": ["https://www.banksecure.com", "http://secure-bank.com", "https://mybank.com"],
        "answer": "http://secure-bank.com"
    },
    {
        "question": "What should you do if you receive a suspicious email?",
        "options": ["Click on all the links to check for issues", "Delete the email immediately", "Report it to your IT department"],
        "answer": "Report it to your IT department"
    }
]

current_question_index = 0  # To keep track of the current question index

# Function to display the current question and options
def display_question(index):
    question_label.config(text=questions[index]["question"])
    selected_option.set(None)  # Reset the selected option for the new question
    for i, option in enumerate(questions[index]["options"]):
        options_var[i].set(option)
        option_buttons[i].config(text=option, value=option)

# Function to check the answer
def check_answer():
    global current_question_index
    selected = selected_option.get()
    if selected == questions[current_question_index]["answer"]:
        messagebox.showinfo("Result", "Correct!")
    else:
        messagebox.showerror("Result", f"Incorrect. The correct answer is: {questions[current_question_index]['answer']}")

    current_question_index += 1
    if current_question_index < len(questions):
        display_question(current_question_index)
    else:
        messagebox.showinfo("Quiz Completed", "You have completed the quiz!")
        root.destroy()

# Create the main application window
root = tk.Tk()
root.title("Phishing Awareness Quiz")

# Question label
question_label = tk.Label(root, text="", wraplength=400, font=("Arial", 14))
question_label.pack(pady=10)

# Options
options_var = [tk.StringVar(value="") for _ in range(3)]
selected_option = tk.StringVar(value="")

option_buttons = []
for i in range(3):
    rb = tk.Radiobutton(root, text="", variable=selected_option, value="", font=("Arial", 12))
    option_buttons.append(rb)
    rb.pack(anchor="w", padx=20)

# Start the quiz by displaying the first question
display_question(current_question_index)

# Submit button
submit_button = tk.Button(root, text="Submit", command=check_answer)
submit_button.pack(pady=10)

# Run the application
root.mainloop()
