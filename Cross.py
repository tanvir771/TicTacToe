# Implements a Cross Element

import pygame


class Cross:

    def __int__(self):
        self.state = 0

    def Draw(self, screen, placement, width, height):
        # placement -  tuple(pos), width, height; where pos represents the position of the box
        pygame.draw.line(screen, (255, 255, 255), ((placement[0] - 1) * width / 3, (placement[1] - 1) * height / 3),
                         (placement[0] * height / 3, placement[1] * width / 3), width=10)
        pygame.draw.line(screen, (255, 255, 255), ((placement[0]) * width / 3, (placement[1] - 1) * height / 3),
                         ((placement[0] - 1) * height / 3, (placement[1]) * width / 3), width=10)
