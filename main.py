import pygame
import time
import math

WHITE =     (255, 255, 255)
BLUE =      (0, 0, 255)
GREEN =     (0, 255, 0)
YELLOW = (255, 255, 0)
RED =       (255, 0, 0)
BLACK = (0, 0, 0)
TEXTCOLOR = (  0,   0,  0)

HEIGHT = 640
WIDTH = 1280

FPS = 60

pygame.init()
clock = pygame.time.Clock()

# music
bgm = pygame.mixer.music.load("resources\\music\\This_is_the_end.mp3")
#pygame.mixer.music.play(-1)

# sounds
resume_sound = pygame.mixer.Sound("resources\\sound_effects\\resume.wav")
button_hover_sound = pygame.mixer.Sound("resources\\sound_effects\\button_hover.wav")

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        #button_hover_sound.play()

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText , WHITE)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def pause():
    global paused
    pygame.mixer.music.pause()
    paused = True 
    while paused:
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    resume()

        largeText =pygame.font.Font("resources\\fonts\\ZOMBIES_REBORN.ttf", 150)
        TextSurf, TextRect = text_objects("Paused", largeText, RED)
        TextRect.center = ((WIDTH/2),(HEIGHT/2))
        screen.blit(TextSurf, TextRect)

        button("Continue", 150, 450 , 100 ,50,GREEN,BLUE,resume)
        button("Quit",550,450,100,50,RED,YELLOW,pygame.quit)

        pygame.display.update()

def resume():
    global paused
    #resume_sound.play()
    paused = False
    pygame.mixer.music.play(-1)


def game_intro():
    global intro
    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        largeText = pygame.font.Font("resources\\fonts\\ZOMBIES_REBORN.ttf",200)
        TextSurf, TextRect = text_objects("TEST1", largeText, RED)
        TextRect.center = ((WIDTH/2),(HEIGHT/2))
        screen.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,GREEN,BLUE,game_loop)
        button("Quit",550,450,100,50,RED,YELLOW,pygame.quit)

        pygame.display.update()
        clock.tick(15)


def bck_impulse(x_impulse, y_impulse):
    global bck_x
    global bck_y

    bck_x += x_impulse
    bck_y += y_impulse

def quake(mag = 1):
    global bck_x
    global bck_y
    global quakecount
    global quaking
    if quakecount == 0:
        bck_impulse(2*mag, 2*mag)
        quakecount += 1
        

    elif quakecount == 1:
        bck_x= bck_y = 0
        bck_impulse(-2*mag, -2*mag)
        quakecount += 1
        

    elif quakecount == 2:
        bck_x= bck_y = 0
        bck_impulse(-1*mag, 1*mag)
        quakecount += 1
        

    elif quakecount == 3:
        bck_x= bck_y = 0
        bck_impulse(1*mag, -1*mag)
        quakecount += 1
        

    else:
        bck_x= bck_y = 0
        quakecount = 0
        #quaking = False
        
    

    

skull_cage_bck = pygame.image.load("resources\\backgrounds\\skull_cage.jpg")
skull_cage_dark_bck = pygame.image.load("resources\\backgrounds\\skull_cage_dark.jpg")
skull_passage_bck = pygame.image.load("resources\\backgrounds\\skull_passage.jpg")
fallen_pillar_bck = pygame.image.load("resources\\backgrounds\\fallen_pillar.jpg")
ruined_passage_bck = pygame.image.load("resources\\backgrounds\\ruined_passage.jpg")
bloody_sewage_bck = pygame.image.load("resources\\backgrounds\\bloody_sewage.jpg")
ruined_passage_dark_bck = pygame.image.load("resources\\backgrounds\\ruined_passage_dark.jpg")
prayer_room_bck = pygame.image.load("resources\\backgrounds\\prayer_room.jpg")
ship_wreck_bck = pygame.image.load("resources\\backgrounds\\ship_wreck.jpg")
violet_bck = pygame.image.load("resources\\backgrounds\\violet.jpg")
graveyard_bck = pygame.image.load("resources\\backgrounds\\graveyard.jpg")
clean_passage_back = pygame.image.load("resources\\backgrounds\\clean_passage.png")

