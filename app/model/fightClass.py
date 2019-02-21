#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import random


class attack():
    def __init__(self, power, speed):
        self.power = power #1-100
        self.speed = speed  #1-100


class defence():
    def __init__(self, speed, efficacy):
        self.speed = speed # 1-100
        self.efficacy = efficacy # 1-100


class rest():
    def __init__(self):
        self.rest = 1


class fight():
    def __init__(self, fighterA, fighterB, actionList=[]):
        self.FighterA = fighterA
        self.FighterB = fighterB
        self.actionList = []

    def addAction(self, action):
        self.actionList.append(action)

        if len(self.actionList) > 1:
            # print("wywoluje kill and win")
            # self.actionListInfo = self.actionList
            self.killAndWin()

    def dupadupa(self):
        print(self.actionList)

    def killAndWin(self):
        # print("Zaczynajo walczyc!")

        actionA = self.actionList[0]
        actionB = self.actionList[1]
        print(self.FighterA, self.actionList[0])
        print(self.FighterB, self.actionList[1])

        # print("Walczo!")

        if isinstance(actionA, attack):
            # print("wykrylem atak")
            if isinstance(actionB, attack):                                                           # obaj atakują
                self.FighterA.health -= int(actionA.power * (random.randrange(7, 13))/10)%150
                self.FighterB.health -= int(actionB.power * (random.randrange(7, 13)/10))%150
                print(self.FighterA.health, self.FighterB.health)

            elif isinstance(actionB, defence):                                                        # A atak B obrona
                speedDiff = abs(actionA.speed) - abs(actionB.speed)
                if speedDiff > -35:
                    chanceFactor = (speedDiff + 150)/2
                    chanceFactor += int(chanceFactor * (random.randrange(8, 18)/10))
                    if chanceFactor > 130:
                        self.FighterB.health -= int(actionA.power * (random.randrange(7, 13)/10) * 100 / ((actionB.efficacy*1.1) + 1))%150

            elif isinstance(actionB, rest):                                                        # A atak B obrona
                if self.FighterB.stamina < 550:
                    self.FighterB.stamina += 75
                self.FighterB.health -= int(actionA.power * (random.randrange(7, 13)/10))%150

        elif isinstance(actionA, defence):                                                           # A obrona B atak
            # print("wykrylem obronę")

            if isinstance(actionB, attack):
                speedDiff = abs(actionB.speed) - abs(actionA.speed)
                print(speedDiff)
                if speedDiff > -35:
                    chanceFactor = (speedDiff + 150) / 2
                    chanceFactor += int(chanceFactor * (random.randrange(8, 18)/10))
                    print(chanceFactor)
                    if chanceFactor > 130:
                        self.FighterA.health -= int(actionB.power * (random.randrange(7, 13)/10) * 100 / ((actionA.efficacy*1.1) + 1))%150

            elif isinstance(actionB, defence):                                                       # Obaj się bronią
                pass

            elif isinstance(actionB, rest):                                                        # A atak B obrona
                if self.FighterB.stamina < 550:
                    self.FighterB.stamina += 75

        elif isinstance(actionA, rest):
            # print("wykrylem odpoczynek")
            if isinstance(actionB, attack):                                                           # obaj atakują
                self.FighterA.health -= int(actionB.power * (random.randrange(7, 13))/10)%150
                if self.FighterA.stamina < 550:
                    self.FighterA.stamina += 75
                print(self.FighterA.health, self.FighterB.health)

            elif isinstance(actionB, defence):                                                        # A atak B obrona
                if self.FighterA.stamina < 550:
                    self.FighterA.stamina += 75

            elif isinstance(actionB, rest):                                                        # A atak B obrona
                if self.FighterA.stamina < 550:
                    self.FighterA.stamina += 75
                if self.FighterB.stamina < 550:
                    self.FighterB.stamina += 75

        self.actionList = []
