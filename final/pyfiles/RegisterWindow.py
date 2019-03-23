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

conn=sqlite3.connect("db.db")
c=conn.cursor()

use=""
AllLands=list(c.execute("Select * from land"))
Item=[]

class RegisterWindow(BoxLayout,Screen):
    namme = ''
    email = ''
    user =''
    password = ''
    mobile = ''
    dob = ''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def completeregister(self):
    	self.namme = self.ids.name_register.text
    	self.email = self.ids.email_register.text
    	# self.dob = self.ids.dob.text
    	self.password = self.ids.password_register.text
    	self.role = self.ids.role.text
    	self.mobile = self.ids.mobile.text
    	str_signup='http://20.0.0.94:4000/signup'
    	headers = {'Content-type': 'application/x-www-form-urlencoded','Accept': 'text/plain'}
    	Json_obj1_SignUp={'mobile':self.mobile,'name':self.namme,'email':self.email,'password':self.password , 'role': self.role}
    	params = urllib.parse.urlencode(Json_obj1_SignUp)
    	req = UrlRequest(str_signup, on_success=self.got_json, req_body=params,req_headers=headers)

    def got_json(self,req, result):
        self.manager.curren="login"
        print(result)
        conn1=sqlite3.connect("signup.db")
        c1=conn1.cursor()
        templist=(result['userToken'],result['user']['mobile'],result['user']['name'],result['user']['email'],result['user']['role'])
        conn1.execute("INSERT into register values(?,?,?,?,?)",templist)
        conn1.commit()
        conn1.close()



    def fake(self):
        self.namme = self.ids.name_register.text
        self.email = self.ids.email_register.text
        self.user = self.ids.username_register.text
        self.pwd = self.ids.password_register.text
        self.info = self.ids.inforegister

        if(self.namme=="" or self.email=="" or self.user=="" or self.pwd==""):
            self.info.text='[color=#FF0000]Please fill all the details![/color]'
        else:
            self.info.text='[color=#FF0000]Succesffully Succesfully Registered[/color]'
            templist=(self.namme,self.email,self.user,self.pwd)
            c.execute("insert into logindetails values(?,?,?,?)",templist)
        self.serverregister()

    def closebutton(self):
        conn.commit()
        App.get_running_app().stop()
