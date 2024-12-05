import os
import pygame


class SoundManager:
    """
    Manages background music and sound effects for the game.
    """

    def __init__(self):
        """
        Initializes the SoundManager with default settings and sound file paths.
        """
        pygame.mixer.init()

        # Define paths to sound files using os.path.join for cross-platform compatibility
        self.audio_folder = "audio"
        self.background_music = None  # Path to the current background music file
        self.sound_effects = {
            "steal_points": os.path.join(self.audio_folder, "steal.mp3"),
            "speed_boost": os.path.join(self.audio_folder, "boost.mp3"),
            "outfit_change": os.path.join(self.audio_folder, "outfit.mp3"),
        }
        self.is_muted = False

    def play_background_music(self, music_file, loop=True):
        """
        Plays or loops the specified background music.

        :param music_file: Path to the music file to play.
        :param loop: Whether to loop the music indefinitely.
        """
        if self.is_muted:
            print("Sound is muted. Background music not playing.")
            return
        self.background_music = os.path.join(self.audio_folder, music_file)
        pygame.mixer.music.load(self.background_music)
        pygame.mixer.music.play(-1 if loop else 0)
        print(f"Playing background music: {self.background_music}")

    def stop_background_music(self):
        """
        Stops the background music.
        """
        pygame.mixer.music.stop()
        print("Background music stopped.")

    def play_sound_effect(self, action):
        """
        Plays the sound effect associated with a specific action.

        :param action: The action triggering the sound effect (e.g., "steal_points").
        """
        if self.is_muted:
            print("Sound is muted. No sound effect played.")
            return
        if action in self.sound_effects:
            sound = pygame.mixer.Sound(self.sound_effects[action])
            sound.play()
            print(f"Playing sound effect for action: {action}")
        else:
            print(f"No sound effect found for action: {action}")

    def mute(self):
        """
        Toggles the mute state for all sounds.
        """
        self.is_muted = not self.is_muted
        pygame.mixer.music.set_volume(0 if self.is_muted else 1)
        print("Sound is now muted." if self.is_muted else "Sound is now unmuted.")

    def update_music(self, new_track, loop=True):
        """
        Updates the background music to a new track.

        :param new_track: Path to the new music file.
        :param loop: Whether to loop the new music.
        """
        self.stop_background_music()
        self.play_background_music(new_track, loop)
        print(f"Background music updated to: {new_track}")