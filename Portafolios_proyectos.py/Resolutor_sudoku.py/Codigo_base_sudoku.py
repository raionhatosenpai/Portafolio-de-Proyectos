'''Utiliza la biblioteca pygame (consulta las instrucciones de instalación de pip) para 
implementar una interfaz gráfica (GUI) que resuelve automáticamente los rompecabezas de 
Sudoku. 
Para resolver un rompecabezas de Sudoku, puedes crear un programa que utilice un algoritmo 
de retroceso (backtracking) que verifica incrementalmente soluciones, adoptando o 
abandonando la solución actual si no es viable. 
Este paso de abandonar una solución es la característica definitoria de un enfoque de 
retroceso, ya que el programa retrocede para probar una nueva solución hasta que encuentra 
una válida. Este proceso se lleva a cabo de manera incremental hasta que todo el tablero se 
haya completado correctamente.'''

import pygame
import sys
import time
import numpy as np

class SudokuSolver:
    def __init__(self, board):
        self.board = board
        self.size = 9
        self.subgrid_size = 3

    def is_valid(self, num, row, col):
        for x in range(self.size):
            if self.board[row][x] == num or self.board[x][col] == num:
                return False

        start_row = row - row % self.subgrid_size
        start_col = col - col % self.subgrid_size
        for i in range(self.subgrid_size):
            for j in range(self.subgrid_size):
                if self.board[i + start_row][j + start_col] == num:
                    return False
        return True

    def solve(self):
        empty = self.find_empty_location()
        if not empty:
            return True
        row, col = empty

        for num in range(1, 10):
            if self.is_valid(num, row, col):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = 0
        return False

    def find_empty_location(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return (i, j)
        return None
    
class SudokuGUI:
    def __init__(self, board):
        pygame.init()
        self.board = board
        self.solver = SudokuSolver(board)
        self.size = 540
        self.cell_size = self.size // 9
        self.screen = pygame.display.set_mode((self.size, self.size))
        pygame.display.set_caption("Sudoku Solver")
        self.font = pygame.font.SysFont("comicsans", 40)

    def draw_board(self):
        self.screen.fill((255, 255, 255))
        for i in range(10):
            thickness = 4 if i % 3 == 0 else 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * self.cell_size), (self.size, i * self.cell_size), thickness)
            pygame.draw.line(self.screen, (0, 0, 0), (i * self.cell_size, 0), (i * self.cell_size, self.size), thickness)

        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    text = self.font.render(str(self.board[i][j]), True, (0, 0, 0))
                    self.screen.blit(text, (j * self.cell_size + 15, i * self.cell_size + 10))

    def update_board(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    text = self.font.render(str(self.board[i][j]), True, (0, 0, 255))
                    self.screen.blit(text, (j * self.cell_size + 15, i * self.cell_size + 10))
                    pygame.display.update()
                    time.sleep(0.05)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw_board()
            pygame.display.update()

            if self.solver.solve():
                self.update_board()
                time.sleep(2)
                running = False

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    sample_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    gui = SudokuGUI(sample_board)
    gui.run()