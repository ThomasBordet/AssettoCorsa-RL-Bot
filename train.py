#!/usr/bin/env python3
"""
Script d'entraînement du modèle RL
"""

import argparse
import logging
from pathlib import Path

from src.ai.rl_model import RLAgent
from src.utils.logger import setup_logging


def main():
    """Entraîner le modèle"""
    parser = argparse.ArgumentParser(description="Entraîner le modèle RL pour Assetto Corsa")
    parser.add_argument(
        "--circuit", type=str, default="imola", help="Circuit d'entraînement"
    )
    parser.add_argument(
        "--timesteps", type=int, default=1000000, help="Nombre de timesteps"
    )
    parser.add_argument(
        "--algorithm", type=str, default="PPO", help="Algorithme RL (PPO, DQN, A2C)"
    )
    parser.add_argument(
        "--learning-rate", type=float, default=3e-4, help="Learning rate"
    )
    parser.add_argument("--debug", action="store_true", help="Mode debug")

    args = parser.parse_args()

    logger = setup_logging("TrainScript", debug=args.debug)
    logger.info(f"🚀 Début entraînement: {args.circuit} ({args.algorithm})")

    # Créer l'agent
    agent = RLAgent(
        circuit=args.circuit,
        algorithm=args.algorithm,
        learning_rate=args.learning_rate,
    )

    # Entraîner
    agent.train(timesteps=args.timesteps)

    # Sauvegarder
    model_path = f"models/trained_models/{args.algorithm.lower()}_{args.circuit}.zip"
    Path("models/trained_models").mkdir(parents=True, exist_ok=True)
    agent.save(model_path)

    logger.info(f"✅ Entraînement terminé! Modèle: {model_path}")


if __name__ == "__main__":
    main()
