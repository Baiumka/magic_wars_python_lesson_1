from pygame import *
font.init()
window = display.set_mode((800, 600))
screen_size = window.get_rect().size

PLAYER_SIZE_X = 200
PLAYER_SIZE_Y = 200


player_font = font.Font(None, 15)


FPS = 60