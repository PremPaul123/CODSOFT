import tkinter as tk
from tkinter import messagebox
import math

# Initialize Board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to check winner
def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    return None

# Check if the board is full
def is_board_full():
    return all(board[row][col] != ' ' for row in range(3) for col in range(3))

# Minimax Algorithm with Alpha-Beta Pruning
def minimax(depth, is_maximizing, alpha, beta):
    winner = check_winner()
    if winner == 'X':
        return -10 + depth  # Minimize for AI
    elif winner == 'O':
        return 10 - depth  # Maximize for AI
    elif is_board_full():
        return 0  # Draw

    if is_maximizing:
        best_score = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    score = minimax(depth + 1, False, alpha, beta)
                    board[row][col] = ' '  
                    best_score = max(best_score, score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    score = minimax(depth + 1, True, alpha, beta)
                    board[row][col] = ' '  
                    best_score = min(best_score, score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return best_score

# AI Move
def best_ai_move():
    best_score = -math.inf
    move = (-1, -1)
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'O'
                score = minimax(0, False, -math.inf, math.inf)
                board[row][col] = ' '
                if score > best_score:
                    best_score = score
                    move = (row, col)
    board[move[0]][move[1]] = 'O'
    update_board()
    check_game_status()

# Update the UI board
def update_board():
    for row in range(3):
        for col in range(3):
            labels[row][col].config(text=board[row][col])

# Handle player move
def player_move(row, col):
    if board[row][col] == ' ':
        board[row][col] = 'X'
        update_board()
        check_game_status()
        if not is_board_full() and not check_winner():
            best_ai_move()

# Check for win/draw
def check_game_status():
    winner = check_winner()
    if winner:
        messagebox.showinfo("Game Over", f"{winner} wins!")
        reset_board()
    elif is_board_full():
        messagebox.showinfo("Game Over", "It's a draw!")
        reset_board()

# Reset the board
def reset_board():
    global board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    update_board()

# Create the Tkinter GUI
root = tk.Tk()
root.title("Tic-Tac-Toe AI")

# Create labels for Tic-Tac-Toe grid
labels = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        label = tk.Label(root, text=' ', font=("Arial", 24), width=5, height=2, borderwidth=2, relief="solid")
        label.grid(row=row, column=col, padx=5, pady=5)
        label.bind("<Button-1>", lambda e, r=row, c=col: player_move(r, c))
        labels[row][col] = label

# Restart Button
reset_button = tk.Button(root, text="Restart Game", font=("Arial", 14), command=reset_board)
reset_button.grid(row=3, column=0, columnspan=3, pady=10)

# Start the Tkinter main loop
root.mainloop()
