import pygame
import sys
import time

# =============================
# SOLVER
# =============================

class SudokuSolver:
    def __init__(self, board):
        self.board = board

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return i, j
        return None

    def is_valid(self, num, row, col):
        if num in self.board[row]:
            return False
        if num in [self.board[i][col] for i in range(9)]:
            return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.board[i][j] == num:
                    return False
        return True

    def solve(self):
        empty = self.find_empty()
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

# =============================
# GUI
# =============================

class SudokuGUI:
    def __init__(self):
        pygame.init()
        self.size = 540
        self.cell = self.size // 9
        self.screen = pygame.display.set_mode((self.size, self.size + 60))
        pygame.display.set_caption("Sudoku Solver")
        self.font = pygame.font.SysFont("arial", 36)
        self.small = pygame.font.SysFont("arial", 22)

        self.board = [[0]*9 for _ in range(9)]
        self.fixed = [[False]*9 for _ in range(9)]
        self.selected = None
        self.message = "Edita el tablero y presiona ENTER"

    # =============================
    # VALIDACIÓN PREVIA
    # =============================
    def validar_tablero(self):
        for i in range(9):
            fila = [n for n in self.board[i] if n != 0]
            if len(fila) != len(set(fila)):
                return False

            col = [self.board[r][i] for r in range(9) if self.board[r][i] != 0]
            if len(col) != len(set(col)):
                return False

        for box_y in range(0, 9, 3):
            for box_x in range(0, 9, 3):
                nums = []
                for i in range(3):
                    for j in range(3):
                        val = self.board[box_y+i][box_x+j]
                        if val != 0:
                            nums.append(val)
                if len(nums) != len(set(nums)):
                    return False
        return True

    # =============================
    # DIBUJO
    # =============================
    def draw(self):
        self.screen.fill((255, 255, 255))

        for i in range(10):
            thick = 4 if i % 3 == 0 else 1
            pygame.draw.line(self.screen, (0,0,0), (0, i*self.cell), (self.size, i*self.cell), thick)
            pygame.draw.line(self.screen, (0,0,0), (i*self.cell, 0), (i*self.cell, self.size), thick)

        for r in range(9):
            for c in range(9):
                if self.board[r][c] != 0:
                    color = (0,0,0) if self.fixed[r][c] else (0,0,200)
                    text = self.font.render(str(self.board[r][c]), True, color)
                    self.screen.blit(text, (c*self.cell+20, r*self.cell+10))

        if self.selected:
            r, c = self.selected
            pygame.draw.rect(self.screen, (255,0,0),
                             (c*self.cell, r*self.cell, self.cell, self.cell), 3)

        info = self.small.render(self.message, True, (0,0,0))
        self.screen.blit(info, (10, self.size + 15))
        pygame.display.update()

    # =============================
    # GUARDAR SOLUCIÓN
    # =============================
    def guardar_solucion(self):
        with open("sudoku_solucion.txt", "w") as f:
            for fila in self.board:
                f.write(" ".join(map(str, fila)) + "\n")
        self.message = "Solución guardada en sudoku_solucion.txt"

    # =============================
    # LOOP PRINCIPAL
    # =============================
    def run(self):
        solver = SudokuSolver(self.board)
        running = True

        while running:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if y < self.size:
                        self.selected = (y // self.cell, x // self.cell)

                if event.type == pygame.KEYDOWN:
                    if self.selected:
                        r, c = self.selected
                        if not self.fixed[r][c]:
                            if event.key in range(pygame.K_1, pygame.K_9+1):
                                self.board[r][c] = event.key - pygame.K_0
                            if event.key in (pygame.K_BACKSPACE, pygame.K_0):
                                self.board[r][c] = 0

                    if event.key == pygame.K_RETURN:
                        if not self.validar_tablero():
                            self.message = "❌ Error: tablero inválido"
                        else:
                            self.fixed = [[self.board[r][c] != 0 for c in range(9)] for r in range(9)]
                            if solver.solve():
                                self.message = "✔ Resuelto | S para guardar"
                            else:
                                self.message = "❌ No tiene solución"

                    if event.key == pygame.K_s:
                        self.guardar_solucion()

                    if event.key == pygame.K_ESCAPE:
                        running = False

        pygame.quit()
        sys.exit()

# =============================
# MAIN
# =============================
if __name__ == "__main__":
    SudokuGUI().run()