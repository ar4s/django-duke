from dataclasses import dataclass
from typing import List, Optional, Type, Union

import pkg_resources
from configurations import Configuration
from django.urls import URLPattern
from django.urls.resolvers import URLResolver


@dataclass
class PluginManifest:
    name: str
    description: str
    version: str
    urls: Optional[List[Union[URLPattern, URLResolver]]] = None


@dataclass
class Plugin:
    configuration: Type[Configuration]
    manifest: PluginManifest


def build_plugin_manifest_from_package(
    *, name, description, urls: Optional[List[Union[URLPattern, URLResolver]]] = None
):
    pkg = pkg_resources.get_distribution(name)
    return PluginManifest(name, description, pkg.version, urls)


def build_plugin(*, configuration: Type[Configuration], manifest: PluginManifest):
    return Plugin(configuration, manifest)
