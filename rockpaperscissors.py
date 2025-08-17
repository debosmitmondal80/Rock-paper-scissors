import tkinter as tk
import random

# Game options
options = ['rock', 'paper', 'scissors']

# Scores
player_score = 0
computer_score = 0

# Determine result
def determine_winner(player_choice):
    global player_score, computer_score
    computer_choice = random.choice(options)

    result_text = f"You chose: {player_choice}\nComputer chose: {computer_choice}\n"

    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'scissors' and computer_choice == 'paper')
    ):
        result = "You Win!"
        player_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(text=result_text + result)
    score_label.config(text=f"You: {player_score}  |  Computer: {computer_score}")

# Reset game
def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    result_label.config(text="Make your move!")
    score_label.config(text="You: 0  |  Computer: 0")

# Setup GUI
window = tk.Tk()
window.title("Rock, Paper, Scissors")
window.geometry("400x300")
window.configure(bg="#f2f2f2")

title = tk.Label(window, text="Rock, Paper, Scissors", font=("Arial", 18, "bold"), bg="#f2f2f2")
title.pack(pady=10)

result_label = tk.Label(window, text="Make your move!", font=("Arial", 14), bg="#f2f2f2")
result_label.pack(pady=10)

score_label = tk.Label(window, text="You: 0  |  Computer: 0", font=("Arial", 12), bg="#f2f2f2")
score_label.pack(pady=5)

# Buttons
btn_frame = tk.Frame(window, bg="#f2f2f2")
btn_frame.pack()

rock_btn = tk.Button(btn_frame, text="Stone", width=10, command=lambda: determine_winner('rock'))
rock_btn.grid(row=0, column=0, padx=10, pady=10)

paper_btn = tk.Button(btn_frame, text="Paper", width=10, command=lambda: determine_winner('paper'))
paper_btn.grid(row=0, column=1, padx=10, pady=10)

scissors_btn = tk.Button(btn_frame, text="Scissors", width=10, command=lambda: determine_winner('scissors'))
scissors_btn.grid(row=0, column=2, padx=10, pady=10)

reset_btn = tk.Button(window, text="Reset Game", command=reset_game)
reset_btn.pack(pady=10)

# Start GUI loop
window.mainloop()
