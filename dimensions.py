import pygame
import sys
class Dimensions:
    def __init__(self, x, y, size=None) : self.x, self.y, self.size = x, y, size

    def is_overlapping(self, object1, object2):
        x_overlap = object1.x < object2.x + object2.size and object1.x + object1.size > object2.x
        y_overlap = object1.y < object2.y + object2.size and object1.y + object1.size > object2.y
        print( x_overlap and y_overlap)
    
    def bound_check(self, snake_object, game_window):
        if snake_object.x < 0 or snake_object.x+snake_object.size > game_window.width or snake_object.y < 0 or snake_object.y + snake_object.size > game_window.height:
            pygame.quit()
            sys.exit()
    
    