bck_list = [skull_cage_bck,skull_cage_dark_bck,skull_passage_bck,fallen_pillar_bck,ruined_passage_bck,bloody_sewage_bck,ruined_passage_dark_bck,prayer_room_bck,\
            ship_wreck_bck,violet_bck,graveyard_bck,clean_passage_back]

screen = pygame.display.set_mode((WIDTH, HEIGHT))#,pygame.FULLSCREEN,pygame.RESIZABLE)

pygame.display.set_caption("1")



wraith_r = [pygame.image.load("resources\\characters\\Wraith_01\\PNG Sequences\\Walking\\%s.png"%frame) for frame in range(1,13)]
wraith_l = [pygame.transform.flip(pygame.image.load("resources\\characters\\Wraith_01\\PNG Sequences\\Walking\\%s.png"%frame), True, False) for frame in range(1,13)]
wraith_idle_r = [pygame.image.load("resources\\characters\\Wraith_01\\PNG Sequences\\Idle Blink\\%s.png"%frame) for frame in range(1,13)]
wraith_idle_l = [pygame.transform.flip(pygame.image.load("resources\\characters\\Wraith_01\\PNG Sequences\\Idle Blink\\%s.png"%frame), True, False) for frame in range(1,13)]
wraith_firing_r = pygame.image.load("resources\\characters\\Wraith_01\\PNG Sequences\\Firing\\1.png")
wraith_firing_l = pygame.transform.flip(pygame.image.load("resources\\characters\\Wraith_01\\PNG Sequences\\Firing\\1.png"), True, False)
wraith_hurt_r = [pygame.image.load("resources\\characters\\Wraith_01\\PNG Sequences\\Hurt\\%s.png"%frame) for frame in range(1,13)]
wraith_hurt_l = [pygame.transform.flip(pygame.image.load("resources\\characters\\Wraith_01\\PNG Sequences\\Hurt\\%s.png"%frame), True, False) for frame in range(1,13)]

wraith2_r = [pygame.image.load("resources\\characters\\Wraith_02\\PNG Sequences\\Walking\\%s.png"%frame) for frame in range(1,13)]
wraith2_l = [pygame.transform.flip(pygame.image.load("resources\\characters\\Wraith_02\\PNG Sequences\\Walking\\%s.png"%frame), True, False) for frame in range(1,13)]
wraith2_idle_r = [pygame.image.load("resources\\characters\\Wraith_02\\PNG Sequences\\Idle Blink\\%s.png"%frame) for frame in range(1,13)]
wraith2_idle_l = [pygame.transform.flip(pygame.image.load("resources\\characters\\Wraith_02\\PNG Sequences\\Idle Blink\\%s.png"%frame), True, False) for frame in range(1,13)]
#wraith2_firing_r = pygame.image.load("resources\\characters\\Wraith_02\\PNG Sequences\\Firing\\1.png")
#wraith2_firing_l = pygame.transform.flip(pygame.image.load("resources\\characters\\Wraith_02\\PNG Sequences\\Firing\\1.png"), True, False)
wraith2_hurt_r = [pygame.image.load("resources\\characters\\Wraith_02\\PNG Sequences\\Hurt\\%s.png"%frame) for frame in range(1,13)]
wraith2_hurt_l = [pygame.transform.flip(pygame.image.load("resources\\characters\\Wraith_02\\PNG Sequences\\Hurt\\%s.png"%frame), True, False) for frame in range(1,13)]

wraith3_r = [pygame.image.load("resources\\characters\\Wraith_03\\PNG Sequences\\Walking\\%s.png"%frame) for frame in range(1,13)]
wraith3_l = [pygame.transform.flip(pygame.image.load("resources\\characters\\Wraith_03\\PNG Sequences\\Walking\\%s.png"%frame), True, False) for frame in range(1,13)]
wraith3_idle_r = [pygame.image.load("resources\\characters\\Wraith_03\\PNG Sequences\\Idle Blink\\%s.png"%frame) for frame in range(1,13)]
wraith3_idle_l = [pygame.transform.flip(pygame.image.load("resources\\characters\\Wraith_03\\PNG Sequences\\Idle Blink\\%s.png"%frame), True, False) for frame in range(1,13)]
#wraith3_firing_r = pygame.image.load("resources\\characters\\Wraith_03\\PNG Sequences\\Firing\\1.png")
#wraith3_firing_l = pygame.transform.flip(pygame.image.load("resources\\characters\\Wraith_03\\PNG Sequences\\Firing\\1.png"), True, False)
wraith3_hurt_r = [pygame.image.load("resources\\characters\\Wraith_03\\PNG Sequences\\Hurt\\%s.png"%frame) for frame in range(1,13)]
wraith3_hurt_l = [pygame.transform.flip(pygame.image.load("resources\\characters\\Wraith_03\\PNG Sequences\\Hurt\\%s.png"%frame), True, False) for frame in range(1,13)]

