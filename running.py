import pygame
from random import randint, choice 
from player import Player
from mob import Mob
from datamanager import DataManager

def update_score() -> int:
    current_score = (pygame.time.get_ticks() - start_time) // 100
    score_text = font.render(f'Punti: {current_score}', False, (64,64,64)) 
    score_rect = score_text.get_rect(midleft = (150, 50))
    
    record_surface = font.render(f'Record: {record}', False, (64,64,64))
    record_rect = record_surface.get_rect(midright = (650, 50))
    
    screen.blit(score_text, score_rect) 
    screen.blit(record_surface, record_rect)
    
    return current_score

# controlla se si sono verificate collisioni tra giocatore e mob
def collision_sprite() -> bool: 
    # ritorna una lista degli sprite che collidono
    if pygame.sprite.spritecollide(player.sprite, mobs, False):
        return True
    
    return False
        
pygame.init() 

w = 800
h = 400

# crea una finestra per il gioco
screen = pygame.display.set_mode((w, h)) 
pygame.display.set_caption('Running game') 

# timer del gioco
clock = pygame.time.Clock()

# controlla se sono in gioco o nei menu
game_active = False 

start_time = 0

# gestione del punteggio e caricamento record
save_manager = DataManager('savedata', 'record.dat') 
score = 0
record = save_manager.load() 
print(f'Record caricato: {record}') 

# carico il font (e specifico la dimensione)
font = pygame.font.Font('font/Pixeltype.ttf', 50)

# carico gli sprite dello sfondo
sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# main screen
player_logo = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_logo = pygame.transform.rotozoom(player_logo, 0, 2)
player_logo_rect = player_logo.get_rect(center = (400, 200)) 

game_name = font.render('Pixel Runner', False, (111,196,169)) 
game_name_rect = game_name.get_rect(center = (400, 80)) 

game_message = font.render('Premi SPAZIO per iniziare', False, (111,196,169))
game_message_rect = game_message.get_rect(center = (400, 330)) 

gameover_message = font.render('GAME OVER', False, (111,196,169))
gameover_message_rect = gameover_message.get_rect(center = (400, 80)) 

# gestione degli sprite del giocatore
player = pygame.sprite.GroupSingle()
player.add(Player())    # istanza del giocatore aggiunta agli sprite

mobs = pygame.sprite.Group()
mobs.add(Mob('snail'))         

# logica dello spawn (23 eventi base, i restanti sono per l'utente)
spawn_timer = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_timer, 1400) 

# game cycle
run = True 
while run:
    # gestione degli eventi
    for event in pygame.event.get():
    
        # controllo la chiusura della finestra
        if event.type == pygame.QUIT:
            run = False
        
        if game_active:
            # controllo se è "scaduto" il timer
            if event.type == spawn_timer:
                mobtype = choice(['fly','snail','snail','snail'])
                mobs.add(Mob(mobtype)) 
               
        # se sono nel menu, riavvio    
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                mobs.empty()        # svuoto i nemici
                start_time = pygame.time.get_ticks()
    
    # update del frame
    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        
        # disegna punteggio
        score = update_score()
        
        player.draw(screen) 
        player.update()
        
        mobs.draw(screen) 
        mobs.update() 
        
        game_active = not collision_sprite()
        
    # game over
    else:
        screen.fill((94, 129, 162)) 
        screen.blit(player_logo, player_logo_rect)
           
        # mostrare punteggio
        score_message = font.render(f'Il tuo punteggio: {score}', False, (111,196,169))
        score_rect = score_message.get_rect(center = (400, 330)) 
               
        if score == 0:
            # schermata principale
            screen.blit(game_message, game_message_rect)
            screen.blit(game_name, game_name_rect)
        else:
            # schermata game over
            screen.blit(gameover_message, gameover_message_rect)
            screen.blit(score_message, score_rect)
            # se ho battuto il record, lo salvo
            if score > record:
                record = score
                save_manager.save(record)
                print(f'Nuovo record: {record}')
    
    # disegno del prossimo frame
    pygame.display.update()
    
    # 60 fps
    clock.tick(60) 
    
pygame.quit()