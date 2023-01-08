import pygame
from random import randint, shuffle


class SoundService:
    def __init__(self):
        self.menu_music_path = 'assets/sounds/menu.mp3'

        self.start_sound = pygame.mixer.Sound('assets/sounds/start.mp3')
        self.start_sound.set_volume(0.2)

        self.death_sound = pygame.mixer.Sound('assets/sounds/death.mp3')
        self.death_sound.set_volume(0.3)

        self.win_sound = pygame.mixer.Sound('assets/sounds/win.mp3')
        self.win_sound.set_volume(0.1)

        self.steps_sound = pygame.mixer.Sound('assets/sounds/steps.mp3')
        self.steps_sound.set_volume(0.2)
        self.steps_channel = pygame.mixer.Channel(1)

        self.game_songs = ['assets/sounds/game1.mp3', 'assets/sounds/game2.mp3', 'assets/sounds/game3.mp3']

    def sound_menu(self):
        pygame.mixer.music.load(self.menu_music_path)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()

    def sound_death(self):
        self.death_sound.play()

    def sound_win(self):
        self.win_sound.play()

    def sound_start(self):
        pygame.mixer.music.stop()
        self.start_sound.play()

    def sound_steps(self, moving):
        if moving:
            if not pygame.mixer.Channel(1).get_busy():
                self.steps_channel.play(self.steps_sound)
        else:
            self.steps_channel.stop()

    def sound_hit(self):
        self.hit_sound = pygame.mixer.Sound(f'assets/sounds/hit{randint(1, 9)}.mp3')
        self.hit_sound.set_volume(0.3)
        self.hit_sound.play()

    def sound_game(self):
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
    def sound_pause():
        pygame.mixer.music.pause()

    @staticmethod
    def sound_unpause():
        pygame.mixer.music.unpause()
