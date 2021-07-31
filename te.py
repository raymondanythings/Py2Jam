import copy
import threading
import time
import pygame
import sys
from videos import *
import os
from note_effect import *
from math import floor
import timeit
import copy

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


def blit_alpha(target, source, location, opacity):
    # build_alpha By http://www.nerdparadise.com/programming/pygameblitopacity
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)


# create Explosion class
class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, path, file, n):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, n+1):
            img = pygame.image.load(
                f"{PATH(CWD,SRC,'%s','%s'+'%s.png')}" % (path, file, num)).convert_alpha()
            # img = pygame.transform.scale(img, (100, 100))
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


# Game Setting
FPS = 70
BGA_FPS = 23.98
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
S_HEIGHT = WINDOW_HEIGHT - 50

SHOWN_TIME = 1500
SPEED_RATE = 1.5
EFFECT_TIME = 1000

SCORE_STRING = ["GREAT", " GOOD", " ALSO", " MISS", "COMBO", "SCORE"]
WHITE = [255, 255, 255]

# Game Variable
score_status = [0, 0, 0, 0]
score = 0
combo = 0
check_combo = 0
display_score = 0


# Game Init
sounds = pygame.mixer
sounds.pre_init(44100, -16, 2, 512)
sounds.init()
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Rhythm Game')
toggle_effect = False

effect_group = pygame.sprite.Group()
banner_group = pygame.sprite.Group()


# Load Images
note_effect = pygame.image.load(
    "src/notes/note_white_blur.png").convert_alpha()

noteImage_white = pygame.image.load(
    f"{PATH(CWD,SRC,'notes','note_flat_white.png')}")
noteImage_blue = pygame.image.load(
    f"{PATH(CWD,SRC,'notes','note_flat_blue.png')}")
noteImage_yellow = pygame.image.load(
    f"{PATH(CWD,SRC,'notes','note_flat_yellow.png')}")
# noteImage = pygame.transform.scale(noteImage, (70, 5))
# note_effect = pygame.image.load("note-effect.png").convert_alpha()
# note_effect.set_alpha(125)
# note_effect = pygame.transform.scale(note_effect, (70, 200))
all_note_list = pygame.sprite.Group()

# Load Chabo
dArray = []
display_chabo = []
readTurn = 0
f = open("note.txt", "r")
for line in f.readlines():
    if line[0] == '#':
        if (readTurn > 0):
            display_chabo.append(dArray)
            dArray = []
        readTurn = int(line[1])
        continue

    line = line.replace("\n", "")
    dArray.append(int(float(line) * 1000))
f.close()
display_chabo.append(dArray)
checking_chabo = copy.deepcopy(display_chabo)


# # LoadBGA
bga_files = []
for file in os.listdir("bga"):
    bga_files.append(file)


def getRuntime():
    end = timeit.default_timer()
    runtime = int((end - start) * 1000)
    return runtime


class Note(pygame.sprite.Sprite):
    def __init__(self, time, noteImg):
        super().__init__()
        self.s_Time = time
        self.image = noteImg
        self.width = 0
        self.rect = self.image.get_rect()

    def update(self):
        if(self.rect.y > 485):
            all_note_list.remove(self)
            return

        end = timeit.default_timer()
        runtime = int((end - start) * 1000)
        self.rect.y = 485 - ((self.s_Time - getRuntime()) / (
            SHOWN_TIME / SPEED_RATE)) * S_HEIGHT - (WINDOW_HEIGHT - S_HEIGHT)


keys_status = [0, 0, 0, 0, 0]


class KeyReader(threading.Thread):
    def run(self):
        while running:
            end = timeit.default_timer()
            runtime = getRuntime()
            keys = pygame.key.get_pressed()

            if keys[pygame.K_s]:
                if(keys_status[0] == 0):
                    checkNote(runtime, 0)
                keys_status[0] = 1

            else:
                keys_status[0] = 0
            if keys[pygame.K_d]:
                if(keys_status[1] == 0):
                    checkNote(runtime, 1)
                keys_status[1] = 1
            else:
                keys_status[1] = 0
            if keys[pygame.K_f]:
                if(keys_status[2] == 0):
                    checkNote(runtime, 2)
                keys_status[2] = 1
            else:
                keys_status[2] = 0
            if keys[pygame.K_SPACE]:
                if(keys_status[3] == 0):
                    checkNote(runtime, 3)
                keys_status[3] = 1
            else:
                keys_status[3] = 0
            if keys[pygame.K_j]:
                if(keys_status[4] == 0):
                    checkNote(runtime, 4)
                keys_status[4] = 1
            else:
                keys_status[4] = 0

            time.sleep(0.001)