## wraith1 list

# Lizard
#lizard_idle_r = [pygame.image.load("E:\\py files\\lost project\\resources\\characters\\MONSTERS\\lizard\\Idle%s.png"%frame) for frame in range(1,4)]
#lizard_idle_l = [pygame.transform.flip(pygame.image.load("E:\\py files\\lost project\\resources\\characters\\MONSTERS\\lizard\\Idle%s.png"%frame),True,False) for frame in range(1,4)]
lizard_r = [pygame.image.load("E:\\py files\\lost project\\resources\\characters\\MONSTERS\\lizard\\Walk%s.png"%frame) for frame in range(1,7)]
lizard_l = [pygame.transform.flip(pygame.image.load("E:\\py files\\lost project\\resources\\characters\\MONSTERS\\lizard\\Walk%s.png"%frame),True,False) for frame in range(1,7)]
lizard_attack_r =[pygame.image.load("E:\\py files\\lost project\\resources\\characters\\MONSTERS\\lizard\\Attack%s.png"%frame) for frame in range(1,6)]
lizard_attack_l = [pygame.transform.flip(pygame.image.load("E:\\py files\\lost project\\resources\\characters\\MONSTERS\\lizard\\Attack%s.png"%frame),True,False) for frame in range(1,6)]

small_dragon_r = [pygame.image.load("E:\\py files\\lost project\\resources\\characters\\MONSTERS\\small_dragon\\Walk%s.png"%frame) for frame in range(1,5)]
small_dragon_l =[pygame.transform.flip(pygame.image.load("E:\\py files\\lost project\\resources\\characters\\MONSTERS\\small_dragon\\Walk%s.png"%frame),True,False) for frame in range(1,5)]
small_dragon_attack_r = [pygame.image.load("E:\\py files\\lost project\\resources\\characters\\MONSTERS\\small_dragon\\Attack%s.png"%frame) for frame in range(1,4)]
small_dragon_attack_l = [pygame.transform.flip(pygame.image.load("E:\\py files\\lost project\\resources\\characters\\MONSTERS\\small_dragon\\Attack%s.png"%frame),True,False) for frame in range(1,4)]

jinn_r = [pygame.image.load("E:\\py files\\lost project\\resources\\characters\\MONSTERS\\jinn_animation\\Flight%s.png"%frame) for frame in range(1,5)]
jinn_l = [pygame.transform.flip(pygame.image.load("E:\\py files\\lost project\\resources\\characters\\MONSTERS\\jinn_animation\\Flight%s.png"%frame),True,False) for frame in range(1,5)]
jinn_attack_r = [pygame.image.load("E:\\py files\\lost project\\resources\\characters\\MONSTERS\\jinn_animation\\Attack%s.png"%frame) for frame in range(1,5)]
jinn_attack_l = [pygame.transform.flip(pygame.image.load("E:\\py files\\lost project\\resources\\characters\\MONSTERS\\jinn_animation\\Attack%s.png"%frame),True,False) for frame in range(1,5)]

demon_r = [pygame.image.load("E:\\py files\\lost project\\resources\\characters\\MONSTERS\\demon\\Walk%s.png"%frame) for frame in range(1,7)]
demon_l = [pygame.transform.flip(pygame.image.load("E:\\py files\\lost project\\resources\\characters\\MONSTERS\\demon\\Walk%s.png"%frame),True,False) for frame in range(1,7)]
demon_attack_r = [pygame.image.load("E:\\py files\\lost project\\resources\\characters\\MONSTERS\\demon\\Attack%s.png"%frame) for frame in range(1,5)]
demon_attack_l = [pygame.transform.flip(pygame.image.load("E:\\py files\\lost project\\resources\\characters\\MONSTERS\\demon\\Attack%s.png"%frame),True,False) for frame in range(1,5)]

