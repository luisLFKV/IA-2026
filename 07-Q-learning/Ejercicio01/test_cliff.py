"""Pruebas sin dependencias extra para el ejercicio 01."""

import unittest
from dataclasses import replace
from pathlib import Path
import random

from qlearn.agent import empty_q, greedy_episode, td_target_q, train
from qlearn.env import load_env


ENV = Path(__file__).parent / "envs" / "cliff.yaml"


class TestCliff(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.env = load_env(ENV)

    def test_dimensions(self):
        self.assertEqual((self.env.rows, self.env.cols), (4, 12))
        self.assertEqual(len(self.env.nonterminal), 37)
        self.assertEqual(self.env.terminals, ("3,11",))

    def test_north_from_start(self):
        tr = self.env.step("3,0", "N")
        self.assertEqual((tr.nxt, tr.reward, tr.done), ("2,0", -1, False))

    def test_east_from_start_resets_without_ending(self):
        tr = self.env.step("3,0", "E")
        self.assertEqual((tr.nxt, tr.reward, tr.done), ("3,0", -100, False))
        Q = empty_q(self.env)
        Q["3,0"]["N"] = 8
        self.assertEqual(td_target_q(self.env, Q, tr.reward, tr.nxt, tr.done), -92)

    def test_goal_ends(self):
        tr = self.env.step("2,11", "S")
        self.assertEqual((tr.nxt, tr.reward, tr.done), ("3,11", -1, True))

    def test_outside_grid_stays(self):
        tr = self.env.step("3,0", "W")
        self.assertEqual((tr.nxt, tr.reward, tr.done), ("3,0", -1, False))

    def test_greedy_policy_is_optimal(self):
        Q, rewards = train(self.env, random.Random(7))
        path, actions, total, reached = greedy_episode(self.env, Q)
        self.assertEqual(len(rewards), 500)
        self.assertTrue(reached)
        self.assertEqual(len(actions), 13)
        self.assertEqual(total, -13)
        self.assertEqual(actions, ["N"] + ["E"] * 11 + ["S"])
        self.assertEqual(path[-1], "3,11")


if __name__ == "__main__":
    unittest.main(verbosity=2)
