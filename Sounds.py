import pygame
import os
from pathlib import Path
from pygame import mixer


pygame.mixer.init()
mixer.music.load(os.path.join('Music', 'Background_music.wav'))
mixer.music.set_volume(0.03)
mixer.music.play(-1)

PICK_UP_SOUND = mixer.Sound(os.path.join('Music', 'Pick_up_fruit_sound.mp3'))
mixer.Sound.set_volume(PICK_UP_SOUND, 0.2)

MENU_CLICK_SOUND = mixer.Sound(os.path.join('Music', 'Menu Selection Click.wav'))
mixer.Sound.set_volume(MENU_CLICK_SOUND, 0.25)

PAGE_TURN_SOUND = mixer.Sound(os.path.join('Music', 'Page Turn.wav'))
mixer.Sound.set_volume(PAGE_TURN_SOUND, 0.1)


def play_sound_effect(sound_effect):
    mixer.Sound.play(sound_effect)


def turn_on_off_music(music, start=False):
    if start:   # Opcja uzywana przy wlaczeniu gry
        if music:
            mixer.music.set_volume(0.03)
        if not music:
            mixer.music.set_volume(0)
        return music

    if music:
        mixer.music.set_volume(0)
        return not music

    if not music:
        mixer.music.set_volume(0.03)
        return not music


def turn_on_off_sounds(sounds, start=False):
    if start:   # Opcja uzywana przy wlaczeniu gry
        if sounds:
            mixer.Sound.set_volume(PICK_UP_SOUND, 0.2)
            mixer.Sound.set_volume(MENU_CLICK_SOUND, 0.25)
            mixer.Sound.set_volume(PAGE_TURN_SOUND, 0.1)
        if not sounds:
            mixer.Sound.set_volume(PICK_UP_SOUND, 0)
            mixer.Sound.set_volume(MENU_CLICK_SOUND, 0)
            mixer.Sound.set_volume(PAGE_TURN_SOUND, 0)
        return sounds

    if sounds:
        mixer.Sound.set_volume(PICK_UP_SOUND, 0)
        mixer.Sound.set_volume(MENU_CLICK_SOUND, 0)
        mixer.Sound.set_volume(PAGE_TURN_SOUND, 0)
        return not sounds

    if not sounds:
        mixer.Sound.set_volume(PICK_UP_SOUND, 0.2)
        mixer.Sound.set_volume(MENU_CLICK_SOUND, 0.25)
        mixer.Sound.set_volume(PAGE_TURN_SOUND, 0.1)
        return not sounds


def startup_music_sound(options_dict):
    options_dict['music'] = turn_on_off_music(options_dict['music'], True)
    options_dict['sound'] = turn_on_off_sounds(options_dict['sound'], True)