def checkNote(time, key):
    global combo, score, score_status, toggle_effect

    abs_min = 999999
    index_min = 0
    if len(checking_chabo[key]) > 0:
        try:
            for i in range(0, len(checking_chabo[key])):
                if abs(checking_chabo[key][i] - time) < abs_min:
                    abs_min = abs(checking_chabo[key][i] - time)
                    index_min = i
            if(abs_min < 250):
                if abs_min < 50:
                    score_status[0] = score_status[0] + 1
                    score = score + (combo * 0.01 + 1) * 300
                    combo = combo + 1
                elif abs_min < 150:
                    score_status[1] = score_status[1] + 1

                    score = score + (combo * 0.01 + 1) * 300
                    combo = combo + 1
                else:
                    score_status[2] = score_status[2] + 1
                    score = score + (combo * 0.01 + 1) * 300
                    combo = combo + 1

                checking_chabo[key].pop(index_min)
                toggle_effect = True
        except:
            pass


def checkMiss():
    global combo, score_status, toggle_effect

    for i in range(0, len(checking_chabo)):
        if(len(checking_chabo[i]) > 0):
            if checking_chabo[i][0] - getRuntime() <= -250:
                checking_chabo[i].pop(0)
                score_status[3] = score_status[3] + 1
                combo = 0
                toggle_effect = False


class ChaboReader(threading.Thread):
    def run(self):
        while running:
            for i in range(0, len(display_chabo)):
                if not len(display_chabo[i]) is 0:
                    end = timeit.default_timer()
                    runtime = int((end - start) * 1000)
                    temp = SHOWN_TIME / SPEED_RATE
                    if display_chabo[i][0] - temp <= runtime:
                        # i <- 노트열 번호
                        # display_chabo[0][0] <- 떨어지는 노트 타이밍(시간)
                        if i == 0 or i == 2 or i == 4 or i == 6:
                            noteImg = noteImage_white
                            wit = i-0.1
                        elif i == 3:
                            noteImg = noteImage_yellow
                            wit = 2.7
                        else:
                            noteImg = noteImage_blue
                            wit = i+0.5
                        createNote(wit, display_chabo[i][0], noteImg)
                        display_chabo[i].pop(0)
            checkMiss()
            time.sleep(0.001)


def createNote(line, time, noteImg):
    note = Note(time, noteImg)
    note.rect.x = 0 + noteImg.get_rect().width * line
    note.rect.y = 0
    all_note_list.add(note)


def blit_alpha(target, source, location, opacity):
    # build_alpha By http://www.nerdparadise.com/programming/pygameblitopacity
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)


bgmImage = 0
prevNum = 0


