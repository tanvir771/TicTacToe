# Driver File

import pygame

from Grid import Grid
from Circle import Circle
from Cross import Cross


background_colour = (0, 0, 0)

(width, height) = (600, 600)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('TicTacToe')
screen.fill(background_colour)

state = {}


grid = Grid(screen, width, height)
circle = Circle()
cross = Cross()

pygame.init()
font = pygame.font.Font(None, 100)

def labelWinner(winner):
  # render text
  if winner == 0:
    winner = "O"
  else:
    winner = "X"

  return "Winner is {}!".format(winner)



def get_placement(pos, width, height):
  grid_numbers = {(200, 200): 1, (400, 200):2, (600, 200): 3}
  row = 0
  column = 0

  x = pos[0]
  y = pos[1]

  print("x y", x, y)

  if x < width*1/3:
    column = 1
  elif x < width*2/3:
    column = 2
  else:
    column = 3

  if y < height*1/3:
    row = 1
  elif y <= height*2/3:
    row = 2
  else:
    row = 3

  return (row, column)


grid.drawGrid()
pygame.display.flip()


running = True
flip = True

playing = True

while running:
  event = pygame.event.get()

  for ev in event:
    # proceed events
    # handles game quit
    winner = -1
    if ev.type == pygame.QUIT:
      running = False
    # handle MOUSEBUTTONUP
    if playing == True:
      if ev.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        (row, column) = get_placement(pos, width, height)
        print(row, column)
        if flip:
          # we will let the player be 0
          #  9 represents empty, 0 represents circle and 1 represents X
          # start with circle, so 0 in third parameteer of updateGrid
          grid.updateGrid(row-1, column-1, 0)
          winner = grid.redrawGrid(circle, cross)
          flip = False
        else:
          grid.updateGrid(row-1, column-1, 1)
          winner = grid.redrawGrid(circle, cross)
          flip = True

        print("winner value ", winner)
        if winner != -1:
          text = labelWinner(winner)
          label = font.render(text, True, (255, 255, 255))
          labelRect = label.get_rect(center=(width // 2, height // 2))
          screen.blit(label, labelRect)
          playing = False
        pygame.display.update()

      if playing == False:
        pygame.display.flip()

#make sure that scroll wheel does not trigger pygame to draw
#we need a current state dictionary to store the state of the game, use that to draw cross/circles; if state already has
#box stored, no more crosses/circles can be drawn on that box