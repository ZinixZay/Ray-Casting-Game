import pygame
from random import shuffle, choice

from paths import SOUND_PATH


class SoundService:
    def __init__(self) -> None:
        self.menu_music = pygame.mixer.Sound(SOUND_PATH+'menu.wav')

        self.hit_sounds = [pygame.mixer.Sound(SOUND_PATH+f'hit{i}.mp3') for i in range(1, 10)]

        self.start_sound = pygame.mixer.Sound(SOUND_PATH+'start.mp3')

        self.death_sound = pygame.mixer.Sound(SOUND_PATH+'death.mp3')

        self.win_sound = pygame.mixer.Sound(SOUND_PATH+'win.mp3')

        self.lose_sound = pygame.mixer.Sound(SOUND_PATH+'lose.mp3')

        self.shot_sound = pygame.mixer.Sound(SOUND_PATH+'shot.mp3')

        self.steps_sound = pygame.mixer.Sound(SOUND_PATH+'steps.mp3')
        self.game_sound_channel = pygame.mixer.Channel(1)
        self.steps_channel = pygame.mixer.Channel(2)
        self.shot_channel = pygame.mixer.Channel(3)

        playlist_sound_game = [SOUND_PATH+'game1.mp3', SOUND_PATH+'game2.mp3', SOUND_PATH+'game3.mp3']
        self.game_songs = [pygame.mixer.Sound(i) for i in playlist_sound_game]

    def sound_menu(self) -> None:
        self.game_sound_channel.stop()
        self.game_sound_channel.play(self.menu_music)

    def sound_death(self) -> None:
        self.death_sound.play()

    def sound_win(self) -> None:
        self.game_sound_channel.stop()
        self.game_sound_channel.play(self.win_sound)

    def sound_lose(self) -> None:
        self.game_sound_channel.stop()
        self.game_sound_channel.play(self.lose_sound)

    def sound_start(self) -> None:
        pygame.mixer.music.stop()
        self.start_sound.play()

    def sound_steps(self, moving) -> None:
        if moving:
            if not pygame.mixer.Channel(1).get_busy():
                self.steps_channel.play(self.steps_sound)
        else:
            self.steps_channel.stop()

    def sound_hit(self) -> None:
        choice(self.hit_sounds).play()

    def shot(self) -> None:
        self.shot_sound.play()

    def sound_game(self) -> None:
        self.game_sound_channel.stop()
        for i in range(6):
            self.game_sound_channel.play(choice(self.game_songs))

    @staticmethod
    def sound_pause() -> None:
        pygame.mixer.music.pause()

    @staticmethod
    def sound_unpause() -> None:
        pygame.mixer.music.unpause()
