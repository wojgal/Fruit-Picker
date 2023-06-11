import pygame.transform
from PygameEvents import *
from BasicSettings import *
import random

# Obrazki owocow I klasy
APPLE_IMG = pygame.image.load(os.path.join('Images', 'Apple.png'))
APPLE_IMG = pygame.transform.rotozoom(APPLE_IMG, 0, 0.5)
BANANA_IMG = pygame.image.load(os.path.join('Images', 'Banana.png'))
BANANA_IMG = pygame.transform.rotozoom(BANANA_IMG, 0, 0.5)
CHERRY_IMG = pygame.image.load(os.path.join('Images', 'Cherry.png'))
CHERRY_IMG = pygame.transform.rotozoom(CHERRY_IMG, 0, 0.5)
LEMON_IMG = pygame.image.load(os.path.join('Images', 'Lemon.png'))
LEMON_IMG = pygame.transform.rotozoom(LEMON_IMG, 0, 0.5)
ORANGE_IMG = pygame.image.load(os.path.join('Images', 'Orange.png'))
ORANGE_IMG = pygame.transform.rotozoom(ORANGE_IMG, 0, 0.48)
PEAR_IMG = pygame.image.load(os.path.join('Images', 'Pear.png'))
PEAR_IMG = pygame.transform.rotozoom(PEAR_IMG, 0, 0.45)

# Obrazki owocow II klasy
STRAWBERRY_IMG = pygame.image.load(os.path.join('Images', 'Strawberry.png'))
STRAWBERRY_IMG = pygame.transform.rotozoom(STRAWBERRY_IMG, 0, 0.5)
PINEAPPLE_IMG = pygame.image.load(os.path.join('Images', 'Pineapple.png'))
PINEAPPLE_IMG = pygame.transform.rotozoom(PINEAPPLE_IMG, 0, 0.50)
RASPBERRY_IMG = pygame.image.load(os.path.join('Images', 'Raspberry.png'))
RASPBERRY_IMG = pygame.transform.rotozoom(RASPBERRY_IMG, 0, 0.45)
WATERMELON_IMG = pygame.image.load(os.path.join('Images', 'Watermelon.png'))
WATERMELON_IMG = pygame.transform.rotozoom(WATERMELON_IMG, 0, 0.5)

# Obrazki slodyczy
DONUT_IMG = pygame.image.load(os.path.join('Images', 'Donut.png'))
DONUT_IMG = pygame.transform.rotozoom(DONUT_IMG, 0, 1.2)
CAKE_IMG = pygame.image.load(os.path.join('Images', 'Cake.png'))
CAKE_IMG = pygame.transform.rotozoom(CAKE_IMG, 0, 1.3)
CANDY_IMG = pygame.image.load(os.path.join('Images', 'Candy.png'))
CANDY_IMG = pygame.transform.rotozoom(CANDY_IMG, 0, 1.3)

# Obrazki coinsow
COIN_IMG = pygame.image.load(os.path.join('Images', 'Coin.png'))
COIN_IMG = pygame.transform.rotozoom(COIN_IMG, 0, 1.05)
COIN_3X_IMG = pygame.image.load(os.path.join('Images', 'Coin3x.png'))
COIN_3X_IMG = pygame.transform.rotozoom(COIN_3X_IMG, 0, 1.05)

# Obrazki specjalne
BOX_IMG = pygame.image.load(os.path.join('Images', 'Fruit Box.png'))
BOX_IMG = pygame.transform.rotozoom(BOX_IMG, 0, 0.55)
STAR_IMG = pygame.image.load(os.path.join('Images', 'Star.gif'))


TEMP_IMG = pygame.image.load(os.path.join('Images', '4.png'))

def generate_fruits():
    if random.randint(1, 60) == 1:
        pygame.event.post(pygame.event.Event(FRUIT_GENERATED))
        return True

    return False


def generate_fruit_x_spawn_location():
    return random.randint(100, 1180)


class Fruit:
    def __init__(self, type, image, speed, value, coins, lose_health):
        self.type = type
        self.image = image
        self.speed = speed
        self.value = value
        self.coins = coins
        self.lose_health = lose_health
        self.rect = pygame.Rect(generate_fruit_x_spawn_location(), 0, FRUIT_WIDTH, FRUIT_HEIGHT)

    def get_type(self):
        return self.type

    def get_image(self):
        return self.image

    def get_speed(self):
        return self.speed

    def get_value(self):
        return self.value

    def get_coins(self):
        return self.coins

    def get_lose_health(self):
        return self.lose_health

    def get_rect(self):
        return self.rect

    def get_coord(self):
        return (self.rect.x, self.rect.y)



FRUIT_WIDTH, FRUIT_HEIGHT = 32, 1   ## Ze względu iż, model obrazka zaczyna się od wysokości głowy postaci, wysokość jest inaczej ustawiona WAZNE ZE DZIALA XD
FRUIT_SPEED = 3


FRUIT_BASKET_SPEED = 3
SWEET_SPEED = 3
COIN_SPEED = 5
STAR_SPEED = 5


FRUIT_CLASS_1_VALUE = 1
FRUIT_CLASS_2_VALUE = 2
SWEET_VALUE = 10
COIN_VALUE = 0
STAR_VALUE = 50

