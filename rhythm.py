import pygame
import sys
from videos import *
import os
from note_effect import *
from math import floor
import timeit

# /\/\/\/\/\/\/\/\/\/\/\ README /\/\/\/\/\/\/\/\/\/\/\
#                                                   #
#                                                   #
#           Video to images => 21653 images         #
#                                                   #
#                                                   #
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\


PATH = os.path.join
CWD = os.getcwd()
SRC = "src"
note_y = 0
note1_path = f"{PATH(CWD, SRC,'notes','note_flat_white.png')}, 3, {note_y}"
note2_path = f"{PATH(CWD, SRC,'notes','note_flat_blue.png')}", 32, note_y
note3_path = f"{PATH(CWD, SRC,'notes','note_flat_white.png')}", 54, note_y
note4_path = f"{PATH(CWD, SRC,'notes','note_flat_yellow.png')}", 82, note_y
note5_path = f"{PATH(CWD, SRC,'notes','note_flat_white.png')}", 113, note_y
note6_path = f"{PATH(CWD, SRC,'notes','note_flat_blue.png')}", 143, note_y
note7_path = f"{PATH(CWD, SRC,'notes','note_flat_white.png')}", 164, note_y


# -------- Resource list

# Note effect

note_effect_list = []

for x in range(1, 11):
    a = f"{PATH(CWD,SRC,'effect','click_1_%s.png')}" % x
    note_effect_list.append(a)


# Combo Resource

combo_list = []


# Life bar

life_bar_list = []
for x in range(1, 61):
    a = f"{PATH(CWD,SRC,'lifebar','lifebar_%d.png')}" % x
    life_bar_list.append(a)


# -------- Function

def getRuntime():
    end = timeit.default_timer()
    runtime = int((end - start) * 1000)
    return runtime


def sort_sprites(list, position, size):
    sp = EffectSprite(list, position, size)
    return pygame.sprite.OrderedUpdates(sp)


def time_banner():
    time_y = 568
    second = str(floor(pygame.time.get_ticks()*0.001))
    if len(second) == 1:
        second = f"00{second}"
    elif len(second) > 1:
        if int(second) >= 60:
            if len(str(int(second) % 60)) == 1:
                second = f"{int(int(second) / 60)}0{int(int(second) % 60)}"
            else:
                second = f"{int(int(second) / 60)}{int(int(second) % 60)}"
        else:
            second = f"0{second}"
    F = pygame.image.load(
        f"{PATH(CWD,SRC,'font','banner_font','banner%s.png')}" % second[2]).convert_alpha()
    S = pygame.image.load(
        f"{PATH(CWD,SRC,'font','banner_font','banner%s.png')}" % second[1]).convert_alpha()
    T = pygame.image.load(
        f"{PATH(CWD,SRC,'font','banner_font','banner%s.png')}" % second[0]).convert_alpha()
    F = pygame.transform.scale(F, (24, 20))
    S = pygame.transform.scale(S, (24, 20))
    T = pygame.transform.scale(T, (24, 20))
    screen.blit(F, (384, time_y))
    screen.blit(S, (358, time_y))
    screen.blit(T, (320, time_y))
    # elif time > 100:
    #     pass
    # else:
    #     pass


def draw_combo(combo):
    pos_y = 230
    scale = (40, 40)
    combo = str(combo)
    if combo == "0":
        pass
    else:
        if len(combo) == 1:
            C = pygame.image.load(
                f"{PATH(CWD,SRC,'combo','number','number%s.png')}" % combo[0]).convert_alpha()
            C = pygame.transform.scale(C, scale)
            screen.blit(C, (74, pos_y))
        elif len(combo) == 2:
            F_C = pygame.image.load(
                f"{PATH(CWD,SRC,'combo','number','number%s.png')}" % combo[1]).convert_alpha()
            S_C = pygame.image.load(
                f"{PATH(CWD,SRC,'combo','number','number%s.png')}" % combo[0]).convert_alpha()
            F_C = pygame.transform.scale(F_C, scale)
            S_C = pygame.transform.scale(S_C, scale)
            screen.blit(F_C, (95, pos_y))
            screen.blit(S_C, (52, pos_y))
        elif len(combo) == 3:
            F_C = pygame.image.load(
                f"{PATH(CWD,SRC,'combo','number','number%s.png')}" % combo[2]).convert_alpha()
            S_C = pygame.image.load(
                f"{PATH(CWD,SRC,'combo','number','number%s.png')}" % combo[1]).convert_alpha()
            T_C = pygame.image.load(
                f"{PATH(CWD,SRC,'combo','number','number%s.png')}" % combo[0]).convert_alpha()
            F_C = pygame.transform.scale(F_C, scale)
            S_C = pygame.transform.scale(S_C, scale)
            T_C = pygame.transform.scale(T_C, scale)
            screen.blit(F_C, (118, pos_y))
            screen.blit(S_C, (74, pos_y))
            screen.blit(T_C, (30, pos_y))
        else:
            F_C = pygame.image.load(
                f"{PATH(CWD,SRC,'combo','number','number%s.png')}" % combo[3]).convert_alpha()
            S_C = pygame.image.load(
                f"{PATH(CWD,SRC,'combo','number','number%s.png')}" % combo[2]).convert_alpha()
            T_C = pygame.image.load(
                f"{PATH(CWD,SRC,'combo','number','number%s.png')}" % combo[1]).convert_alpha()
            FF_C = pygame.image.load(
                f"{PATH(CWD,SRC,'combo','number','number%s.png')}" % combo[0]).convert_alpha()
            F_C = pygame.transform.scale(F_C, scale)
            S_C = pygame.transform.scale(S_C, scale)
            T_C = pygame.transform.scale(T_C, scale)
            FF_C = pygame.transform.scale(FF_C, scale)
            screen.blit(F_C, (138, pos_y))
            screen.blit(S_C, (95, pos_y))
            screen.blit(T_C, (52, pos_y))
            screen.blit(FF_C, (9, pos_y))


