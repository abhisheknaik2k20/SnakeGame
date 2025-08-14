import sys
import pygame
class SnakeGame:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.screen = None
        self.dot_x=width//2
        self.dot_y=height//2
        self.dot_size=20
        self.speed=0.2
        pygame.init()
        self.show_game_window()

    def show_game_window(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Mini Snake Game")

        while True:
            self.handle_events()
            self.update_screen()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.dot_x > 0:
            self.dot_x -= self.speed
        elif keys[pygame.K_RIGHT] and self.dot_x < self.width - self.dot_size:
            self.dot_x += self.speed
        elif keys[pygame.K_UP] and self.dot_y > 0:
            self.dot_y -= self.speed
        elif keys[pygame.K_DOWN] and self.dot_y < self.height - self.dot_size:
            self.dot_y += self.speed

    def update_screen(self):
        self.screen.fill((0,0,0)) 
        pygame.draw.rect(
            self.screen, (200, 50, 50), (self.dot_x, self.dot_y, self.dot_size, self.dot_size)
        )
        pygame.display.flip()


if __name__ == '__main__':
    SnakeGame()
