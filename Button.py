from config import *

class Button():
    def __init__(self, x, y, img, name):
        self.img = transform.scale(image.load(img), (200, 30))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name
    def show(self):
        window.blit(self.img, (self.rect.x, self.rect.y))
        button_text = button_font.render(self.name, True, (0, 0, 0))
        window.blit(button_text, (self.rect.x + 5, self.rect.y + 5))
