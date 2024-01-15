from importlib.metadata import EntryPoint

from duke.get_plugins import get_plugins


def test_get_plugins(
    valid_plugin_entry_point: EntryPoint, invalid_plugin_entry_point: EntryPoint
):
    assert (
        len(
            get_plugins(
                entry_points=[valid_plugin_entry_point, invalid_plugin_entry_point]
            )
        )
        == 1
    )
