import tkinter as tk
from tkinter import messagebox


def is_valid(board, row, col, num):
    num = str(num)
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def has_duplicates(board):
    for row in range(9):
        seen_row = set()
        seen_col = set()
        for col in range(9):
            if board[row][col] != '':
                if board[row][col] in seen_row:
                    return True
                seen_row.add(board[row][col])
            if board[col][row] != '':
                if board[col][row] in seen_col:
                    return True
                seen_col.add(board[col][row])
    return False


def solve_sudoku(board):
    if has_duplicates(board):
        messagebox.showerror("Error", "Invalid input: Duplicate numbers found in row or column!")
        return False

    for row in range(9):
        for col in range(9):
            if board[row][col] == '':
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = str(num)
                        if solve_sudoku(board):
                            return True
                        board[row][col] = ''
                return False
    return True


def get_board():
    return [[entries[row][col].get() for col in range(9)] for row in range(9)]


def solve_and_display():
    board = get_board()
    if solve_sudoku(board):
        for row in range(9):
            for col in range(9):
                entries[row][col].delete(0, tk.END)
                entries[row][col].insert(0, board[row][col])


def clear_board():
    for row in range(9):
        for col in range(9):
            entries[row][col].delete(0, tk.END)


root = tk.Tk()
root.title("Sudoku Solver")

entries = []
for row in range(9):
    row_entries = []
    for col in range(9):
        entry = tk.Entry(root, width=3, font=('Arial', 16), justify='center')
        entry.grid(row=row, column=col, padx=2, pady=2)
        row_entries.append(entry)
    entries.append(row_entries)

tk.Button(root, text="Solve", command=solve_and_display, font=('Arial', 14)).grid(row=9, column=0, columnspan=4,
                                                                                  pady=10)
tk.Button(root, text="Clear", command=clear_board, font=('Arial', 14)).grid(row=9, column=5, columnspan=4, pady=10)

root.mainloop()
