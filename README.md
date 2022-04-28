# Gabposter

Posts to a gab account text and image.

# Install

`python -m pip install gabposter`

# Api

```
from gabposter import gab_post

USER = "gabusername"
PASS = "gabpassword"
FILE_JPG = "myfile.jpg"

gab_post(USER, PASS, "test", jpg_path=FILE_JPG)
```

# Tests

Just simply run `tox` at the command line and everything should be tested. You may need to install `tox` with `python -m pip tox`.

# Changes

  * 1.0.3: Fixed a bug where posts would sometimes not go through, due to the browser exiting too quickly.
  * 1.0.0: Initial code submit