import sys
import pygame
import random
class Position:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
class Snake:
    def __init__(self,game_window):
        self.position= Position(game_window.width //2 , game_window.height//2)
        self.size=20
        self.speed=0.1
        self.direction=(1,0)
        self.length=1
        self.direction_map={ pygame.K_UP: (0,-1), pygame.K_DOWN: (0,1), pygame.K_LEFT: (-1,0), pygame.K_RIGHT: (1,0)}
    
    def move_snake_object(self):
        self.position.x += self.direction[0] * self.speed
        self.position.y += self.direction[1] * self.speed
    
    def handle_direction_change(self, key):
        if key in self.direction_map:
            new_direction = self.direction_map[key]
            if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
                self.direction = new_direction
    
    def draw(self, screen):
        pygame.draw.rect(screen, (200, 50, 50), (self.position.x, self.position.y, self.size, self.size))

class FoodObject:
    def __init__(self, game_window):
        self.position=Position(random.randint(0,game_window.width-20),random.randint(0,game_window.height-20))
        self.size=20
    
    def draw(self, screen):
        pygame.draw.rect(screen, (0,255,0), (self.position.x, self.position.y, self.size, self.size))
    
    def regenerate_position(self, game_window):
        self.position.x = random.randint(0, game_window.width - self.size)
        self.position.y = random.randint(0, game_window.height - self.size)

class SnakeGameWindow:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.screen = None
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
