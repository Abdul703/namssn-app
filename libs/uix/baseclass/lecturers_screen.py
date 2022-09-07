from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, ListProperty
from libs.uix.database import databases as db
from kivy.uix.recycleview import RecycleView
from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout


class LecturerContainer(MDBoxLayout):
    '''frame for picture and information of lecturers'''
    name = StringProperty()
    source = StringProperty()
    rank = StringProperty()
    phone = StringProperty()


class RV1(RecycleView):
    '''scroll part of the page'''
    rv_data_list = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #fetching info from database and putting them in screen
        self.l = db.all_lecturers()
        self.rv_data_list = [{
            "source": "assets/images/lecturers/"+item[0]+".jpg",
            "name": item[1],
            "rank": item[2],
            "phone": "Phone No.: "+item[3],
            'w_size': (dp(290), dp(400))}
            for item in self.l]


class LecturersScreen(MDScreen, ThemableBehavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
