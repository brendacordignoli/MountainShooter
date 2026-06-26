#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.entity import entity1


class Player(entity1):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.Attribute1 = None

    def move(self, ):
        pass
