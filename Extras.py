from BasicSettings import *
from BasicDrawing import *
from Sounds import *
from Button import *


# Extras napisy
STATISTICS_TEXT = FONT_BIG.render("STATYSTYKI", 1, BLACK)
ACHIEVEMENTS_TEXT = FONT_BIG.render("OSIAGNIECIA", 1, BLACK)
CUSTOMISATION_TEXT = FONT_BIG.render("KUSTOMIZACJA", 1, BLACK)
RETURN_TEXT = FONT_BIG.render("WROC", 1, BLACK)

# Extras buttons
CUSTOMISATION_BUTTON = Button((WINDOW_WIDTH - CUSTOMISATION_TEXT.get_width()) // 2, 300, CUSTOMISATION_TEXT)
STATISTICS_BUTTON = Button((WINDOW_WIDTH - STATISTICS_TEXT.get_width()) // 2, 350, STATISTICS_TEXT)
ACHIEVEMENTS_BUTTON = Button((WINDOW_WIDTH - ACHIEVEMENTS_TEXT.get_width()) // 2, 400, ACHIEVEMENTS_TEXT)
RETURN_BUTTON = Button((WINDOW_WIDTH - RETURN_TEXT.get_width()) / 2, 450, RETURN_TEXT)
# Extras obiekty
CUSTOMISATION_OBJECT = Image_with_Rect(CUSTOMISATION_TEXT, (WINDOW_WIDTH - CUSTOMISATION_TEXT.get_width()) / 2, 300, CUSTOMISATION_TEXT.get_width(), CUSTOMISATION_TEXT.get_height())
STATISTICS_OBJECT = Image_with_Rect(STATISTICS_TEXT, (WINDOW_WIDTH - STATISTICS_TEXT.get_width()) / 2, 350, STATISTICS_TEXT.get_width(), STATISTICS_TEXT.get_height())
ACHIEVEMENTS_OBJECT = Image_with_Rect(ACHIEVEMENTS_TEXT, (WINDOW_WIDTH - ACHIEVEMENTS_TEXT.get_width()) / 2, 400, ACHIEVEMENTS_TEXT.get_width(), ACHIEVEMENTS_TEXT.get_height())
RETURN_OBJECT = Image_with_Rect(RETURN_TEXT, (WINDOW_WIDTH - RETURN_TEXT.get_width()) / 2, 450, RETURN_TEXT.get_width(), RETURN_TEXT.get_height())

EXTRAS_BUTTONS = [CUSTOMISATION_BUTTON, STATISTICS_BUTTON, ACHIEVEMENTS_BUTTON, RETURN_BUTTON]
EXTRAS_OBJECTS = [CUSTOMISATION_OBJECT, STATISTICS_OBJECT, ACHIEVEMENTS_OBJECT, RETURN_OBJECT]


def draw_extras():
    WINDOW.blit(BACKGROUND, (0, 0))

    WINDOW.blit(LOGO, (500, 200))

    for button in EXTRAS_BUTTONS:
        WINDOW.blit(button.get_image(), button.get_cords())

    draw_game_version()
    draw_cursor()

    pygame.display.update()

def extras():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 'quit'
        
        if event.type == pygame.MOUSEBUTTONDOWN:

            if CUSTOMISATION_BUTTON.check_click():
                play_sound_effect(MENU_CLICK_SOUND)
                return 'customisation'
                
            if STATISTICS_BUTTON.check_click():
                play_sound_effect(MENU_CLICK_SOUND)
                return 'statistics'
                
            if ACHIEVEMENTS_BUTTON.check_click():
                play_sound_effect(MENU_CLICK_SOUND)
                return 'achievements'
            
            if RETURN_BUTTON.check_click():
               play_sound_effect(MENU_CLICK_SOUND)
               return 'main menu'

    draw_extras()

    return 'extras'