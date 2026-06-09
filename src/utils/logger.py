#!/usr/bin/env python3
"""
Configuration du logging
"""

import logging
import sys
from pathlib import Path


def setup_logging(name: str, debug: bool = False, log_file: str = "logs/app.log"):
    """Configurer le logging"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG if debug else logging.INFO)

    # Créer le répertoire logs s'il n'existe pas
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    # Format de log
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)-8s [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Handler console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG if debug else logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Handler fichier
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
