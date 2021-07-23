import pygame
import sys
from videos import *

from pygame import sprite
from note_effect import *


# /\/\/\/\/\/\/\/\/\/\/\ README /\/\/\/\/\/\/\/\/\/\/\
#                                                   #
#                                                   #
#           Video to images => 21653 images         #
#                                                   #
#                                                   #
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\


# from PIL import Image  # < - - - - - - - - - - - - - - Image controll module - if u want use, uncomment this line

# - cropping image file
# img = Image.open("Pictures/Note_BG.png")
# cropped_img = img.crop((0, 200, 200, 600))

# PIL to pygameSurface function

# - 이미지 크로핑
# img = Image.open("Pictures/Note_BG.png")
# cropped_img = img.crop((0, 200, 200, 600))
# pygameSurface = pilImageToSurface(cropped_img)  # PIL to pygameSurface
# re = pygame.transform.scale(pygameSurface, (196, 400))
# screen.blit(re, (5, 200))


# -------- Resource list

# Note effect

note_effect_list = ['src/effect/click_1_1.png',
                    'src/effect/click_1_2.png',
                    'src/effect/click_1_3.png',
                    'src/effect/click_1_4.png',
                    'src/effect/click_1_5.png',
                    'src/effect/click_1_6.png',
                    'src/effect/click_1_7.png',
                    'src/effect/click_1_8.png',
                    'src/effect/click_1_9.png',
                    'src/effect/click_1_10.png']


# Combo Resource

combo_list = []


# Life bar

life_bar_list = []
for x in range(1, 61):
    a = f"src/lifebar/lifebar_{x}.png"
    life_bar_list.append(a)


# -------- Function

def pilImageToSurface(pilImage):
    return pygame.image.fromstring(
        pilImage.tobytes(), pilImage.size, pilImage.mode).convert()


def sort_sprites(list, position, size):
    sp = EffectSprite(list, position, size)
    return pygame.sprite.OrderedUpdates(sp)


def time_banner():
    second = str(round(pygame.time.get_ticks()*0.001))
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
        f"src/font/banner_font/banner{second[2]}.png").convert_alpha()
    S = pygame.image.load(
        f"src/font/banner_font/banner{second[1]}.png").convert_alpha()
    T = pygame.image.load(
        f"src/font/banner_font/banner{second[0]}.png").convert_alpha()
    F = pygame.transform.scale(F, (24, 20))
    S = pygame.transform.scale(S, (24, 20))
    T = pygame.transform.scale(T, (24, 20))
    screen.blit(F, (382, 571))
    screen.blit(S, (356, 571))
    screen.blit(T, (318, 571))
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
                f"src/combo/number/number{combo}.png").convert_alpha()
            C = pygame.transform.scale(C, scale)
            screen.blit(C, (74, pos_y))
        elif len(combo) == 2:
            print(type(combo))
            print(combo[0], "    ", combo[1])
            F_C = pygame.image.load(
                f"src/combo/number/number{combo[1]}.png").convert_alpha()
            S_C = pygame.image.load(
                f"src/combo/number/number{combo[0]}.png").convert_alpha()
            F_C = pygame.transform.scale(F_C, scale)
            S_C = pygame.transform.scale(S_C, scale)
            screen.blit(F_C, (95, pos_y))
            screen.blit(S_C, (52, pos_y))
        elif len(combo) == 3:
            F_C = pygame.image.load(
                f"src/combo/number/number{combo[2]}.png").convert_alpha()
            S_C = pygame.image.load(
                f"src/combo/number/number{combo[1]}.png").convert_alpha()
            T_C = pygame.image.load(
                f"src/combo/number/number{combo[0]}.png").convert_alpha()
            F_C = pygame.transform.scale(F_C, scale)
            S_C = pygame.transform.scale(S_C, scale)
            T_C = pygame.transform.scale(T_C, scale)
            screen.blit(F_C, (118, pos_y))
            screen.blit(S_C, (74, pos_y))
            screen.blit(T_C, (30, pos_y))
        else:
            F_C = pygame.image.load(
                f"src/combo/number/number{combo[3]}.png").convert_alpha()
            S_C = pygame.image.load(
                f"src/combo/number/number{combo[2]}.png").convert_alpha()
            T_C = pygame.image.load(
                f"src/combo/number/number{combo[1]}.png").convert_alpha()
            FF_C = pygame.image.load(
                f"src/combo/number/number{combo[0]}.png").convert_alpha()
            F_C = pygame.transform.scale(F_C, scale)
            S_C = pygame.transform.scale(S_C, scale)
            T_C = pygame.transform.scale(T_C, scale)
            FF_C = pygame.transform.scale(FF_C, scale)
            screen.blit(F_C, (138, pos_y))
            screen.blit(S_C, (95, pos_y))
            screen.blit(T_C, (52, pos_y))
            screen.blit(FF_C, (9, pos_y))


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

screen = pygame.display.set_mode((WINDOW))
pygame.display.set_caption(
    'Py2Jam : Billie Eilish - NDA')   # <-------- Sample Name
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

life_effect = sort_sprites(life_bar_list, position=(201, 247), size=(9, 302))


# Combo Effect

combo_size = (64, 64)
combo_effect = sort_sprites(
    [f"src/combo/combo_title{x}.png" for x in range(1, 13)], (64, 150), combo_size)


# -------- Main Frames load


img_note = pygame.image.load("src/frames/note_frame.png")
img_note = pygame.transform.scale(img_note, (200, 600))
img_play = pygame.image.load("src/frames/bg_frame.png").convert_alpha()
img_play = pygame.transform.scale(img_play, (600, 560))
img_menu = pygame.image.load("src/frames/bottom_frame.png")
img_menu = pygame.transform.scale(img_menu, (600, 40))
test = pygame.image.load("src/frames/images.png")
test = pygame.transform.scale(test, (600, 600))
life_bar = pygame.image.load("src/lifebar/empty_bar.png")
white_note = pygame.image.load("src/notes/note_white_1.png")
blue_note = pygame.image.load("src/notes/note_blue_2.png")
yellow_note = pygame.image.load("src/notes/note_yellow_4.png")
white_blur = pygame.image.load("src/notes/note_white_blur.png")
blue_blur = pygame.image.load("src/notes/note_blue_blur.png")
blue_blur2 = pygame.image.load("src/notes/note_blue_blur.png")
blue_blur2 = pygame.transform.scale(blue_blur2, (29, 480))
yellow_blur = pygame.image.load("src/notes/note_yellow_blur.png")
fever_gage = pygame.image.load("src/frames/fever_gage.png")
jam_frame = pygame.image.load("src/frames/jam_frame.png")


'''
keys = pygame.key.get_pressed()
white = [keys[pygame.K_s], keys[pygame.K_f],
         keys[pygame.K_j], keys[pygame.K_l]]
blue = [keys[pygame.K_d], keys[pygame.K_k]]
yellow = keys[pygame.K_SPACE]
'''

#  -------- System init


n = 1
playing = True
FEVER = False


# -------- BGM Settings

pygame.mixer.music.load('src/music/bgm.mp3')
pygame.mixer.music.play()
pygame.mixer.music.pause()


# --------  Background Video


# video_sprite1 = VideoSprite(pygame.Rect(
#     200, -150, 600, 850), 'src/music/billie2.mpg')   # <-------- Full Size Video

video_sprite1 = VideoSprite(pygame.Rect(
    200, 0, 600, 600), 'src/music/billie2.mpg')  # <-------- Middle Size Video
sprite_group = pygame.sprite.Group()
sprite_group.add(video_sprite1)

minute = 0
combo = 0


while playing:
    pygame.mixer.music.unpause()
    #  Key list
    keys = pygame.key.get_pressed()
    white = [keys[pygame.K_s], keys[pygame.K_f],
             keys[pygame.K_j], keys[pygame.K_l]]
    blue = [keys[pygame.K_d], keys[pygame.K_k]]
    yellow = keys[pygame.K_SPACE]

    # Bliting default frames
    screen.fill(color_white)
    sprite_group.draw(screen)
    screen.blit(img_play, (200, 0))
    screen.blit(img_note, (0, 0))
    screen.blit(img_menu, (200, 560))
    screen.blit(fever_gage, (2, 536))
    screen.blit(life_bar, (201, 247))
    screen.blit(jam_frame, (222, 504))
    time_banner()
    life_effect.draw(screen)
    life_effect.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()
            sys.exit()

    # Note controllers

    if white[0] == 1:
        screen.blit(white_note, (3, 487))
        screen.blit(white_blur, (6, 215))
        note_ef_1.draw(screen)
        note_ef_1.update()
        combo_effect.draw(screen)
        combo_effect.update()
        combo += 1
        draw_combo(combo)

    if blue[0] == 1:
        screen.blit(blue_note, (32, 487))
        screen.blit(blue_blur, (31, 0))
        note_ef_2.draw(screen)
        note_ef_2.update()
        combo_effect.draw(screen)
        combo_effect.update()
    if white[1] == 1:
        screen.blit(white_note, (52, 487))
        screen.blit(white_blur, (54, 215))
        note_ef_3.draw(screen)
        note_ef_3.update()
        combo_effect.draw(screen)
        combo_effect.update()
    if yellow == 1:
        screen.blit(yellow_note, (80, 487))
        screen.blit(yellow_blur, (79, 0))
        note_ef_4.draw(screen)
        note_ef_4.update()
        combo_effect.draw(screen)
        combo_effect.update()
    if white[2] == 1:
        screen.blit(white_note, (111, 487))
        screen.blit(white_blur, (112, 215))
        note_ef_5.draw(screen)
        note_ef_5.update()
        combo_effect.draw(screen)
        combo_effect.update()
    if blue[1] == 1:
        screen.blit(blue_note, (140, 487))
        screen.blit(blue_blur2, (136, 1))
        note_ef_6.draw(screen)
        note_ef_6.update()
        combo_effect.draw(screen)
        combo_effect.update()
    if white[3] == 1:
        screen.blit(white_note, (161, 487))
        # print(pygame.time.get_ticks()) -> 실시간 틱 단위 출력
        screen.blit(white_blur, (165, 215))
        note_ef_7.draw(screen)
        note_ef_7.update()
        combo_effect.draw(screen)
        combo_effect.update()  # ----- !!! all combo_effect is sample
    sprite_group.update()
    pygame.display.flip()
    clock.tick(60)
