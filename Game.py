import pygame

from BasicSettings import *
from BasicDrawing import *
from Sounds import *
from CharacterAndBasket import *
from Fruits import *

# Napisy pause
PAUSE_TEXT = FONT_HUGE.render("PAUZA", 1, BLACK)
# Obrazki pause
BLACK_SCREEN_IMG = pygame.image.load(os.path.join('Images', 'Black screen.png'))
BLACK_SCREEN_IMG.set_alpha(50)
# Obiekty pause
PAUSE_OBJECT = Image_with_Rect(PAUSE_TEXT, (WINDOW_WIDTH - PAUSE_TEXT.get_width()) / 2, WINDOW_HEIGHT / 2,
                               PAUSE_TEXT.get_width(), PAUSE_TEXT.get_height())

def draw_pause():
    WINDOW.blit(BLACK_SCREEN_IMG, (0, 0))
    WINDOW.blit(PAUSE_OBJECT.get_image(), PAUSE_OBJECT.get_coordinates())

    pygame.display.update()


HEALTH_APPLE = pygame.image.load(os.path.join('Images', 'Health Apple.png'))

def draw_health(health):
    for x in range(health):
        WINDOW.blit(HEALTH_APPLE, (WINDOW_WIDTH - (1 + x) * HEALTH_APPLE.get_width() - x * 5 - 10, 10))


def draw_game(character, fruits, score, health):
    WINDOW.blit(BACKGROUND, (0, 0))
    WINDOW.blit(character.get_image(), (character.get_image_coord()))

    score_text = FONT_BIG.render(str(score), 1, BLACK)
    WINDOW.blit(score_text, ((WINDOW_WIDTH - score_text.get_width()) / 2, 25 ))

    for fruit in fruits:
        WINDOW.blit(fruit.image, fruit.get_coord())

    draw_health(health)
    draw_game_version()

    pygame.display.update()


def game(character, fruits, score, statistics_dict):
    clock = pygame.time.Clock()

    cant_generate_fruit = 0
    health = 3
    collected_coins = 0

    fruits_picked_up = []
    fruits_lost = []

    jump = False
    ticks = 0
    pause = False

    run = True

    while run:
        clock.tick(FPS)

        button_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if button_pressed[pygame.K_ESCAPE]:     # Wlaczenie pauzy
                pause = not pause
                draw_pause()
            if (button_pressed[pygame.K_SPACE] or button_pressed[pygame.K_UP]) and not jump:
                jump = True
            if event.type == FRUIT_GENERATED:
                fruit = create_fruit(score)
                fruits.append(fruit)
            if event.type == FRUIT_PICKED_UP:
                play_sound_effect(PICK_UP_SOUND)
                fruit = fruits_picked_up.pop(0)
                score += fruit.get_value()
                collected_coins += fruit.get_coins()
                statistics_dict[fruit.get_type()] += 1
                statistics_dict['all_time_fruits'] += 1
            if event.type == FRUIT_LOST:
                fruit = fruits_lost.pop(0)
                if fruit.get_lose_health():
                    health -= 1

        if health == 0:
            return 'game lost', score, collected_coins + score // 10

        if pause:
            continue

        if jump:
            if ticks == 43:
                jump = False
                ticks = 0
            else:
                character.jump(ticks)
                ticks += 1

        #character_movement(button_pressed, character)
        character.movement(button_pressed)

        if not cant_generate_fruit:
            if generate_fruits():
                    cant_generate_fruit = FPS * 2 / 3
        else:
            cant_generate_fruit -= 1

        nowe_fruits_actions(fruits, character, fruits_picked_up, fruits_lost)

        draw_game(character, fruits, score, health)

    return 'quit', score, collected_coins + score // 10


# Game lost napisy
PLAY_AGAIN_TEXT = FONT.render("ZAGRAJ PONOWNIE", 1, BLACK)
RETURN_TO_MAIN_MENU_TEXT = FONT.render("WROC DO MENU", 1, BLACK)

# Tworzenie obiektow game lost na klasie Image_with_Rect
PLAY_AGAIN_OBJECT = Image_with_Rect(PLAY_AGAIN_TEXT, WINDOW_WIDTH / 2 - PLAY_AGAIN_TEXT.get_width() - 30, WINDOW_HEIGHT / 2 + 30,
                                    PLAY_AGAIN_TEXT.get_width(), PLAY_AGAIN_TEXT.get_height())
RETURN_TO_MAIN_MENU_OBJECT = Image_with_Rect(RETURN_TO_MAIN_MENU_TEXT, WINDOW_WIDTH / 2 + 30, WINDOW_HEIGHT / 2 + 30,
                                               RETURN_TO_MAIN_MENU_TEXT.get_width(), RETURN_TO_MAIN_MENU_TEXT.get_height())


def draw_game_lost(character, fruits, score, collected_coins):
    WINDOW.blit(BACKGROUND, (0, 0))
    WINDOW.blit(character.get_image(), (character.get_image_coord()))

    for fruit in fruits:
        WINDOW.blit(fruit.get_image(), fruit.get_coord())

    end_score_text = FONT_BIG.render("Wynik: " + str(score), 1, BLACK)
    WINDOW.blit(end_score_text,((WINDOW_WIDTH - end_score_text.get_width()) / 2, WINDOW_HEIGHT / 2 - 100))

    collected_coins_text = FONT.render('Zdobyte monety: ' + str(collected_coins), 1, BLACK)
    WINDOW.blit(collected_coins_text, ((WINDOW_WIDTH - collected_coins_text.get_width()) / 2, WINDOW_HEIGHT / 2  + end_score_text.get_height() - 80))

    WINDOW.blit(PLAY_AGAIN_OBJECT.get_image(), PLAY_AGAIN_OBJECT.get_coordinates())
    WINDOW.blit(RETURN_TO_MAIN_MENU_OBJECT.get_image(), RETURN_TO_MAIN_MENU_OBJECT.get_coordinates())

    draw_game_version()
    draw_cursor()

    pygame.display.update()



def game_lost(character, fruits, score, collected_coins):
    clock = pygame.time.Clock()

    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()

                if PLAY_AGAIN_OBJECT.get_rect().collidepoint(mouse_position):
                    play_sound_effect(MENU_CLICK_SOUND)
                    return 'game'
                elif RETURN_TO_MAIN_MENU_OBJECT.get_rect().collidepoint(mouse_position):
                    play_sound_effect(MENU_CLICK_SOUND)
                    return 'main menu'

        draw_game_lost(character, fruits, score, collected_coins)

    return 'quit'