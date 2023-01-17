import pygame
from random import shuffle, choice

from paths import SOUND_PATH


class SoundService:
    """
    Cares for all game sounds
    """
    def __init__(self) -> None:
        """
        Loading all paths for sounds, setting volume
        """
        self.menu_music = pygame.mixer.Sound(SOUND_PATH+'menu.wav')

        self.hit_sounds = [pygame.mixer.Sound(SOUND_PATH+f'hit{i}.mp3') for i in range(1, 10)]
        for sound in self.hit_sounds:
            sound.set_volume(1.4)

        self.start_sound = pygame.mixer.Sound(SOUND_PATH+'start.mp3')
        self.start_sound.set_volume(0.3)

        self.death_sound = pygame.mixer.Sound(SOUND_PATH+'death.mp3')

        self.win_sound = pygame.mixer.Sound(SOUND_PATH+'win.mp3')
        self.win_sound.set_volume(0.3)

        self.lose_sound = pygame.mixer.Sound(SOUND_PATH+'lose.mp3')
        self.lose_sound.set_volume(0.3)

        self.shot_sound = pygame.mixer.Sound(SOUND_PATH+'shot.mp3')
        self.shot_sound.set_volume(0.1)

        self.get_sound = pygame.mixer.Sound(SOUND_PATH+'get_item.mp3')
        self.get_sound.set_volume(2.4)

        self.steps_sound = pygame.mixer.Sound(SOUND_PATH+'steps.mp3')
        self.steps_sound.set_volume(2)

        self.game_sound_channel = pygame.mixer.Channel(1)

        self.steps_channel = pygame.mixer.Channel(2)

        self.shot_channel = pygame.mixer.Channel(3)

        self.playlist_sound_game = [SOUND_PATH+'game1.mp3', SOUND_PATH+'game2.mp3', SOUND_PATH+'game3.mp3']
        self.game_songs = [pygame.mixer.Sound(i) for i in self.playlist_sound_game]
        for sound in self.game_songs:
            sound.set_volume(0.1)

    def sound_menu(self) -> None:
        self.game_sound_channel.stop()
        self.game_sound_channel.play(self.menu_music)

    def sound_death(self) -> None:
        self.death_sound.play()

    def get_item_sound(self) -> None:
        self.get_sound.play()

    def sound_win(self) -> None:
        self.game_sound_channel.stop()
        self.game_sound_channel.play(self.win_sound)
        pygame.mixer.music.stop()

    def sound_lose(self) -> None:
        self.game_sound_channel.stop()
        self.game_sound_channel.play(self.lose_sound)
        pygame.mixer.music.stop()

    def sound_start(self) -> None:
        pygame.mixer.music.stop()
        self.start_sound.play()

    def sound_steps(self, moving) -> None:
        if moving:
            if not pygame.mixer.Channel(2).get_busy():
                self.steps_channel.play(self.steps_sound)
        else:
            self.steps_channel.stop()

    def sound_hit(self) -> None:
        choice(self.hit_sounds).play()

    def shot(self) -> None:
        self.shot_channel.stop()
        self.shot_channel.play(self.shot_sound)

    def sound_game(self) -> None:
        self.game_sound_channel.stop()
        playlist = self.playlist_sound_game.copy()
        shuffle(playlist)
        pygame.mixer.music.load(playlist[0])
        playlist.pop(0)
        pygame.mixer.music.play()
        while len(playlist) != 0:
            pygame.mixer.music.queue(playlist[0])
            playlist.pop(0)
        for song in self.playlist_sound_game:
            pygame.mixer.music.queue(song)
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play()

    @staticmethod
    def sound_pause() -> None:
        pygame.mixer.music.pause()

    @staticmethod
    def sound_unpause() -> None:
        pygame.mixer.music.unpause()
