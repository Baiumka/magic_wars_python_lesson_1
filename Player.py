from config import *
from Projectile import *

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
    def take_damage(self, hp):
        self.hp -= hp

    def attack(self, target):
        new_projectile = Projectile("Fire.png", self, target)
        self.projectiles.append(new_projectile)

    def show(self):
        window.blit(self.model, (self.rect.x, self.rect.y))

        draw.rect(window, (0, 0, 0), (self.rect.x-2, self.rect.y-50-2, (self.maxHP / 10)+4, 10+4))
        draw.rect(window, (100, 0, 0), (self.rect.x, self.rect.y-50, self.maxHP / 10, 10))
        draw.rect(window, (255, 0, 0), (self.rect.x, self.rect.y-50, self.hp / 10, 10))

        player_name_text = player_font.render(self.name, True, (0, 0, 0))
        window.blit(player_name_text, (self.rect.x, self.rect.y - 65))
        for proj in self.projectiles:
            proj.show()

