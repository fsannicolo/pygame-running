import pygame 
from pygame.sprite import Sprite

class Player(Sprite):   # ereditato
    
    # costruttore
    def __init__(self):
        super().__init__()
        walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
        walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
        
        # sprite del giocatore
        self.image = walk_1 
        
        # hitbox
        self.rect = self.image.get_rect(midbottom = (80, 300))
        
        # fisica del giocatore
        self.gravity = 0
        
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom == 300: 
            self.gravity = -20 
            
    def apply_gravity(self):
        self.gravity += 1   # ad ogni frame riduco la gravità
        self.rect.y += self.gravity
        
        # se non sta toccando per terra
        if self.rect.bottom > 300:
            self.rect.bottom = 300
    
    def update(self):
        self.input()
        self.apply_gravity()