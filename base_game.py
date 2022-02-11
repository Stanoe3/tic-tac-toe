class TicTacToe():
    def __init__(self):
        self.size = 3
        self.grid = [[None for y in range(self.size)]for x in range(self.size)]
        self.turn_count = 0

    def fill_cell(self, player_symbol, row, column):
        self.grid[row][column] = player_symbol

    def checkValid(self, row, column):
        if row >= self.size or column >= self.size:
            return False
        if self.grid[row][column]:
            return False
        return True


    def check_horizontal_victory(self):
        for row in self.grid:
            empty = False
            for cell in row:
                if not cell:
                    empty = True
                    break
            if empty:
                continue
            if max(row) == min(row):
                return True
        return False

    def check_vertical_victory(self):
        for row in [*zip(*self.grid)]:
            empty = False
            for cell in row:
                if not cell:
                    empty = True
                    break
            if empty:
                continue
            if max(row) == min(row):
                return True
        return False



if __name__ == '__main__':
    tic = TicTacToe()
    tic.fill_cell("x",1,0)
    tic.fill_cell("x",1,1)
    #tic.fill_cell("x",1,2)
    tic.fill_cell("x",0,1)
    tic.fill_cell("x",2,1)


