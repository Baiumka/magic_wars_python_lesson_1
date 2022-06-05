from config import *
from Projectile import *
from magic_creator import *

class Player():
    def __init__(self, model, maxHP, x, y, name):
        self.maxHP = maxHP
        self.hp = maxHP-250
        self.name = name

        self.model = transform.scale(image.load(model), (PLAYER_SIZE_X, PLAYER_SIZE_Y))
        self.rect = self.model.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.projectiles = []
        self.spell_list = []
    def take_damage(self, hp):
        self.hp -= hp

    def attack(self, target):
        i = 0
        for skill in self.spell_list:
            i += 1
            new_projectile = Projectile(skill, self, target, i * 5)
            self.projectiles.append(new_projectile)
        self.spell_list.clear()

    def add_spell(self, skill):
        if len(self.spell_list) < 2:
            self.spell_list.append(skill)

            new_skill = check_combination(self.spell_list)
            if new_skill != None:
                self.spell_list.append(new_skill)

    def show(self):
        window.blit(self.model, (self.rect.x, self.rect.y))

        draw.rect(window, (0, 0, 0), (self.rect.x-2, self.rect.y-50-2, (self.maxHP / 10)+4, 10+4))
        draw.rect(window, (100, 0, 0), (self.rect.x, self.rect.y-50, self.maxHP / 10, 10))
        draw.rect(window, (255, 0, 0), (self.rect.x, self.rect.y-50, self.hp / 10, 10))

        player_name_text = player_font.render(self.name, True, (0, 0, 0))
        window.blit(player_name_text, (self.rect.x, self.rect.y - 65))
        for proj in self.projectiles:
            proj.show()

        i = 0
        for spell in self.spell_list:
            window.blit(spell.img,  (self.rect.x+i*25, self.rect.y-10))
            i+=1

