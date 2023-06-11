from BasicDrawing import *
from Sounds import *
from Button import *


OPTIONS_FILE_PATH = Path(os.path.join('Data', 'Options.txt'))
OPTIONS_FILE_PATH.touch(exist_ok=True)

def options_file_read(options_dict):
    with open(OPTIONS_FILE_PATH, 'r+') as file:
        while True:
            option = file.readline()

            if not option:
                break

            option = option.replace('\n', '')
            option_name, option_boolean = option.split('=')

            if option_boolean == 'True':
                options_dict[option_name] = True
                
            elif option_boolean == 'False':
                options_dict[option_name] = False



def options_file_update(options_dict):
    with open(OPTIONS_FILE_PATH, 'w+') as file:
        for option_name in options_dict:
            option_boolean = options_dict.get(option_name)

            write_line = f'{option_name}={option_boolean}\n'
            
            file.write(write_line)

        file.truncate()



BLACK_BOX = pygame.image.load(os.path.join('Images', 'Black Square.png'))
BLACK_BOX_X = pygame.image.load(os.path.join('Images', 'Black Square X.png'))

# Statistics i options napisy
MUSIC_SETTINGS_TEXT = FONT.render("MUZYKA", 1, BLACK)
SOUNDS_SETTINGS_TEXT = FONT.render("EFEKTY DZWIEKOWE", 1, BLACK)
RETURN_TEXT = FONT_BIG.render('WROC', 1, BLACK)
OPTIONS_TEXT = FONT_BIG.render('OPCJE', 1, BLACK)

MUSIC_SETTINGS_BUTTON = Button((WINDOW_WIDTH - PARCHMENT.get_width()) // 2 + MUSIC_SETTINGS_TEXT.get_width() + 90, (WINDOW_HEIGHT - MUSIC_SETTINGS_TEXT.get_height()) // 2, BLACK_BOX)
#MUSIC_SETTINGS_BOX_OBJECT = Image_with_Rect(BLACK_BOX, (WINDOW_WIDTH - PARCHMENT.get_width()) / 2 + MUSIC_SETTINGS_TEXT.get_width() + 90, (WINDOW_HEIGHT - MUSIC_SETTINGS_TEXT.get_height()) / 2,
                                            #BLACK_BOX.get_width(), BLACK_BOX.get_height())
#SOUNDS_SETTINGS_BOX_OBJECT = Image_with_Rect(BLACK_BOX, (WINDOW_WIDTH - PARCHMENT.get_width()) / 2 + SOUNDS_SETTINGS_TEXT.get_width() + 90, (WINDOW_HEIGHT - SOUNDS_SETTINGS_TEXT.get_height()) / 2 + MUSIC_SETTINGS_TEXT.get_height() + 20,
                                             #BLACK_BOX.get_width(), BLACK_BOX.get_height())
SOUNDS_SETTINGS_BUTTON = Button((WINDOW_WIDTH - PARCHMENT.get_width()) // 2 + SOUNDS_SETTINGS_TEXT.get_width() + 90, (WINDOW_HEIGHT - SOUNDS_SETTINGS_TEXT.get_height()) // 2 + MUSIC_SETTINGS_TEXT.get_height() + 20, BLACK_BOX)

RETURN_BUTTON = Button((WINDOW_WIDTH - RETURN_TEXT.get_width()) // 2, 540, RETURN_TEXT)
OPTIONS_BUTTON = Button((WINDOW_WIDTH - OPTIONS_TEXT.get_width()) / 2, 155, OPTIONS_TEXT)

#RETURN_OBJECT = Image_with_Rect(RETURN_TEXT, (WINDOW_WIDTH - RETURN_TEXT.get_width()) / 2, 540, RETURN_TEXT.get_width(), RETURN_TEXT.get_height())
#OPTIONS_OBJECT = Image_with_Rect(OPTIONS_TEXT, (WINDOW_WIDTH - OPTIONS_TEXT.get_width()) / 2, 155, OPTIONS_TEXT.get_width(), OPTIONS_TEXT.get_height())


def draw_options(options_dict):
    WINDOW.blit(BACKGROUND, (0, 0))
    WINDOW.blit(PARCHMENT, ((WINDOW_WIDTH - PARCHMENT.get_width()) / 2, (WINDOW_HEIGHT - PARCHMENT.get_height()) / 2) )

    WINDOW.blit(OPTIONS_TEXT, ((WINDOW_WIDTH - OPTIONS_TEXT.get_width()) / 2 , (WINDOW_HEIGHT - PARCHMENT.get_height()) / 2 + 70))

    WINDOW.blit(MUSIC_SETTINGS_TEXT, ((WINDOW_WIDTH - PARCHMENT.get_width()) / 2 + 70, WINDOW_HEIGHT / 2))
    WINDOW.blit(MUSIC_SETTINGS_BUTTON.get_image(), MUSIC_SETTINGS_BUTTON.get_cords())
    WINDOW.blit(SOUNDS_SETTINGS_TEXT, ((WINDOW_WIDTH - PARCHMENT.get_width()) / 2 + 70, WINDOW_HEIGHT / 2 + MUSIC_SETTINGS_TEXT.get_height() + 20))
    WINDOW.blit(SOUNDS_SETTINGS_BUTTON.get_image(), SOUNDS_SETTINGS_BUTTON.get_cords())

    if options_dict['music']:
        WINDOW.blit(BLACK_BOX_X, MUSIC_SETTINGS_BUTTON.get_cords())
    if options_dict['sound']:
        WINDOW.blit(BLACK_BOX_X, SOUNDS_SETTINGS_BUTTON.get_cords())

    WINDOW.blit(RETURN_BUTTON.get_image(), RETURN_BUTTON.get_cords())

    draw_game_version()
    draw_cursor()

    pygame.display.update()


def options(options_dict):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 'quit'
        
        if event.type == pygame.MOUSEBUTTONDOWN:

            if RETURN_BUTTON.check_click():
                play_sound_effect(MENU_CLICK_SOUND)
                return 'main menu'
            
            if MUSIC_SETTINGS_BUTTON.check_click():
                play_sound_effect(MENU_CLICK_SOUND)
                options_dict['music'] = turn_on_off_music(options_dict['music'])

            if SOUNDS_SETTINGS_BUTTON.check_click():
                play_sound_effect(MENU_CLICK_SOUND)
                options_dict['sound'] = turn_on_off_sounds(options_dict['sound'])

    draw_options(options_dict)

    return 'options'
