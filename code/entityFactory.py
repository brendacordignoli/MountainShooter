#!/usr/bin/python
# -*
import random

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.background import background
from code.Enemy import Enemy
from code.Player import Player


class entityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):

        match entity_name:

            case 'Level1Bg':
                list_bg = []

                for i in range(7):
                    # fundo inicial
                    list_bg.append(
                        background(f'Level1Bg{i}', (0, 0))
                    )

                    # fundo deslocado para a direita
                    list_bg.append(
                        background(f'Level1Bg{i}', (WIN_WIDTH, 0))
                    )

                return list_bg

            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))

            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
