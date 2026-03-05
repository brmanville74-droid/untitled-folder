import tkinter as tk
from tkinter import messagebox
import random


class ComputerLogic:
    def __init__(self, difficulty="Medium", ai="O", human="X"):
        self.difficulty = difficulty
        self.ai = ai
        self.human = human
        self.cheat_used = False

    def get_move(self, board):
        if self.difficulty == "Easy":
            return random.choice(self.available_moves(board))
        if self.difficulty == "Medium":
            return self.medium_move(board)
        return self.minimax(board, True)["index"]

    def medium_move(self, board):
        for i in self.available_moves(board):
            board[i] = self.ai
            if self.check_winner(board, self.ai):
                board[i] = ""
                return i
            board[i] = ""

        for i in self.available_moves(board):
            board[i] = self.human
            if self.check_winner(board, self.human):
                board[i] = ""
                return i
            board[i] = ""

        return random.choice(self.available_moves(board))

    def minimax(self, board, is_max):
        if self.check_winner(board, self.ai):
            return {"score": 1}
        if self.check_winner(board, self.human):
            return {"score": -1}
        if not self.available_moves(board):
            return {"score": 0}

        best = {"score": -float("inf")} if is_max else {"score": float("inf")}

        for i in self.available_moves(board):
            board[i] = self.ai if is_max else self.human
            result = self.minimax(board, not is_max)
            board[i] = ""
            result["index"] = i

            if is_max and result["score"] > best["score"]:
                best = result
            if not is_max and result["score"] < best["score"]:
                best = result

        return best

    def available_moves(self, board):
        return [i for i in range(9) if board[i] == ""]

    def check_winner(self, board, p):
        wins = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]
        return any(all(board[i] == p for i in w) for w in wins)


class TicTacToeUI:
    CELL = 133

    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe (Cheating AI)")

        self.board = [""] * 9
        self.game_over = False
        self.scores = {"X": 0, "O": 0, "Draw": 0}

        self.difficulty = tk.StringVar(value="Medium")
        self.logic = ComputerLogic(self.difficulty.get())

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        controls = tk.Frame(root)
        controls.pack(pady=5)

        tk.Label(controls, text="Difficulty:").pack(side="left")
        tk.OptionMenu(
            controls,
            self.difficulty,
            "Easy", "Medium", "Hard",
            command=self.change_difficulty
        ).pack(side="left")

        self.score_label = tk.Label(root, text=self.score_text())
        self.score_label.pack()

        tk.Button(root, text="Reset Game", command=self.reset_game).pack(pady=5)

        self.canvas.bind("<Button-1>", self.handle_click)
        self.draw_board()

    def score_text(self):
        return f"X: {self.scores['X']}  O: {self.scores['O']}  Draws: {self.scores['Draw']}"

    def change_difficulty(self, _):
        self.logic = ComputerLogic(self.difficulty.get())

    def draw_board(self):
        self.canvas.delete("all")
        for r in range(3):
            for c in range(3):
                x1 = c * self.CELL
                y1 = r * self.CELL
                x2 = x1 + self.CELL
                y2 = y1 + self.CELL
                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill="black", outline="white", width=2
                )

        for i, val in enumerate(self.board):
            if val:
                self.draw_symbol(i, val)

    def handle_click(self, event):
        if self.game_over:
            return

        col = event.x // self.CELL
        row = event.y // self.CELL
        idx = row * 3 + col

        if 0 <= idx < 9 and self.board[idx] == "":
            self.make_move(idx, "X")

            if not self.game_over:
                ai_move = self.logic.get_move(self.board)
                self.make_move(ai_move, "O")
                self.maybe_cheat()

    def maybe_cheat(self):
        if self.logic.cheat_used:
            return

        xs = [i for i, v in enumerate(self.board) if v == "X"]
        if not xs:
            return

        if random.random() < 0.4:  # 40% chance to cheat
            victim = random.choice(xs)
            self.board[victim] = ""
            self.logic.cheat_used = True
            self.draw_board()
            messagebox.showinfo("Computer", "HAHAHAHA 😈\nI deleted one of your X's!")

    def make_move(self, index, player):
        self.board[index] = player
        self.draw_symbol(index, player)

        if self.logic.check_winner(self.board, player):
            self.end_game(player)
        elif "" not in self.board:
            self.end_game("Draw")

    def draw_symbol(self, index, player):
        r, c = divmod(index, 3)
        pad = 25
        x1 = c * self.CELL + pad
        y1 = r * self.CELL + pad
        x2 = (c + 1) * self.CELL - pad
        y2 = (r + 1) * self.CELL - pad

        if player == "X":
            self.canvas.create_line(x1, y1, x2, y2, fill="red", width=4)
            self.canvas.create_line(x1, y2, x2, y1, fill="red", width=4)
        else:
            self.canvas.create_oval(x1, y1, x2, y2, outline="blue", width=4)

    def end_game(self, winner):
        self.game_over = True
        self.scores[winner] += 1
        self.score_label.config(text=self.score_text())

        if winner == "X":
            msg = "Get a life bro, it's tic tac toe"
        elif winner == "O":
            msg = "You suck lol!"
        else:
            msg = "It's a draw."

        messagebox.showinfo("Game Over", msg)

    def reset_game(self):
        self.board = [""] * 9
        self.game_over = False
        self.logic.cheat_used = False
        self.draw_board()


if __name__ == "__main__":
    root = tk.Tk()
    TicTacToeUI(root)
    root.mainloop()
