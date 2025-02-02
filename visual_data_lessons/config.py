# config.py

from pathlib import Path

import manimpango
from dotenv import load_dotenv
from loguru import logger
from manim import DARK_BLUE

load_dotenv()

PROJ_ROOT = Path(__file__).resolve().parents[1]
logger.info(f"PROJ_ROOT path is: {PROJ_ROOT}")

ASSETS_DIR = PROJ_ROOT / "assets"
FONTS_DIR = ASSETS_DIR / "fonts"
IMAGES_DIR = ASSETS_DIR / "images"
SOUNDS_DIR = ASSETS_DIR / "sounds"

# Registrar las fuentes necesarias
FIRA_CODE_MONO = FONTS_DIR / "FiraCode" / "FiraCodeNerdFontMono-Regular.ttf"
manimpango.register_font(str(FIRA_CODE_MONO))  # Registrar la fuente FiraCode Nerd Font Mono

# Fuente por defecto para Manim
DEFAULT_FONT = "FiraCode Nerd Font Mono"  # Usamos el nombre de la fuente registrada


VIDEO_FORMAT = "mp4"  # Formato de salida de video
RESOLUTION = (1920, 1080)  # Resolución del video final
FRAME_RATE = 30  # Frames por segundo para la animación


# Configuración de la cámara
CAMERA_CONFIG = {
    "background_color": DARK_BLUE,
    "frame_height": 9,
    "frame_width": 16,
    "pixel_height": 1000,
    "pixel_width": 1500,
}

# Configuración de las animaciones
ANIMATION_DURATION = 2  # Duración estándar de las animaciones
FADE_IN_DURATION = 1.5  # Duración de las animaciones de fade-in
FADE_OUT_DURATION = 1.5  # Duración de las animaciones de fade-out


SHOW_FPS = False  # Mostrar los FPS en pantalla
SHOW_END_TEXT = True  # Mostrar el texto de fin

DEBUG_MODE = False  # Activa el modo debug para ver detalles adicionales de las animaciones
