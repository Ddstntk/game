# import random
#
# class fighter():
#     def __init__(self, name, health, stamina, strg, agi, sta, **kwargs):
#         self.health = health
#         self.stamina = stamina
#         # self.vit = vit
#         self.name = name
#         self.strg = strg
#         self.agi = agi
#         self.sta = sta
#
#         self.quickCost = 30
#         self.strongCost = 50
#         self.defendCost = 20
#         self.dodgeCost = 25
#
#     def action(self, action, opponent, fight):
#         pass
#
#     def quickAtc(self, fight):
#         if self.stamina < self.quickCost:
#             print(self.name, "Brakuje pary")
#             return attack(0, 0)
#         else:
#             self.stamina -= self.quickCost
#             atkStr = 7 * self.strg
#             atkSpd = 15 * self.agi
#             print(self.name, " szybko: str - ", atkStr, " spd - ", atkSpd)
#             return attack(atkStr, atkSpd)
#
#     def strongAtc(self, fight):
#         if self.stamina < self.strongCost:
#             print(self.name, "Brakuje pary")
#             return attack(0, 0)
#         else:
#             self.stamina -= self.strongCost
#             atkStr = 10 * self.strg
#             atkSpd = 10 * self.agi
#             print(self.name, " mocno: str - ", atkStr, " spd - ", atkSpd)
#             return attack(atkStr, atkSpd)
#
#     def defend(self, fight):
#         if self.stamina < self.defendCost:
#             print(self.name, "Brakuje pary")
#             return defence(-1, -1)
#         else:
#             self.stamina -= self.defendCost
#             defSpd = 150
#             defEff = 14 * self.sta
#             print(self.name, " obrona: spd - ", defSpd, " spd - ", defEff)
#             return defence(defSpd, defEff)
#
#     def dodge(self, fight):
#         if self.stamina < self.dodgeCost:
#             print(self.name, "Brakuje pary")
#             return defence(-1, -1)
#         else:
#             self.stamina -= self.dodgeCost
#             defSpd = 14 * self.agi
#             defEff = 150
#             print(self.name, " unik: spd - ", defSpd, " spd - ", defEff)
#             return defence(10 * self.agi, 150)
#
#     def rest(self, fight):
#         self.stamina += 75
#         return attack(0, 0)
#
#
# class fighterPlayer(fighter):
#     def __init__(self, name, health, stamina, strg, agi, sta, **kwargs):
#         fighter.__init__(self, name, health, stamina, strg, agi, sta, **kwargs)
#
#     def action(self, action, opponent, fight):
#
#         if action == "quick":
#             return self.quickAtc(fight)
#         elif action == "strong":
#             return self.strongAtc(fight)
#         elif action == "defend":
#             return self.defend(fight)
#         elif action == "dodge":
#             return self.dodge(fight)
#         elif action == "rest":
#             return self.rest(fight)
#
#
# class AIfighter(fighter):
#     def __init__(self, name, health, stamina, strg, agi, sta, **kwargs):
#         fighter.__init__(self, name, health, stamina, strg, agi, sta, **kwargs)
#         # self.personality = personality
#
#     def action(self, opponent, fight):
#         qatck = 1
#         satck = 1
#         ddg = 1
#         df = 1
#         rst = 1
#
#         if self.stamina < 20:
#             rst += 100
#         else:
#             if self.health/opponent.health > 1.75:
#                 satck += 2
#                 if self.stamina < 50:
#                     rst += 5
#                 else:
#                     qatck += 2
#             if opponent.health < 30:
#                 satck += 2
#                 qatck += 2
#             if opponent.stamina < 30:
#                 satck += 6
#                 qatck += 6
#             else:
#                 df += 1
#                 ddg += 1
#             if self.agi >= self.strg:
#                 qatck += self.agi - self.strg
#             else:
#                 satck += self.strg - self.agi
#             if self.health < 20:                #mała wartość, możliwa do zabrania jednorazowo
#                 satck += 2
#                 qatck += 2
#             if self.health > opponent.health:
#                 df += 1
#             else:
#                 qatck += 2
#                 satck += 2
#             # if self.agi > self.vit:
#             #     ddg += 2
#             # else:
#             #     df += 1
#
#         qatck *= random.randrange(1, 3)
#         satck *= random.randrange(1, 3)
#         df *= random.randrange(1, 3)
#         ddg *= random.randrange(1, 3)
#
#         data = [["quatck", qatck], ["satck", satck], ["df", df], ["ddg", ddg], ["rst", rst]]
#
#         data_sorted = sorted(data, key=lambda p: p[1], reverse=True)
#         actionNum = 0
#         while actionNum < data_sorted.__len__():
#             action = data_sorted[actionNum][0]
#             if action == "satck" and self.stamina >= self.strongCost:
#                 return self.strongAtc(opponent, fight)
#                 break
#             elif action == "qatck" and self.stamina >= self.quickCost:
#                 return self.quickAtc(opponent, fight)
#                 break
#             elif action == "df" and self.stamina >= self.defendCost:
#                 return self.defend(opponent, fight)
#                 break
#             elif action == "ddg" and self.stamina >= self.dodgeCost:
#                 return self.dodge(opponent, fight)
#                 break
#             elif action == "rest":
#                 return self.rest()
#                 break
#             else:
#                 actionNum += 1
#
#
#
# class attack():
#     def __init__(self, power, speed):
#         self.power = power #1-100
#         self.speed = speed  #1-100
#
#
# class defence():
#     def __init__(self, speed, efficacy):
#         self.speed = speed # 1-100
#         self.efficacy = efficacy # 1-100
#
#
#
# class fight():
#     def __init__(self, fighterA, fighterB, actionList=[]):
#         self.FighterA = fighterA
#         self.FighterB = fighterB
#         self.actionList = []
#
#     def addAction(self, action):
#         self.actionList.append(action)
#
#         if len(self.actionList) > 1:
#             self.killAndWin()
#
#     def killAndWin(self):
#         actionA = self.actionList[0]
#         actionB = self.actionList[1]
#         print("Zaczynajo walczyć!")
#
#         while self.FighterB.health > 0 and self.FighterA.health > 0:
#             print("Walczo!")
#             if isinstance(actionA, attack):
#
#                 if isinstance(actionB, attack):                                                           # obaj atakują
#                     self.FighterA.health -= int(actionA.power * (random.randrange(7, 13))/10)
#                     self.FighterB.health -= int(actionB.power * (random.randrange(7, 13)/10))
#                     print(self.FighterA.health, self.FighterB.health)
#
#                 elif isinstance(actionB, defence):                                                        # A atak B obrona
#                     speedDiff = actionA.speed - actionB.speed
#                     if speedDiff < -50:
#                         chanceFactor = (speedDiff + 100)/2
#                         chanceFactor += int(chanceFactor * (random.randrange(8, 18)/10))
#                         if chanceFactor > -45:
#                             self.FighterA.health -= int(actionA.power * (random.randrange(7, 13)/10) * 100/actionB.efficacy)
#
#             elif isinstance(actionA, defence):                                                           # A obrona B atak
#                 if isinstance(actionB, attack):
#                     speedDiff = actionB.speed - actionA.speed
#                     if speedDiff < -50:
#                         chanceFactor = (speedDiff + 100) / 2
#                         chanceFactor += int(chanceFactor * (random.randrange(8, 18)/10))
#                         if chanceFactor > -45:
#                             self.FighterB.health -= int(actionB.power * (random.randrange(7, 13)/10) * 100 / actionA.efficacy)
#
#                 elif isinstance(actionB, defence):                                                       # Obaj się bronią
#                     pass
#
#                 self.actionList = []
#                 yield
#
#
#         if self.FighterB.health > self.FighterA.health:
#             print("wojownik wygrał")
#         else:
#             print("gracz wygrał")
