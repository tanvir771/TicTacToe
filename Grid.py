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
        # takes a grid of its own
        for row in grid:
            if len(set(row)) == 1 and row[0] != 9:
                # 9 9 9 should not mean anyone won
                return row[0]
        return -1

    def checkDiagoanlsWinner(self):
        # Checks both diagonals for winners
        if len(set([self.grid[i][i] for i in range(len(self.grid))])) == 1 and self.grid[0][0] != 9:
            return self.grid[0][0]
        if len(set([self.grid[i][len(self.grid) - i - 1] for i in range(len(self.grid))])) == 1 and self.grid[0][
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
        if self.grid[row][column] == 9:
            self.grid[row][column] = x

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

    def make_best_move(self, player):
        # player - 0 representing O and 1 representing x
        bestScore = -9999
        bestMove = (0, 0)
        for rowIndex in range(len(self.grid)):
            for columnIndex in range(len(self.grid[rowIndex])):
                if self.grid[rowIndex][columnIndex] == 9:  # represents empty
                    self.grid[rowIndex][columnIndex] = player
                    score = self.minimax(player, self.grid)
                    self.grid[rowIndex][columnIndex] = 9  # undo move
                    if score > bestScore:
                        bestScore = score
                        bestMove = (rowIndex, columnIndex)
        self.grid[bestMove[0]][bestMove[1]] = player

    def minimax(self, maximizerPlayer, board):
        winner = self.check_winner()
        if winner == -1:
            # draw
            return 0
        elif winner == 0 or winner == 1:
            if winner == maximizerPlayer:
                return 1
            else:
                return -1

        scores = []
        for rowIndex in range(len(self.grid)):
            for columnIndex in range(len(self.grid[rowIndex])):
                if board[rowIndex][columnIndex] == 9:  # represents empty
                    self.grid[rowIndex][columnIndex] = maximizerPlayer
                    scores.append(self.minimax(maximizerPlayer, board))
                    self.grid[rowIndex][columnIndex] = 9  # undo move

        return max(scores)
