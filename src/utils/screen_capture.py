#!/usr/bin/env python3
"""
Capture d'écran pour vision du bot
"""

import numpy as np
import logging
from typing import Optional

try:
    import mss
except ImportError:
    print("⚠️  mss not installed. Install: pip install mss")


class ScreenCapture:
    """Capture d'écran du jeu"""

    def __init__(self, width: int = 640, height: int = 480):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.width = width
        self.height = height
        self.sct = mss.mss()
        self.logger.info(f"✅ Capture d'écran initialisée ({width}x{height})")

    def capture(self) -> Optional[np.ndarray]:
        """Capturer l'écran du jeu"""
        try:
            # Capturer l'écran principal
            screenshot = self.sct.grab(self.sct.monitors[1])
            frame = np.array(screenshot)
            # Redimensionner
            frame = self._resize(frame)
            return frame
        except Exception as e:
            self.logger.error(f"Erreur de capture: {e}")
            return None

    def _resize(self, frame: np.ndarray) -> np.ndarray:
        """Redimensionner l'image"""
        try:
            from cv2 import resize, INTER_LINEAR
            return resize(frame, (self.width, self.height), interpolation=INTER_LINEAR)
        except:
            return frame
