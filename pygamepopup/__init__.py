"""Lightweight shim for the external `pygame-popup` package.

This module provides minimal, safe no-op implementations of the
features used by the game so the import can be resolved by linters
and the game can run even when the real package isn't installed.

It is intentionally small and permissive — it will not reproduce the
full behavior of the upstream package.
"""
from types import SimpleNamespace

__all__ = ["init", "configuration", "components", "menu_manager"]


def init():
    """Initialize the popup subsystem (no-op shim)."""
    return None


class _Configuration:
    def set_info_box_title_font(self, *args, **kwargs):
        pass

    def set_info_box_background(self, *args, **kwargs):
        pass

    def set_button_title_font(self, *args, **kwargs):
        pass

    def set_dynamic_button_title_font(self, *args, **kwargs):
        pass

    def set_button_background(self, *args, **kwargs):
        pass

    def set_text_element_font(self, *args, **kwargs):
        pass

    def set_close_button_text(self, *args, **kwargs):
        pass


configuration = _Configuration()

# Provide lightweight submodules as SimpleNamespace objects so
# `from pygamepopup.components import Button` style imports resolve.
components = SimpleNamespace()
menu_manager = SimpleNamespace()

from . import components as components  # re-export package object
from . import menu_manager as menu_manager
