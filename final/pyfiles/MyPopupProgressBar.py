from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen,WipeTransition
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.dropdown import DropDown
from kivy.uix.progressbar import ProgressBar
from kivy.properties import ObjectProperty
from kivy.clock import Clock
import sqlite3

conn=sqlite3.connect("db.db")
c=conn.cursor()
use=""
AllLands=list(c.execute("Select * from land"))
Item=[]

class MyPopupProgressBar(Screen,BoxLayout):
    progress_bar = ObjectProperty()

    def __init__(self, **kwa):
        super( MyPopupProgressBar, self).__init__(**kwa)

        self.progress_bar = ProgressBar()
        self.popup = Popup(title='Loading: {}%'.format(int(self.progress_bar.value)),
            content=self.progress_bar)
        self.popup.bind(on_open=self.puopen)
        Clock.schedule_once(self.pop)

    def jinchurki(self, dt):
        self.popup.title='Loading: {}%'.format(int(self.progress_bar.value))


    def pop(self, instance):
        self.progress_bar.value = 1
        self.popup.open()

    def next(self, dt):
        if self.progress_bar.value>=100:
            self.manager.current="login"
            self.popup.dismiss()
            return False
        self.progress_bar.value += 2.5

    def puopen(self, instance):
        Clock.schedule_interval(self.next,1/100)
        Clock.schedule_interval(self.jinchurki,1/100)
