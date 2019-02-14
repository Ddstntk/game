#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from .fightClass import *
from .fighterClass import *

class AIfighter(fighter):
    def __init__(self, name, health, stamina, strg, agi, sta, **kwargs):
        fighter.__init__(self, name, health, stamina, strg, agi, sta, **kwargs)
        # self.personality = personality

    def action(self, opponent, fight):
        qatck = 1
        satck = 1
        ddg = 1
        df = 1
        rst = 1

        if self.stamina < 20:
            rst += 100
        else:
            if self.health/opponent.health > 1.75:
                satck += 2
                if self.stamina < 50:
                    rst += 5
                else:
                    qatck += 2
            if opponent.health < 30:
                satck += 2
                qatck += 2
            if opponent.stamina < 30:
                satck += 6
                qatck += 6
            else:
                df += 1
                ddg += 1
            if self.agi >= self.strg:
                qatck += self.agi - self.strg
            else:
                satck += self.strg - self.agi
            if self.health < 20:                #mała wartość, możliwa do zabrania jednorazowo
                satck += 2
                qatck += 2
            if self.health > opponent.health:
                df += 1
            else:
                qatck += 2
                satck += 2
            # if self.agi > self.vit:
            #     ddg += 2
            # else:
            #     df += 1

        qatck *= random.randrange(1, 3)
        satck *= random.randrange(1, 3)
        df *= random.randrange(1, 3)
        ddg *= random.randrange(1, 3)

        data = [["quatck", qatck], ["satck", satck], ["df", df], ["ddg", ddg], ["rst", rst]]

        data_sorted = sorted(data, key=lambda p: p[1], reverse=True)
        actionNum = 0
        while actionNum < data_sorted.__len__():
            action = data_sorted[actionNum][0]
            if action == "satck" and self.stamina >= self.strongCost:
                return self.strongAtc(fight)
                break
            elif action == "qatck" and self.stamina >= self.quickCost:
                return self.quickAtc(fight)
                break
            elif action == "df" and self.stamina >= self.defendCost:
                return self.defend(fight)
                break
            elif action == "ddg" and self.stamina >= self.dodgeCost:
                return self.dodge(fight)
                break
            elif action == "rst":
                return self.rst(fight)
                break
            else:
                actionNum += 1

