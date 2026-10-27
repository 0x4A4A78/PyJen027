import subprocess
import sys
import unittest
from decimal import Decimal
from calculator import add


class CalculatorTests(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative(self):
        self.assertEqual(add(-4, 3), -1)

    def test_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_decimals(self):
        self.assertEqual(add("0.1", "0.2"), Decimal("0.3"))

    def test_cli(self):
        run = subprocess.run([sys.executable, "calculator.py", "2", "3"], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0)
        self.assertIn("2 + 3 = 5", run.stdout)

    def test_invalid(self):
        run = subprocess.run([sys.executable, "calculator.py", "abc", "3"], capture_output=True)
        self.assertNotEqual(run.returncode, 0)


if __name__ == "__main__":
    unittest.main()
