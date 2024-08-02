'''
This file contains the Enemy class.
'''
import pygame
import secrets

class Enemy:
    def __init__(self):
        self.x = secrets.SystemRandom().randint(0, 750)
        self.y = secrets.SystemRandom().randint(50, 200)
        self.width = 50
        self.height = 50
        self.velocity = secrets.SystemRandom().randint(1, 2)
    def update(self):
        self.y += self.velocity
        if self.y > 600:
            self.y = secrets.SystemRandom().randint(50, 200)
            self.x = secrets.SystemRandom().randint(0, 750)
    def draw(self, window):
        pygame.draw.rect(window, (0, 0, 255), (self.x, self.y, self.width, self.height))
