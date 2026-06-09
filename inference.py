#!/usr/bin/env python3
"""
Script d'inférence - Lancer le bot en mode autonome
"""

import argparse
from pathlib import Path

from src.main import AssettoBot
from src.utils.logger import setup_logging


def main():
    """Lancer le bot en mode autonome"""
    parser = argparse.ArgumentParser(description="Lancer le bot IA autonome")
    parser.add_argument(
        "--model",
        type=str,
        required=True,
        help="Chemin du modèle pré-entraîné",
    )
    parser.add_argument(
        "--circuit", type=str, default="imola", help="Circuit à utiliser"
    )
    parser.add_argument(
        "--episodes", type=int, default=10, help="Nombre de tours"
    )
    parser.add_argument("--debug", action="store_true", help="Mode debug")

    args = parser.parse_args()

    logger = setup_logging("InferenceScript", debug=args.debug)
    logger.info(f"🏁 Lancement du bot: {args.circuit}")

    # Vérifier que le modèle existe
    if not Path(args.model).exists():
        logger.error(f"❌ Modèle non trouvé: {args.model}")
        return

    # Créer et lancer le bot
    bot = AssettoBot(
        circuit=args.circuit,
        model_path=args.model,
        debug=args.debug,
    )

    bot.run_inference(max_episodes=args.episodes)


if __name__ == "__main__":
    main()
