from BasicSettings import *
from BasicDrawing import *
from Sounds import *


# Extras napisy
STATISTICS_TEXT = FONT_BIG.render("STATYSTYKI", 1, BLACK)
ACHIEVEMENTS_TEXT = FONT_BIG.render("OSIAGNIECIA", 1, BLACK)
CUSTOMISATION_TEXT = FONT_BIG.render("KUSTOMIZACJA", 1, BLACK)
RETURN_TEXT = FONT_BIG.render("WROC", 1, BLACK)

# Extras obiekty
CUSTOMISATION_OBJECT = Image_with_Rect(CUSTOMISATION_TEXT, (WINDOW_WIDTH - CUSTOMISATION_TEXT.get_width()) / 2, 300, CUSTOMISATION_TEXT.get_width(), CUSTOMISATION_TEXT.get_height())
STATISTICS_OBJECT = Image_with_Rect(STATISTICS_TEXT, (WINDOW_WIDTH - STATISTICS_TEXT.get_width()) / 2, 350, STATISTICS_TEXT.get_width(), STATISTICS_TEXT.get_height())
ACHIEVEMENTS_OBJECT = Image_with_Rect(ACHIEVEMENTS_TEXT, (WINDOW_WIDTH - ACHIEVEMENTS_TEXT.get_width()) / 2, 400, ACHIEVEMENTS_TEXT.get_width(), ACHIEVEMENTS_TEXT.get_height())
RETURN_OBJECT = Image_with_Rect(RETURN_TEXT, (WINDOW_WIDTH - RETURN_TEXT.get_width()) / 2, 450, RETURN_TEXT.get_width(), RETURN_TEXT.get_height())

EXTRAS_OBJECTS = [CUSTOMISATION_OBJECT, STATISTICS_OBJECT, ACHIEVEMENTS_OBJECT, RETURN_OBJECT]


def draw_extras():
    WINDOW.blit(BACKGROUND, (0, 0))

    WINDOW.blit(LOGO, (500, 200))

    for object in EXTRAS_OBJECTS:
        WINDOW.blit(object.get_image(), object.get_coordinates())

    draw_game_version()
    draw_cursor()

    pygame.display.update()

def extras():
    clock = pygame.time.Clock()

    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()

                if CUSTOMISATION_OBJECT.get_rect().collidepoint(mouse_position):
                    play_sound_effect(MENU_CLICK_SOUND)
                    return 'customisation'
                if STATISTICS_OBJECT.get_rect().collidepoint(mouse_position):
                    play_sound_effect(MENU_CLICK_SOUND)
                    return 'statistics'
                if ACHIEVEMENTS_OBJECT.get_rect().collidepoint(mouse_position):
                    play_sound_effect(MENU_CLICK_SOUND)
                    return 'achievements'
                if RETURN_OBJECT.get_rect().collidepoint(mouse_position):
                    play_sound_effect(MENU_CLICK_SOUND)
                    return 'main menu'

        draw_extras()

    return 'quit'