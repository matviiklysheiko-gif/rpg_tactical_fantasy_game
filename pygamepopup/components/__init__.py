"""Shim components for pygamepopup used by the game.

Provides lightweight, forgiving classes for import-time resolution and
basic runtime no-op behavior.
"""
from typing import Any

__all__ = [
    "BoxElement",
    "Button",
    "DynamicButton",
    "InfoBox",
    "TextElement",
]


class BoxElement:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def draw(self, surface: Any):
        pass


class Button:
    def __init__(self, title: str = "", callback=None, *args, **kwargs):
        self.title = title
        self.callback = callback

    def set_title(self, title: str):
        self.title = title

    def click(self):
        if callable(self.callback):
            try:
                self.callback()
            except Exception:
                pass


class DynamicButton(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class InfoBox:
    def __init__(self, *args, **kwargs):
        self.visible = False
        self.args = args
        self.kwargs = kwargs

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False


class TextElement:
    def __init__(self, text: str = "", *args, **kwargs):
        self.text = text

    def set_text(self, text: str):
        self.text = text
