"""ImageButton shim for pygamepopup.components.image_button."""

class ImageButton:
    def __init__(self, image_path: str = "", callback=None, *args, **kwargs):
        self.image_path = image_path
        self.callback = callback

    def click(self):
        if callable(self.callback):
            try:
                self.callback()
            except Exception:
                pass
