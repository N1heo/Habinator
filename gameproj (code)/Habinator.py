import pygame
from sys import exit
from random import randint, choice
from math import ceil

class Player(pygame.sprite.Sprite):
        def __init__(self):
                super().__init__()
                player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
                player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
                self.player_walk = [player_walk_1,player_walk_2]
                self.player_index = 0
                self.player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()

                self.image = self.player_walk[self.player_index]
                self.rect = self.image.get_rect(midbottom = (80,300))
                self.gravity = 0

                self.jump_sound = pygame.mixer.Sound('audio/jump.wav')
                self.jump_sound.set_volume(0.5)
                
        def player_input(self):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
                        self.gravity = -20
                        self.jump_sound.play()

        def apply_gravity(self):
                self.gravity += 1
                self.rect.y += self.gravity
                if self.rect.bottom >= 300:
                        self.rect.bottom = 300

        def animation_state(self):
                if self.rect.bottom < 300: 
                        self.image = self.player_jump            
                else:
                        self.player_index += 0.1
                        if self.player_index >= len(self.player_walk):self.player_index = 0
                        self.image = self.player_walk[int(self.player_index)]
                        
        def update(self):
                self.player_input()
                self.apply_gravity()
                self.animation_state()
                
class Plus(pygame.sprite.Sprite):
        def __init__(self,type):
                super().__init__()
                
                if type == 'books':
                        books_1 = pygame.image.load('graphics/books/books1.png').convert_alpha()
                        books_2 = pygame.image.load('graphics/books/books2.png').convert_alpha()
                        self.frames = [books_1,books_2]
                        y_pos = 300
                        self.anim_speed = 0.1
                elif type == 'sport':
                        sport_1 = pygame.image.load('graphics/sport/sport1.png').convert_alpha()
                        sport_2 = pygame.image.load('graphics/sport/sport2.png').convert_alpha()
                        self.frames = [sport_1,sport_2]
                        y_pos = 300
                        self.anim_speed = 0.1
                elif type == 'coding':
                        coding_1 = pygame.image.load('graphics/coding/coding1.png').convert_alpha()
                        coding_1 = pygame.transform.rotozoom(coding_1,0,1.2)
                        coding_2 = pygame.image.load('graphics/coding/coding2.png').convert_alpha()
                        coding_2 = pygame.transform.rotozoom(coding_2,0,1.2)
                        self.frames =[coding_1,coding_2]
                        y_pos = 300
                        self.anim_speed = 0.05
                elif type == 'tennis':
                        tennis_1=pygame.image.load('graphics/tennis/tennis1.png').convert_alpha()
                        tennis_2=pygame.image.load('graphics/tennis/tennis2.png').convert_alpha()
                        tennis_3=pygame.image.load('graphics/tennis/tennis3.png').convert_alpha()
                        self.frames = [tennis_1,tennis_2,tennis_3]
                        y_pos = 210
                        self.anim_speed = 0.14
                        
                self.animation_index = 0
                self.image = self.frames[self.animation_index]
                self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))

        def animation_state(self):
                self.animation_index += self.anim_speed
                if self.animation_index >= len(self.frames): self.animation_index = 0
                self.image = self.frames[int(self.animation_index)]

        def update(self):
                self.animation_state()
                x=0
                y=5
                z=7
                if 0<=scoref<5:
                        self.rect.x -= 7
                elif 5<=scoref<10:
                        self.rect.x -= 9
                elif 10<=scoref<15:
                        self.rect.x -= 11
                elif 15<=scoref<20:
                        self.rect.x -= 15
                elif 20<=scoref<25:
                        self.rect.x -= 20
                elif 25<=scoref<30:
                        self.rect.x -= 26
                elif 30<=scoref:
                        self.rect.x -= 35
                self.destroy()
                self.killer()

        def destroy(self):
                if self.rect.x <= -100: 
                        self.kill()
		
        def killer(self):                      
                if pygame.sprite.spritecollide(player.sprite,plus_group,False):
                        global scoref
                        scoref = scoref +1
                        self.kill()
                        return scoref
			
			
