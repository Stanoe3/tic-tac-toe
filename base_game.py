import random

class TicTacToe():
    def __init__(self):
        self.size = 3
        self.players = ["Player", "Computer"]
        self.grid = [[None for y in range(self.size)]for x in range(self.size)]
        self.turn_count = 0
        self.player_symbol = input("Please enter your symbol: ")
        if self.player_symbol.lower() == "o":
            self.AI_symbol = "X"
        else:
            self.AI_symbol = "O"
        self.symbol_dict = {
            self.AI_symbol: "Computer",
            self.player_symbol: "Player"
        }

        self.play()

    def fill_cell(self, player_symbol, row, column):
        self.grid[row][column] = player_symbol

    def check_valid(self, row, column):
        if row >= self.size or column >= self.size:
            return False
        if self.grid[row][column] != None:
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
                return row[0]
        return False

    def check_vertical_victory(self):
        for col in [*zip(*self.grid)]:
            empty = False
            for cell in col:
                if not cell:
                    empty = True
                    break
            if empty:
                continue
            if max(col) == min(col):
                return col[0]
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
                return left_diag[0]
        if not right_diag_empty:
            if min(right_diag) == max(right_diag):
                return right_diag[0]
        return False

    def check_victory(self):
        if (self.check_diagonal_victory()
            or self.check_horizontal_victory()
            or self.check_vertical_victory()):
            return self.check_diagonal_victory()
        return False

    def play(self):
        while not self.check_victory():
            current_player = self.players[self.turn_count % 2]
            if current_player == "Player":
                self.get_player_turn()
            else:
                self.get_AI_turn()
            self.turn_count += 1
            print(self.grid)
        winning_symbol = self.check_victory()
        print(f"Congratulations {self.symbol_dict[winning_symbol]}! You win!")



    def get_player_turn(self):
        valid = False
        while not valid:
            row = -1 +int(input("Please enter the row: "))
            column = -1 + int(input("Please enter the column: "))
            valid = self.check_valid(row, column)
        self.fill_cell(self.player_symbol, row, column)


    def get_AI_turn(self):
        valid = False
        while not valid:
            row = random.randint(0,2)
            column = random.randint(0,2)
            valid = self.check_valid(row, column)
        self.fill_cell(self.AI_symbol, row, column)





if __name__ == '__main__':
    tic = TicTacToe()


