#!/usr/bin/python
# -*
from pygame.examples.grid import WINDOW_WIDTH

from code import background
from code.background import Background


class entityFactory:

    @staticmethod

    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'level1Bg':
                list_bg = []
                for i in range(2):
                    list_bg.append(background(f'level1Bg{i}', position(0.0)))
                    list_bg.append(background(f'level1Bg{i}', position(WINDOW_WIDTH,0)))
                return list_bg
