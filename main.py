import pygame
import os
import random
import time

from card import Card
# Card(fname, x1, y1, x2, y2) for initialize
# Card.set_target(tx1, ty1, tx2, ty2) to set a new position
# Card.update() to update card position
# Card.render(screen) to render card on screen

screen_width = 1200
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))

from util import parsing_word_list

words_file = "./data/word_list_with_img_url_new.txt"
word2data = parsing_word_list(words_file)


from util import render_image

render_image("冰箱")
render_image("黑夜")
render_image("不存在")
