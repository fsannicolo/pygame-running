import pygame
from pygame.sprite import Sprite
from random import randint

class Mob(Sprite):
    
    def __init__(self, type):
        super().__init__()  # costruttore dello sprite
        
        if type == 'snail':
            snail_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300
            
        else: # fly
            fly_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
            fly_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2] 
            y_pos = randint(150, 210)       
        
        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(bottomleft = (randint(900, 1100), y_pos))
          
    def animate(self):
        self.index += 0.1
        if self.index >= 2:
            self.index = 0
        self.image = self.frames[int(self.index)]
        
    def update(self):
        self.animate()
        self.rect.x -= 5
        self.destroy()
        
    # rimuovere lo sprite quando esce dallo schermo
    def destroy(self):
        if self.rect.right <= 0:
            self.kill() 
        