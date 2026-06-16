#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.entity import Entity1


class Player(Entity1):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.Attribute1 = None

    def move(self, ):
        pass
