import pygame

background_colour = (0, 0, 0)

(width, height) = (600, 600)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('TicTacToe')
screen.fill(background_colour)

pygame.draw.line(screen, (255, 255, 255), (200, 0), (200, 600))
pygame.draw.line(screen, (255, 255, 255), (400, 0), (400, 600))
pygame.draw.line(screen, (255, 255, 255), (600, 0), (600, 600))

pygame.draw.line(screen, (255, 255, 255), (0, 200), (600, 200))
pygame.draw.line(screen, (255, 255, 255), (0, 400), (600, 400))
pygame.draw.line(screen, (255, 255, 255), (0, 600), (600, 600))


pygame.display.flip()


running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False