from coffee.latte import latte
import unittest

class TestBaseConfig(unittest.TestCase):
    class TestBaseConfig(unittest.TestCase):
        def test_base_config_defaults(self) -> None:
            self.assertEqual(latte.make(), "latte")


if __name__ == "__main__":
    unittest.main()