def draw():
    global display_score, score_status, bgmImage, prevNum, combo, check_combo

    try:
        # Clear Sreen
        # screen.fill((0, 0, 0))
        bgaNum = int((getRuntime() / 1000) * BGA_FPS)
        if (str(bgaNum) + ".jpg") in bga_files:
            if prevNum == bgaNum:
                screen.blit(bgmImage, (200, 0))
            else:
                bgmImage = pygame.image.load("bga/" + str(bgaNum) + ".jpg")
                bgmImage = pygame.transform.scale(
                    bgmImage, (700, 600))
                screen.blit(bgmImage, (200, 0))
                prevNum = bgaNum

        screen.blit(img_play, (204, 0))
        screen.blit(img_note, (0, 0))
        screen.blit(img_menu, (204, 558))
        screen.blit(fever_gage, (2, 536))
        screen.blit(life_bar, (204, 247))
        screen.blit(jam_frame, (222, 504))

        # Draw Lines And Key Boxes
        # pygame.draw.line(screen, WHITE, [100 + noteImage.get_rect().width * 0, 0], [
        #                  100 + noteImage.get_rect().width * 0, WINDOW_HEIGHT], 4)
        # for i in range(1, 5):
        #     pygame.draw.line(screen, WHITE, [100 + noteImage.get_rect().width * i, 0], [
        #                      100 + noteImage.get_rect().width * i, WINDOW_HEIGHT], 2)
        # pygame.draw.line(screen, WHITE, [100 + noteImage.get_rect().width * 5, 0], [
        #                  100 + noteImage.get_rect().width * 5, WINDOW_HEIGHT], 4)

        # pygame.draw.line(screen, WHITE, [100, S_HEIGHT], [
        #                  100 + noteImage.get_rect().width * 5, S_HEIGHT], 2)
        # for i in range(0, 5):
        #     keyBox = pygame.Rect(100 + noteImage.get_rect().width * i + 2, S_HEIGHT + 2,
        #                          noteImage.get_rect().width - 2, WINDOW_HEIGHT - S_HEIGHT - 2)
        #     if i % 2 == 0:
        #         pygame.draw.rect(screen, [255, 107, 108], keyBox)
        #     else:
        #         pygame.draw.rect(screen, [51, 134, 238], keyBox)

        explosion_group.draw(screen)
        explosion_group.update()
        if white[0] == 1:
            screen.blit(white_note, (3, 487))
            screen.blit(white_blur, (4, 0))
            effect = Explosion(18, 482, 'effect', 'click_1_', 10)
            effect_group.add(effect)

        if blue[0] == 1:
            screen.blit(blue_note, (32, 487))
            screen.blit(blue_blur, (31, 0))
            effect = Explosion(42, 482, 'effect', 'click_1_', 10)
            effect_group.add(effect)

        if white[1] == 1:
            screen.blit(white_note, (53, 487))
            screen.blit(white_blur, (54, 0))
            effect = Explosion(69, 482, 'effect', 'click_1_', 10)
            effect_group.add(effect)

        if yellow == 1:
            screen.blit(yellow_note, (83, 487))
            screen.blit(yellow_blur, (79, 0))
            effect = Explosion(98, 482, 'effect', 'click_1_', 10)
            effect_group.add(effect)

        if white[2] == 1:
            screen.blit(white_note, (113, 487))
            screen.blit(white_blur, (112, 0))
            effect = Explosion(129, 482, 'effect', 'click_1_', 10)
            effect_group.add(effect)

        if blue[1] == 1:
            screen.blit(blue_note, (143, 487))
            screen.blit(blue_blur2, (136, 0))
            effect = Explosion(153, 482, 'effect', 'click_1_', 10)
            effect_group.add(effect)

        if white[3] == 1:
            screen.blit(white_note, (164, 487))
            screen.blit(white_blur, (165, 0))
            effect = Explosion(180, 482, 'effect', 'click_1_', 10)
            effect_group.add(effect)

        # if start_clock == 2.0:
        # if ba == []:
        #     ba.append(sp_bar)
        # ba[0].show(screen)
        # ba[0].po_y += spd
        # if ba[0].po_y >= 480:
        #     ba[0].po_y = 0
        #     del ba[0]

        # Note controllers

        all_note_list.update()
        all_note_list.draw(screen)

        # Label Drawer
        myfont = pygame.font.SysFont("Dotum", 25)

        if display_score < int(score):
            display_score = display_score + 20

        totalHit = score_status[0] + score_status[1] + \
            score_status[2] + score_status[3] + 0.0001
        for i in range(0, 4):
            label = myfont.render(SCORE_STRING[i], 1, WHITE)
            screen.blit(label, (500, 100 + i * 50))
            label = myfont.render(str(
                score_status[i]) + "    ( " + str(int(score_status[i] / totalHit * 100)) + "% )", 1, WHITE)
            screen.blit(label, (600, 100 + i * 50))

        label = myfont.render(SCORE_STRING[4], 1, WHITE)
        screen.blit(label, (500, 300))
        label = myfont.render(str(combo), 1, WHITE)
        screen.blit(label, (600, 300))
        label = myfont.render(SCORE_STRING[5], 1, WHITE)
        screen.blit(label, (500, 350))
        label = myfont.render(str(int(display_score)), 1, WHITE)
        screen.blit(label, (600, 350))
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     pos = pygame.mouse.get_pos()
        #     explosion = Explosion(pos[0], pos[1])
        #     explosion_group.add(explosion)

        '''
            if keys[pygame.K_s]:
                effect_opacity[0] = 255
                if(keys_status[0] == 0):
                    # sounds.Sound("hihat.wav").play()
                    checkNote(runtime, 0)
                    keys_status[0] = 1
                else:
                    keys_status[0] = 0
            if keys[pygame.K_d]:
                effect_opacity[1] = 255
                if(keys_status[1] == 0):
                    # sounds.Sound("hihat.wav").play()
                    checkNote(runtime, 1)
                keys_status[1] = 1
            else:
                keys_status[1] = 0
            if keys[pygame.K_f]:
                effect_opacity[2] = 255
                if(keys_status[2] == 0):
                    # sounds.Sound("hihat.wav").play()
                    checkNote(runtime, 2)
                keys_status[2] = 1
            else:
                keys_status[2] = 0
            if keys[pygame.K_SPACE]:
                effect_opacity[3] = 255
                if(keys_status[3] == 0):
                    # sounds.Sound("hihat.wav").play()
                    checkNote(runtime, 3)
                keys_status[3] = 1
            else:
                keys_status[3] = 0
            if keys[pygame.K_j]:
                effect_opacity[4] = 255
                if(keys_status[4] == 0):
                    # sounds.Sound("hihat.wav").play()
                    checkNote(runtime, 4)
                keys_status[4] = 1
            else:
                keys_status[4] = 0
            time.sleep(0.001)
        draw_combo(combo)
        '''
        if check_combo != combo:
            banner = Explosion(100, 150, 'combo', 'combo_title', 12)
            banner_group.add(banner)
            check_combo += 1
        if combo == 0:
            check_combo = 0
        draw_combo(combo)
        effect_group.draw(screen)
        effect_group.update()
        banner_group.draw(screen)
        banner_group.update()
        time_banner()
        pygame.display.flip()
    except:
        print("???")


    # -------- Basic settings
