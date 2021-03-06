# Gabposter

[![Actions Status](https://github.com/zackees/gabposter/workflows/MacOS_Tests/badge.svg)](https://github.com/zackees/gabposter/actions/workflows/test_macos.yml)
[![Actions Status](https://github.com/zackees/gabposter/workflows/Win_Tests/badge.svg)](https://github.com/zackees/gabposter/actions/workflows/test_win.yml)
[![Actions Status](https://github.com/zackees/gabposter/workflows/Ubuntu_Tests/badge.svg)](https://github.com/zackees/gabposter/actions/workflows/test_ubuntu.yml)

Posts to a gab account text and image.

# Install

`python -m pip install gabposter`

# Api

```
from gabposter import gab_post, gab_test

USER = "gabusername"
PASS = "gabpassword"
FILE_JPG = "myfile.jpg"

assert gab_test(), "Webdriver doesn't work on your system"

gab_post(USER, PASS, "test", jpg_path=FILE_JPG)
```

# Tests

Just simply run `tox` at the command line and everything should be tested. You may need to install `tox` with `python -m pip tox`.

# Changes
  * 1.2.8: Adds concurrent open_webdriver 1.3.0
  * 1.2.7: Updates the use of `open-webdriver` to v1.2.9
  * 1.2.3: `open-webdriver` now uses v1.1.7 or greater.
  * 1.2.2: Now uses `open-webdriver` to handle the setup of webdriver.
  * 1.2.1: Now works on windows/linux. Had to switch to `webdriver-setup`. Github platform unit tests now run on every update.
  * 1.2.0: Headless feature now implemented for chrome/brave. Experimental firefox support. Driver can now be selected as chrome/brave/firefox.
  * 1.1.0: Driver now uses chrome by default. Logic improved to work across browsers.
  * 1.0.6: Fix bug where some paths used a different driver directory
  * 1.0.5: Stash downloaded selenium driver in app directory rather than current, to improve app bundling.
  * 1.0.4: Adds gab_test() for testing that connecting to gab works using the webdriver.
  * 1.0.3: Fixed a bug where posts would sometimes not go through, due to the browser exiting too quickly.
  * 1.0.0: Initial code submit
