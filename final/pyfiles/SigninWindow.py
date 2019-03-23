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
import urllib
from kivy.network.urlrequest import UrlRequest



use=""
# AllLands=list(c.execute("Select * from land"))
Item=[]

class SigninWindow(BoxLayout,Screen):
    Email=''
    password=''

    def __init__(self, **kwargs):
       super().__init__(**kwargs)


    def got_json(self,req, result):
        print(result)
        print("yes")

    def validate_user(self):
        self.email = self.ids.username_field.text
        self.pwd = self.ids.pwd_field.text

        str_signup='http://20.0.0.94:4000/login'
        headers = {'Content-type': 'application/x-www-form-urlencoded','Accept': 'text/plain'}
        Json_obj1_SignUp={'email':self.email,'password':self.pwd }
        params = urllib.parse.urlencode(Json_obj1_SignUp)
        req = UrlRequest(str_signup, on_success=self.got_json, req_body=params,req_headers=headers)

    def got_json(self,req, result):
        print(result)
        if result['success']:
            templist=(result['userToken'],result['user']['mobile'],result['user']['name'],result['user']['email'],result['user']['role'])
            conn=sqlite3.connect("signup.db")
            c=conn.cursor()
            conn.execute("INSERT into register values(?,?,?,?,?)",templist)
            conn.commit()
            conn.close()
            if result['user']['role'] == 'admin':
                self.manager.current = 'addland'
            else:
                self.manager.current="BasicSearch"
        else:
            popup = Popup(title='Alert!',content=Label(text=result['message']),size_hint=(None, None), size=(200, 200))
            popup.open()
            print(result['message'])


    def closebutton(self):
        App.get_running_app().stop()