pygame.init()

pygame.mixer.init()


# -------- Loading Log


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

# !- All different x - position
note_ef_2 = sort_sprites(note_effect_list, (-17, note_y), nf_size)
note_ef_3 = sort_sprites(note_effect_list, (9, note_y), nf_size)
note_ef_4 = sort_sprites(note_effect_list, (35, note_y), nf_size)
note_ef_5 = sort_sprites(note_effect_list, (66, note_y), nf_size)


# Life bar


life_effect = sort_sprites(life_bar_list, position=(204, 247), size=(9, 302))


combo_size = (64, 64)


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

pygame.mixer.music.load(f"{PATH(CWD,'bgm.wav')}")
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
running = True
start = timeit.default_timer()
KeyReader().start()
ChaboReader().start()


t = 0
start = timeit.default_timer()
screen.fill(color_white)
while running:

    runtime = getRuntime()
    start_clock = round(pygame.time.get_ticks()*0.001, 1)
# Define ms
    if t == start_clock:
        pass
    else:
        t = start_clock
    if t >= 0.5:
        pygame.mixer.music.unpause()
    # if t >= 0.2:
    # note1.draw_note(screen, spd)

    # screen.fill(color_white)
    # sprite_group.draw(screen)
    # sprite_group.update()

    # screen.blit(load_img, (100, 0))
    #  Key list
    keys = pygame.key.get_pressed()
    white = [keys[pygame.K_s], keys[pygame.K_f],
             keys[pygame.K_j], keys[pygame.K_l]]
    blue = [keys[pygame.K_d], keys[pygame.K_k]]
    yellow = keys[pygame.K_SPACE]

    # Bliting default frames

    life_effect.draw(screen)
    life_effect.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    draw()
    pygame.display.update()
    clock.tick(FPS)
