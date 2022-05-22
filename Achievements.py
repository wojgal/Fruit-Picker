from BasicSettings import *
from BasicDrawing import *
from pathlib import Path
from Sounds import *
from AchievementsUnlocking import *

# Odczytywanie i zapisywanie osiagniec
ACHIEVEMENTS_FILE_PATH = Path(os.path.join('Data', 'Achievements.txt'))
ACHIEVEMENTS_FILE_PATH.touch(exist_ok=True)
ACHIEVEMENTS_FILE = open(ACHIEVEMENTS_FILE_PATH, 'r+')

def achievements_file_read(achievements_dict):
    while True:
        achievement = ACHIEVEMENTS_FILE.readline()

        if achievement == '':
            ACHIEVEMENTS_FILE.seek(0)
            break

        achievement = achievement.replace('\n', '')     # Usuniecie znaku nowej lini

        achievement_list = achievement.split('=')
        achievement_name, achievement_boolean = achievement_list[0], achievement_list[1]

        if achievement_boolean == 'True':
            achievement_boolean = True
        else:
            achievement_boolean = False

        achievements_dict[achievement_name] = achievement_boolean


def achievemenets_file_update(achievements_dict):
    for achiev_key in achievements_dict:
        achiev_name, achiev_boolean = achiev_key, achievements_dict[achiev_key]
        write_line = str(achiev_name) + '=' + str(achiev_boolean) + '\n'
        ACHIEVEMENTS_FILE.write(write_line)

    ACHIEVEMENTS_FILE.truncate()
    ACHIEVEMENTS_FILE.seek(0)
    ACHIEVEMENTS_FILE.close()


def check_for_achievement_unlock(achievements_dict, statistics_dict):
    games_played_achievements(achievements_dict, statistics_dict['all_games_played'])
    all_fruits_picked_achievements(achievements_dict, statistics_dict['all_time_fruits'])
    highscore_achievements(achievements_dict, statistics_dict['highscore'])


# Generowanie napisow
ACHIEVEMENTS_TEXT =  FONT_BIG.render('OSIAGNIECIA', 1, BLACK)
RETURN_TEXT = FONT_BIG.render('WROC', 1, BLACK)

# Generowanie obiektow na napisach
ACHIEVEMENTS_OBJECT = Image_with_Rect(ACHIEVEMENTS_TEXT, (WINDOW_WIDTH - ACHIEVEMENTS_TEXT.get_width()) / 2, 350,
                                      ACHIEVEMENTS_TEXT.get_width(), ACHIEVEMENTS_TEXT.get_width())
RETURN_OBJECT = Image_with_Rect(RETURN_TEXT, (WINDOW_WIDTH - RETURN_TEXT.get_width()) / 2, 450, RETURN_TEXT.get_width(), RETURN_TEXT.get_height())

ACHIEVEMENTS_OBJECTS = [ACHIEVEMENTS_OBJECT, RETURN_TEXT]


def draw_achievements(achievements_dict):
    WINDOW.blit(BACKGROUND, (0, 0))
    WINDOW.blit(PARCHMENT, ((WINDOW_WIDTH - PARCHMENT.get_width()) / 2, (WINDOW_HEIGHT - PARCHMENT.get_height()) / 2))

    for object in ACHIEVEMENTS_OBJECTS:
        WINDOW.blit(object.get_image(), object.get_coordinates())

    draw_game_version()
    draw_cursor()

    pygame.display.update()


def achievements(achievements_dict):
    clock = pygame.time.Clock()

    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()

                if RETURN_OBJECT.get_rect().collidepoint(mouse_position):
                    play_sound_effect(MENU_CLICK_SOUND)
                    return 'extras'

        draw_achievements(achievements_dict)

    return 'quit'
