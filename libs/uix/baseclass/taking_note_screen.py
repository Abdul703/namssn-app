from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen
from kivy.factory import Factory
from libs.uix.root import NumberedParagraph


class TakingNoteScreen(ThemableBehavior, MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.first = True
        self.L = [line.strip() for line in open('assets/txt/note_tips.txt') if line.strip() != '']

    def on_enter(self):
        if self.first:
            self.first = False

            for i in range(7):
                self.ids.note_ctn.add_widget(
                    Factory.NumberedParagraph(num=str(i+1), parag=self.L[i]))
