from config import *
from Player import *
from Button import *
from magic_creator import *


background = transform.scale((image.load('bg.jpg')), screen_size)
clock = time.Clock()


player1 = Player('player.png', 1000, 100, 300, "Player 1")
player2 = Player('player.png', 1000, 600, 300, "Player 2")

button_attack = Button(100, 100, "cloud.png", "Атаковать")


attack_pause = 0
isWork = True
while isWork:

    display.update()
    for e in event.get():
        if e.type == QUIT:
            isWork = False
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                x, y = e.pos
                if button_attack.rect.collidepoint(x, y):
                    player1.attack(player2)
                for skill in base_skill_list:
                    if skill.rect.collidepoint(x, y):
                        player1.add_spell(skill)

    #attack_pause += 1

    #if attack_pause >= FPS/1:
    #    attack_pause = 0
    #    if player1.hp > 0 and player2.hp > 0:
    #       player1.attack(player2)
    #        player2.attack(player1)


    window.blit(background, (0, 0))
    player1.show()
    player2.show()
    button_attack.show()
    for skill in base_skill_list:
        skill.show()
    clock.tick(FPS)

