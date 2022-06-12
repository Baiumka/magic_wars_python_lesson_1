from config import *

class Effect():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def re_draw(self):
        player_name_text = player_font.render(self.name, True, (0, 0, 0))
        window.blit(player_name_text, (self.rect.x, self.rect.y - 65))