medusa_r = [pygame.image.load("E:\\py files\\lost project\\resources\\characters\\MONSTERS\\medusa\\Walk%s.png"%frame) for frame in range(1,5)]
medusa_l = [pygame.transform.flip(pygame.image.load("E:\\py files\\lost project\\resources\\characters\\MONSTERS\\medusa\\Walk%s.png"%frame),True,False) for frame in range(1,5)]
medusa_attack_r = [pygame.image.load("E:\\py files\\lost project\\resources\\characters\\MONSTERS\\medusa\\Attack%s.png"%frame) for frame in range(1,7)]
medusa_attack_l =[pygame.transform.flip(pygame.image.load("E:\\py files\\lost project\\resources\\characters\\MONSTERS\\medusa\\Attack%s.png"%frame),True,False) for frame in range(1,7)]

dragon_r = [pygame.image.load("E:\\py files\\lost project\\resources\\characters\\MONSTERS\\dragon\\Walk%s.png"%frame) for frame in range(1,6)]
dragon_l = [pygame.transform.flip(pygame.image.load("E:\\py files\\lost project\\resources\\characters\\MONSTERS\\dragon\\Walk%s.png"%frame),True,False) for frame in range(1,6)]
dragon_attack_r = [pygame.image.load("E:\\py files\\lost project\\resources\\characters\\MONSTERS\\dragon\\Attack%s.png"%frame) for frame in range(1,5)]
dragon_attack_l = [pygame.transform.flip(pygame.image.load("E:\\py files\\lost project\\resources\\characters\\MONSTERS\\dragon\\Attack%s.png"%frame),True,False) for frame in range(1,5)]

boss_r = [pygame.image.load("resources\\characters\\Satyr_03\\PNG Sequences\\Walking\\W%s.png"%frame) for frame in range(1,18)]
boss_l = [pygame.transform.flip(pygame.image.load("resources\\characters\\Satyr_03\\PNG Sequences\\Walking\\W%s.png"%frame), True, False) for frame in range(1,18)]
boss_attack_r = [pygame.image.load("resources\\characters\\Satyr_03\\PNG Sequences\\Attacking\\%s.png"%frame) for frame in range(1,13)]
boss_attack_l = [pygame.transform.flip(pygame.image.load("resources\\characters\\Satyr_03\\PNG Sequences\\Attacking\\%s.png"%frame), True, False) for frame in range(1,13)]
#idle
i = 0
for picture in wraith_idle_r:
    wraith_idle_r[i] = pygame.transform.scale(picture, (250, 203))
    i += 1

i = 0
for picture in wraith_idle_l:
    wraith_idle_l[i] = pygame.transform.scale(picture, (250, 203))
    i += 1

i = 0
for picture in wraith_hurt_r:
    wraith_hurt_r[i] = pygame.transform.scale(picture, (250, 203))
    i += 1

i = 0
for picture in wraith_hurt_l:
    wraith_hurt_l[i] = pygame.transform.scale(picture, (250, 203))
    i += 1
## wraith2 list
#walking
i = 0
for picture in wraith2_r:
    wraith2_r[i] = pygame.transform.scale(picture, (250, 203))
    i += 1

i = 0
for picture in wraith2_l:
    wraith2_l[i] = pygame.transform.scale(picture, (250, 203))
    i += 1
i = 0
for picture in wraith2_hurt_r:
    wraith2_hurt_r[i] = pygame.transform.scale(picture, (250, 203))
    i += 1

i = 0
for picture in wraith2_hurt_l:
    wraith2_hurt_l[i] = pygame.transform.scale(picture, (250, 203))
    i += 1
#idle
i = 0
for picture in wraith2_idle_r:
    wraith2_idle_r[i] = pygame.transform.scale(picture, (250, 203))
    i += 1

i = 0
for picture in wraith2_idle_l:
    wraith2_idle_l[i] = pygame.transform.scale(picture, (250, 203))
    i += 1

## wraith3 list
#walking
i = 0
for picture in wraith3_r:
    wraith3_r[i] = pygame.transform.scale(picture, (250, 203))
    i += 1

