from base_game import TicTacToe
from tkinter import Tk, Canvas, NW

class GraphicalGame(TicTacToe):
    def __init__(self):
        super().__init__()
        self.window_size = (600,600)
        self.root = Tk()
        self.cell_width = self.window_size[0] / self.size
        self.root.geometry(f"{self.window_size[0]}x{self.window_size[1]}")
        self.canvas = Canvas(self.root, width=self.window_size[0],
                             height=self.window_size[1])
        self.canvas.place(x=0, y=0, anchor=NW)
        self.game_over = False
        self.waiting = False
        self.draw_board()
        self.create_buttons()

    def draw_board(self):
        for i in range(self.window_size[0] - 1):
            self.canvas.create_line((i+1) * self.window_size[0] / self.size, 0,
                                    (i+1) * self.window_size[1] / self.size, self.window_size[0])
            self.canvas.create_line(0, (i+1) * self.window_size[0] / self.size,
                                    self.window_size[1], (i+1) * self.window_size[0] / self.size)

    def update_board(self):
        for row_num, row in enumerate(self.grid):
            for col_num, cell in enumerate(row):
                if cell == "X":
                    self.draw_x(row_num, col_num)
                if cell == "O":
                    self.draw_o(row_num, col_num)

    def draw_x(self, row_num, col_num):
        cell_center = (self.cell_width / 2 + row_num * self.cell_width,
                       self.cell_width / 2 + col_num * self.cell_width)
        points_left = [cell_center[0] - 50, cell_center[1] - 40, cell_center[0] - 40, cell_center[1] - 50,
                       cell_center[0] + 50, cell_center[1] + 40, cell_center[0] + 40, cell_center[1] + 50]
        points_right = [cell_center[0] + 50, cell_center[1] - 40, cell_center[0] + 40, cell_center[1] - 50,
                       cell_center[0] - 50, cell_center[1] + 40, cell_center[0] - 40, cell_center[1] + 50]
        self.canvas.create_polygon(points_left)
        self.canvas.create_polygon(points_right)
        self.canvas.update()

    def draw_o(self, row_num, col_num):
        cell_center = (self.cell_width / 2 + row_num * self.cell_width,
                       self.cell_width / 2 + col_num * self.cell_width)
        self.canvas.create_oval(cell_center[0] - 50, cell_center[1] - 50,
                                cell_center[0] + 50, cell_center[1] + 50, width=5)

    def is_valid_cell(self, row_num, col_num):
        return False if self.grid[row_num][col_num] != "_" else True

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                self.canvas.create_rectangle(i * self.cell_width, j * self.cell_width,
                                             (i + 1) * self.cell_width, (j + 1) * self.cell_width,
                                             tags="cell")
        self.canvas.update()
        self.canvas.bind("<Button-1>", self.clicked_cell)
        self.canvas.pack()

    def clicked_cell(self, event):
        if self.game_over or self.waiting:
            return
        row_pressed = int(event.x // self.cell_width)
        col_pressed = int(event.y // self.cell_width)
        if self.is_valid_cell(row_pressed, col_pressed):
            self.fill_cell("X", row_pressed, col_pressed)
            self.turn_count += 1
            self.update_board()
        self.get_AI_turn()
        self.waiting = True
        self.update_board()
        self.waiting = False
        self.winner = self.check_victory()
        if self.winner:
            self.game_over = True
            self.end_game()

    def end_game(self):
        self.canvas.create_text(self.window_size[0] //2,
                                self.window_size[1] // 2,
                                text=f"Game Over, {self.winner} won!",
                                fill="red",
                                font=("Helvetica", 32))
        self.canvas.update()



if __name__ == '__main__':
    ##run
    new_game = GraphicalGame()
    new_game.root.mainloop()