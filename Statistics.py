from BasicDrawing import *
from Sounds import *
from Fruits import *

STATISTICS_FILE_PATH = Path(os.path.join('Data', 'Statistics.txt.'))
STATISTICS_FILE_PATH.touch(exist_ok=True)
#STATISTICS_FILE = open(STATISTICS_FILE_PATH, 'r+')


def statistics_file_read(statistics_dict):
    with open(STATISTICS_FILE_PATH, 'r+') as file:
        while True:
            statistic = file.readline()

            if not statistic:
                break

            statistic = statistic.replace('\n', '')
            statistic_name, statistic_value = statistic.split('=')

            statistics_dict[statistic_name] = int(statistic_value)



def statistics_file_update(statistics_dict):
    with open(STATISTICS_FILE_PATH, 'w+') as file:
        for statistic_name in statistics_dict:
            statistic_value = statistics_dict.get(statistic_name)

            write_line = f'{statistic_name}={statistic_value}\n'

            file.write(write_line)
        
        file.truncate()



def statistics_update_after_game(score, collected_coins, statistics_dict):
    if score > statistics_dict['highscore']:
        statistics_dict['highscore'] = score

    statistics_dict['money'] += collected_coins
    statistics_dict['all_time_score'] += score
    statistics_dict['all_games_played'] += 1



def draw_items_with_amount(statistics_dict, list_of_items):
    px_width, px_height = 500, 220

    for idx, item in enumerate(list_of_items):
        if idx == 5:    # Tworzenie drugiej kolumny
            px_width = 700
            px_height = 220

        type_, img = item[0], item[1]
        text = FONT.render(str(statistics_dict[type_]), 1, BLACK)

        WINDOW.blit(img, (px_width, px_height))
        WINDOW.blit(text, (px_width + img.get_width() + 15, px_height + img.get_height()/2 - text.get_height()/2))

        px_height += img.get_height() + 15


STATISTICS_TEXT = FONT_BIG.render('STATYSTYKI', 1, BLACK)
RETURN_TEXT = FONT_BIG.render('WROC', 1, BLACK)

STATISTICS_OBJECT = Image_with_Rect(STATISTICS_TEXT, (WINDOW_WIDTH - STATISTICS_TEXT.get_width()) /2, 155, STATISTICS_TEXT.get_width(), STATISTICS_TEXT.get_height())
RETURN_OBJECT = Image_with_Rect(RETURN_TEXT, (WINDOW_WIDTH - RETURN_TEXT.get_width()) / 2, 540, RETURN_TEXT.get_width(), RETURN_TEXT.get_height())

STATISTICS_PAGES = 3

def draw_statistics_page_1(statistics_dict):
    WINDOW.blit(BACKGROUND, (0, 0))
    WINDOW.blit(PARCHMENT, ((WINDOW_WIDTH - PARCHMENT.get_width()) / 2, (WINDOW_HEIGHT - PARCHMENT.get_height()) / 2))

    WINDOW.blit(STATISTICS_OBJECT.get_image(), STATISTICS_OBJECT.get_coordinates())

    highscore_text = FONT.render("NAJLEPSZY WYNIK: " + str(statistics_dict['highscore']), 1, BLACK)
    WINDOW.blit(highscore_text, ((WINDOW_WIDTH - highscore_text.get_width()) / 2, 250))

    money_text = FONT.render("ILOSC MONET: " + str(statistics_dict['money']), 1, BLACK)
    WINDOW.blit(money_text, ((WINDOW_WIDTH - money_text.get_width()) / 2, 250 + highscore_text.get_height() + 15))

    all_time_score_text = FONT.render('ZEBRANE PUNKTY LACZNIE: ' + str(statistics_dict['all_time_score']), 1, BLACK)
    WINDOW.blit(all_time_score_text, ((WINDOW_WIDTH - all_time_score_text.get_width()) / 2, 250 + highscore_text.get_height() + money_text.get_height() + 30))

    all_time_fruits_text = FONT.render('ZEBRANE OWOCE LACZNIE: ' + str(statistics_dict['all_time_fruits']), 1, BLACK)
    WINDOW.blit(all_time_fruits_text, ((WINDOW_WIDTH - all_time_fruits_text.get_width()) / 2,
                250 + highscore_text.get_height() + money_text.get_height() + all_time_score_text.get_height() + 45))

    games_played = FONT.render('ROZEGRANE GRY: ' + str(statistics_dict['all_games_played']), 1, BLACK)
    WINDOW.blit(games_played, ((WINDOW_WIDTH - games_played.get_width()) / 2,
                               250 + highscore_text.get_height() + money_text.get_height() + all_time_score_text.get_height() + all_time_fruits_text.get_height() + 60))

    WINDOW.blit(RETURN_OBJECT.get_image(), RETURN_OBJECT.get_coordinates())

    draw_game_version()
    draw_number_of_page(1, STATISTICS_PAGES)
    draw_arrows()
    draw_cursor()

    pygame.display.update()


