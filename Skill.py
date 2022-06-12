from config import *
from buff_creator import *

class Skill():
    def __init__(self, power, icon, name, x, y):
        self.power = power
        self.name = name

        self.img = transform.scale(image.load(icon), (50, 50))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
    def show(self):
        window.blit(self.img, (self.rect.x, self.rect.y))
    def action(self, owner, target):
        print("Использем " + self.name)


class FireSkill(Skill):
    def action(self, owner, target):
        target.TakeEffect(fire_effect, 3)

class WaterSkill(Skill):
    def action(self, owner, target):
        owner.take_damage(-100)

class WindSkill(Skill):
    def action(self, owner, target):
        owner.take_damage(-100)

class EarthSkill(Skill):
    def action(self, owner, target):
        owner.TakeEffect(armour_effect, 10)
        #Добавляет броню


class SteamSkill(Skill):
    def action(self, owner, target):
        owner.take_damage(-100)
        #Увеличивает уклонения
