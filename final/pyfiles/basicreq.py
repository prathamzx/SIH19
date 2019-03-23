from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

class BasicSearch(BoxLayout,Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    def validate_user(self):
        area=self.ids.area_field


        info=self.ids.info


        areatext=area.text
        print(areatext+"kk")
        if(areatext==""):
            popup = Popup(title='Error!',content=Label(text='Please Enter Location!'),size_hint=(None, None), size=(200, 200))
            popup.open()
        else:
            self.manager.current = "homepage"


        #info.text='Area '+ areatext+" "+ " Price ="+slidervalue