i = 0
for picture in wraith3_l:
    wraith3_l[i] = pygame.transform.scale(picture, (250, 203))
    i += 1
#idle
i = 0
for picture in wraith3_idle_r:
    wraith3_idle_r[i] = pygame.transform.scale(picture, (250, 203))
    i += 1

i = 0
for picture in wraith3_idle_l:
    wraith3_idle_l[i] = pygame.transform.scale(picture, (250, 203))
    i += 1
i = 0
for picture in wraith3_hurt_r:
    wraith3_hurt_r[i] = pygame.transform.scale(picture, (250, 203))
    i += 1

i = 0
for picture in wraith3_hurt_l:
    wraith3_hurt_l[i] = pygame.transform.scale(picture, (250, 203))
    i += 1
    
class Villain(pygame.sprite.Sprite):
    def __init__(self, bck_pos, y_pos, leftimgs, rytimgs, attack_l, attack_r, leftidle = None, rytidle = None, anim_speed = 0.2, attack_range = 100):
        pygame.sprite.Sprite.__init__(self)
        self.bck_pos = bck_pos
        self.r_imgs = rytimgs
        self.l_imgs = leftimgs
        self.leftidle = leftidle
        self.rytidle = rytidle
        self.attack_l = attack_l
        self.attack_r = attack_r
        self.len_r_imgs = len(self.r_imgs)
        self.len_l_imgs = len(self.l_imgs)
        self.len_r_attack = len(self.attack_r)
        self.len_l_attack = len(self.attack_l)
        self.image = self.l_imgs[0]
        self.rect = self.image.get_rect()
        self.y_pos = y_pos
        self.rect.center = (500,1000)
        self.velocity_x = 3
        self.velocity_y = 0
        self.attack_range = attack_range
        self.right = False
        self.left = False
        self.walking = True
        self.attacking = False
        self.walkcount = 0
        self.attackcount = 0
        self.idlecount = 0
        self.anim_speed = anim_speed

    def attack(self):
        if self.right == True and self.attacking == True:
            if self.attackcount < self.len_r_attack - 1:
                self.image = self.attack_r[int(self.attackcount)]
                self.attackcount += self.anim_speed
            else:
                self.attackcount = 0

        elif self.left == True and self.attacking == True:
            if self.attackcount < self.len_l_attack - 1:
                self.image = self.attack_l[int(self.attackcount)]
                self.attackcount += self.anim_speed
            else:
                self.attackcount = 0
        wraith.hurting = True
        wraith.hurt()

    def update(self):
        if bck_index != self.bck_pos:
            self.rect.bottom = 2000

        else:
            self.rect.bottom = self.y_pos

        if self.rect.left < 190 or self.rect.right > 1200:
            self.velocity_x *= -1

        if self.velocity_x*-1 == math.fabs(self.velocity_x) and self.velocity_x != 0:
            self.right = False
            self.left = True
        elif self.velocity_x*1 == math.fabs(self.velocity_x) and self.velocity_x != 0:
            self.left = False
            self.right = True
            
        self.rect.x += self.velocity_x + bck_x
        self.rect.y += self.velocity_y + bck_y

        if self.right == True and self.walking == True:
            if self.walkcount < self.len_r_imgs - 1:
                self.image = self.r_imgs[int(self.walkcount)]
                self.walkcount += self.anim_speed
            else:
                self.walkcount = 0

        elif self.left == True and self.walking == True:
            if self.walkcount < self.len_l_imgs - 1:
                self.image = self.l_imgs[int(self.walkcount)]
                self.walkcount += self.anim_speed

            else:
                self.walkcount = 0
        '''
        elif self.left == True and self.walking == False:
            if self.idlecount < 11:
                self.image = self.leftidle[int(self.idlecount)]
                self.idlecount += self.anim_speed

            else:
                self.idlecount = 0

        elif self.right == True and self.walking == False:
            if self.idlecount < 11:
                self.image = self.rytidle[int(self.idlecount)]
                self.idlecount += self.anim_speed

            else:
                self.idlecount = 0
        '''
        if math.fabs(wraith.rect.x - self.rect.x) < self.attack_range and self.rect.bottom < 1000:
            self.attacking = True
            self.velocity_x = 0
            self.walking = False
            self.attack()
        else:
            self.attacking = False
            if self.right == True:
                self.velocity_x = 3

            if self.left == True:
                self.velocity_x = -3
            self.walking = True
        
