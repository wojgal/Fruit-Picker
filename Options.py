from BasicDrawing import *
from Sounds import *


OPTIONS_FILE_PATH = Path(os.path.join('Data', 'Options.txt'))
OPTIONS_FILE_PATH.touch(exist_ok=True)
OPTIONS_FILE = open(OPTIONS_FILE_PATH, 'r+')


def options_file_read(options_dict):
    while True:
        option = OPTIONS_FILE.readline()

        if option == '':
            OPTIONS_FILE.seek(0)
            break

        option = option.replace('\n', '')
        option_list = option.split('=')
        option_name, option_boolean = option_list[0], option_list[1]

        if option_boolean == 'False':
            option_boolean = False
        else:
            option_boolean = True

        options_dict[option_name] = option_boolean


def options_file_update(options_dict):
    for option_key in options_dict:
        option_name, option_boolean = option_key, options_dict[option_key]
        write_line = str(option_name) + '=' + str(option_boolean) + '\n'
        OPTIONS_FILE.write(write_line)

    OPTIONS_FILE.truncate()
    OPTIONS_FILE.seek(0)
    OPTIONS_FILE.close()



BLACK_BOX = pygame.image.load(os.path.join('Images', 'Black Square.png'))
BLACK_BOX_X = pygame.image.load(os.path.join('Images', 'Black Square X.png'))

# Statistics i options napisy
MUSIC_SETTINGS_TEXT = FONT.render("MUZYKA", 1, BLACK)
SOUNDS_SETTINGS_TEXT = FONT.render("EFEKTY DZWIEKOWE", 1, BLACK)
RETURN_TEXT = FONT_BIG.render('WROC', 1, BLACK)
OPTIONS_TEXT = FONT_BIG.render('OPCJE', 1, BLACK)

MUSIC_SETTINGS_BOX_OBJECT = Image_with_Rect(BLACK_BOX, (WINDOW_WIDTH - PARCHMENT.get_width()) / 2 + MUSIC_SETTINGS_TEXT.get_width() + 90, (WINDOW_HEIGHT - MUSIC_SETTINGS_TEXT.get_height()) / 2,
                                            BLACK_BOX.get_width(), BLACK_BOX.get_height())
SOUNDS_SETTINGS_BOX_OBJECT = Image_with_Rect(BLACK_BOX, (WINDOW_WIDTH - PARCHMENT.get_width()) / 2 + SOUNDS_SETTINGS_TEXT.get_width() + 90, (WINDOW_HEIGHT - SOUNDS_SETTINGS_TEXT.get_height()) / 2 + MUSIC_SETTINGS_TEXT.get_height() + 20,
                                             BLACK_BOX.get_width(), BLACK_BOX.get_height())
RETURN_OBJECT = Image_with_Rect(RETURN_TEXT, (WINDOW_WIDTH - RETURN_TEXT.get_width()) / 2, 540, RETURN_TEXT.get_width(), RETURN_TEXT.get_height())
OPTIONS_OBJECT = Image_with_Rect(OPTIONS_TEXT, (WINDOW_WIDTH - OPTIONS_TEXT.get_width()) / 2, 155, OPTIONS_TEXT.get_width(), OPTIONS_TEXT.get_height())


def draw_options(options_dict):
    WINDOW.blit(BACKGROUND, (0, 0))
    WINDOW.blit(PARCHMENT, ((WINDOW_WIDTH - PARCHMENT.get_width()) / 2, (WINDOW_HEIGHT - PARCHMENT.get_height()) / 2) )

    WINDOW.blit(OPTIONS_TEXT, ((WINDOW_WIDTH - OPTIONS_TEXT.get_width()) / 2 , (WINDOW_HEIGHT - PARCHMENT.get_height()) / 2 + 70))

    WINDOW.blit(MUSIC_SETTINGS_TEXT, ((WINDOW_WIDTH - PARCHMENT.get_width()) / 2 + 70, WINDOW_HEIGHT / 2))
    WINDOW.blit(MUSIC_SETTINGS_BOX_OBJECT.get_image(), MUSIC_SETTINGS_BOX_OBJECT.get_coordinates())
    WINDOW.blit(SOUNDS_SETTINGS_TEXT, ((WINDOW_WIDTH - PARCHMENT.get_width()) / 2 + 70, WINDOW_HEIGHT / 2 + MUSIC_SETTINGS_TEXT.get_height() + 20))
    WINDOW.blit(SOUNDS_SETTINGS_BOX_OBJECT.get_image(), SOUNDS_SETTINGS_BOX_OBJECT.get_coordinates())

    if options_dict['music']:
        WINDOW.blit(BLACK_BOX_X, MUSIC_SETTINGS_BOX_OBJECT.get_coordinates())
    if options_dict['sound']:
        WINDOW.blit(BLACK_BOX_X, SOUNDS_SETTINGS_BOX_OBJECT.get_coordinates())

    WINDOW.blit(RETURN_OBJECT.get_image(), RETURN_OBJECT.get_coordinates())

    draw_game_version()
    draw_cursor()

    pygame.display.update()


def options(options_dict):
    clock = pygame.time.Clock()

    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()

                if RETURN_OBJECT.get_rect().collidepoint(mouse_position):
                    play_sound_effect(MENU_CLICK_SOUND)
                    return 'main menu'
                if MUSIC_SETTINGS_BOX_OBJECT.get_rect().collidepoint(mouse_position):
                    play_sound_effect(MENU_CLICK_SOUND)
                    options_dict['music'] = turn_on_off_music(options_dict['music'])
                if SOUNDS_SETTINGS_BOX_OBJECT.get_rect().collidepoint(mouse_position):
                    play_sound_effect(MENU_CLICK_SOUND)
                    options_dict['sound'] = turn_on_off_sounds(options_dict['sound'])

        draw_options(options_dict)

    return 'quit'
