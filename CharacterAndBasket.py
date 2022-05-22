import pygame.transform

from BasicSettings import *
from PygameEvents import *

CHARACTER_WITH_BASKET_IMG = pygame.image.load(os.path.join('Images', 'Character with basket.png'))
CHARACTER_WITH_BASKET_WIDTH, CHARACTER_WITH_BASKET_HEIGHT = 105, 112
CHARACTER_SPEED = 10

BASKET_WIDTH, BASKET_HEIGHT = 64, 32    # Ze względu iż, model obrazka zaczyna się od wysokości głowy postaci, wysokość jest inaczej ustawiona WAZNE ZE DZIALA XD

class Character:
    def __init__(self, image, x, y, width, height):
        self.image = image
        self.image_x = x
        self.image_y = y
        self.rect = pygame.Rect(x, y, width, height)
        self.direction = 'left'

    def get_image(self):
        return self.image

    def get_image_x(self):
        return self.image_x

    def get_image_y(self):
        return self.image_y

    def get_image_coord(self):
        return self.image_x, self.image_y

    def get_rect(self):
        return self.rect

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def get_width(self):
        return self.rect.width

    def get_height(self):
        return self.rect.height

    def get_rect_coord(self):
        return self.rect.x, self.rect.y

    def change_direction(self):
        move = CHARACTER_WITH_BASKET_WIDTH - BASKET_WIDTH

        self.image = pygame.transform.flip(self.image, True, False)

        if self.direction == 'right':
            self.rect.x -= move
            self.direction = 'left'

        elif self.direction == 'left':
            self.rect.x += move
            self.direction = 'right'

    def reset_for_new_game(self):
        self.rect.x = self.image_x = (WINDOW_WIDTH - CHARACTER_WITH_BASKET_WIDTH) / 2
        self.rect.y = self.image_y = 525
        if self.direction == 'right':
            self.change_direction()

    def movement(self, button_pressed):
        if button_pressed[pygame.K_a] or button_pressed[pygame.K_LEFT]:
            if self.direction == 'right' and not button_pressed[pygame.K_LSHIFT]:
                self.change_direction()

            self.rect.x -= CHARACTER_SPEED
            self.image_x -= CHARACTER_SPEED

            if self.rect.x < - CHARACTER_WITH_BASKET_WIDTH / 2:
                self.rect.x = WINDOW_WIDTH - CHARACTER_WITH_BASKET_WIDTH / 2
                self.image_x = WINDOW_WIDTH - CHARACTER_WITH_BASKET_WIDTH / 2

        if button_pressed[pygame.K_d] or button_pressed[pygame.K_RIGHT]:
            if self.direction == 'left' and not button_pressed[pygame.K_LSHIFT]:
                self.change_direction()

            self.rect.x += CHARACTER_SPEED
            self.image_x += CHARACTER_SPEED

            if self.rect.x > WINDOW_WIDTH - CHARACTER_WITH_BASKET_WIDTH / 2:
                self.rect.x = -CHARACTER_WITH_BASKET_WIDTH / 2 + CHARACTER_WITH_BASKET_WIDTH - BASKET_WIDTH
                self.image_x = -CHARACTER_WITH_BASKET_WIDTH / 2

    def jump(self, tick):   #ZROBIONY PROWIZORYCZNIE, WYMAGA POPRAWY
        up = 0 <= tick < 20
        down = 22 < tick <= 42

        if up:
            self.rect.y -= 7
            self.image_y -= 7
        if down:
            self.rect.y += 7
            self.image_y += 7



