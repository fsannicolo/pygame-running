import pygame
from pygame.sprite import Sprite
from random import randint

class Mob(Sprite):
    
    def __init__(self):
        super().__init__()  # costruttore dello sprite
        
        snail_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
        snail_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
        
        y_pos = 300
        
        self.image = snail_1 
        self.rect = self.image.get_rect(bottomleft = (randint(900, 1100), y_pos))
        
    def update(self):
        self.rect.x -= 5
        self.destroy()
        
    # rimuovere lo sprite quando esce dallo schermo
    def destroy(self):
        if self.rect.right <= 0:
            self.kill() 
        