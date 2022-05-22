import os.path
import pygame

pygame.init()
pygame.font.init()

# Deklaracja kolorow
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

GAME_NAME = "Fruit Picker"
GAME_VERSION = 0.5
FPS = 60

pygame.display.set_caption(GAME_NAME)
pygame.display.set_icon(pygame.image.load(os.path.join('Images', 'Apple.png')))

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

FONT_PATH = os.path.join('Fonts', 'PressStart2P-Regular.ttf')
FONT = pygame.font.Font(FONT_PATH, 15)
FONT_BIG = pygame.font.Font(FONT_PATH, 30)
FONT_HUGE = pygame.font.Font(FONT_PATH, 45)
FONT_SMALL = pygame.font.Font(FONT_PATH, 12)
FONT_SO_SMALL = pygame.font.Font(FONT_PATH, 8)

class Image_with_Rect():
    def __init__(self, image, coord_x, coord_y, width, height):
        self.image = image
        self.rect = pygame.Rect(coord_x, coord_y, width, height)

    def get_image(self):
        return self.image

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

    def get_coordinates(self):
        return self.rect.x, self.rect.y

    def set_coordinates(self, coord_x, coord_y):
        self.rect.x = coord_x
        self.rect.y = coord_y

    def set_width_and_height(self, width, height):
        self.rect.width = width
        self.rect.height = height





