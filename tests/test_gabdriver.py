"""
    Tests the gab driver.
"""
import os
import unittest

from gabposter import gab_post, gab_test

HERE = os.path.dirname(os.path.abspath(__file__))
TEST_DATA = os.path.join(HERE, "data")
SMALL_IMG = os.path.join(TEST_DATA, "small.jpg")


USER = "testgabposter"
PASS = "Yq4F2H9Lvp"


class GabDriverTest(unittest.TestCase):
    """Gab driver test framework."""

    def test_gab_test(self) -> None:
        """Tests that gab_test works."""
        for driver in ["firefox", "chrome", "brave"]:
            ok, err = gab_test(driver)  # pylint: disable=invalid-name
            self.assertTrue(ok, f"gab_test failed: {err}")

    def test_dryrun_posting(self) -> None:
        """Tests that gab_post works, but doesn't not post."""
        gab_post(USER, PASS, "test", jpg_path=SMALL_IMG, dry_run=True)

    def test_dryrun_posting_with_image(self) -> None:
        """Tests that gab_post works, but doesn't not post."""
        gab_post(USER, PASS, "test", dry_run=True)

    @unittest.skip("Live testing disabled")
    def test_live_posting(self) -> None:
        """Tests that gab_post works"""
        gab_post(USER, PASS, "test", dry_run=False)


if __name__ == "__main__":
    unittest.main()
