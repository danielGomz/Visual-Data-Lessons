# config.py

from pathlib import Path

import manimpango
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

PROJ_ROOT = Path(__file__).resolve().parents[1]
logger.info(f"PROJ_ROOT path is: {PROJ_ROOT}")

ASSETS_DIR = PROJ_ROOT / "assets"
FONTS_DIR = ASSETS_DIR / "fonts"
IMAGES_DIR = ASSETS_DIR / "images"
SOUNDS_DIR = ASSETS_DIR / "sounds"
FIRA_CODE_MONO = FONTS_DIR / "FiraCode" / "FiraCodeNerdFontMono-Regular.ttf"

manimpango.register_font(str(FIRA_CODE_MONO))

DEFAULT_FONT = "FiraCode Nerd Font Mono"
DEFAULT_BACKGROUND_COLOR = "#283055"
