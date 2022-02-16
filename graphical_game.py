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
        self.draw_board()
        self.grid[0][0] = "O"
        self.update_board()

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
                                cell_center[1] + 50, cell_center[1] + 50, width=5)

    def is_valid_cell(self, row_num, col_num):
        return False if self.grid[row_num][col_num] != "_" else True


if __name__ == '__main__':
    ##run
    new_game = GraphicalGame()
    new_game.root.mainloop()