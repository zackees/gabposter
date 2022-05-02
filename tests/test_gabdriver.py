"""
    Tests the gab driver.
"""
import os
import sys
import unittest

from gabposter import gab_post, gab_test

HERE = os.path.dirname(os.path.abspath(__file__))
TEST_DATA = os.path.join(HERE, "data")
SMALL_IMG = os.path.join(TEST_DATA, "small.jpg")


USER = "testgabposter"
PASS = "Yq4F2H9Lvp"

FULL_TESTS = False
LIVE_TESTING_ENABLED = False  # Warning, will post to gab.com.

if FULL_TESTS:
    all_drivers = ["chrome", "firefox", "brave"]
else:
    all_drivers = ["chrome"]


class GabDriverTest(unittest.TestCase):
    """Gab driver test framework."""

    def test_gab_test(self) -> None:
        """Tests that gab_test works."""
        for driver in all_drivers:
            ok, err = gab_test(driver, headless=False)  # pylint: disable=invalid-name
            self.assertTrue(ok, f"gab_test failed: {err}")

    def test_gab_test_headless(self) -> None:
        """Tests that gab_test works."""
        for driver in all_drivers:
            ok, err = gab_test(driver, headless=True)  # pylint: disable=invalid-name
            self.assertTrue(ok, f"gab_test failed: {err}")

    @unittest.skipIf(sys.platform == "linux", "pyjpgclipboard doesn't work on linux")
    def test_dryrun_posting(self) -> None:
        """Tests that gab_post works, but doesn't not post."""
        for driver in all_drivers:
            gab_post(USER, PASS, "test", driver_name=driver, jpg_path=SMALL_IMG, dry_run=True)

    @unittest.skipIf(sys.platform == "linux", "pyjpgclipboard doesn't work on linux")
    def test_dryrun_posting_headless(self) -> None:
        """Tests that gab_post works, but doesn't not post."""
        for driver in all_drivers:
            gab_post(USER, PASS, "test", driver_name=driver, jpg_path=SMALL_IMG, dry_run=True)

    def test_dryrun_posting_with_image(self) -> None:
        """Tests that gab_post works, but doesn't not post."""
        for driver in all_drivers:
            gab_post(USER, PASS, "test", driver_name=driver, dry_run=True)

    @unittest.skipUnless(LIVE_TESTING_ENABLED, "Live testing disabled")
    def test_live_posting(self) -> None:
        """Tests that gab_post works"""
        for driver in all_drivers:
            gab_post(USER, PASS, "new test", driver_name=driver, headless=True, dry_run=False)


if __name__ == "__main__":
    unittest.main()
