from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen
from kivy.uix.image import Image
from kivy.clock import Clock


class HomeScreen(ThemableBehavior, MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.first = True

    def on_enter(self):
        if self.first:
            self.first = False
            self.add_carousel_images()
            Clock.schedule_interval(self.callback_clock, 8)

    def callback_clock(self, dt):
        '''change the images of the menu screen'''
        self.ids.img_carousel.load_next()

    def add_carousel_images(self):
        '''adding sliding images in menu screen'''
        for i in range(1, 6):
            self.ids.img_carousel.add_widget(
                Image(source='assets/images/sliders/slide_'+str(i)+'.png',
                      pos_hint={'center_x': .5}
                      )
                )
