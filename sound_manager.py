class SoundManager:
    def __init__(self):
        self.background_music = None
        self.sound_effects = {
            "steal_points": "steal.mp3",
            "speed_boost": "boost.mp3"
        }
        self.is_muted = False

    def play_background_music(self):
        pass

    def stop_background_music(self):
        pass

    def play_sound_effect(self, action):
        pass

    def mute(self):
        pass