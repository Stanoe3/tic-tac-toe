import random

class TicTacToe():
    def __init__(self):
        self.size = 3
        self.players = ["Player", "Computer"]
        self.grid = [["_" for y in range(self.size)]for x in range(self.size)]
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
        if self.grid[row][column] != "_":
            return False
        return True

    def check_horizontal_victory(self):
        for row in self.grid:
            empty = False
            for cell in row:
                if cell == "_":
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
                if cell == "_":
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
            if left_cell == "_":
                left_diag_empty = True
        for right_cell in right_diag:
            if right_cell == "_":
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
            return (self.check_diagonal_victory()
                or self.check_horizontal_victory()
                or self.check_vertical_victory())
        # print(f"Check Diagonal {self.check_diagonal_victory()}")
        # print(f"Check Horizontal {self.check_horizontal_victory()}")
        # print(f"Check Vertical {self.check_vertical_victory()}")
        return False

    def play(self):
        draw = False
        while not self.check_victory() and self.moves_left():
            current_player = self.players[self.turn_count % 2]
            if current_player == "Player":
                self.get_player_turn()
                print(f"Check Diagonal {self.check_diagonal_victory()}")
                print(f"Check Horizontal {self.check_horizontal_victory()}")
                print(f"Check Vertical {self.check_vertical_victory()}")
            else:
                self.get_AI_turn()
            self.turn_count += 1
            for row in self.grid:
                print(row)
        winning_symbol = self.check_victory()
        if not winning_symbol:
            print(f"It's a draw!")
        else:
            print(f"Congratulations {self.symbol_dict[winning_symbol]}! You win!")

    def get_player_turn(self):
        valid = False
        while not valid:
            row = -1 +int(input("Please enter the row: "))
            column = -1 + int(input("Please enter the column: "))
            valid = self.check_valid(row, column)
        self.fill_cell(self.player_symbol, row, column)


    def get_AI_turn(self):
        move = self.find_best_move(self.grid)
        if self.check_valid(move[0], move[1]):
            self.fill_cell(self.AI_symbol, move[0], move[1])
        else:
            pass

    def moves_left(self):
        for row in self.grid:
            for cell in row:
                if cell == "_":
                    return True
        return False

    def minimax(self, board, depth, is_max):
        if self.check_victory() == self.player_symbol:
            score = -10
            return score
        if self.check_victory() == self.AI_symbol:
            score = 10
            return score
        else:
            score = 0

        if not self.moves_left():
            return 0

        if is_max:
            best_value = -100
            for row_num in range(self.size):
                for col_num in range(self.size):
                    if board[row_num][col_num] == "_":
                        board[row_num][col_num] = self.AI_symbol

                        best_value = max(best_value, self.minimax(board,
                                                                  depth+1,
                                                                  not is_max))
                        board[row_num][col_num] = "_"
            return best_value
        else:
            best_value = 1000

            for row_num in range(self.size):
                for col_num in range(self.size):
                    if board[row_num][col_num] == "_":
                        board[row_num][col_num] = self.player_symbol

                        best_value = min(best_value, self.minimax(board,
                                                                  depth+1,
                                                                  not is_max))
                        board[row_num][col_num] = "_"
            return best_value

    def find_best_move(self, board):
        best_value = -1000
        best_move = (-1, -1)

        for row_num in range(self.size):
            for col_num in range(self.size):
                if board[row_num][col_num] == "_":
                    board[row_num][col_num] = self.AI_symbol
                    move_value = self.minimax(board, 0, False)
                    board[row_num][col_num] = "_"
                    if move_value > best_value:
                        best_move = (row_num, col_num)
                        best_value = move_value
        return best_move


if __name__ == '__main__':
    tic = TicTacToe()


