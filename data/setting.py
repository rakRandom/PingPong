try:
    import pygame

    from random import randint
    from time import time
    from sys import exit
except: raise ImportError("Error 1: cannot import modules")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
SCREEN_NAME = "Ping Pong"
SCREEN_ICON = "image\ping.ico"
FRAMES_PER_SECOND = -1

GAME_SPEED = 1
PLAYER_SPEED = 250
BALL_SPEED = 500
NPC_SPEED = 250

FALLING_PIPE_SOUND = False