def draw_statistics_page_2(statistics_dict):
    WINDOW.blit(BACKGROUND, (0, 0))
    WINDOW.blit(PARCHMENT, ((WINDOW_WIDTH - PARCHMENT.get_width()) / 2, (WINDOW_HEIGHT - PARCHMENT.get_height()) / 2))

    WINDOW.blit(STATISTICS_OBJECT.get_image(), STATISTICS_OBJECT.get_coordinates())

    draw_items_with_amount(statistics_dict, FRUITS_CLASS_1_TYPES_WITH_IMG + FRUITS_CLASS_2_TYPES_WITH_IMG)

    WINDOW.blit(RETURN_OBJECT.get_image(), RETURN_OBJECT.get_coordinates())

    draw_game_version()
    draw_number_of_page(2, STATISTICS_PAGES)
    draw_arrows()
    draw_cursor()

    pygame.display.update()


def draw_statistics_page_3(statistics_dict):
    WINDOW.blit(BACKGROUND, (0, 0))
    WINDOW.blit(PARCHMENT, ((WINDOW_WIDTH - PARCHMENT.get_width()) / 2, (WINDOW_HEIGHT - PARCHMENT.get_height()) / 2))

    WINDOW.blit(STATISTICS_OBJECT.get_image(), STATISTICS_OBJECT.get_coordinates())

    draw_items_with_amount(statistics_dict, SWEETS_TYPES_WITH_IMG + COINS_TYPES_WITH_IMG + SPECIAL_ITEMS_TYPES_WITH_IMG)

    WINDOW.blit(RETURN_OBJECT.get_image(), RETURN_OBJECT.get_coordinates())

    draw_game_version()
    draw_number_of_page(3, STATISTICS_PAGES)
    draw_arrows()
    draw_cursor()

    pygame.display.update()


def draw_statistics(statistics_dict, page):
    if page == 1:
        draw_statistics_page_1(statistics_dict)
    elif page == 2:
        draw_statistics_page_2(statistics_dict)
    elif page == 3:
        draw_statistics_page_3(statistics_dict)


def statistics(statistics_dict):
    page = 1

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            return 'quit'
        
        if event.type == pygame.MOUSEBUTTONDOWN:

            if ARROW_RIGHT_BUTTON.check_click():
                play_sound_effect(PAGE_TURN_SOUND)
                if not page + 1 > STATISTICS_PAGES:
                    page += 1

            elif ARROW_LEFT_BUTTON.check_click():
                play_sound_effect(PAGE_TURN_SOUND)
                if not page - 1 < 1:
                    page -= 1

            elif RETURN_OBJECT.get_rect().collidepoint(pygame.mouse.get_pos()):
                play_sound_effect(MENU_CLICK_SOUND)
                return 'extras'

    draw_statistics(statistics_dict, page)

    return 'statistics'