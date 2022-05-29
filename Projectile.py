from config import *

class Projectile():
    def __init__(self, img, owner, target):
        self.model = transform.scale(image.load(img), (50, 50))
        self.rect = self.model.get_rect()
        self.rect.x = owner.rect.x
        self.rect.y = owner.rect.y

        self.owner = owner
        self.target = target
        self.speed = 5


    def move(self):
        if self.owner.rect.x > self.target.rect.x:
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        if abs(self.rect.x - self.target.rect.x) < 10:
            self.target.take_damage(100)
            self.owner.projectiles.remove(self)



    def show(self):
        self.move()
        window.blit(self.model, (self.rect.x, self.rect.y))

