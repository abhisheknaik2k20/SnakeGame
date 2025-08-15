import pygame
from dimensions import Dimensions

class Snake:
    def __init__(self, game_window):
        self.size = 20
        self.dim = Dimensions(game_window.width // 2, game_window.height // 2, self.size)
        self.speed = 0.2
        self.direction = (1, 0)
        self.length = 1
        self.direction_map = {pygame.K_UP: (0, -1), pygame.K_DOWN: (0, 1), pygame.K_LEFT: (-1, 0), pygame.K_RIGHT: (1, 0)}
        self.body = [Dimensions(self.dim.x, self.dim.y, self.size)]
        self.tail = []
    
    def move_snake_object(self):
        self.tail.append((self.dim.x, self.dim.y))
        self.dim.x += self.direction[0] * self.speed
        self.dim.y += self.direction[1] * self.speed
        if len(self.tail) > self.length * (self.size / self.speed):
            self.tail.pop(0)
        for i in range(1, len(self.body)):
            idx = min(i * int(self.size / self.speed), len(self.tail) - 1)
            if idx >= 0 and idx < len(self.tail):
                self.body[i].x, self.body[i].y = self.tail[len(self.tail) - 1 - idx]
        self.body[0].x, self.body[0].y = self.dim.x, self.dim.y
    
    def grow(self):
        self.body.append(Dimensions(self.body[-1].x, self.body[-1].y, self.size))
        self.length += 1
    
    def handle_direction_change(self, key):
        if key in self.direction_map:
            new_direction = self.direction_map[key]
            if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
                self.direction = new_direction
    
    def draw(self, screen):
        for i, segment in enumerate(self.body):
            color = (255, 100, 100) if i == 0 else (200, 50, 50)
            pygame.draw.rect(screen, color, (segment.x, segment.y, self.size, self.size))