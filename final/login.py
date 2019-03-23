from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
import sqlite3

conn=sqlite3.connect("db.db")
c=conn.cursor()


class ConnectingSigninRegister(ScreenManager):
    pass

class AddWindow(BoxLayout,Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def addland(self):
        land=self.ids.land_name.text
        price=self.ids.land_price.text
        address=self.ids.land_address.text
        area=self.ids.area.text

        if(land=="" or price=="" or address=="" or area==""):
            info.text='[color=#FF0000]Please fill all the details![/color]'
        else:
            info.text='[color=#FF0000]Land Added Succesfully[/color]'
            templist=(land,price,address,area)
            c.execute("insert into land_info values(?,?,?,?)",templist)

class HomePage(Screen,BoxLayout):
    def aff(self):
        AllLands=list(c.execute("select * from land"))
        for i in range(0,len(AllLands)):
            txt=str("")
            txt+="[b][color=ff3333]"
            txt+=str(AllLands[i][0]+" - "+AllLands[i][1]+" - "+AllLands[i][2]+" - "+AllLands[i][3])
            txt+='[/color][/b]'
            land = Label(text=txt,markup = True)
            self.ids.grid.add_widget(land)


class SigninWindow(BoxLayout,Screen):
    def __init__(self, **kwargs):
       super().__init__(**kwargs)

    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.infologin

        uname=user.text
        passw=pwd.text
        templist=(uname,passw)
        fetchlist=list(c.execute("select username,password from logindetails"))
        if(templist in fetchlist):
            info.text='[color=#FF0000]Login Success[/color]'
            self.manager.current="homepage"
        else:
            info.text='[color=#FF0000]Wrong Username or password[/color]'


    def closebutton(self):
        conn.commit()
        App.get_running_app().stop()

class RegisterWindow(BoxLayout,Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def completeregister(self):
        name = self.ids.name_register.text
        email = self.ids.email_register.text
        user = self.ids.username_register.text
        pwd = self.ids.password_register.text
        info = self.ids.inforegister


        if(name=="" or email=="" or user=="" or pwd==""):
            info.text='[color=#FF0000]Please fill all the details![/color]'
        else:
            info.text='[color=#FF0000]Succesffully Succesfully Registered[/color]'
            templist=(name,email,user,pwd)
            c.execute("insert into logindetails values(?,?,?,?)",templist)


    def closebutton(self):
        conn.commit()
        App.get_running_app().stop()

kv=Builder.load_file("my.kv")

class SigninApp(App):
    def build(self):
        return kv

obj=SigninApp()
obj.run()
