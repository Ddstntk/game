#! /usr/bin/env python3

from .fightClass import *
import random

class roomC():
    def __init__(self, host):
        # self.id = id
        self.host = host
        # self.name = name
        # self.fighters = []
        # self.fighters[0] = self.host
    def setFirst(self, fighter):
        self.firstFighter = fighter

    def setSecond(self, fighter):
        self.secondFighter = fighter

    def setFight(self):
        self.fight = fight(self.firstFighter, self.secondFighter).__dict__