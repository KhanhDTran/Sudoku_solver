import pygame
from pygame.key import get_pressed

Yellow = (252, 247, 204)
pygame.font.init()

clicked = False
counter = 0

class Button():

    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.text = text
        self.width = width
        self.height = height
        self.text_size = 30

        self.button_color = (156, 243, 255)
        self.clicked_color = (184, 246, 255)
        self.hover_color = (75, 255, 255)
        self.text_color = (0, 0, 0)
        self.number = 0

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.enable = True

    def drawButton(self, screen):
        global clicked
        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos) and self.enable:
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, self.clicked_color, self.rect)

            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_color, self.rect)

        else:
            pygame.draw.rect(screen, self.button_color, self.rect)

        font = pygame.font.Font("freesansbold.ttf", self.text_size)
        text_img = font.render(self.text, True, self.text_color)
        text_length = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) -
                    int(text_length / 2), self.y + 10))
        return action