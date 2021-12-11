import pygame
import sys
from day11 import make_step

pygame.init()
display_screen = pygame.display.set_mode((800,1000))
pygame.display.set_caption("AoC day 11")
pygame.display.update()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
NEW_STEP = pygame.USEREVENT+1
pygame.time.set_timer(NEW_STEP, 50)

input_f = open('input.txt', mode='r')
octopuses = [[int(c) for c in line] for line in input_f.read().splitlines()]

clock = pygame.time.Clock()
octopuses_rendered = False
step = 0
while 1:
    if not octopuses_rendered:
        display_screen.fill(pygame.Color("black"))
        for y in range(len(octopuses)):
            for x in range(len(octopuses)):
                color = (255, 255, 255) if octopuses[y][x] == 0 else (255 / 9 * octopuses[y][x], 0, 0)
                pygame.draw.rect(display_screen, color, (x * 80 + 10, y * 80 + 10, 60, 60))
        textsurface = myfont.render(str(step), False, (255, 255, 255))
        display_screen.blit(textsurface, (400, 900))
        pygame.display.update()
        octopuses_rendered = True
    for event in pygame.event.get():
        if event.type == NEW_STEP:
            if all([o == [0] * len(octopuses) for o in octopuses]):
                continue
            step += 1
            octopuses = make_step(octopuses)
            octopuses_rendered = False
        elif event.type == pygame.QUIT:
            sys.exit()

    clock.tick(60)