# create Explosion class
class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 11):
            img = pygame.image.load(
                f"{PATH(CWD,SRC,'effect','click_1_%s.png')}" % num)
            img = pygame.transform.scale(img, (100, 100))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0

    def update(self):
        explosion_speed = 2.5
        # update explosion animation
        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        # if the animation is complete, reset animation index
        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()

    # -------- Basic settings
pygame.init()

pygame.mixer.init()


# -------- Loading Log

print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\")
print("")
print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\      N   O   W           L   O   A   D   I   N   G   ...         /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\")
print("")
print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\")

WINDOW = (800, 600)
BPM = 120
BPS = 1 / round(BPM / 60)
spd = 8

screen = pygame.display.set_mode((WINDOW))
pygame.display.set_caption(
    'Py2Jam : RAMDARAM x AIRCOC')   # <-------- Sample Name
clock = pygame.time.Clock()
color_white = (255, 255, 255)

# -------- Make orderd sprites group

# video to image convert


# Note effects - First
note_y = 427
nf_position = (-43, note_y)
nf_size = (120, 120)

# !- All different x - position -!
note_ef_1 = sort_sprites(note_effect_list, nf_position, nf_size)
note_ef_2 = sort_sprites(note_effect_list, (-17, note_y), nf_size)
note_ef_3 = sort_sprites(note_effect_list, (9, note_y), nf_size)
note_ef_4 = sort_sprites(note_effect_list, (35, note_y), nf_size)
note_ef_5 = sort_sprites(note_effect_list, (66, note_y), nf_size)
note_ef_6 = sort_sprites(note_effect_list, (92, note_y), nf_size)
note_ef_7 = sort_sprites(note_effect_list, (116, note_y), nf_size)

# Life bar


life_effect_size = (9, 302)

life_effect = sort_sprites(life_bar_list, position=(204, 247), size=(9, 302))


# Combo Effect

combo_size = (64, 64)
combo_effect = sort_sprites(
    [f"{PATH(CWD,SRC,'combo','combo_title%s.png')}" % x for x in range(1, 13)], (64, 150), combo_size)


# -------- Main Frames load


img_note = pygame.image.load(f"{PATH(CWD, SRC, 'frames', 'note_frame.png')}")
img_play = pygame.image.load(
    f"{PATH(CWD, SRC, 'frames', 'bg_frame.png')}").convert_alpha()
img_menu = pygame.image.load(f"{PATH(CWD, SRC,'frames','bottom_frame.png')}")
life_bar = pygame.image.load(f"{PATH(CWD, SRC,'lifebar','empty_bar.png')}")
white_note = pygame.image.load(f"{PATH(CWD, SRC,'notes','note_white_1.png')}")
blue_note = pygame.image.load(f"{PATH(CWD, SRC,'notes','note_blue_2.png')}")
yellow_note = pygame.image.load(
    f"{PATH(CWD, SRC,'notes','note_yellow_4.png')}")
white_blur = pygame.image.load(
    f"{PATH(CWD, SRC,'notes','note_white_blur.png')}")
blue_blur = pygame.image.load(f"{PATH(CWD, SRC,'notes','note_blue_blur.png')}")
blue_blur2 = pygame.image.load(
    f"{PATH(CWD, SRC,'notes','note_blue_blur.png')}")
blue_blur2 = pygame.transform.scale(blue_blur2, (29, 480))
yellow_blur = pygame.image.load(
    f"{PATH(CWD, SRC,'notes','note_yellow_blur.png')}")
fever_gage = pygame.image.load(f"{PATH(CWD, SRC,'frames','fever_gage.png')}")
jam_frame = pygame.image.load(f"{PATH(CWD, SRC,'frames','jam_frame.png')}")
load_img = pygame.image.load(f"{PATH(CWD, SRC,'frames','loading.jpeg')}")
sp_bar = MakeNote(PATH(CWD, SRC, 'notes', 'sp_bar.png'), 4, 0)


#  -------- System init


n = 1
playing = True
FEVER = False


# -------- BGM Settings

pygame.mixer.music.load(f"{PATH(CWD,SRC,'music','bpm120.mp3')}")
pygame.mixer.music.play()
pygame.mixer.music.pause()


# --------  Background Video


