import pygame
import os

class SoundManager:
    def __init__(self):
        pygame.mixer.init()

        # Background music playlist
        self.music_playlist = [
            "audio/iflooks.mp3",
            "audio/location.mp3"
        ]
        self.current_track_index = 0

        # Preload sound effects with new sound files
        self.coin_collect_sound = self.load_sound("audio/coinsound.mp3")
        self.game_over_sound = self.load_sound("audio/gameoversound.mp3")

    def load_sound(self, file_path):
        """Load a sound effect."""
        try:
            if os.path.exists(file_path):
                return pygame.mixer.Sound(file_path)
            else:
                print(f"Sound file not found: {file_path}")
                return None
        except Exception as e:
            print(f"Error loading sound {file_path}: {e}")
            return None

    def play_music(self):
        """Play the current track in the music playlist."""
        try:
            track = self.music_playlist[self.current_track_index]
            if os.path.exists(track):
                pygame.mixer.music.load(track)
                pygame.mixer.music.play(-1)  # Loop indefinitely
            else:
                print(f"Music file not found: {track}")
        except Exception as e:
            print(f"Error playing music track: {e}")

    def next_music(self):
        """Switch to the next track in the playlist."""
        self.current_track_index = (self.current_track_index + 1) % len(self.music_playlist)
        self.play_music()

    def play_coin_collect(self):
        """Play the coin collection sound effect."""
        if self.coin_collect_sound:
            self.coin_collect_sound.play()
        else:
            print("Coin sound is not available.")

    def play_game_over(self):
        """Play the game over sound effect."""
        if self.game_over_sound:
            self.game_over_sound.play()
        else:
            print("Game over sound is not available.")
