# Implements a Grid to use for TicTacToe game
import pygame


class Grid:
    """A simple, 3x3 grid that has a state and a method to draw it onscreen"""

    def __init__(self, screen, width, height):
        # Grid - 9 represents empty, 0 represents circle and 1 represents X
        # Using lists because order matters
        self.grid = [[9, 9, 9],
                     [9, 9, 9],
                     [9, 9, 9]]
        self.screen = screen
        self.width = width
        self.height = height

    def checkRowsWinner(self, grid):
        # Check rows for winner
        for row in self.grid:
            if len(set(row)) == 1 and row[0] != 9:
                # 9 9 9 should not mean anyone won
                return row[0]
        return -1

    def checkDiagoanlsWinner(self):
        # Checks both diagonals for winners
        if len(set([self.grid[i][i] for i in range(len(self.grid))])) == 1 and self.grid[0][0] != 9:
            return self.grid[0][0]
        if len(set([self.grid[i][len(self.grid) - i - 1] for i in range(len(self.grid))])) == 1 and self.grid[2][
            2] != 9:
            return self.grid[0][len(self.grid) - 1]
        return -1

    def check_winner(self):
        winner = self.checkRowsWinner(self.grid)
        if winner == -1:
            winner = self.checkDiagoanlsWinner()
        if winner == -1:
            # Checks columns by transposing grid
            winner = self.checkRowsWinner(list(zip(*self.grid)))

        return winner

    def updateGrid(self, row, column, x):
        # row and column for grid
        # x takes values, 9, 0 or 1; 9 represents empty, 0 represents circle and 1 represents X
        if self.grid[column][row] == 9:
            self.grid[column][row] = x

    def drawGrid(self):
        # draws a grid with 3 vertical and 3 horizontal lines
        pygame.draw.line(self.screen, (255, 255, 255), (self.width * 1 / 3, 0), (self.width * 1 / 3, 600))
        pygame.draw.line(self.screen, (255, 255, 255), (self.width * 2 / 3, 0), (self.width * 2 / 3, 600))
        pygame.draw.line(self.screen, (255, 255, 255), (self.width, 0), (self.width, 600))

        pygame.draw.line(self.screen, (255, 255, 255), (0, self.height * 1 / 3), (600, self.height * 1 / 3))
        pygame.draw.line(self.screen, (255, 255, 255), (0, self.height * 2 / 3), (600, self.height * 2 / 3))
        pygame.draw.line(self.screen, (255, 255, 255), (0, self.height), (600, self.height))

    def redrawGrid(self, circle, cross):
        # circle - an instance of Circle class
        # cross - an instance of Cross class
        # Updates the grid based on the state of the grid
        # Grid broken into {(200, 200): 1, (400, 200):2, (600, 200): 3}
        for i in range(1, 4):
            for j in range(1, 4):
                if self.grid[i - 1][j - 1] == 0:
                    circle.Draw(self.screen, (i, j), self.width, self.height)
                elif self.grid[i - 1][j - 1] == 1:
                    cross.Draw(self.screen, (i, j), self.width, self.height)

        winner = self.check_winner()
        return winner
