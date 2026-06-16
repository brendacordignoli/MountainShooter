#!/usr/bin/python
import abc

import pygame


class entity(abc.ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png')
        self.rect = self.surf.get_rect(left=position[0], top=[1])
        self.speed = 0

    @abc.abstractmethod
    def move(self, ):
        self.rect.centerx -=1
        pass
