import pygame
import random
from dimensions import Dimensions
class FoodObject:
    def __init__(self, game_window):
        self.size=20
        self.dim=Dimensions(random.randint(0,game_window.width-20),random.randint(0,game_window.height-20), self.size)
    
    def draw(self, screen): pygame.draw.rect(screen, (0,255,0), (self.dim.x, self.dim.y, self.size, self.size))
    
    def regenerate_position(self, game_window):
        self.dim.x = random.randint(0, game_window.width - self.size)
        self.dim.y = random.randint(0, game_window.height - self.size)