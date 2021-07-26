import pygame
import subprocess


class VideoSprite(pygame.sprite.Sprite):
    FFMPEG_BIN = "/usr/local/bin/ffmpeg"   # Full path to ffmpeg executable

    def __init__(self, rect, filename, FPS=30):  # <-----   !--- frames mismatched ---!
        pygame.sprite.Sprite.__init__(self)
        command = [self.FFMPEG_BIN,
                   '-loglevel', 'quiet',
                   '-i', filename,
                   '-f', 'image2pipe',
                   '-s', '%dx%d' % (rect.width, rect.height),
                   '-pix_fmt', 'rgb24',
                   '-vcodec', 'rawvideo', '-']
        self.bytes_per_frame = rect.width * rect.height * 3
        self.proc = subprocess.Popen(
            command, stdout=subprocess.PIPE, bufsize=self.bytes_per_frame*3)
        self.image = pygame.Surface(
            (rect.width, rect.height), pygame.HWSURFACE)
        self.rect = self.image.get_rect()
        self.rect.x = rect.x
        self.rect.y = rect.y
        # Used to maintain frame-rate
        self.last_at = 0           # time frame starts to show
        self.frame_delay = 1000 / FPS  # milliseconds duration to show frame
        self.video_stop = False

    def update(self):
        if (not self.video_stop):
            time_now = pygame.time.get_ticks()
            if (time_now > self.last_at + self.frame_delay):   # has the frame shown for long enough
                self.last_at = time_now
                try:
                    raw_image = self.proc.stdout.read(self.bytes_per_frame)
                    self.image = pygame.image.frombuffer(
                        raw_image, (self.rect.width, self.rect.height), 'RGB')
                    # self.proc.stdout.flush()  - doesn't seem to be necessary
                except:
                    # error getting data, end of file?  Black Screen it
                    self.image = pygame.Surface(
                        (self.rect.width, self.rect.height), pygame.HWSURFACE)
                    self.image.fill((0, 0, 0))
                    self.video_stop = True
 