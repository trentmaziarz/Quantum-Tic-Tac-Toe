#__________________________________________________________________________________________________________
# The following code is just a traditional tic-tac-toe game developed in Python (We aren't Quantum yet!)
#__________________________________________________________________________________________________________
#                             Traditional Tic-Tac-Toe

import enum

class TicTacSquare(enum.Enum):
    EMPTY = 0
    X = 1
    O = 2
    DRAW = 'Because the game ended in a draw!'

class TicTacToe:
    def __init__(self):
        self.board = [
            [TicTacSquare.EMPTY, TicTacSquare.EMPTY, TicTacSquare.EMPTY],
            [TicTacSquare.EMPTY, TicTacSquare.EMPTY, TicTacSquare.EMPTY],
            [TicTacSquare.EMPTY, TicTacSquare.EMPTY, TicTacSquare.EMPTY],
        ]
        self.turn = TicTacSquare.X
        self.winner = TicTacSquare.EMPTY

    def game_controller(self):
        self.decide_turn()
        while self.winner == TicTacSquare.EMPTY: #goes until Winner is found
            self.take_your_turn() #Takes current player turn
            self.print_board()
            self.check_draw()
            self.check_winner()
            self.switch_turn()
        return self.winner
    
    def decide_turn(self):
        if input(f'The starting turn is currently Player {self.turn.name} Would you like to change it to {'O' if self.turn == TicTacSquare.X else 'X'}\nEnter Yes or No\n').lower() == 'yes':
            self.switch_turn()

    def switch_turn(self):
        if self.turn == TicTacSquare.X: #Switches between each players turn
                self.turn = TicTacSquare.O
        else:
                self.turn = TicTacSquare.X

    def take_your_turn(self):
        valid_move = False
        while not valid_move:
            placement = input(f'Where would you like to place your {self.turn.name} (Input it row column with a space separating them)').strip().split()
            row, col = int(placement[0]), int(placement[1])
            if 0 <= row <= 2 and 0 <= col <= 2:
                if self.board[row][col] == TicTacSquare.EMPTY:
                    valid_move = True
                else:
                    print('INVALID MOVE CHOSEN!\nMake sure you are picking a spot that is unchosen already')
            else:
                print('INVALID MOVE CHOSEN!\nMake sure you are picking a spot that is on the board')
        self.board[row][col] = self.turn
        self.check_winner()

    def check_winner(self):
        for index, row_column in enumerate(self.board):
            self.check_row(index)
            self.check_column(index)
        self.check_diagnol()

    def check_row(self, row_check):
        if self.board[row_check][0] == self.board[row_check][1] == self.board[row_check][2] != TicTacSquare.EMPTY:
            self.winner = self.turn

    def check_column(self, column_check):
        if self.board[0][column_check] == self.board[1][column_check] == self.board[2][column_check] != TicTacSquare.EMPTY:
            self.winner = self.turn

    def check_diagnol(self):
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != TicTacSquare.EMPTY:
            self.winner = self.turn
        elif self.board[0][2] == self.board[1][1] and self.board[2][0] != TicTacSquare.EMPTY:
            self.winner = self.turn

    def check_draw(self):
        counter = 0
        for row in self.board:
            for value in row:
                if value != TicTacSquare.EMPTY:
                    counter += 1
                if counter == 9:
                    self.winner = TicTacSquare.DRAW

    def print_board(self):
        for row in self.board:
            for value in row:
                print('-' if value == TicTacSquare.EMPTY else value.name, end=' ')
            print()

game = TicTacToe()
game.game_controller()
print(f'Player {game.winner.name} is the winner of TicTacToe! {TicTacSquare.DRAW.value if game.winner == TicTacSquare.DRAW else ""}')

#__________________________________________________________________________________________________________