class Wraith(pygame.sprite.Sprite):
    def __init__(self, leftimgs, rytimgs, leftidle, rytidle, hurt_l, hurt_r):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("resources\\characters\\Wraith_01\\PNG Sequences\\Walking\\1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (0,600)
        self.velocity_x = 0
        self.velocity_y = 0
        self.r_imgs = rytimgs
        self.l_imgs = leftimgs
        self.leftidle = leftidle
        self.rytidle = rytidle
        self.hurt_l = hurt_l
        self.hurt_r = hurt_r
        self.len_l_hurt = len(hurt_l)
        self.len_r_hurt = len(hurt_r)
        self.len_r_imgs = len(self.r_imgs)
        self.len_l_imgs = len(self.l_imgs)
        self.jump = False
        self.jump_power = 8
        self.jumpcount = self.jump_power
        self.right = False
        self.left = False
        self.walking = False
        self.firing = False
        self.hurting = False
        self.walkcount = 0
        self.idlecount = 0
        self.hurtcount = 0
    
    def hurt(self):
        if self.rect.bottom ==  HEIGHT:
            if self.right == True and self.hurting == True:
                if self.hurtcount < self.len_r_hurt - 1:
                    self.image = self.hurt_r[int(self.hurtcount)]
                    self.hurtcount += 0.5
                else:
                    self.hurtcount = 0

            elif self.left == True and self.hurting == True:
                if self.hurtcount < self.len_l_hurt - 1:
                    self.image = self.hurt_l[int(self.hurtcount)]
                    self.hurtcount += 0.5
                else:
                    self.hurtcount = 0
    
    def update(self):
        self.rect.x += self.velocity_x + bck_x
        self.rect.y += self.velocity_y + bck_y

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

        if self.right == True and self.walking == True:
            if self.walkcount < self.len_r_imgs - 1:
                self.image = self.r_imgs[int(self.walkcount)]
                self.walkcount+=0.5
            else:
                self.walkcount = 0

        elif self.left == True and self.walking == True:
            if self.walkcount < self.len_l_imgs - 1:
                self.image = self.l_imgs[int(self.walkcount)]
                self.walkcount += 0.5

            else:
                self.walkcount = 0

        elif self.left == True and self.walking == False:
            if self.idlecount < 11:
                self.image = self.leftidle[int(self.idlecount)]
                self.idlecount += 0.2

            else:
                self.idlecount = 0

        elif self.right == True and self.walking == False:
            if self.idlecount < 11:
                self.image = self.rytidle[int(self.idlecount)]
                self.idlecount += 0.2

            else:
                self.idlecount = 0

        if self.jump == True:
            if self.jumpcount >= -self.jump_power:
                if self.jumpcount < 0:
                    self.velocity_y = self.jumpcount**2
                    
                else:
                    self.velocity_y = -self.jumpcount**2
                self.jumpcount -= 1

            else:
                self.jump = False
                self.jumpcount = self.jump_power

        if wraith.firing == True:
            quaking = True
            if wraith.right == True:
                self.image = wraith_firing_r
            elif wraith.left == True:
                self.image = wraith_firing_l
            

all_sprites = pygame.sprite.Group()

wraith = Wraith(wraith_l, wraith_r, wraith_idle_l, wraith_idle_r, wraith_hurt_l, wraith_hurt_r)
all_sprites.add(wraith)                                                                                 #bck_pos, leftimgs, rytimgs, leftidle, rytidle

lizard = Villain(1, 690, lizard_l, lizard_r,lizard_attack_l,lizard_attack_r)#, lizard_idle_l, lizard_idle_r)
small_dragon = Villain(2, 635, small_dragon_l, small_dragon_r,small_dragon_attack_l,small_dragon_attack_r)
jinn = Villain(4, 585, jinn_l, jinn_r,jinn_attack_l,jinn_attack_r)
demon = Villain(5, 660, demon_l, demon_r,demon_attack_l,demon_attack_r)
medusa = Villain(6, 610, medusa_l, medusa_r,medusa_attack_l,medusa_attack_r)
dragon = Villain(8, 650, dragon_l, dragon_r,dragon_attack_l,dragon_attack_r)
boss = Villain(10, 700, boss_l, boss_r,boss_attack_l,boss_attack_r, anim_speed = 0.4)
all_sprites.add(lizard,small_dragon,jinn,demon,medusa,dragon,boss)


bck_index = 0
running = True

#index_update_constant = 0

bck_x = 0
bck_y = 0
quakecount = 0
quaking = False

def game_loop():
    global bck_x
    global bck_y
    global quakecount
    global quaking
    pygame.mixer.music.play(-1)
    intro = False
    #global wraith_r
    #global wraith_l
    global index_update_constant
    global bck_index
    global running
    while running:

        clock.tick(FPS)
        
        for event in pygame.event.get():
            # Quit
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            # Keydown
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    wraith.velocity_y = -8

                elif event.key == pygame.K_s:
                    wraith.velocity_y = 8

                if event.key == pygame.K_a:
                    #wraith.image = wraith_l[index_update_constant]
                    wraith.walking = True
                    wraith.right = False
                    wraith.left = True                        
                    wraith.velocity_x = -12

                elif event.key == pygame.K_d:
                    #wraith.image = wraith_r[index_update_constant]
                    wraith.walking = True
                    wraith.right = True
                    wraith.left = False
                    wraith.velocity_x = 12

                if event.key == pygame.K_w:
                    if wraith.jump == False:
                        wraith.jump = True

                if event.key == pygame.K_KP9:
                    quaking = True

                if event.key == pygame.K_KP0:
                    quaking = True
                    wraith.firing = True

                if event.key == pygame.K_p:
                    resume_sound.play()
                    pause()

                # Character change
                if event.key == pygame.K_1:
                    wraith.r_imgs = wraith_r
                    wraith.l_imgs = wraith_l
                    wraith.leftidle = wraith_idle_l
                    wraith.rytidle = wraith_idle_r
                    wraith.hurt_l = wraith_hurt_l
                    wraith.hurt_r = wraith_hurt_r
                    
                if event.key == pygame.K_2:
                    wraith.r_imgs = wraith2_r
                    wraith.l_imgs = wraith2_l
                    wraith.leftidle = wraith2_idle_l
                    wraith.rytidle = wraith2_idle_r
                    wraith.hurt_l = wraith2_hurt_l
                    wraith.hurt_r = wraith2_hurt_r

                if event.key == pygame.K_3:
                    wraith.r_imgs = wraith3_r
                    wraith.l_imgs = wraith3_l
                    wraith.leftidle = wraith3_idle_l
                    wraith.rytidle = wraith3_idle_r
                    wraith.hurt_l = wraith3_hurt_l
                    wraith.hurt_r = wraith3_hurt_r
                    
            # Keyup
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    wraith.velocity_y = 0

                elif event.key == pygame.K_s:
                    wraith.velocity_y = 0

                if event.key == pygame.K_a:
                    wraith.walking = False
                    wraith.velocity_x = 0

                elif event.key == pygame.K_d:
                    wraith.walking = False
                    wraith.velocity_x = 0

                if event.key == pygame.K_KP0:
                    quaking = False
                    wraith.firing = False
                    #bck_x = 0
                    #bck_y = 0

        if quaking == True:
            #quaking = False
            quake(2)

        else:
            bck_x = 0
            bck_x = 0

            
        
        #screen.fill((BLACK))
        try:
            screen.blit(bck_list[bck_index], (bck_x,bck_y))
        except:
                bck_index = 0


        if wraith.rect.left > WIDTH:
            if bck_index != 11:
                wraith.rect.right = 0
                bck_index += 1
            else:
                wraith.rect.left = WIDTH

        elif wraith.rect.right < 0 :
            if bck_index != 0:
                wraith.rect.left = WIDTH
                bck_index -= 1
            else:
                wraith.rect.right = 0

        print("bck_index = ",bck_index)

        #index_update_constant += 1
        # Update
        all_sprites.update()
        # Draw
        all_sprites.draw(screen)
        # display flip
        pygame.display.flip()



game_intro()
game_loop()

