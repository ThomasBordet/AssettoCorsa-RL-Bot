#!/usr/bin/env python3
"""
Détection automatique du circuit
"""

import json
from pathlib import Path
from typing import Optional, Dict, Any


class CircuitDetector:
    """Détecteur de circuit"""

    CIRCUITS_DIR = Path("config/circuits")

    @staticmethod
    def get_available_circuits() -> list:
        """Lister tous les circuits disponibles"""
        circuits = []
        for file in CircuitDetector.CIRCUITS_DIR.glob("*.json"):
            circuits.append(file.stem)
        return circuits

    @staticmethod
    def load_circuit_config(circuit_name: str) -> Optional[Dict[str, Any]]:
        """Charger la configuration d'un circuit"""
        config_file = CircuitDetector.CIRCUITS_DIR / f"{circuit_name}.json"
        if config_file.exists():
            with open(config_file, "r") as f:
                return json.load(f)
        return None

    @staticmethod
    def detect_current_circuit() -> Optional[str]:
        """Détecter le circuit actuel en jeu (via télémétrie)"""
        # À implémenter: connexion à Assetto Corsa pour obtenir le circuit
        pass
