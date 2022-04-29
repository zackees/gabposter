"""
    Tests the gab driver.
"""
import unittest

from gabposter.app_dir import app_dir


class AppDir(unittest.TestCase):
    """Gab driver test framework."""

    def test_app_dir(self) -> None:
        """Tests that gab_test works."""
        the_app_dir = app_dir()
        self.assertTrue(the_app_dir.exists())
        print(f"Found app directory at {the_app_dir}")



if __name__ == "__main__":
    unittest.main()
