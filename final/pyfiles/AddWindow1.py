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

class AddWindow(BoxLayout,Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def addland(self):
        name=self.ids.add_land_name.text
        price=self.ids.add_land_price.text
        address=self.ids.add_land_address.text
        area=self.ids.add_land_area.text
        info=self.ids.infoAdd
        if(name=="" or price=="" or address=="" or area==""):
            info.text='[color=#FF0000]Please fill all the details![/color]'
        else:
            info.text='[color=#FF0000]Land Added Succesfully[/color]'
            templist=(name,price,area,address)
            c.execute("insert into land values(?,?,?,?)",templist)

    def closebutton(self):
        conn.commit()
        App.get_running_app().stop()
