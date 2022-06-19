from config import *
from Projectile import *
from magic_creator import *

class Player():
    def __init__(self, model, maxHP, x, y, name, flip):
        self.maxHP = maxHP
        self.hp = maxHP-250
        self.name = name
        a = transform.scale(image.load(model), (PLAYER_SIZE_X, PLAYER_SIZE_Y))
        self.model = transform.flip(a, flip, False)
        self.rect = self.model.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.projectiles = []
        self.spell_list = []
        self.effects = {}


        a1 = transform.scale(image.load("1.png"), (PLAYER_SIZE_X, PLAYER_SIZE_Y))
        a1 = transform.flip(a1, flip, False)
        a2 = transform.scale(image.load("2.png"), (PLAYER_SIZE_X, PLAYER_SIZE_Y))
        a2 = transform.flip(a2, flip, False)
        a3 = transform.scale(image.load("3.png"), (PLAYER_SIZE_X, PLAYER_SIZE_Y))
        a3 = transform.flip(a3, flip, False)
        a4 = transform.scale(image.load("4.png"), (PLAYER_SIZE_X, PLAYER_SIZE_Y))
        a4 = transform.flip(a4, flip, False)
        self.animWalk = [a1, a2, a3, a4]

        a1 = transform.scale(image.load("1.png"), (PLAYER_SIZE_X, PLAYER_SIZE_Y))
        a1 = transform.flip(a1, flip, False)
        a2 = transform.scale(image.load("2.png"), (PLAYER_SIZE_X, PLAYER_SIZE_Y))
        a2 = transform.flip(a2, flip, False)
        a3 = transform.scale(image.load("3.png"), (PLAYER_SIZE_X, PLAYER_SIZE_Y))
        a3 = transform.flip(a3, flip, False)
        a4 = transform.scale(image.load("4.png"), (PLAYER_SIZE_X, PLAYER_SIZE_Y))
        a4 = transform.flip(a4, flip, False)
        self.animAttack = [a1, a2, a3, a4]

        self.currentF = 0


        self.activeAnim = self.animWalk



    def TakeEffect(self, effect, turns):
        if effect in self.effects:
            self.effects[effect] += turns
        else:
            self.effects[effect] = turns


    def take_damage(self, damage):

        if self.check_effect(armour_effect) == True:
            damage /= 2

        self.hp -= damage

    def attack(self, target):
        i = 0
        for skill in self.spell_list:
            i += 1
            new_projectile = Projectile(skill, self, target, i * 5)
            self.projectiles.append(new_projectile)
        self.activeAnim = self.animAttack
        self.spell_list.clear()
        self.end_turn()

    def add_spell(self, skill):
        if len(self.spell_list) < 2:
            self.spell_list.append(skill)

            new_skill = check_combination(self.spell_list)
            if new_skill != None:
                self.spell_list.append(new_skill)
        self.end_turn()

    def check_effect(self, effect):
        if effect in self.effects:
            if self.effects[effect] > 0:
                return True
        return False

    def end_turn(self):
        if self.check_effect(fire_effect):
            self.hp -= 250

        for effect in self.effects:
            if self.effects[effect] > 0:
                self.effects[effect] -= 1

    def show(self):
        window.blit(self.activeAnim[self.currentF//10], (self.rect.x, self.rect.y))
        self.currentF += 1
        if self.currentF > (len(self.activeAnim)-1)*10:
            self.currentAnim = 0

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

        buff_count = 0
        for k in self.effects:
            if self.effects[k] > 0:
                buff_text = player_font.render(k.name + ": " + str(self.effects[k]) + " ходов.", True, (0, 0, 0))
                window.blit(buff_text, (self.rect.x - 100, self.rect.y - 65 + (buff_count * 15)))
                buff_count += 1

