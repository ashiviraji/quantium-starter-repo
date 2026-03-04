import os
from pathlib import Path

import pytest
from dash.testing.composite import DashComposite
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def dash_duo(request, dash_thread_server, tmp_path):
    # 1) Download geckodriver and add it to PATH
    gecko_path = GeckoDriverManager().install()
    gecko_dir = str(Path(gecko_path).parent)
    os.environ["PATH"] = gecko_dir + os.pathsep + os.environ.get("PATH", "")

    # 2) Start DashComposite using Firefox (headless)
    with DashComposite(
        server=dash_thread_server,
        browser="firefox",
        headless=True,
        download_path=str(tmp_path / "download"),
        options=request.config.hook.pytest_setup_options(),
        remote=request.config.getoption("remote"),
        remote_url=request.config.getoption("remote_url"),
        percy_assets_root=request.config.getoption("percy_assets"),
        percy_finalize=request.config.getoption("nopercyfinalize"),
        pause=request.config.getoption("pause"),
    ) as dc:
        yield dc