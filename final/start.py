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
from kivy.properties import ObjectProperty,StringProperty
from kivy.clock import Clock
import sqlite3
from pyfiles.basicreq import BasicSearch
from  pyfiles.AddWindow import AddWindow
from  pyfiles.BookmarkScreen import BookmarkScreen
from  pyfiles.Auction import Auction
from  pyfiles.FilterPage import FilterPage
from  pyfiles.HomePage import HomePage
from  pyfiles.MyPopupProgressBar import MyPopupProgressBar
from  pyfiles.RegisterWindow import RegisterWindow
from  pyfiles.SigninWindow import SigninWindow
from  pyfiles.ConnectingSigninRegister import ConnectingSigninRegister
# from AddLand import AddLand
from kivy.garden.mapview import MapView,MapMarker
from kivy.uix.widget import Widget
from kivy.base import runTouchApp
from kivy.uix.relativelayout import RelativeLayout
from kivy.garden.mapview import MapSource,MapMarkerPopup,MapView


use=""
# AllLands=list(c.execute("Select * from land"))
# Item=[]


kv=Builder.load_file("views/my1.kv")
kv1=Builder.load_file("views/myabc.kv")
adminKv=Builder.load_file("views/adminNew.kv")

class ggg(RelativeLayout):
    def get(self):
        x=self.ids.latitude.text4
        print(x)
        print(self.ids.longitude.text)
class SigninApp(App):
    def build(self):
        conn=sqlite3.connect("signup.db")
        c=conn.cursor()
        user =(list(c.execute("Select * from register")))
        conn.commit()
        c.close()
        if(len(user)) and user[0][4] == "admin":
    		#print("admin")
    	    return adminKv
        elif len(user):
            return kv1
        else:
    	    return kv

obj=SigninApp()
obj.run()
