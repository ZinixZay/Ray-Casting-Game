import pygame
from random import shuffle, choice

from paths import SOUND_PATH


class SoundService:
    def __init__(self) -> None:
        self.menu_music_path = SOUND_PATH+'menu.wav'

        self.hit_sounds = [pygame.mixer.Sound(SOUND_PATH+f'hit{i}.mp3') for i in range(1, 10)]
        for sound in self.hit_sounds:
            sound.set_volume(0.3)

        self.start_sound = pygame.mixer.Sound(SOUND_PATH+'start.mp3')
        self.start_sound.set_volume(0.2)

        self.death_sound = pygame.mixer.Sound(SOUND_PATH+'death.mp3')
        self.death_sound.set_volume(0.3)

        self.win_sound = pygame.mixer.Sound(SOUND_PATH+'win.mp3')
        self.win_sound.set_volume(0.1)

        self.lose_sound = pygame.mixer.Sound(SOUND_PATH+'lose.mp3')
        self.lose_sound.set_volume(0.9)

        self.shot_sound = pygame.mixer.Sound(SOUND_PATH+'shot.mp3')
        self.shot_sound.set_volume(0.2)

        self.steps_sound = pygame.mixer.Sound(SOUND_PATH+'steps.mp3')
        self.steps_sound.set_volume(0.2)
        self.steps_channel = pygame.mixer.Channel(1)

        self.game_songs = [SOUND_PATH+'game1.mp3', SOUND_PATH+'game2.mp3', SOUND_PATH+'game3.mp3']

    def sound_menu(self) -> None:
        pygame.mixer.music.load(self.menu_music_path)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()

    def sound_death(self) -> None:
        self.death_sound.play()

    def sound_win(self) -> None:
        pygame.mixer.music.stop()
        self.win_sound.play()

    def sound_lose(self) -> None:
        pygame.mixer.music.stop()
        self.lose_sound.play()

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
        playlist = self.game_songs.copy()
        shuffle(playlist)
        pygame.mixer.music.load(playlist[0])
        playlist.pop(0)
        pygame.mixer.music.play()
        while len(playlist) != 0:
            pygame.mixer.music.queue(playlist[0])
            playlist.pop(0)
        for song in self.game_songs:
            pygame.mixer.music.queue(song)
            pygame.mixer.music.set_volume(0.02)
            pygame.mixer.music.play()

    @staticmethod
    def sound_pause() -> None:
        pygame.mixer.music.pause()

    @staticmethod
    def sound_unpause() -> None:
        pygame.mixer.music.unpause()
