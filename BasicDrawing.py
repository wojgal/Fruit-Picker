import pygame.transform

from BasicSettings import *

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Images', 'Background2.jpg')), (WINDOW_WIDTH, WINDOW_HEIGHT))
LOGO = pygame.image.load(os.path.join('Images', 'Fruit Picker.png'))
PARCHMENT = pygame.image.load(os.path.join('Images', 'Parchment.png'))
PARCHMENT = pygame.transform.rotozoom(PARCHMENT, 0, 1.1)



CURSOR = pygame.image.load(os.path.join('Images', 'Cursor.png'))

def draw_cursor():
    coordinates = pygame.mouse.get_pos()
    WINDOW.blit(CURSOR, coordinates)


GAME_VERSION_TEXT = FONT_SO_SMALL.render("Wersja " + str(GAME_VERSION), 1, BLACK)

def draw_game_version():
    WINDOW.blit(GAME_VERSION_TEXT, (WINDOW_WIDTH - GAME_VERSION_TEXT.get_width() - 10, WINDOW_HEIGHT - GAME_VERSION_TEXT.get_height() - 10))


def draw_number_of_page(current_page, max_page):
    text = FONT_SMALL.render(str(current_page) + '/' + str(max_page), 1, BLACK)
    WINDOW.blit(text, ((WINDOW_WIDTH - PARCHMENT.get_width()) / 2 + 25, (WINDOW_HEIGHT - PARCHMENT.get_height()) / 2 + PARCHMENT.get_height() - 33))


ARROW_RIGHT_IMG = pygame.image.load(os.path.join('Images', 'Arrow.png'))
ARROW_LEFT_IMG = pygame.transform.flip(ARROW_RIGHT_IMG, True, False)

ARROW_RIGHT_OBJECT = Image_with_Rect(ARROW_RIGHT_IMG, (WINDOW_WIDTH + PARCHMENT.get_width()) / 2 - ARROW_RIGHT_IMG.get_width() - 20, WINDOW_HEIGHT / 2, 28, 28)
ARROW_LEFT_OBJECT = Image_with_Rect(ARROW_LEFT_IMG, (WINDOW_WIDTH - PARCHMENT.get_width()) / 2 + 20, WINDOW_HEIGHT / 2, 28, 28)

def draw_arrows():
    WINDOW.blit(ARROW_RIGHT_OBJECT.get_image(), ARROW_RIGHT_OBJECT.get_coordinates())
    WINDOW.blit(ARROW_LEFT_OBJECT.get_image(), ARROW_LEFT_OBJECT.get_coordinates())