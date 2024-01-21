# Quantum Tic-Tac-Toe

This Python script uses the Qiskit library to implement a game of Quantum Tic-Tac-Toe.

## Overview

The game is played on a 3x3 board, similar to traditional Tic-Tac-Toe. However, instead of 'X' and 'O', the players place quantum gates on the board. The state of each square on the board is determined by a quantum bit (qubit), which can be in a superposition of states.

## Classes

The script defines several classes:

- `QuantumSquare`: Represents a square on the game board. Each square has a quantum circuit with one qubit. The square's state is determined by the state of this qubit.

- `QuantumTicTacSquare`: An enumeration that represents the possible states of a square in the game. It includes the states 'EMPTY', 'X', and 'O', as well as a 'DRAW' state.

- `QuantumTicTacToe`: Represents a game of Quantum Tic-Tac-Toe. It includes methods to control the game flow, decide the turn, switch turns, and take turns. The `game_controller` method is the main game loop, which continues until a winner is found or the game ends in a draw.

## Usage

To play the game, run the script. The game will start automatically. The script will prompt you to enter the row and column where you want to place your quantum gate. The game continues until there's a winner or all squares are filled (in which case, the game is a draw).

## Play Setup

The game is played on a 3x3 grid, as shown below:
```
   0 1 2
0 - - -
1 - - -
2 - - -
```
Each cell in the grid can be identified by its row and column numbers. The top-left cell is (0, 0), the top-right cell is (0, 2), the bottom-left cell is (2, 0), and the bottom-right cell is (2, 2).

To place your 'X' or 'O' on the board, you need to specify the row and column numbers of the cell where you want to place your mark. For example, to place your mark in the top-left cell, you would type `0 0`. The first number is the row, and the second number is the column.


## Dependencies

This script requires the Qiskit library for quantum computing. You can install it using pip:

```bash
pip install qiskit
```
## Running the Script

This script was developed and tested using a virtual environment in Visual Studio Code. To run the script, you may need to set up a similar environment. Here’s how you can do it:

1. Create a new virtual environment: `python -m venv .venv`
2. Activate the virtual environment:
   - On Windows: `.venv\Scripts\activate`
   - On Unix or MacOS: `source .venv/bin/activate`
3. Install the required packages: `pip install -r requirements.txt`
4. Run the script: `python quantum_tictactoe.py`

# Traditional Tic-Tac-Toe

This repository also includes a script for a traditional game of Tic-Tac-Toe. This game is included for comparison purposes, to highlight the differences between traditional and quantum games.

## Overview

The traditional game of Tic-Tac-Toe is played on a 3x3 board. Players take turns placing 'X' and 'O' on the board. The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner. If all squares are filled and no player has won, the game is a draw.

## Usage

To play the traditional game of Tic-Tac-Toe, run the corresponding script. The game will start automatically. The script will prompt you to enter the row and column where you want to place your mark. The game continues until there’s a winner or all squares are filled (in which case, the game is a draw).