class Minus(pygame.sprite.Sprite):
        def __init__(self,type):
                super().__init__()

                if type == 'computer':
                        ncomputer_1 = pygame.image.load('graphics/ncomputer/ncomputer1.png').convert_alpha()
                        ncomputer_1 = pygame.transform.rotozoom(ncomputer_1,0,1.2)
                        ncomputer_2 = pygame.image.load('graphics/ncomputer/ncomputer2.png').convert_alpha()
                        ncomputer_2 = pygame.transform.rotozoom(ncomputer_2,0,1.2)
                        self.frames = [ncomputer_1,ncomputer_2]
                        y_pos  = 300
                        self.anim_speed = 0.05
                elif type == 'bottle':
                        bottle_1 = pygame.image.load('graphics/bottle/bottle1.png').convert_alpha()
                        bottle_1 = pygame.transform.rotozoom(bottle_1,0,1.2)
                        bottle_2 = pygame.image.load('graphics/bottle/bottle2.png').convert_alpha()
                        bottle_2 = pygame.transform.rotozoom(bottle_2,0,1.2)
                        bottle_3 = pygame.image.load('graphics/bottle/bottle3.png').convert_alpha()
                        bottle_3 = pygame.transform.rotozoom(bottle_3,0,1.2)
                        bottle_4 = pygame.image.load('graphics/bottle/bottle4.png').convert_alpha()
                        bottle_4 = pygame.transform.rotozoom(bottle_4,0,1.2)
                        bottle_5 = pygame.image.load('graphics/bottle/bottle5.png').convert_alpha()
                        bottle_5 = pygame.transform.rotozoom(bottle_5,0,1.2)
                        bottle_6 = pygame.image.load('graphics/bottle/bottle6.png').convert_alpha()
                        bottle_6 = pygame.transform.rotozoom(bottle_6,0,1.2)
                        bottle_7 = pygame.image.load('graphics/bottle/bottle7.png').convert_alpha()
                        bottle_7 = pygame.transform.rotozoom(bottle_7,0,1.2)
                        bottle_8 = pygame.image.load('graphics/bottle/bottle8.png').convert_alpha()
                        bottle_8 = pygame.transform.rotozoom(bottle_8,0,1.2)
                        self.frames = [bottle_1,bottle_2,bottle_3,bottle_4,bottle_5,bottle_6,bottle_7,bottle_8]
                        y_pos = 210
                        self.anim_speed= 0.2
                elif type == 'smoke':
                        smoke_1 = pygame.image.load('graphics/smoke/smoke1.png').convert_alpha()
                        smoke_1 = pygame.transform.rotozoom(smoke_1,0,1.2)
                        smoke_2 = pygame.image.load('graphics/smoke/smoke2.png').convert_alpha()
                        smoke_2 = pygame.transform.rotozoom(smoke_2,0,1.2)
                        smoke_3 = pygame.image.load('graphics/smoke/smoke3.png').convert_alpha()
                        smoke_3 = pygame.transform.rotozoom(smoke_3,0,1.2)
                        self.frames = [smoke_1,smoke_2,smoke_3]
                        y_pos = 300
                        self.anim_speed =0.12
                        
                self.animation_index = 0
                self.image = self.frames[self.animation_index]
                self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))

        def animation_state(self):
                self.animation_index += self.anim_speed
                if self.animation_index >= len(self.frames): self.animation_index = 0
                self.image = self.frames[int(self.animation_index)]
                
        def update(self):
                self.animation_state()
                if 0<=scoref<5:
                        self.rect.x -= 7
                elif 5<=scoref<10:
                        self.rect.x -= 9
                elif 10<=scoref<15:
                        self.rect.x -= 11
                elif 15<=scoref<20:
                        self.rect.x -= 15
                elif 20<=scoref<25:
                        self.rect.x -= 20
                elif 25<=scoref<30:
                        self.rect.x -= 26
                elif 30<=scoref:
                        self.rect.x -= 35
                self.destroy()
                self.killer()
		
        def destroy(self):
                if self.rect.x <= -100: 
                        self.kill()
        def killer(self):
                if pygame.sprite.spritecollide(player.sprite,minus_group,False):
                        global scoref
                        scoref = scoref - 1
                        self.kill()
                        return scoref
                
scoref = 0
def new_score():
        global scoref
        scoref = scoref
        score_surf = test_font.render(f'Score: {round(scoref)}',False,(64,64,64))
        score_rect = score_surf.get_rect(center = (400,50))
        screen.blit(score_surf,score_rect)
        return scoref 


def collision_sprite():
        global scoref
        if scoref<0:
                minus_group.empty()
                plus_group.empty()
                scoref =0
                return False
        else: return True

class Sky(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.index = 0
        sky1 = pygame.image.load('graphics/Sky/Sky1.png').convert()
        sky2 = pygame.image.load('graphics/Sky/Sky2.png').convert()
        sky3 = pygame.image.load('graphics/Sky/Sky3.png').convert()
        sky4 = pygame.image.load('graphics/Sky/Sky4.png').convert()
        sky5 = pygame.image.load('graphics/Sky/Sky5.png').convert()
        sky6 = pygame.image.load('graphics/Sky/Sky6.png').convert()
        sky7 = pygame.image.load('graphics/Sky/Sky7.png').convert()
        sky8 = pygame.image.load('graphics/Sky/Sky8.png').convert()
        self.frames = [sky1,sky2,sky3,sky4,sky5,sky6,sky7,sky8]
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(midbottom = (400,300))

    def sky_anim(self):
        self.index +=0.05
        if self.index >=len(self.frames): self.index = 0
        self.image = self.frames[int(self.index)]

    def update(self):
            self.sky_anim()
            

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Habinator')
programIcon = pygame.image.load('graphics/icon.png')
pygame.display.set_icon(programIcon)
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.play(loops = -1)


#Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

sky= pygame.sprite.GroupSingle()
sky.add(Sky())

minus_group = pygame.sprite.Group()
plus_group = pygame.sprite.Group()

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# Intro screen
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render('Habinator',False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render('Press space to run',False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400,330))

# Timer 
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                if game_active:
                        if event.type == obstacle_timer:
                                randnumber = choice([1,2])
                                if randnumber == 1:
                                        minus_group.add(choice([Minus(choice(['bottle','computer','smoke'])),]))
                                elif randnumber == 2:
                                        plus_group.add(choice([Plus(choice(['sport','books','coding','tennis'])),]))
        				
                else:
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                                game_active = True
                                start_time = int(pygame.time.get_ticks() / 1000)
				
        if game_active:
                screen.blit(sky_surface,(0,0))
                screen.blit(ground_surface,(0,300))
		
                sky.draw(screen)
                sky.update()

                score = new_score()
		
                player.draw(screen)
                player.update()

                minus_group.draw(screen)
                minus_group.update()
		
                plus_group.draw(screen)
                plus_group.update()
                         
                game_active = collision_sprite()
			
        else:
                screen.fill((94,129,162))
                screen.blit(player_stand,player_stand_rect)

                score_message = test_font.render(f'Your score: {score}',False,(111,196,169))
                score_message_rect = score_message.get_rect(center = (400,330))
                screen.blit(game_name,game_name_rect)

                if score == 0: screen.blit(game_message,game_message_rect)
                else: screen.blit(score_message,score_message_rect)

        pygame.display.update()
        clock.tick(60)
