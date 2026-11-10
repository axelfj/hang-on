import contextlib
import importlib.util
import io
from pathlib import Path
import unittest
from unittest.mock import patch

path = next(Path(__file__).resolve().parents[1].glob("*.py"))
spec = importlib.util.spec_from_file_location("hang_on", path)
game = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(game)

class GameTests(unittest.TestCase):
    def play(self, answers):
        output = io.StringIO()
        with patch("builtins.input", side_effect=answers), contextlib.redirect_stdout(output):
            game.ahorcado()
        return output.getvalue()

    def test_win_helper(self):
        self.assertTrue(game.haGanado("sol", list("sol")))
        self.assertFalse(game.haGanado("sol", list("s_l")))

    def test_eight_correct_letters_win(self):
        output = self.play(["abcdefgh", *"abcdefgh", "no"])
        self.assertIn("lo has conseguido", output)
        self.assertNotIn("No lo conseguiste", output)

    def test_seven_misses_then_win(self):
        output = self.play(["a", *"bcdefgh", "a", "no"])
        self.assertIn("lo has conseguido", output)

    def test_eight_misses_lose(self):
        output = self.play(["a", *"bcdefghi", "no"])
        self.assertIn("No lo conseguiste", output)

    def test_repeated_letters_not_counted(self):
        output = self.play(["a", *(["b"] * 10), "a", "no"])
        self.assertIn("lo has conseguido", output)

    def test_accented_and_uppercase_input(self):
        output = self.play(["Ú", "Ú", "no"])
        self.assertIn("lo has conseguido", output)

    def test_restart_returns_to_caller(self):
        output = self.play(["a", "a", "si", "b", "b", "no"])
        self.assertEqual(output.count("lo has conseguido"), 2)

if __name__ == "__main__":
    unittest.main()