# Owoce klasy pierwszej
FRUITS_CLASS_1_TYPES_WITH_IMG = [['apple', APPLE_IMG], ['banana', BANANA_IMG], ['cherry', CHERRY_IMG], ['lemon', LEMON_IMG],
                                 ['orange', ORANGE_IMG], ['pear', PEAR_IMG], ['strawberry', STRAWBERRY_IMG]]

# Owoce klasy drugiej
FRUITS_CLASS_2_TYPES_WITH_IMG = [['pineapple', PINEAPPLE_IMG], ['raspberry', RASPBERRY_IMG], ['watermelon', WATERMELON_IMG]]

# Slodkosci
SWEETS_TYPES_WITH_IMG = [['candy', CANDY_IMG], ['donut', DONUT_IMG], ['cake', CAKE_IMG]]

# Monety
COINS_TYPES_WITH_IMG = [['coin', COIN_IMG], ['coin3x', COIN_3X_IMG]]

# Specjalne przedmioty
SPECIAL_ITEMS_TYPES_WITH_IMG = [['box', BOX_IMG], ['star', STAR_IMG]]


def random_fruit_class_1():
    idx = random.randint(0, len(FRUITS_CLASS_1_TYPES_WITH_IMG) - 1)
    type_, img = FRUITS_CLASS_1_TYPES_WITH_IMG[idx]
    fruit = Fruit(type_, img, FRUIT_SPEED, FRUIT_CLASS_1_VALUE, 0, True)
    return fruit


def random_fruit_class_2():
    idx = random.randint(0, len(FRUITS_CLASS_2_TYPES_WITH_IMG) - 1)
    type_, img = FRUITS_CLASS_2_TYPES_WITH_IMG[idx]
    fruit = Fruit(type_, img, FRUIT_SPEED, FRUIT_CLASS_2_VALUE, 0, True)
    return fruit


def random_sweet():
    idx = random.randint(0, len(SWEETS_TYPES_WITH_IMG) - 1)
    type_, img = SWEETS_TYPES_WITH_IMG[idx]
    sweet = Fruit(type_, img, SWEET_SPEED, SWEET_VALUE, 0, True)
    return sweet


def random_fruit_box(score):
    value = 0
    coins = 0
    items = max(5, score // 15)
    for x in range(items):
        id = random.randint(0, 182)

        if 1 <= id <= 100:
            value += FRUIT_CLASS_1_VALUE
        elif 101 <= id <= 150:
            value += FRUIT_CLASS_2_VALUE
        elif 151 <= id <= 165:
            coins += 1
        elif 166 <= id <= 175:
            value += SWEET_VALUE
        elif 176 <= id <= 182:
            coins += 3

    box = Fruit('box', BOX_IMG, FRUIT_BASKET_SPEED, value, coins, True)
    return box


# Zasiegi owocow (rzadkosc)
# Owoc klasa I: 1-100 (100)
# Owoc klasa II: 101 - 150 (50)
# Coin: 151 - 165 (15)
# Slodkosci: 166 - 175 (10)
# Coin3x: 176 - 182 (7)
# Paczka: 183 - 188 (6)
# Gwiazkda: 189 - 190  (2)


def create_fruit(score):

    if score < 15:  # Owoce klasa I i II
        random_range = random.randint(1, 150)
    elif 15 <= score < 25:  # + coin
        random_range = random.randint(1, 165)
    elif 25 <= score < 50:  # + sweet
        random_range = random.randint(1, 175)
    elif 50 <= score < 100: # + coin3x i box
        random_range = random.randint(1, 188)
    elif score >= 100:  # + star
        random_range = random.randint(1, 190)

    fruit_class_1_range = 1 <= random_range <= 100
    fruit_class_2_range = 101 <= random_range <= 150
    coin_range = 151 <= random_range <= 165
    sweet_range = 166 <= random_range <= 175
    coin3x_range = 176 <= random_range <= 182
    box_range = 183 <= random_range <= 188
    star_range = 189 <= random_range <= 190

    if fruit_class_1_range:
        return random_fruit_class_1()
    if fruit_class_2_range:
        return random_fruit_class_2()
    if coin_range:
        return Fruit('coin', COIN_IMG, COIN_SPEED, COIN_VALUE, 1, False)
    if sweet_range:
        return random_sweet()
    if coin3x_range:
        return Fruit('coin3x', COIN_3X_IMG, COIN_SPEED, COIN_VALUE, 3, False)
    if box_range:
        return random_fruit_box(score)
    if star_range:
        return Fruit('star', STAR_IMG, STAR_SPEED, STAR_VALUE, 0, False)


def nowe_fruits_actions(fruits, character, fruits_picked_up, fruits_lost):
    for fruit in fruits:
        fruit.get_rect().y += fruit.get_speed()

        if character.get_rect().colliderect(fruit.get_rect()):
            pygame.event.post(pygame.event.Event(FRUIT_PICKED_UP))
            fruits_picked_up.append(fruit)
            fruits.remove(fruit)

        elif fruit.get_rect().y > WINDOW_HEIGHT:
            pygame.event.post(pygame.event.Event(FRUIT_LOST))
            fruits_lost.append(fruit)
            fruits.remove(fruit)

