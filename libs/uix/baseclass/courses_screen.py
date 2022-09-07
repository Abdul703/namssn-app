from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.tab import MDTabsBase
from kivy.metrics import dp
from libs.uix.baseclass.datatables import MDDataTable
from libs.uix.database import databases as db
from kivymd.app import MDApp


class Level1Tab(ThemableBehavior, MDBoxLayout, MDTabsBase):
    pass


class Level2Tab(ThemableBehavior, MDBoxLayout, MDTabsBase):
    pass


class Level3Tab(ThemableBehavior, MDBoxLayout, MDTabsBase):
    pass


class CoursesScreen(MDScreen, ThemableBehavior):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.l1 = False
        self.l2 = False
        self.l3 = False

    def on_enter(self):
        if not self.l1:
            self.ids.lv1s1.add_widget(self.tables('1', '1'))
            self.ids.lv1s2.add_widget(self.tables('1', '2'))
            self.l1 = True
        MDApp.get_running_app().loading_page.dismiss()

    #creating tables on a page taking level and semester as parameters
    #for example tables('1', '2'), mean level 1 semester 1
    def tables(self, l, s):
        data_tables = MDDataTable(
            column_data=[
                ("S/No.", dp(10)),
                ("Code", dp(15)),
                ("Course Title", dp(30)),
                ("Unit", dp(10)),
                ("Type", dp(10)),
            ],
            row_data=db.courses_per_level_semester(l, s)
        )
        return data_tables

    #what happen when tab is clicked
    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        MDApp.get_running_app().show_loading()

        #if tab is clicked for the 1st time the tables will be created
        if tab_text == '[b]200 Level[/b]' and not self.l2:
            self.ids.lv2s1.add_widget(self.tables('2', '1'))
            self.ids.lv2s2.add_widget(self.tables('3', '2'))
            self.l2 = True

        elif tab_text == '[b]300 Level[/b]' and not self.l3:
            self.ids.lv3s2.add_widget(self.tables('3', '2'))
            self.l3 = True
        MDApp.get_running_app().loading_page.dismiss()
