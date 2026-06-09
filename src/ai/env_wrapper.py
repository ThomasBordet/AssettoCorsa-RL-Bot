#!/usr/bin/env python3
"""
Environnement Gym pour Assetto Corsa
"""

import gym
from gym import spaces
import numpy as np
from typing import Tuple, Dict, Any


class AssettoEnv(gym.Env):
    """Environnement Gym pour Assetto Corsa"""

    metadata = {"render.modes": ["human"]}

    def __init__(self, circuit: str = "imola"):
        super().__init__()
        self.circuit = circuit
        self.max_steps = 5000
        self.step_count = 0

        # Espace d'observation: [speed, rpm, steering, throttle, brake, spline_pos, lat_acc, long_acc]
        self.observation_space = spaces.Box(
            low=-np.inf, high=np.inf, shape=(8,), dtype=np.float32
        )

        # Espace d'actions: [throttle, brake, steering, clutch, gear]
        self.action_space = spaces.Box(
            low=np.array([-1, 0, -1, 0, -1]),
            high=np.array([1, 1, 1, 1, 1]),
            dtype=np.float32,
        )

    def reset(self) -> np.ndarray:
        """Réinitialiser l'environnement"""
        self.step_count = 0
        return self._get_observation()

    def step(self, action: np.ndarray) -> Tuple[np.ndarray, float, bool, Dict]:
        """Exécuter une étape"""
        self.step_count += 1

        # Appliquer l'action
        obs = self._get_observation()
        reward = self._compute_reward(obs, action)
        done = self.step_count >= self.max_steps

        info = {"circuit": self.circuit, "step": self.step_count}

        return obs, reward, done, info

    def _get_observation(self) -> np.ndarray:
        """Obtenir l'état actuel"""
        return np.array(
            [
                np.random.uniform(0, 300),  # speed
                np.random.uniform(0, 10000),  # rpm
                np.random.uniform(-1, 1),  # steering
                np.random.uniform(0, 1),  # throttle
                np.random.uniform(0, 1),  # brake
                np.random.uniform(0, 1),  # spline position
                np.random.uniform(-10, 10),  # lat acceleration
                np.random.uniform(-10, 10),  # long acceleration
            ],
            dtype=np.float32,
        )

    def _compute_reward(self, obs: np.ndarray, action: np.ndarray) -> float:
        """Calculer la récompense"""
        speed = obs[0]
        spline_pos = obs[5]
        on_track = 0.2 < spline_pos < 0.8

        # Bonus pour vitesse
        speed_reward = speed / 300.0 * 0.5

        # Pénalité pour être hors piste
        track_penalty = 0 if on_track else -5

        # Pénalité pour accélération brutale
        smoothness_penalty = -0.1 * (abs(action[0]) + abs(action[2]))

        reward = speed_reward + track_penalty + smoothness_penalty

        return reward

    def render(self, mode="human"):
        pass
