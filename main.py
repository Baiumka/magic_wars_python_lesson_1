from config import *
from Player import *
from Button import *
from Bot import *
from magic_creator import *


background = transform.scale((image.load('bg.jpg')), screen_size)
clock = time.Clock()


player1 = Player('1.png', 1000, 100, 300, "Player 1", True)
player2 = Player('1.png', 1000, 600, 300, "Player 2", False)
bot = Bot(player2, player1)
button_attack = Button(100, 100, "cloud.png", "Атаковать")

bot_thinking = 0
is_your_turn = True
def wake_up_bot():
    global is_your_turn
    global bot_thinking
    is_your_turn = False
    bot_thinking = 120

def bot_make_turn():
    global is_your_turn
    bot.next_turn()
    is_your_turn = True


isWork = True
while isWork:
    display.update()
    for e in event.get():
        if e.type == QUIT:
            isWork = False
        if is_your_turn == True:
            if e.type == MOUSEBUTTONDOWN:
                if e.button == 1:
                    x, y = e.pos
                    if button_attack.rect.collidepoint(x, y):
                        player1.attack(player2)
                        wake_up_bot()
                    for skill in base_skill_list:
                        if skill.rect.collidepoint(x, y):
                            player1.add_spell(skill)
                            wake_up_bot()

    #attack_pause += 1

    #if attack_pause >= FPS/1:
    #    attack_pause = 0
    #    if player1.hp > 0 and player2.hp > 0:
    #       player1.attack(player2)
    #        player2.attack(player1)

    if bot_thinking > 0:
        bot_thinking -= 1
        if bot_thinking <= 0:
            bot_make_turn()

    window.blit(background, (0, 0))
    player1.show()
    player2.show()
    button_attack.show()
    for skill in base_skill_list:
        skill.show()
    clock.tick(FPS)

