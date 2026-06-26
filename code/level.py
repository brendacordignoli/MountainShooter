#!/usr/bin/python
# -*- coding: utf-8 -*-
from xml.dom.minidom import Entity

import pygame

from code import entity
from code.entityFactory import entityFactory


class level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[entity] = []
        self.entity_list.extend(entityFactory.get_entity('Level1Bg'))


    def run(self):

        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
        pass

