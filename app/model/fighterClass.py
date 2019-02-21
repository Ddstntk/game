#! /usr/bin/env python3

from .fightClass import *
class fighter():
    def __init__(self, name, health, stamina, strg, agi, sta, **kwargs):
        self.health = health
        self.stamina = stamina
        # self.vit = vit
        self.name = name
        self.strg = strg
        self.agi = agi
        self.sta = sta

        self.quickCost = 30
        self.strongCost = 50
        self.defendCost = 20
        self.dodgeCost = 25

        self.actionMemory = ""

    def action(self, action, opponent, fight):
        pass

    def quickAtc(self, fight):
        if self.stamina < self.quickCost:
            # print(self.name, "Brakuje pary")
            return attack(0, 0)
        else:
            self.stamina -= self.quickCost
            atkStr = 7 * self.strg
            atkSpd = 15 * self.agi
            # print(self.name, " szybko: str - ", atkStr, " spd - ", atkSpd)
            self.actionMemory = "quick"
            return attack(atkStr, atkSpd)

    def strongAtc(self, fight):
        if self.stamina < self.strongCost:
            # print(self.name, "Brakuje pary")
            return attack(0, 0)
        else:
            self.stamina -= self.strongCost
            atkStr = 10 * self.strg
            atkSpd = 10 * self.agi
            # print(self.name, " mocno: str - ", atkStr, " spd - ", atkSpd)
            self.actionMemory = "strong"
            return attack(atkStr, atkSpd)

    def defend(self, fight):
        if self.stamina < self.defendCost:
            # print(self.name, "Brakuje pary")
            return defence(-1, -1)
        else:
            self.stamina -= self.defendCost
            defSpd = 0
            defEff = 14 * self.sta
            # print(self.name, " obrona: spd - ", defSpd, " spd - ", defEff)
            self.actionMemory = "defend"
            return defence(defSpd, defEff)

    def dodge(self, fight):
        if self.stamina < self.dodgeCost:
            # print(self.name, "Brakuje pary")
            return defence(-1, -1)
        else:
            self.stamina -= self.dodgeCost
            defSpd = 14 * self.agi
            defEff = 150
            # print(self.name, " unik: spd - ", defSpd, " spd - ", defEff)
            self.actionMemory = "dodge"
            return defence(10 * self.agi, 150)

    def rst(self, fight):
        # self.stamina += 75
        self.actionMemory = "rest"
        return rest()
