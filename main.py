import sys
import pygame
from snake import Snake
from dimensions import Dimensions
from food import FoodObject

class SnakeGameWindow:
    def __init__(self, width=800, height=600):
        self.width, self.height = width, height
        self.dim = Dimensions(0, 0)
        self.snake_object = Snake(self)
        self.food_object = FoodObject(self)
        pygame.init()
        self.render_game_window()

    def render_game_window(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")
        while True:
            self.handle_events()
            self.snake_object.move_snake_object()
            self.dim.bound_check(self.snake_object.dim, self)
            if self.dim.is_overlapping(self.snake_object.dim, self.food_object.dim):
                self.food_object.regenerate_position(self)
                self.snake_object.grow()
            self.screen.fill((0, 0, 0))
            self.snake_object.draw(self.screen)
            self.food_object.draw(self.screen)
            pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.snake_object.handle_direction_change(event.key)

if __name__ == '__main__':
    SnakeGameWindow()