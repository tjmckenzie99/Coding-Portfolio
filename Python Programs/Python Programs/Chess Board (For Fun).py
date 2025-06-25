import tkinter as tk

chess_board = [
    ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
    ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
    ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
]

class ChessBoard:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Chess Board")
        self.canvas = tk.Canvas(self.parent, width=400, height=400)
        self.canvas.pack()

        self.square_size = 50
        self.board_colors = ["white", "gray"]
        self.piece_symbols = {
            "wp": "♙",
            "wr": "♖",
            "wn": "♘",
            "wb": "♗",
            "wq": "♕",
            "wk": "♔",
            "bp": "♟",
            "br": "♜",
            "bn": "♞",
            "bb": "♝",
            "bq": "♛",
            "bk": "♚"
        }

        self.draw_board()
        self.add_piece_bindings()

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                x0 = col * self.square_size
                y0 = row * self.square_size
                x1 = x0 + self.square_size
                y1 = y0 + self.square_size
                color = self.board_colors[(row+col) % 2]
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
    
        for row in range(8):
            for col in range(8):
                piece = chess_board[row][col]
                if piece != "":
                    x0 = col * self.square_size
                    y0 = row * self.square_size
                    self.canvas.create_text(x0+self.square_size//2, y0+self.square_size//2, text=self.piece_symbols[piece], tags=(piece, "piece"), font=("Arial", 32))


    def add_piece_bindings(self):
        self.canvas.tag_bind("piece", "<ButtonPress-1>", self.on_piece_press)
        self.canvas.tag_bind("piece", "<ButtonRelease-1>", self.on_piece_release)
        self.canvas.tag_bind("piece", "<B1-Motion>", self.on_piece_motion)

    def on_piece_press(self, event):
        self.selected_piece = event.widget.find_closest(event.x, event.y)[0]
        self.selected_piece_offset = (event.x, event.y)

    def on_piece_release(self, event):
        self.selected_piece = None
        self.selected_piece_offset = None

    def on_piece_motion(self, event):
        if self.selected_piece:
            x, y = self.selected_piece_offset
            dx = event.x - x
            dy = event.y - y
            self.canvas.move(self.selected_piece, dx, dy)
            self.selected_piece_offset = (event.x, event.y)

root = tk.Tk()
chess = ChessBoard(root)
root.mainloop()
