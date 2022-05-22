from pathlib import Path
import os

HIGH_SCORE_FILE_PATH = Path(os.path.join('Data', 'High Score.txt'))
HIGH_SCORE_FILE_PATH.touch(exist_ok=True)
HIGH_SCORE_FILE = open(HIGH_SCORE_FILE_PATH, 'r+')


def high_score_read():
    high_score = HIGH_SCORE_FILE.read()
    HIGH_SCORE_FILE.seek(0)

    if high_score == '':
        HIGH_SCORE_FILE.write('0')
        HIGH_SCORE_FILE.seek(0)
        high_score = 0

    return high_score


def high_score_file_save(score):
    high_score = high_score_read()

    if score > int(high_score):
        HIGH_SCORE_FILE.write(str(score))
        HIGH_SCORE_FILE.truncate()
        HIGH_SCORE_FILE.seek(0)


def high_score_file_close():
    HIGH_SCORE_FILE.close()


FRUITS_PICKED_FILE_PATH = Path(os.path.join('Data', 'Fruits Picked.txt'))
FRUITS_PICKED_FILE_PATH.touch(exist_ok=True)
FRUITS_PICKED_FILE = open(FRUITS_PICKED_FILE_PATH, 'r+')


def fruits_picked_file_close():
    FRUITS_PICKED_FILE.close()








COINS_FILE_PATH = Path(os.path.join('Data', 'Coins.txt'))
COINS_FILE_PATH.touch(exist_ok=True)
COINS_FILE = open(COINS_FILE_PATH, 'r+')


def coins_file_read():
    coins = COINS_FILE.read()
    COINS_FILE.seek(0)

    if coins == '':
        COINS_FILE.write('0')
        COINS_FILE.seek(0)
        coins = 0

    return coins


def coins_file_save(coins):
    COINS_FILE.write(str(coins))
    COINS_FILE.truncate()
    COINS_FILE.seek(0)


def coins_file_close():
    COINS_FILE.close()


def close_all_files():
    high_score_file_close()
    fruits_picked_file_close()
    coins_file_close()