from BasicSettings import *
from BasicDrawing import *
from Sounds import *

# Generowanie napisow
START_GAME_TEXT = FONT_BIG.render("ROZPOCZNIJ GRE", 1, BLACK)
EXTRAS_TEXT = FONT_BIG.render("DODATKI", 1, BLACK)
OPTIONS_TEXT = FONT_BIG.render("OPCJE", 1, BLACK)
QUIT_GAME_TEXT = FONT_BIG.render("WYJDZ", 1, BLACK)

# Generowanie obiektow na napisach
START_GAME_OBJECT = Image_with_Rect(START_GAME_TEXT,(WINDOW_WIDTH - START_GAME_TEXT.get_width()) / 2, 300, START_GAME_TEXT.get_width(), START_GAME_TEXT.get_height())
EXTRAS_OBJECT = Image_with_Rect(EXTRAS_TEXT, (WINDOW_WIDTH - EXTRAS_TEXT.get_width()) / 2, 350, EXTRAS_TEXT.get_width(), EXTRAS_TEXT.get_height())
OPTIONS_OBJECT = Image_with_Rect(OPTIONS_TEXT,(WINDOW_WIDTH - OPTIONS_TEXT.get_width()) / 2, 400, OPTIONS_TEXT.get_width(), OPTIONS_TEXT.get_height())
QUIT_GAME_OBJECT = Image_with_Rect(QUIT_GAME_TEXT,(WINDOW_WIDTH - QUIT_GAME_TEXT.get_width()) / 2, 450, QUIT_GAME_TEXT.get_width(), QUIT_GAME_TEXT.get_height())


MAIN_MENU_OBJECTS = [START_GAME_OBJECT, EXTRAS_OBJECT, OPTIONS_OBJECT, QUIT_GAME_OBJECT]


def draw_main_menu():
    WINDOW.blit(BACKGROUND, (0, 0))

    WINDOW.blit(LOGO, (500, 200))

    for object in MAIN_MENU_OBJECTS:
        WINDOW.blit(object.get_image(), object.get_coordinates())

    draw_game_version()
    draw_cursor()

    pygame.display.update()


def main_menu():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()

                if START_GAME_OBJECT.get_rect().collidepoint(mouse_position):   # Wybranie rozpoczecia gry
                    play_sound_effect(MENU_CLICK_SOUND)
                    return 'game'
                elif EXTRAS_OBJECT.rect.collidepoint(mouse_position):       # Wybranie dodatkow
                    play_sound_effect(MENU_CLICK_SOUND)
                    return 'extras'
                elif OPTIONS_OBJECT.rect.collidepoint(mouse_position):          # Wybranie opcji
                    play_sound_effect(MENU_CLICK_SOUND)
                    return 'options'
                elif QUIT_GAME_OBJECT.rect.collidepoint(mouse_position):        # Wybranie wyjscia
                    play_sound_effect(MENU_CLICK_SOUND)
                    run = False

        draw_main_menu()

    return 'quit'