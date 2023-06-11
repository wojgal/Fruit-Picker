from BasicSettings import *
from BasicDrawing import *
from Sounds import *
from Button import *

# Generowanie napisow
START_GAME_TEXT = FONT_BIG.render("ROZPOCZNIJ GRE", 1, BLACK)
EXTRAS_TEXT = FONT_BIG.render("DODATKI", 1, BLACK)
OPTIONS_TEXT = FONT_BIG.render("OPCJE", 1, BLACK)
QUIT_GAME_TEXT = FONT_BIG.render("WYJDZ", 1, BLACK)

# Tworzenie przyciskow
START_GAME_BUTTON = Button((WINDOW_WIDTH - START_GAME_TEXT.get_width()) // 2, 300, START_GAME_TEXT)
EXTRAS_BUTTON = Button((WINDOW_WIDTH - EXTRAS_TEXT.get_width()) // 2, 350, EXTRAS_TEXT)
OPTIONS_BUTTON = Button((WINDOW_WIDTH - OPTIONS_TEXT.get_width()) // 2, 400, OPTIONS_TEXT)
QUIT_GAME_BUTTON = Button((WINDOW_WIDTH - QUIT_GAME_TEXT.get_width()) // 2, 450, QUIT_GAME_TEXT)

MAIN_MENU_BUTTONS = [START_GAME_BUTTON, EXTRAS_BUTTON, OPTIONS_BUTTON, QUIT_GAME_BUTTON]



def draw_main_menu():
    WINDOW.blit(BACKGROUND, (0, 0))

    WINDOW.blit(LOGO, (500, 200))

    for button in MAIN_MENU_BUTTONS:
        WINDOW.blit(button.get_image(), button.get_cords())

    draw_game_version()
    draw_cursor()

    #CRASHUJE TUTAJ, CHUJ WIE CZEMU
    pygame.display.update()


def main_menu():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 'quit'
        
        if event.type == pygame.MOUSEBUTTONDOWN:

            if START_GAME_BUTTON.check_click():   # Wybranie rozpoczecia gry
                play_sound_effect(MENU_CLICK_SOUND)
                return 'game'
            
            elif EXTRAS_BUTTON.check_click():      # Wybranie dodatkow
                play_sound_effect(MENU_CLICK_SOUND)
                return 'extras'
                
            elif OPTIONS_BUTTON.check_click():         # Wybranie opcji
                play_sound_effect(MENU_CLICK_SOUND)
                return 'options'
                
            elif QUIT_GAME_BUTTON.check_click():      # Wybranie wyjscia
                play_sound_effect(MENU_CLICK_SOUND)
                return 'quit'
                    
    draw_main_menu()

    return 'main menu'