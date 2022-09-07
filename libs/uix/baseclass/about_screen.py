from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen


class AboutScreen(ThemableBehavior, MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.first = True

    def on_enter(self):
        if self.first:
            self.first = False
            f = [line.strip() for line in open('assets/txt/appabout.txt')
                 if line.strip() != '']

            self.ids.one.text = f[0]
            self.ids.two.text = f[1]
            self.ids.three.text = f[2]
            self.ids.four.text = f[3]
            self.ids.five.text = f[4]
