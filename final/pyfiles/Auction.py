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
from operator import itemgetter
import sqlite3
# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
conn=sqlite3.connect("dbauc.db")
c=conn.cursor()

AllLands=list(c.execute("Select * from land"))


class Auction(Screen):
    cur=-1;
    def nextland(self):
        global AllLands
        if(len(AllLands)==self.cur+1):
            popup = Popup(title='Error!',content=Label(text='No More Lands!!'),size_hint=(None, None), size=(200, 200))
            popup.open()
            return
        else:
            self.ids.acc.clear_widgets()
            if(len(AllLands)-1-self.cur>=4):
                for i in range(self.cur+1,self.cur+5):
                    txt=str("")
                    txt+="[b][color=87ceeb]"
                    txt+=str(str(AllLands[i][0])+"\n "+AllLands[i][1]+"\n"+AllLands[i][2]+"\n"+AllLands[i][3])
                    txt+='[/color][/b]'
                    item = AccordionItem(title='Land %d' % (i+1),orientation='vertical')
                    item.add_widget(Button(text=txt,markup=True))
                    self.ids.acc.add_widget(item)
                self.cur+=4
            else:
                for i in range(self.cur+1,len(AllLands)):
                    print("Yes")
                    txt=str("")
                    txt+="[b][color=87ceeb]"
                    txt+=str(str(AllLands[i][0])+"\n "+AllLands[i][1]+"\n"+AllLands[i][2]+"\n"+AllLands[i][3])
                    txt+='[/color][/b]'
                    item = AccordionItem(title='Land %d' % (i+1),orientation='vertical')
                    print(txt)
                    item.add_widget(Button(text=txt,markup=True))
                    self.ids.acc.add_widget(item)
                self.cur=len(AllLands)-1



    def prevland(self):
        global AllLands
        if(self.cur<=3):
            popup = Popup(title='Error!',content=Label(text='No More Lands!!'),size_hint=(None, None), size=(200, 200))
            popup.open()
            return
        elif(self.cur>=3):
            self.cur-=4
            self.ids.acc.clear_widgets()
            for i in range(self.cur,self.cur+4):
                txt=str("")
                txt+="[b][color=87ceeb]"
                txt+=str(str(AllLands[i][0])+"\n "+AllLands[i][1]+"\n"+AllLands[i][2]+"\n"+AllLands[i][3])
                txt+='[/color][/b]'
                item = AccordionItem(title='Land %d' % (i+1),orientation='vertical')
                item.add_widget(Button(text=txt,markup=True))
                self.ids.acc.add_widget(item)
        else:
            self.cur=0
            self.ids.acc.clear_widgets()
            for i in range(self.cur,self.cur+4):
                txt=str("")
                txt+="[b][color=87ceeb]"
                txt+=str(str(AllLands[i][0])+"\n "+AllLands[i][1]+"\n"+AllLands[i][2]+"\n"+AllLands[i][3])
                txt+='[/color][/b]'
                item = AccordionItem(title='Land %d' % (i+1),orientation='vertical')
                item.add_widget(Button(text=txt,markup=True))
                self.ids.acc.add_widget(item)
            self.cur=3
    def gotofilter(self):
        self.ids.acc.clear_widgets()
        self.manager.current="filterpage"

    def clearbutton(self):
        global AllLands
        AllLands=list(c.execute("select * from land"))
        self.ids.acc.clear_widgets()
        cur=-1

    def sort1(self):
        global AllLands
        self.ids.dropdown.select('Price')
        self.cur=-1
        print(AllLands)
        self.clearbutton()
        AllLands=list(c.execute("Select * from land order by LandId asc"))
        self.nextland()


    def sort2(self):
        global AllLands
        self.ids.dropdown.select('Area')
        AllLands=list(c.execute("Select * from land order by LandId asc"))
        self.cur=-1
        self.clearbutton()
        AllLands=list(c.execute("Select * from land order by LandId asc"))
        self.nextland()
        print(AllLands)


    def logout(self):
        self.ids.acc.clear_widgets()
        self.manager.current="login"
        self.cur=-1

    def closebutton(self):
        conn.commit()
        App.get_running_app().stop()
