from MainMenu import *
from Extras import *
from Game import *
from Options import *
from Statistics import *
from Achievements import *
from Customisation import *


def test():
    pass

def main():
    window_type = 'main menu'

    pygame.mouse.set_visible(False)

    options_dict = {}
    options_file_read(options_dict)

    startup_music_sound(options_dict)

    achievements_dict = {}
    achievements_file_read(achievements_dict)

    statistics_dict = {}
    statistics_file_read(statistics_dict)

    character = Character(CHARACTER_WITH_BASKET_IMG, (WINDOW_WIDTH - CHARACTER_WITH_BASKET_WIDTH) / 2, 525, BASKET_WIDTH, BASKET_HEIGHT)
    fruits = []
    score = 0

    while window_type != 'quit':
        check_for_achievement_unlock(achievements_dict, statistics_dict)    # ZASTANOWIC SIE GDZIE NAJLEPIEJ TO DAC
        if window_type == 'main menu':
            window_type = main_menu()

        elif window_type == 'game':
            fruits.clear()
            score = 0
            character.reset_for_new_game()
            window_type, score, collected_coins = game(character, fruits, score, statistics_dict)
            statistics_update_after_game(score, collected_coins, statistics_dict)

        elif window_type == 'game lost':
            window_type = game_lost(character, fruits, score, collected_coins)

        elif window_type == 'extras':
            window_type = extras()

            if window_type == 'customisation':
                window_type = 'extras'

            elif window_type == 'statistics':
                window_type = statistics(statistics_dict)

            elif window_type == 'achievements':
                window_type = 'extras'

        elif window_type == 'options':
            window_type = options(options_dict)

    options_file_update(options_dict)
    achievemenets_file_update(achievements_dict)
    statistics_file_update(statistics_dict)

    pygame.quit()

if __name__ == '__main__':
    main()
