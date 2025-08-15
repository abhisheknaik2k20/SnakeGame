import sys
import pygame
import random
class SnakeGame:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.screen = None
        self.dot_x=width//2
        self.dot_y=height//2
        self.dot_size=20
        self.speed=0.1
        self.direction=(1,0)
        self.direction_map={ pygame.K_UP: (0,-1), pygame.K_DOWN: (0,1), pygame.K_LEFT: (-1,0), pygame.K_RIGHT: (1,0)}
        self.food_coords=(random.randint(0,self.width),random.randint(0,600))
        pygame.init()
        self.show_game_window()

    def show_game_window(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Mini Snake Game")
        while True:
            self.handle_events()
            self.update_screen()
            self.move_dot()
    
    def move_dot(self):
        self.dot_x+=self.direction[0]*self.speed
        self.dot_y+=self.direction[1]*self.speed

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key in self.direction_map:
                    print(event.key)
                    self.direction=self.direction_map[event.key]


    def update_screen(self):
        self.screen.fill((0,0,0)) 
        pygame.draw.rect(self.screen, (200, 50, 50), (self.dot_x, self.dot_y, self.dot_size, self.dot_size))
        pygame.draw.rect(self.screen, (0,255,0), (*self.food_coords, self.dot_size, self.dot_size), 10)
        pygame.display.flip()
    
    def handle_collisions(self):
        pass


if __name__ == '__main__':
    SnakeGame()
