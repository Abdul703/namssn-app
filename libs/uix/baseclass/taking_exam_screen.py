from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen
from kivy.factory import Factory
from libs.uix.root import NumberedParagraph


#class Numbered_Paragraph(MDGridLayout):
#    num = StringProperty()
#    parag = StringProperty()


class TakingExamScreen(ThemableBehavior, MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.first = True
        self.L = [line.strip() for line in open('assets/txt/exam_tips.txt') if line.strip() != '']

    def on_enter(self):
        if self.first:
            self.first = False

            for i in range(9):
                self.ids.taking_exam_ctn.add_widget(
                    Factory.NumberedParagraph(num=str(i+1), parag=self.L[i]))
