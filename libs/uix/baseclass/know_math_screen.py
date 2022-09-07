from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen
from kivy.factory import Factory


class Know_mathScreen(MDScreen, ThemableBehavior):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.first = True
        self.L = [line.strip() for line in open('assets/txt/know_maths.txt') if line.strip() != '']
        self.L[1] = self.L[1]+'\n'+self.L.pop(2)
        self.L[4] = self.L[4]+'\n'+self.L.pop(5)
        self.L[7] = self.L[7]+'\n'+self.L.pop(8)

    def on_enter(self):
        if self.first:
            self.first = False

            for line in self.L:
                self.ids.study_ctn.add_widget(Factory.Paragraph(text=line))
