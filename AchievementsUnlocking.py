def games_played_achievements(achievements_dict, games_played):
    if not achievements_dict['1_game_played']:
        if games_played >= 1:
            achievements_dict['1_game_played'] = True

    if not achievements_dict['100_games_played']:
        if games_played >= 100:
            achievements_dict['100_games_played'] = True

    if not achievements_dict['1k_games_played']:
        if games_played >= 1000:
            achievements_dict['1k_games_played'] = True


def all_fruits_picked_achievements(achievements_dict, all_fruits_picked):
    if not achievements_dict['1_fruit_picked']:
        if all_fruits_picked >= 1:
            achievements_dict['1_fruit_picked'] = True

    if not achievements_dict['100_fruits_picked']:
        if all_fruits_picked >= 100:
            achievements_dict['100_fruits_picked'] = True

    if not achievements_dict['1k_fruits_picked']:
        if all_fruits_picked >= 1000:
            achievements_dict['1k_fruits_picked'] = True

    if not achievements_dict['10k_fruits_picked']:
        if all_fruits_picked >= 10000:
            achievements_dict['10k_fruits_picked'] = True

    if not achievements_dict['100k_fruits_picked']:
        if all_fruits_picked >= 100000:
            achievements_dict['100k_fruits_picked'] = True


def highscore_achievements(achievements_dict, highscore):
    if not achievements_dict['highscore_50']:
        if highscore >= 50:
            achievements_dict['highscore_50'] = True

    if not achievements_dict['highscore_100']:
        if highscore >= 100:
            achievements_dict['highscore_100'] = True

    if not achievements_dict['highscore_250']:
        if highscore >= 250:
            achievements_dict['highscore_250'] = True

    if not achievements_dict['highscore_1k']:
        if highscore >= 1000:
            achievements_dict['highscore_1k'] = True


