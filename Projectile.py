from config import *

class Projectile():
    def __init__(self, spell, owner, target, speed):
        self.spell = spell

        self.model = transform.scale(spell.img, (50, 50))

        self.rect = self.model.get_rect()
        self.rect.x = owner.rect.x
        self.rect.y = owner.rect.y

        self.owner = owner
        self.target = target
        self.speed = speed


    def move(self):
        if self.owner.rect.x > self.target.rect.x:
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        if abs(self.rect.x - self.target.rect.x) < 10:
            #self.target.take_damage(100)
            self.spell.action(self.owner, self.target)
            self.owner.projectiles.remove(self)



    def show(self):
        self.move()
        window.blit(self.model, (self.rect.x, self.rect.y))

