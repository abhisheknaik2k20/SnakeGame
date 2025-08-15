import pygame
import random
from position import Position
class FoodObject:
    def __init__(self, game_window):
        self.size=20
        self.position=Position(random.randint(0,game_window.width-20),random.randint(0,game_window.height-20), self.size)
    
    def draw(self, screen): pygame.draw.rect(screen, (0,255,0), (self.position.x, self.position.y, self.size, self.size))
    
    def regenerate_position(self, game_window):
        self.position.x = random.randint(0, game_window.width - self.size)
        self.position.y = random.randint(0, game_window.height - self.size)