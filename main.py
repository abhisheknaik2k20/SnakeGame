import pygame
import sys

class SnakeGame:
    def __init__(self):
        self.height,self.width=800,600
        self.show_game_window()

    def show_game_window(self):
        pygame.init()
        screen =pygame.display.set_mode((self.height,self.width))
        pygame.display.set_caption("Mini Snake Game")
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            screen.fill((30,30,30))

if __name__=='__main__':
    s=SnakeGame()
