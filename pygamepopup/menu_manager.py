"""Minimal MenuManager shim for pygamepopup.menu_manager."""

class MenuManager:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def open_menu(self, *args, **kwargs):
        return None

    def close_menu(self, *args, **kwargs):
        return None
