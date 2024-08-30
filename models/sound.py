from playsound import playsound
import pygame

SOUNDPATH = r"models\you-are-an-idiot.mp3"

class Sound:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load(SOUNDPATH)
        pygame.mixer.music.play(-1)  # -1は無限ループを意味します
