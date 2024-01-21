#__________________________________________________________________________________________________________
#                             Quantum Tic-Tac-Toe

import qiskit
from qiskit import BasicAer
from qiskit import QuantumCircuit, execute
from qiskit.circuit.library import XGate, HGate
import enum

class QuantumSquare:
    def __init__(self, state_name, circuit):
        self.state_name = state_name
        self.circuit = circuit
        self.is_empty = True if state_name == 'EMPTY' else False

    def apply_gate(self, gate):
        self.circuit.append(gate, [0])
        self.is_empty = False  # Set is_empty to False when a gate is applied
        if isinstance(gate, XGate):
            self.state_name = 'X'
        elif isinstance(gate, HGate):
            self.state_name = 'O'

    def measure(self):
        if not self.is_empty:  # Only perform a measurement if a move has been made
            self.circuit.measure([0], [0])
            backend = BasicAer.get_backend('qasm_simulator')
            job = execute(self.circuit, backend, shots=1)
            result = job.result()
            counts = result.get_counts(self.circuit)
            measured_state = max(counts, key=counts.get)
            if measured_state == '0':
                return 'O'
            elif measured_state == '1':
                return 'X'
        else:
            return '-'  # Return '-' for EMPTY

    def get_state(self):
        if self.is_empty:
            return '-'
        else:
            return self.state_name
        
    def get_state_with_measurement(self):
        if self.is_empty:
            return '-'
        else:
            return self.measure()

class QuantumTicTacSquare(enum.Enum):
    EMPTY = QuantumSquare('EMPTY', QuantumCircuit(1, 1))  # |0> state
    X = QuantumSquare('X', QuantumCircuit(1, 1))  # |1> state
    X.circuit.append(XGate(), [0])  # Apply X gate at initialization
    O = QuantumSquare('O', QuantumCircuit(1, 1))  # |+> state
    O.circuit.append(HGate(), [0])  # Apply H gate at initialization
    DRAW = 'Because the game ended in a draw!'

class QuantumTicTacToe: 
    def __init__(self):
        self.board = [
            [QuantumSquare(QuantumTicTacSquare.EMPTY.value.state_name, QuantumCircuit(1, 1)) for _ in range(3)],
            [QuantumSquare(QuantumTicTacSquare.EMPTY.value.state_name, QuantumCircuit(1, 1)) for _ in range(3)],
            [QuantumSquare(QuantumTicTacSquare.EMPTY.value.state_name, QuantumCircuit(1, 1)) for _ in range(3)],
        ]
        self.turn = QuantumTicTacSquare.X
        self.winner = QuantumTicTacSquare.EMPTY
        self.backend = BasicAer.get_backend('statevector_simulator')

    def game_controller(self):
        self.decide_turn()
        while self.winner == QuantumTicTacSquare.EMPTY: #goes until Winner is found
            self.take_your_turn() #Takes current player turn
            self.print_board()
            self.check_draw()
            self.check_winner()
            self.switch_turn()
        return self.winner
    
    def decide_turn(self):
        if input(f'The starting turn is currently Player {self.turn.name} Would you like to change it to {'O' if self.turn == QuantumTicTacSquare.X else 'X'}\nEnter Yes or No\n').lower() == 'yes':
            self.switch_turn()
        print(f'The current turn is: {self.turn.name}')

    def switch_turn(self):
        if self.turn == QuantumTicTacSquare.X:
            self.turn = QuantumTicTacSquare.O
        else:
            self.turn = QuantumTicTacSquare.X
    
    def take_your_turn(self):
        valid_move = False
        while not valid_move:
            placement = input(f'Where would you like to place your {self.turn.name} (Input it row column with a space separating them)').strip().split()
            row, col = int(placement[0]), int(placement[1])
            if 0 <= row <= 2 and 0 <= col <= 2:
                if self.board[row][col].is_empty:  # Check if the square is empty
                    valid_move = True
                else:
                    print('INVALID MOVE CHOSEN!\nMake sure you are picking a spot that is unchosen already')
            else:
                print('INVALID MOVE CHOSEN!\nMake sure you are picking a spot that is on the board')
        if self.turn == QuantumTicTacSquare.X:
            self.board[row][col].apply_gate(XGate())  # Apply X gate for player X
        else:
            self.board[row][col].apply_gate(HGate())  # Apply H gate for player O
        self.check_winner()  # Check for a winner after each move


    def check_winner(self):
        for index, row_column in enumerate(self.board):
            self.check_row(index)
            self.check_column(index)
        self.check_diagonal()

    def check_row(self, row_check):
        row_state = [self.board[row_check][i].get_state() for i in range(3)]
        if all(state != '-' for state in row_state) and all(state == 'X' for state in row_state):  # All X
            self.winner = QuantumTicTacSquare.X
        elif all(state != '-' for state in row_state) and all(state == 'O' for state in row_state):  # All O
            self.winner = QuantumTicTacSquare.O

    def check_column(self, column_check):
        column_state = [self.board[i][column_check].get_state() for i in range(3)]
        if all(state != '-' for state in column_state) and all(state == 'X' for state in column_state):  # All X
            self.winner = QuantumTicTacSquare.X
        elif all(state != '-' for state in column_state) and all(state == 'O' for state in column_state):  # All O
            self.winner = QuantumTicTacSquare.O

    def check_diagonal(self):
        diagonal1_state = [self.board[i][i].get_state() for i in range(3)]
        diagonal2_state = [self.board[i][2-i].get_state() for i in range(3)]
        if (all(state != '-' for state in diagonal1_state) and all(state == 'X' for state in diagonal1_state)) or \
           (all(state != '-' for state in diagonal2_state) and all(state == 'X' for state in diagonal2_state)):  # All X
            self.winner = QuantumTicTacSquare.X
        elif (all(state != '-' for state in diagonal1_state) and all(state == 'O' for state in diagonal1_state)) or \
             (all(state != '-' for state in diagonal2_state) and all(state == 'O' for state in diagonal2_state)):  # All O
            self.winner = QuantumTicTacSquare.O

    def check_draw(self):
        for row in self.board:
            for square in row:
                if square.is_empty:  # If any square is empty
                    return
        self.winner = QuantumTicTacSquare.DRAW  # If all squares are filled, it's a draw

    def print_board(self):
        for row in self.board:
            for square in row:
                print(f'{square.get_state()} ', end='')
            print()

game = QuantumTicTacToe()
game.game_controller()
print(f'Player {game.winner.name} is the winner of Quantum TicTacToe! {QuantumTicTacSquare.DRAW.value if game.winner == QuantumTicTacSquare.DRAW else ""}')
#__________________________________________________________________________________________________________