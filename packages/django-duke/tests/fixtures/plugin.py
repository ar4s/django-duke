from configurations import Configuration
from duke.common import PluginManifest, build_plugin


class PluginConfiguration(Configuration):
    pass


def plugin():
    manifest = PluginManifest(
        name="test-plugin",
        description="Test plugin",
        version="0.1.0",
        views=None,
    )
    return build_plugin(configuration=PluginConfiguration, manifest=manifest)
