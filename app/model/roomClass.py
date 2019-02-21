#! /usr/bin/env python3

from .fightClass import *
import random

class room():
    def __init__(self, id, name, host):
        self.id = id
        self.host = host
        self.name = name
        self.fighters[0] = self.host

