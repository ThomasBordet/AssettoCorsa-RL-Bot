#!/usr/bin/env python3
"""
Configuration du logging
"""

import logging
import sys
from pathlib import Path

def setup_logging(name: str = "app", debug: bool = False, log_file: str = "logs/app.log"):
    """Configurer le logging"""
    # Créer le répertoire logs
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG if debug else logging.INFO)
    
    # Format de log
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)-8s [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    # Handler console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # Handler fichier
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger
