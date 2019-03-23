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

class FilterPage(BoxLayout,Screen):
    def filtersearchbutton(self):
        global AllLands
        price=int(self.ids.slider_id.value)-1+48 #48 is added due to ascii value of 0
        area=str(self.ids.area_filter.text)
        address="%"+str(self.ids.address_filter.text)+"%"
        AllLands=list(c.execute(''' SELECT * FROM land where Address like ? and Price<=? and Area=? ''',(address,price,area)))
        if(len(AllLands)==0):
            AllLands=list(c.execute(''' SELECT * FROM land '''))
            popup = Popup(title='Oops!',content=Label(text='No Such Lands!'),size_hint=(None, None), size=(200, 200))
            popup.open()
        else:
            self.ids.area_filter.text=""
            self.ids.address_filter.text=""
            self.ids.slider_id.value=1
            popup = Popup(title='Oops!',content=Label(text='Lands are filtered!! \n Click on show lands!!'),size_hint=(None, None), size=(200, 200))
            popup.open()
            AllLands=list(c.execute(''' SELECT * FROM land where Address like ? and Price<=? and Area=? ''',(address,price,area)))
            self.manager.current="homepage"



    def showland(self):
        self.manager.current="homepage"

    def nextland(self):
        popup = Popup(title='Oops!',content=Label(text='Go to main page first!'),size_hint=(None, None), size=(200, 200))
        popup.open()

    def prevland(self):
        popup = Popup(title='Oops!',content=Label(text='Go to main page first!'),size_hint=(None, None), size=(200, 200))
        popup.open()

    def gotofilter(self):
        popup = Popup(title='Oops!',content=Label(text='Already on Filter!'),size_hint=(None, None), size=(200, 200))
        popup.open()

    def clearbutton(self):
        self.manager.current="homepage"

    def logout(self):
        self.manager.current="login"
        self.cur=-1

    def closebutton(self):
        conn.commit()
        App.get_running_app().stop()