from magic_creator import *
from random import *

class Bot:
    def __init__(self, bot, target):
        self.bot = bot
        self.target = target

    def next_turn(self):
        if (len(self.bot.spell_list) < 2):

            if self.bot.hp >= 300:
                use_skill = base_skill_list[randint(0, len(base_skill_list) - 1)]
            else:
                use_skill = water_skill

            self.bot.add_spell(use_skill)
        else:
            self.bot.attack(self.target)