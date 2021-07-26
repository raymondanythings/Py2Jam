import pygame


# --------  Make Sprite object

class EffectSprite(pygame.sprite.Sprite):
    def __init__(self, pictures_path, position, size):
        super(EffectSprite, self).__init__()
        size = size
        images = [pygame.image.load(picture) for picture in pictures_path]
        self.rect = pygame.Rect(position, size)
        self.images = [pygame.transform.scale(image, size) for image in images]
        #self.images = [image.convert_alpha() for image in load_images]
        self.index = 0
        self.image = images[self.index]

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]


# Frame height - > 480 -> top

class MakeNote:
    def __init__(self, cwd, x, y):
        self.po_x = x
        self.po_y = y
        self.speed = 0
        self.image = pygame.image.load(cwd).convert_alpha()
        self.sx, self.sy = self.image.get_size()
        # self.size = self.get_rect().size

    def show(self, screen):
        screen.blit(self.image, (self.po_x, self.po_y))

    def draw_note(self, screen, spd):
        screen.blit(self.image, (self.po_x, self.po_y))
        self.po_y += spd
        if self.po_y >= 480:
            self.po_y = 0