# video_sprite1 = VideoSprite(pygame.Rect(
#     200, -150, 600, 850), 'src/music/billie2.mpg')   # <-------- Full Size Video

video_sprite1 = VideoSprite(pygame.Rect(
    100, 0, 800, 600), f"{PATH(CWD,SRC,'music','BG_video.mp4')}")
sprite_group = pygame.sprite.Group()
sprite_group.add(video_sprite1)


explosion_group = pygame.sprite.Group()

combo = 0
div = 0
beat = 0
bar = 0
ba = []

t = 0
start = timeit.default_timer()
screen.fill(color_white)
while playing:
    runtime = getRuntime()
    start_clock = round(pygame.time.get_ticks()*0.001, 1)
    print(runtime)
# Define ms

    if t == start_clock:
        pass
    else:
        t = start_clock

    if t == 7:
        note1.draw_note(screen, spd)

    if start_clock % BPS == 0:
        pass
    if start_clock >= 1:
        pygame.mixer.music.unpause()
        screen.fill(color_white)
        sprite_group.draw(screen)
        sprite_group.update()
    else:
        screen.blit(load_img, (100, 0))
    #  Key list
    keys = pygame.key.get_pressed()
    white = [keys[pygame.K_s], keys[pygame.K_f],
             keys[pygame.K_j], keys[pygame.K_l]]
    blue = [keys[pygame.K_d], keys[pygame.K_k]]
    yellow = keys[pygame.K_SPACE]

    # Bliting default frames
    screen.blit(img_play, (204, 0))
    screen.blit(img_note, (0, 0))
    screen.blit(img_menu, (204, 558))
    screen.blit(fever_gage, (2, 536))
    screen.blit(life_bar, (204, 247))
    screen.blit(jam_frame, (222, 504))
    time_banner()
    life_effect.draw(screen)
    life_effect.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                draw_combo(combo)
                combo += 1

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            explosion = Explosion(pos[0], pos[1])
            explosion_group.add(explosion)

    explosion_group.draw(screen)
    explosion_group.update()
    if white[0] == 1:
        screen.blit(white_note, (3, 487))
        screen.blit(white_blur, (4, 0))
        note_ef_1.draw(screen)
        note_ef_1.update()
        combo_effect.draw(screen)
        combo_effect.update()

    if blue[0] == 1:
        screen.blit(blue_note, (32, 487))
        screen.blit(blue_blur, (31, 0))
        note_ef_2.draw(screen)
        note_ef_2.update()
        combo_effect.draw(screen)
        combo_effect.update()

    if white[1] == 1:
        screen.blit(white_note, (53, 487))
        screen.blit(white_blur, (54, 0))
        note_ef_3.draw(screen)
        note_ef_3.update()
        combo_effect.draw(screen)
        combo_effect.update()

    if yellow == 1:
        screen.blit(yellow_note, (83, 487))
        screen.blit(yellow_blur, (79, 0))
        note_ef_4.draw(screen)
        note_ef_4.update()
        combo_effect.draw(screen)
        combo_effect.update()

    if white[2] == 1:
        screen.blit(white_note, (113, 487))
        screen.blit(white_blur, (112, 0))
        note_ef_5.draw(screen)
        note_ef_5.update()
        combo_effect.draw(screen)
        combo_effect.update()

    if blue[1] == 1:
        screen.blit(blue_note, (143, 487))
        screen.blit(blue_blur2, (136, 0))
        note_ef_6.draw(screen)
        note_ef_6.update()
        combo_effect.draw(screen)
        combo_effect.update()

    if white[3] == 1:
        screen.blit(white_note, (164, 487))
        # print(pygame.time.get_ticks()) -> 실시간 틱 단위 출력
        screen.blit(white_blur, (165, 0))
        note_ef_7.draw(screen)
        note_ef_7.update()
        combo_effect.draw(screen)
        combo_effect.update()  # ----- !!! all combo_effect is sample
        draw_combo(combo)
        combo += 1

    # if start_clock == 2.0:
    if ba == []:
        ba.append(sp_bar)
    ba[0].show(screen)
    ba[0].po_y += spd
    if ba[0].po_y >= 480:
        ba[0].po_y = 0
        del ba[0]

    # Note controllers
    note_y = 0
    note1 = MakeNote(
        f"{PATH(CWD, SRC,'notes','note_flat_white.png')}", 3, note_y)
    note2 = MakeNote(
        f"{PATH(CWD, SRC,'notes','note_flat_blue.png')}", 32, note_y)
    note3 = MakeNote(
        f"{PATH(CWD, SRC,'notes','note_flat_white.png')}", 54, note_y)
    note4 = MakeNote(
        f"{PATH(CWD, SRC,'notes','note_flat_yellow.png')}", 82, note_y)
    note5 = MakeNote(
        f"{PATH(CWD, SRC,'notes','note_flat_white.png')}", 113, note_y)
    note6 = MakeNote(
        f"{PATH(CWD, SRC,'notes','note_flat_blue.png')}", 143, note_y)
    note7 = MakeNote(
        f"{PATH(CWD, SRC,'notes','note_flat_white.png')}", 164, note_y)
    pygame.display.update()
    clock.tick(70)
