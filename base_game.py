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

    def check_diagonal_victory(self):
        left_diag = []
        right_diag = []
        left_diag_empty = False
        right_diag_empty = False
        for row_index in range(self.size):
            left_diag.append(self.grid[row_index][row_index])
            right_diag.append(self.grid[self.size-row_index-1][row_index])
        for left_cell in left_diag:
            if not left_cell:
                left_diag_empty = True
        for right_cell in right_diag:
            if not right_cell:
                right_diag_empty = True
        if right_diag_empty and left_diag_empty:
            return False
        if not left_diag_empty:
            if min(left_diag) == max(left_diag):
                return True
        if not right_diag_empty:
            if min(right_diag) == max(right_diag):
                return True
        return False

    def check_victory(self):
        if (self.check_diagonal_victory()
            or self.check_horizontal_victory()
            or self.check_vertical_victory()):
            return True
        return False





if __name__ == '__main__':
    tic = TicTacToe()
    tic.fill_cell("x",1,0)
    tic.fill_cell("x",1,1)
    tic.fill_cell("x", 0, 2)
    #tic.fill_cell("x",1,2)
    tic.fill_cell("x",0,1)
    tic.fill_cell("x",2,1)
    tic.fill_cell("x",2,0)
    print(tic.grid)
    print(tic.check_victory())


