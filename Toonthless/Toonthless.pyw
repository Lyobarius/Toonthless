import threading
import pygame
from pygame import *

def InitMP3():
    pygame.mixer.init()
    pygame.mixer_music.load("ALANWALKER_DARKSIDE.mp3")
    pygame.mixer_music.play(-1)
    x = threading.Event()
    x.wait();
if __name__ == "__main__":
    InitMP3()
