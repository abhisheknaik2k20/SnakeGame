import pygame
from dimensions import Dimensions
class Snake:
    def __init__(self,game_window):
        self.size=20
        self.dim = Dimensions(game_window.width // 2 , game_window.height// 2, self.size)
        self.speed=0.2
        self.direction=(1,0)
        self.length=1
        self.direction_map={pygame.K_UP: (0,-1), pygame.K_DOWN: (0,1), pygame.K_LEFT: (-1,0), pygame.K_RIGHT: (1,0)}
    
    def move_snake_object(self):
        self.dim.x += self.direction[0] * self.speed
        self.dim.y += self.direction[1] * self.speed
    
    def handle_direction_change(self, key):
        if key in self.direction_map:
            new_direction = self.direction_map[key]
            if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
                self.direction = new_direction
    
    def draw(self, screen) : pygame.draw.rect(screen, (200, 50, 50), (self.dim.x, self.dim.y, self.size, self.size))