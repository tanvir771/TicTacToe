import pygame

background_colour = (0, 0, 0)

(width, height) = (600, 600)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('TicTacToe')
screen.fill(background_colour)

def draw_grid(width, height):
  # draws a grid with 3 vertical and 3 horizontal lines
  pygame.draw.line(screen, (255, 255, 255), (width*1/3, 0), (width*1/3, 600))
  pygame.draw.line(screen, (255, 255, 255), (width*2/3, 0), (width*2/3, 600))
  pygame.draw.line(screen, (255, 255, 255), (width, 0), (width, 600))

  pygame.draw.line(screen, (255, 255, 255), (0, height*1/3), (600, height*1/3))
  pygame.draw.line(screen, (255, 255, 255), (0, height*2/3), (600, height*2/3))
  pygame.draw.line(screen, (255, 255, 255), (0, height), (600, height))

def get_placement(pos, width, height):
  grid_numbers = {(200, 200): 1, (400, 200):2, (600, 200): 3}
  box_x = 0
  box_y = 0

  x = pos[0]
  y = pos[1]
  if x < width*1/3:
    box_x = 1
  elif x < width*2/3:
    box_x = 2
  else:
    box_x = 3

  if y < height*1/3:
    box_y = 1
  elif y <= height*2/3:
    box_y = 2
  else:
    box_y = 3

  return (box_x, box_y)



def draw_cross(placement):
  pygame.draw.line(screen, (255, 255, 255), ((placement[0]-1)*width/3, (placement[1]-1)*height/3), (placement[0]*height/3, placement[1]*width/3))
  pygame.draw.line(screen, (255, 255, 255), ((placement[0])*width/3, (placement[1]-1)*height/3), ((placement[0]-1)*height/3, (placement[1])*width/3))

def draw_circle(placement):
  pygame.draw.circle(screen, (255, 255, 255), (((placement[0]-1)*width/3 + (width/6)), ((placement[1]-1)*height/3) + (height/6)), width/6, width=10)
  # last width is pygame.draw.circle's argument, width=0 by default, which gives filled in circle

draw_grid(width, height)
pygame.display.flip()


running = True
while running:
  # for event in pygame.event.get():
    # get all events
    event = pygame.event.get()
    # proceed events
    for ev in event:
      # handles game quit
      if ev.type == pygame.QUIT:
        running = False
      # handle MOUSEBUTTONUP
      if ev.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        draw_circle(get_placement(tuple(pos), width, height))
        pygame.display.update()