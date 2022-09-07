from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog

from libs.uix.root import Root, ShowLoading

#Window.size = (350, 580)


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title = "Namssn app"

        Window.keyboard_anim_args = {"d": 0.2, "t": "linear"}
        Window.softinput_mode = "below_target"

    def build(self):
        self.root = Root()
        self.root.set_current("home")

    #called by namssn icon of menu page when clicked
    def do_nothing(self):
        pass

    #loading dialog for courses page
    loading_page = None

    def show_loading(self):
        if not self.loading_page:
            self.loading_page = MDDialog(type='custom',
                                         content_cls=ShowLoading())
        self.loading_page.open()

    #function that is called when back-icon button is clicked
    #function changed screen to menu page
    def move_back(self, page):
        if page == 'home':
            self.root.set_current('home', side='right')
            self.root.history = self.root.history[:1]


if __name__ == "__main__":
    MainApp().run()
