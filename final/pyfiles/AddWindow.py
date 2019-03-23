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
from kivy.uix.relativelayout import RelativeLayout
conn=sqlite3.connect("signup.db")
c=conn.cursor()
use=""
# AllLands=list(c.execute("Select * from land"))
Item=[]
class ggg(RelativeLayout):
    popup = ""
    def get(self):
        x=self.ids.latitude.text
        templist=[]
        templist.append(x)
        templist.append(self.ids.longitude.text)
        print(templist)
        AddWindow.geoList = templist
        self.popup.dismiss()

class EditWindow(BoxLayout,Screen):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
        def editland(self):
            name=self.ids.edit_land_name.text
            price=self.ids.edit_land_price.text
            address=self.ids.edit_land_address.text
            area=self.ids.edit_land_area.text
            info=self.ids.infoEdit

            name2=self.ids.edit_land_name2.text
            price2=self.ids.edit_land_price2.text
            address2=self.ids.edit_land_address2.text
            area2=self.ids.edit_land_area2.text
            info2=self.ids.infoEdit

            if((name=="" or price=="" or address=="" or area=="")or(name2=="" or price2=="" or address2=="" or area2=="") ):
                info.text='[color=#FF0000]Please fill all the details![/color]'
            else:
                info.text='[color=#FF0000]Land Added Succesfully[/color]'
                templist=(name,price,area,address,name2,price2,area2,address2)
                #print(name+" "+price+" "+address+" "+area+" "+info.text+" ")
                #print(name2+" "+price2+" "+address2+" "+area2+" "+info.text+" ")
                #print(templist)
                #c.execute("UPDATE land SET Name=(?), Price=(?), Area=(?), Adress=(?) WHERE Name = (?), Price=(?), Area=(?), Adress=(?)",templist)
                #c.execute("DELETE FROM land WHERE Name=(?) AND Price=(?) AND Area=(?) AND Adress=(?)",templist)
                c.execute("UPDATE land SET Name=(?), Price=(?), Area=(?), Adress=(?) WHERE Name = (?) AND Price=(?) AND Area=(?) AND Adress=(?)",templist)
        def closebutton(self):
            conn.commit()
            App.get_running_app().stop()
class DelWindow(BoxLayout,Screen):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

        def delland(self):
            name=self.ids.del_land_name.text
            price=self.ids.del_land_price.text
            address=self.ids.del_land_address.text
            area=self.ids.del_land_area.text
            info=self.ids.infoDel
            if(name=="" or price=="" or address=="" or area==""):
                info.text='[color=#FF0000]Please fill all the details![/color]'
            else:
                info.text='[color=#FF0000]Land Added Succesfully[/color]'
                templist=(name,price,area,address)
                #print(name+" "+price+" "+address+" "+area+" "+info.text+" ")
                #c.execute('DELETE FROM land WHERE Name=?',(name))
                c.execute("DELETE FROM land WHERE Name=(?) AND Price=(?) AND Area=(?) AND Adress=(?)",templist)

        def closebutton(self):
            conn.commit()
            App.get_running_app().stop()

class AddWindow(BoxLayout,Screen):
    Email=''
    password=''
    geoList= ""
    def logout(self):
        c.execute("DELETE from register")
        conn.commit()
        conn.close()
        self.manager.current="login"
    def close(self):
        self.manager.current="addwindow"
    def got_json(self,req, result):
        print(result)
        print("yes")

    def openmap(self):
            content=[]
            geo = ggg()
            popup=Popup(content=geo)
            print(content)
            geo.popup = popup
            popup.open()
            print(content)
    def add_lands(self):
        self.name = self.ids.add_land_name.text
        self.area = self.ids.add_land_area.text
        self.price = self.ids.add_land_price.text
        self.address = self.ids.add_land_address.text
        self.description = self.ids.add_land_description.text
        self.userToken = ""
        self.latitude = self.geoList[1]
        self.longitude = self.geoList[0]
        # print(self.latitude)

        conn=sqlite3.connect("signup.db")
        c=conn.cursor()
        user =(list(c.execute("Select * from register")))
        conn.commit()
        c.close()
        if len(user) :
            self.userToken = user[0][0]
        str_signup='http://20.0.0.94:4000/land/add'
        headers = {'Content-type': 'application/x-www-form-urlencoded','Accept': 'text/plain'}
        Json_obj1_SignUp={'name':self.name,'latitude':self.latitude,'longitude':self.longitude,'area':self.area , 'price':self.price , 'address': self.address , 'description':self.description, 'userToken':self.userToken }
        params = urllib.parse.urlencode(Json_obj1_SignUp)
        req = UrlRequest(str_signup, on_success=self.got_json, req_body=params,req_headers=headers)

    def got_json(self,req, result):
        print(result)
        popup = Popup(title='Success',content=Label(text='Land Added!!'),size_hint=(None, None), size=(200, 200))
        popup.open()
        # templist=(result['userToken'],result['user']['mobile'],result['user']['name'],result['user']['email'],result['user']['role'])
        # conn.execute("INSERT into register values(?,?,?,?,?)",templist)
        # conn.commit()
        # conn.close()
        #self.manager.current="homepage"


    def closebutton(self):
        App.get_running_app().stop()
