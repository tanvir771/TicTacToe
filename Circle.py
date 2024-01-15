# Implements a Circle Element

import pygame


class Circle:

    def __int__(self):
        self.state = 0

    def Draw(self, screen, placement, width, height):
        # placement -  tuple(pos), width, height; where pos represents the position of the box
        pygame.draw.circle(screen, (255, 255, 255), (
            ((placement[0] - 1) * width / 3 + (width / 6)), ((placement[1] - 1) * height / 3) + (height / 6)),
                           width / 6,
                           width=10)
        # last width is pygame.draw.circle's argument, width=0 by default, which gives filled in circle
