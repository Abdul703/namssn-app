from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen


class CombinationScreen(MDScreen, ThemableBehavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
