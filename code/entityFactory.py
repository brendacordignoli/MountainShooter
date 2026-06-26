#!/usr/bin/python
# -*
from pygame.examples.grid import WINDOW_WIDTH


def background(name, position):
    pass


class entityFactory:

    @staticmethod

    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(background(f'Level1Bg{i}', position (0.0)))
                    list_bg.append(background(f'Level1Bg{i}', position (WINDOW_WIDTH,0)))
                return list_bg
