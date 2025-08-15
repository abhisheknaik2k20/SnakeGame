import sys
import pygame
from snake import Snake
from position import Position
from food import FoodObject

class SnakeGameWindow:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.screen = None
        self.pos=Position(0,0)
        self.snake_object=Snake(self)
        self.food_object=FoodObject(self) 
        pygame.init()
        self.show_game_window()

    def show_game_window(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Mini Snake Game")
        while True:
            self.handle_events()
            self.update_screen()
            self.snake_object.move_snake_object()
            self.pos.is_overlapping(self.snake_object.position, self.food_object.position)
            self.out_of_bounds()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_0: self.end_game()
                self.snake_object.handle_direction_change(event.key)

    def update_screen(self):
        self.screen.fill((0,0,0)) 
        self.snake_object.draw(self.screen)
        self.food_object.draw(self.screen)
        pygame.display.flip()
    
    def out_of_bounds(self) -> bool :
        if self.snake_object.position.x < 0 or self.snake_object.position.x+self.snake_object.size > self.width or self.snake_object.position.y < 0 or self.snake_object.position.y + self.snake_object.size > self.height:
            self.end_game() 
    
    def end_game(self):
        print("*"*5+"GAME OVER"+"*"*5)
        pygame.quit()
        sys.exit()

       

if __name__ == '__main__': 
    SnakeGameWindow()