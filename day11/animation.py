import pygame
import sys

from pygame import color
from pygame.math import Vector3

from day11 import make_step


class Game(object):

    NEXT_STEP_TIME_MS = 100
    FPS = 60
    TRANSFORM_SPEED = 0.4
    TRANSFORM_NEXT_TIME_MS = 50

    NEW_STEP_EVENT = pygame.USEREVENT + 1
    TRANSFORM_EVENT = pygame.USEREVENT + 2

    def __init__(self):
        pygame.init()
        self.display_screen = pygame.display.set_mode((800, 1000))
        pygame.display.set_caption("AoC day 11")
        pygame.display.update()
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        pygame.time.set_timer(self.NEW_STEP_EVENT, self.NEXT_STEP_TIME_MS)
        pygame.time.set_timer(self.TRANSFORM_EVENT, self.TRANSFORM_NEXT_TIME_MS)
        self.clock = pygame.time.Clock()
        self.step_rendered = False
        input_f = open('input.txt', mode='r')
        self.octopuses = [[int(c) for c in line] for line in input_f.read().splitlines()]
        self.step = 0
        self.target_graphic = self.convert_octopuses_to_graphic()
        self.current_graphic = [[Vector3()] * len(self.octopuses) for row in self.octopuses]

    def start(self):
        while 1:
            if not self.step_rendered:
                self.display_screen.fill(pygame.Color("black"))
                text_surface = self.font.render(str(self.step), False, (255, 255, 255))
                self.display_screen.blit(text_surface, (400, 900))
                self.step_rendered = True
                self.render_octopuses()
                pygame.display.update()
            self.event_loop()
            self.clock.tick(self.FPS)

    def render_octopuses(self):
        for y in range(len(self.octopuses)):
            for x in range(len(self.octopuses)):
                pygame.draw.rect(self.display_screen, color.Color(self.current_graphic[y][x]),
                                 (x * 80 + 10, y * 80 + 10, 60, 60))
        pygame.display.update()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == self.NEW_STEP_EVENT:
                if self.is_all_octopuses_flashes():
                    continue
                self.step += 1
                self.octopuses = make_step(self.octopuses)
                self.target_graphic = self.convert_octopuses_to_graphic()
                self.step_rendered = False
            elif event.type == self.TRANSFORM_EVENT:
                changed = False
                for y in range(len(self.octopuses)):
                    for x in range(len(self.octopuses)):
                        current_c = self.current_graphic[y][x]
                        target_c = self.target_graphic[y][x]
                        if (current_c - target_c).length() > 2:
                            changed = True
                            self.current_graphic[y][x] = current_c + (target_c - current_c) * self.TRANSFORM_SPEED
                if changed:
                    self.render_octopuses()
            elif event.type == pygame.QUIT:
                sys.exit()

    def is_all_octopuses_flashes(self):
        return all([o == [0] * len(self.octopuses) for o in self.octopuses])

    def convert_octopuses_to_graphic(self):
        result = [[Vector3()] * len(self.octopuses) for row in self.octopuses]
        for y in range(len(self.octopuses)):
            for x in range(len(self.octopuses)):
                c = Vector3(255, 255, 255) if self.octopuses[y][x] == 0 else Vector3(int(255 / 9 * self.octopuses[y][x]), 0, 0)
                result[y][x] = c
        return result
