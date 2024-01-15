import os
from importlib.metadata import EntryPoint

import configurations
import pytest


@pytest.fixture(autouse=True, scope="session")
def setup_configurations():
    os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"
    os.environ["DJANGO_CONFIGURATION"] = "Base"
    configurations.setup()


@pytest.fixture
def valid_plugin_entry_point():
    return EntryPoint(name="plugin", value="tests.fixtures.plugin:plugin", group="duke")


@pytest.fixture
def invalid_plugin_entry_point():
    return EntryPoint(
        name="plugin", value="tests.fixtures.plugin:invalid_plugin", group="duke"
    )
