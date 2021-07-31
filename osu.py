#!/usr/bin/python3

import shutil
import zipfile
import os
import sys
from math import *
fps = 60
size = (500, 500)


try:
    import tkinter as tk
    from tkinter import filedialog
    from tkinter import simpledialog as easy
    from tkinter import messagebox
except:
    print("Sorry, you need tkinter to choose a file.\nIf you want, you can just run `python3 osu.py <filename>` for now.")
    sys.exit()
else:
    root = tk.Tk()
    root.withdraw()

try:
    import pygame
except:
    messagebox.showerror(
        "missing library", "Sorry, you need pygame to play.", type="ok")
    sys.exit()


def col(a): return pygame.Color(str(a))


curdir = os.path.dirname(os.path.abspath(__file__))
impath = os.path.realpath((sys.argv+[""])[1])
tmpdir = os.path.join(curdir, "tmp", '')
mapdir = os.path.join(curdir, "maps", '')
fntdir = os.path.join(curdir, "fonts", '')

a = 'retry'
if os.path.isdir(impath):
    while a == 'retry':
        impath = filedialog.askopenfilename(
            initialdir=mapdir, title="Select Map")
        if len(impath) == 0:
            a = messagebox.showerror(
                "cancellation", "File selection cancelled.", type="retrycancel")
            if a == 'cancel':
                sys.exit()
        else:
            a = 'other thing'
            try:
                with zipfile.ZipFile(impath, 'r') as osz:
                    osz.extractall(tmpdir)
            except zipfile.BadZipFile:
                messagebox.showerror(
                    "format error", "Not even a valid zip file. Sad.")
                a = 'retry'

files = os.listdir(tmpdir)

maps = []
hasbg = False
hassong = False
hasmap = False
for file in files:
    if file[-3:] == "png" or file[-3:] == "jpg" or file[-4:] == "jpeg":
        hasbg = True
    if file[-3:] == "mp3" or file[-3:] == "wav":
        hassong = True
    if file[-3:] == "osu":
        hasmap = True
        maps = maps + [tmpdir+file]

if hasbg == False or hassong == False or hasmap == False:
    messagebox.showerror(
        "format error", "Not a valid osz. Missing a song, background, and/or map file(s).")
    sys.exit()

name = os.path.split(maps[0])[-1].split('.')[0].split('[')[0]
artist = name.split(' - ')[0]
songname = name.split(' - ')[1].split(' (')[0]
creator = name.split(' (')[1].split(') ')[0]

#print('name: '+name)
#print('artist: '+artist)
#print('song name: '+songname)
#print('creator: '+creator)

diffs = []
for mapname in maps:
    diffs = diffs+[os.path.split(mapname)[-1].split('.')
                   [0].split('[')[1].split(']')[0]]

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("osu! python edition")
clock = pygame.time.Clock()

lilfont = pygame.font.Font(os.path.join(fntdir, 'lil.ttf'), 25)
bigfont = pygame.font.Font(os.path.join(fntdir, 'big.ttf'), 90)
tinfont = pygame.font.Font(os.path.join(fntdir, 'lil.ttf'), 11)

logo = pygame.transform.scale(pygame.image.load(
    os.path.join(curdir, "icon.png")), (3*size[0]//4, 3*size[1]//4))
pygame.display.set_icon(pygame.transform.scale(logo, (32, 32)))

done = False
ticks = 0
truefps = 0
secs = 0
chosendiff = ""
page = 0
sections = []
content = ""
version = ""
sectitles = []
keys = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
        pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_0]
chosendiff = None
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = messagebox.askquestion(
                " ", "Really leave osu! python edition?", type="yesno")
            if a == 'yes':
                done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    if page == 0:
        screen.fill(col('magenta'))
        screen.blit(logo, (size[0]//8, size[1]//8))

    if page == 1:
        screen.fill(col('pink'))

        text = lilfont.render("artist - "+artist, True, col('cyan'))
        screen.blit(text, (10, 10))

        text = lilfont.render("song name - "+songname, True, col('orange'))
        screen.blit(text, (10, 40))

        text = lilfont.render("creator - "+creator, True, col('green'))
        screen.blit(text, (10, 70))

        pygame.display.set_caption(songname)

        text = lilfont.render("Difficulties:", True, col('black'))
        screen.blit(text, (10, 120))

        i = 0
        for diff in diffs:
            text = lilfont.render(str(int(i+1))+") "+diff, True, col('black'))
            screen.blit(text, (25, 30*i+150))
            i = i + 1

        pygame.display.flip()

        if chosendiff == None:
            chosendiff = easy.askinteger(" ", "Pick a map \N{number sign}:")
        else:
            page = 2

    if page == 2:
        screen.fill(col('white'))
        pygame.display.set_caption(songname + " - " + diffs[chosendiff-1])
        map = maps[chosendiff-1]

        if len(content) == 0:
            content = open(map, 'r').read()

        if len(sections) == 0:
            sections = content.split('\n\n')
            i = 0
            for sect in sections:
                lines = sect.split('\n')
                if not lines[0].startswith('[') and len(version) == 0:
                    version = lines[0]

                if lines[0].startswith('[') and lines[0].endswith(']'):
                    sectitles = sectitles + [lines[0][1:-1]]

                i = i + 1

        text = tinfont.render(
            '['+'], ['.join(sectitles)+']', True, col('blue'))
        screen.blit(text, (10, 45))

        text = lilfont.render(version, True, col('black'))
        screen.blit(text, (10, 10))

    if round(ticks/fps, 0) == ticks/fps and round(ticks/fps, 0) > 0:
        truefps = int(ticks//round(ticks/fps, 0))

    if secs > 2.5 and page == 0:
        page = 1

    text = lilfont.render(str(truefps)+" fps", True, col('yellow'))
    screen.blit(text, (10, size[1]-45))

    secs = ticks//fps
    clock.tick(fps)
    ticks = ticks + 1
    pygame.display.flip()

pygame.quit()
shutil.rmtree(tmpdir)
