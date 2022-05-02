"""
    Handles the creation of the web driver.
"""

import ssl
from pathlib import Path  # type: ignore
from typing import Any, Optional

from autoselenium import Driver  # type: ignore
from selenium.webdriver import ChromeOptions  # type: ignore
from selenium.webdriver import FirefoxOptions

ssl._create_default_https_context = (  # pylint: disable=protected-access
    ssl._create_unverified_context  # pylint: disable=protected-access
)

from webdriver_setup import get_webdriver_for  # type: ignore


def open_webdriver(
    driver_name: str, download_directory: Optional[Path], headless: bool
) -> Driver:
    """Opens the web driver."""
    opts: Any = None
    if download_directory is not None:
        download_directory.mkdir(exist_ok=True, parents=True)
    if headless:
        if driver_name in ["chrome", "brave"]:
            opts = ChromeOptions()
            opts.add_argument("--headless")
            opts.add_argument("--disable-gpu")
            opts.add_argument("--disable-dev-shm-usage")
        elif driver_name == "firefox":
            opts = FirefoxOptions()
            opts.headless = True
        else:
            raise NotImplementedError(
                f"{__file__}: headless mode for {driver_name} is not supported."
            )
    if driver_name == "firefox":
        print(f"{__file__}: Warning: firefox browser has known issues.")
    driver = get_webdriver_for(driver_name, opts)
    # driver = Driver(driver_name, root=download_directory, driver_options=opts)
    return driver
