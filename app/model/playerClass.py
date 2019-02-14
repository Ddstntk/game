#! /usr/bin/env python3

from .fighterClass import *


class fighterPlayer(fighter):
    def __init__(self, name, health, stamina, strg, agi, sta, **kwargs):
        fighter.__init__(self, name, health, stamina, strg, agi, sta, **kwargs)

    def action(self, action, opponent, fight):

        if action == "quick":
            return self.quickAtc(fight)
        elif action == "strong":
            return self.strongAtc(fight)
        elif action == "defend":
            return self.defend(fight)
        elif action == "dodge":
            return self.dodge(fight)
        elif action == "rst":
            return self.rst(fight)
