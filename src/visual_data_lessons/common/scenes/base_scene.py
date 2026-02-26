import logging
import sys

from manim import Scene, Text, config

from ..config import DEFAULT_FONT

logging.basicConfig(level=logging.INFO)

Text.set_default(font=DEFAULT_FONT)


class BaseScene(Scene):
    portrait_scale: float = 0.6
    default_landscape = True

    def __init__(self, *args, **kwargs):
        self.apply_custom_config()
        super().__init__(*args, **kwargs)

    @classmethod
    def apply_custom_config(cls):
        config.background_color = "#283055"

        if "--portrait" in sys.argv:
            logging.info("📱✨ Portrait mode activated! 9:16 vertical vibes 🚀")
            logging.info("🔧 Resolution set to 1080x1920")
            config.pixel_width = 1080
            config.pixel_height = 1920
            config.frame_width = 9
            config.frame_height = 16
        else:
            logging.info("🌄🎬 Landscape mode activated! 16:9 cinematic mode 🔥")
            logging.info("🔧 Resolution set to 1920x1080")
            config.pixel_width = 1920
            config.pixel_height = 1080
            config.frame_width = 16
            config.frame_height = 9

    def add_safe_sound(self, sound_file, *args, **kwargs):
        """
        Adds a sound to the scene if the sound file exists.
        Logs a warning and skips playing the sound if the file is missing.

        Parameters
        ----------
        sound_file : str or pathlib.Path
            Path to the sound file to add.
        *args : tuple
            Additional positional arguments to pass to `self.add_sound`.
        **kwargs : dict
            Additional keyword arguments to pass to `self.add_sound`.

        Returns
        -------
        None
        """
        try:
            self.add_sound(sound_file, *args, **kwargs)
        except Exception as e:
            logging.warning(f"⚠️ [AUDIO SKIPPED] Could not load sound '{sound_file}': {e}")

    @classmethod
    def get_text_size_factor(cls) -> float:
        """
        Returns a scale factor for text size based on screen orientation.

        Returns
        -------
        float
            A smaller factor (0.6) for portrait mode, or 1 for landscape mode.
        """
        from manim import config

        return cls.portrait_scale if config.pixel_height > config.pixel_width else 1
