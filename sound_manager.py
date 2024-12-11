import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.music_playlist = [
            "GameAudio/iflooks.mp3",  # Correct file paths as needed
            "GameAudio/location.mp3"
        ]
        self.current_track_index = 0
        self.is_music_playing = False

    def play_current_track(self):
        if not self.is_music_playing:
            pygame.mixer.music.load(self.music_playlist[self.current_track_index])
            pygame.mixer.music.play(-1)
            self.is_music_playing = True

    def check_music(self):
        if not pygame.mixer.music.get_busy():
            self.next_track()

    def next_track(self):
        self.current_track_index = (self.current_track_index + 1) % len(self.music_playlist)
        pygame.mixer.music.load(self.music_playlist[self.current_track_index])
        pygame.mixer.music.play(-1)

    def toggle_music(self):
        if self.is_music_playing:
            pygame.mixer.music.pause()
            self.is_music_playing = False
        else:
            pygame.mixer.music.unpause()
            self.is_music_playing = True