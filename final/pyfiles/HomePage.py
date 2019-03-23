from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.widget import Widget
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
import urllib
from kivy.network.urlrequest import UrlRequest
from kivy.garden.mapview import MapView,MapMarker
from kivy.uix.widget import Widget
from kivy.base import runTouchApp
from kivy.uix.relativelayout import RelativeLayout
from kivy.garden.mapview import MapSource,MapMarkerPopup,MapView

conn=sqlite3.connect("signup.db")
c=conn.cursor()
use=""
# AllLands=list(c.execute("Select * from land"))
dictresult=[]
imlist=["Images/1.jpg","Images/2.jpg","Images/3.jpg","Images/4.jpg"]
AllLands={}
class MouseWidget(BoxLayout):
    image=ObjectProperty()
    label=ObjectProperty()
    source=StringProperty()

class ggg(RelativeLayout):
    def get(self):
        x=self.ids.latitude.text
        print(x)
        print(self.ids.longitude.text)
class HomePage(BoxLayout,Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        user =(list(c.execute("Select * from register")))
        # print(user[0][4])
        # if(len(user) and user[0][4] == "admin"):
        #     self.manager.current = 'addland'
        #     # self.manager.current="filterpage"

    cur=-1;
    def openmap(self):
        popup=Popup(content=ggg(),title="MapView")

    def addbookmark(self,tkn,idd):
            str_signup='http://20.0.0.94:4000/bookmark/save'
            headers = {'Content-type': 'application/x-www-form-urlencoded','Accept': 'text/plain'}
            Json_obj1_SignUp={'userToken':tkn,'landId':idd }
            params = urllib.parse.urlencode(Json_obj1_SignUp)
            req = UrlRequest(str_signup, on_success=self.addBook, req_body=params,req_headers=headers)

    def addBook(self,req, result):
        popup = Popup(title='Added!',content=Label(text='Bookmark Added!!'),size_hint=(None, None), size=(200, 200))
        popup.open()
        print(result)
        return


    def requestForLands(self):
        print("request")
        str_signup='http://20.0.0.94:4000/land/getall'
        headers = {'Content-type': 'application/x-www-form-urlencoded','Accept': 'text/plain'}
        Json_obj1_SignUp={'ese' : "fsd"}
        params = urllib.parse.urlencode(Json_obj1_SignUp)
        req = UrlRequest(str_signup, on_success=self.showland, req_body=params,req_headers=headers)



    def showland(self,req , result):
        global dictresult
        dictresult=result['lands']
        print(dictresult)

        self.cur=-1
        self.x=1
        self.ids.acc.clear_widgets()
        if(len(dictresult)<4):
            self.cur=len(dictresult)-1
            if len(dictresult)==1:
                txt=str("")
                txt+="[b][color=87ceeb]"
                txt+=str("Id:"+str(dictresult[0]['id'])+"\nName:"+str(dictresult[0]['name'])+"\nPrice:"+str(dictresult[0]['price'])+"\nAddress:"+str(dictresult[0]['address']))
                txt+='[/color][/b]'
                item = AccordionItem(title='Land %d' % (1),orientation='vertical')
                item.add_widget(Button(text=txt,markup=True))
                item1=MouseWidget(source=imlist[0])
                item.add_widget(item1)
                conn=sqlite3.connect("signup.db")
                c=conn.cursor()
                x=list(c.execute("select * from register"))
                print(x)
                tok=x[0][0]
                item.add_widget(Button(text="Bookmark",size_hint_x=0.2,on_press=lambda a:self.addbookmark(tok,dictresult[0]['id'])))
                self.ids.acc.add_widget(item)
            elif len(dictresult)==2:
                txt=str("")
                txt+="[b][color=87ceeb]"
                txt+=str("Id:"+str(dictresult[0]['id'])+"\nName:"+str(dictresult[0]['name'])+"\nPrice:"+str(dictresult[0]['price'])+"\nAddress:"+str(dictresult[0]['address']))
                txt+='[/color][/b]'
                item = AccordionItem(title='Land %d' % (1),orientation='vertical')
                item.add_widget(Button(text=txt,markup=True))
                item1=MouseWidget(source=imlist[0])
                item.add_widget(item1)
                conn=sqlite3.connect("signup.db")
                c=conn.cursor()
                x=list(c.execute("select * from register"))
                print(x)
                tok=x[0][0]
                item.add_widget(Button(text="Bookmark",size_hint_x=0.2,on_press=lambda a:self.addbookmark(tok,dictresult[0]['id'])))
                self.ids.acc.add_widget(item)
                txt=str("")
                txt+="[b][color=87ceeb]"
                txt+=str("Id:"+str(dictresult[1]['id'])+"\nName:"+str(dictresult[1]['name'])+"\nPrice:"+str(dictresult[1]['price'])+"\nAddress:"+str(dictresult[1]['address']))
                txt+='[/color][/b]'
                item = AccordionItem(title='Land %d' % (2),orientation='vertical')
                item.add_widget(Button(text=txt,markup=True))
                item1=MouseWidget(source=imlist[1])
                item.add_widget(item1)
                conn=sqlite3.connect("signup.db")
                c=conn.cursor()
                x=list(c.execute("select * from register"))
                print(x)
                tok=x[0][0]
                item.add_widget(Button(text="Bookmark",size_hint_x=0.2,on_press=lambda a:self.addbookmark(tok,dictresult[1]['id'])))
                self.ids.acc.add_widget(item)
            elif len(dictresult)==3:
                txt=str("")
                txt+="[b][color=87ceeb]"
                txt+=str("Id:"+str(dictresult[0]['id'])+"\nName:"+str(dictresult[0]['name'])+"\nPrice:"+str(dictresult[0]['price'])+"\nAddress:"+str(dictresult[0]['address']))
                txt+='[/color][/b]'
                item = AccordionItem(title='Land %d' % (1),orientation='vertical')
                item.add_widget(Button(text=txt,markup=True))
                item1=MouseWidget(source=imlist[0])
                item.add_widget(item1)
                conn=sqlite3.connect("signup.db")
                c=conn.cursor()
                x=list(c.execute("select * from register"))
                print(x)
                tok=x[0][0]
                item.add_widget(Button(text="Bookmark",size_hint_x=0.2,on_press=lambda a:self.addbookmark(tok,dictresult[0]['id'])))
                self.ids.acc.add_widget(item)
                txt=str("")
                txt+="[b][color=87ceeb]"
                txt+=str("Id:"+str(dictresult[1]['id'])+"\nName:"+str(dictresult[1]['name'])+"\nPrice:"+str(dictresult[1]['price'])+"\nAddress:"+str(dictresult[1]['address']))
                txt+='[/color][/b]'
                item = AccordionItem(title='Land %d' % (2),orientation='vertical')
                item.add_widget(Button(text=txt,markup=True))
                item1=MouseWidget(source=imlist[1])
                item.add_widget(item1)
                conn=sqlite3.connect("signup.db")
                c=conn.cursor()
                x=list(c.execute("select * from register"))
                print(x)
                tok=x[0][0]
                item.add_widget(Button(text="Bookmark",size_hint_x=0.2,on_press=lambda a:self.addbookmark(tok,dictresult[1]['id'])))
                self.ids.acc.add_widget(item)
                txt=str("")
                txt+="[b][color=87ceeb]"
                txt+=str("Id:"+str(dictresult[2]['id'])+"\nName:"+str(dictresult[2]['name'])+"\nPrice:"+str(dictresult[2]['price'])+"\nAddress:"+str(dictresult[2]['address']))
                txt+='[/color][/b]'
                item = AccordionItem(title='Land %d' % (3),orientation='vertical')
                item.add_widget(Button(text=txt,markup=True))
                item1=MouseWidget(source=imlist[2])
                item.add_widget(item1)
                conn=sqlite3.connect("signup.db")
                c=conn.cursor()
                x=list(c.execute("select * from register"))
                print(x)
                tok=x[0][0]
                item.add_widget(Button(text="Bookmark",size_hint_x=0.2,on_press=lambda a:self.addbookmark(tok,dictresult[2]['id'])))
                self.ids.acc.add_widget(item)
        else:
                txt=str("")
                txt+="[b][color=87ceeb]"
                txt+=str("Id:"+str(dictresult[0]['id'])+"\nName:"+str(dictresult[0]['name'])+"\nPrice:"+str(dictresult[0]['price'])+"\nAddress:"+str(dictresult[0]['address']))
                txt+='[/color][/b]'
                item = AccordionItem(title='Land %d' % (1),orientation='vertical')
                item1=MouseWidget(source=imlist[0])
                item.add_widget(item1)
                item.add_widget(Button(text=txt,markup=True))
                conn=sqlite3.connect("signup.db")
                c=conn.cursor()
                x=list(c.execute("select * from register"))
                print(x)
                tok=x[0][0]
                item.add_widget(Button(text="Bookmark",size_hint_x=0.2,on_press=lambda a:self.addbookmark(tok,dictresult[0]['id'])))
                self.ids.acc.add_widget(item)
                txt=str("")
                txt+="[b][color=87ceeb]"
                txt+=str("Id:"+str(dictresult[1]['id'])+"\nName:"+str(dictresult[1]['name'])+"\nPrice:"+str(dictresult[1]['price'])+"\nAddress:"+str(dictresult[1]['address']))
                txt+='[/color][/b]'
                item = AccordionItem(title='Land %d' % (2),orientation='vertical')
                item1=MouseWidget(source=imlist[1])
                item.add_widget(item1)
                item.add_widget(Button(text=txt,markup=True))
                conn=sqlite3.connect("signup.db")
                c=conn.cursor()
                x=list(c.execute("select * from register"))
                print(dictresult[1]['id'])
                tok=x[0][0]
                item.add_widget(Button(text="Bookmark",size_hint_x=0.2,on_press=lambda a:self.addbookmark(tok,dictresult[1]['id'])))
                self.ids.acc.add_widget(item)
                txt=str("")
                txt+="[b][color=87ceeb]"
                txt+=str("Id:"+str(dictresult[2]['id'])+"\nName:"+str(dictresult[2]['name'])+"\nPrice:"+str(dictresult[2]['price'])+"\nAddress:"+str(dictresult[2]['address']))
                txt+='[/color][/b]'
                item = AccordionItem(title='Land %d' % (3),orientation='vertical')
                item1=MouseWidget(source=imlist[2])
                item.add_widget(item1)
                item.add_widget(Button(text=txt,markup=True))
                conn=sqlite3.connect("signup.db")
                c=conn.cursor()
                x=list(c.execute("select * from register"))
                print("sadfgh")
                tok=x[0][0]
                item.add_widget(Button(text="Bookmark",size_hint_x=0.2,on_press=lambda a:self.addbookmark(tok,dictresult[2]['id'])))
                self.ids.acc.add_widget(item)
                txt=str("")
                txt+="[b][color=87ceeb]"
                txt+=str("Id:"+str(dictresult[3]['id'])+"\nName:"+str(dictresult[3]['name'])+"\nPrice:"+str(dictresult[3]['price'])+"\nAddress:"+str(dictresult[3]['address']))
                txt+='[/color][/b]'
                item = AccordionItem(title='Land %d' % (4),orientation='vertical')
                item1=MouseWidget(source=imlist[3])
                item.add_widget(item1)
                item.add_widget(Button(text=txt,markup=True))
                conn=sqlite3.connect("signup.db")
                c=conn.cursor()
                x=list(c.execute("select * from register"))
                print(x)
                tok=x[0][0]
                item.add_widget(Button(text="Bookmark",size_hint_x=0.2,on_press=lambda a:self.addbookmark(tok,dictresult[3]['id'])))
                self.ids.acc.add_widget(item)
                self.cur+=4



    def nextland(self):
        global dictresult
        if(len(dictresult)==self.cur+1):
            popup = Popup(title='Error!',content=Label(text='No More Lands!!'),size_hint=(None, None), size=(200, 200))
            popup.open()
            return
        else:
            self.ids.acc.clear_widgets()
            if(len(dictresult)-1-self.cur>=4):
                a=self.cur+1
                txt1=str("")
                txt1+="[b][color=87ceeb]"
                txt1+=str("Id:"+str(dictresult[a]['id'])+"\nName:"+str(dictresult[a]['name'])+"\nPrice:"+str(dictresult[a]['price'])+"\nAddress:"+str(dictresult[a]['address']))
                txt1+='[/color][/b]'
                item = AccordionItem(title='Land %d' % (a+1),orientation='vertical')
                item1=MouseWidget(source=imlist[0])
                item.add_widget(item1)
                item1.add_widget(Button(text=txt1,markup=True))
                btn1=Button(text="Bookmark",size_hint_x=0.2)
                item.add_widget(btn1)
                btn1.bind(on_press=lambda ab:self.addbookmark(dictresult[a]))





                self.ids.acc.add_widget(item)
                a+=1
                txt1=str("")
                txt1+="[b][color=87ceeb]"
                txt1+=str("Id:"+str(dictresult[a]['id'])+"\nName:"+str(dictresult[a]['name'])+"\nPrice:"+str(dictresult[a]['price'])+"\nAddress:"+str(dictresult[a]['address']))
                txt1+='[/color][/b]'
                item=MouseWidget(source=imlist[1])
                item1 = AccordionItem(title='Land %d' % (a+1),orientation='vertical')
                item1.add_widget(item)
                item1.add_widget(Button(text=txt1,markup=True))


                btn1=Button(text="Bookmark",size_hint_x=0.2)
                item1.add_widget(btn1)
                btn1.bind(on_press=lambda ab:self.addbookmark(dictresult[a]))
                self.ids.acc.add_widget(item1)
                a+=1
                txt1=str("")
                txt1+="[b][color=87ceeb]"
                txt1+=str("Id:"+str(dictresult[a]['id'])+"\nName:"+str(dictresult[a]['name'])+"\nPrice:"+str(dictresult[a]['price'])+"\nAddress:"+str(dictresult[a]['address']))
                txt1+='[/color][/b]'
                item=MouseWidget(source=imlist[1])
                item1 = AccordionItem(title='Land %d' % (a+1),orientation='vertical')
                item1.add_widget(item)
                item1.add_widget(Button(text=txt1,markup=True))
                btn1=Button(text="Bookmark",size_hint_x=0.2)
                item1.add_widget(btn1)
                btn1.bind(on_press=lambda ab:self.addbookmark(dictresult[a]))
                self.ids.acc.add_widget(item1)
                a+=1
                txt1=str("")
                txt1+="[b][color=87ceeb]"
                txt1+=str("Id:"+str(dictresult[a]['id'])+"\nName:"+str(dictresult[a]['name'])+"\nPrice:"+str(dictresult[a]['price'])+"\nAddress:"+str(dictresult[a]['address']))
                txt1+='[/color][/b]'
                item=MouseWidget(source=imlist[1])
                item1 = AccordionItem(title='Land %d' % (a+1),orientation='vertical')
                item1.add_widget(item)
                item1.add_widget(Button(text=txt1,markup=True))

                btn1=Button(text="Bookmark",size_hint_x=0.2)
                item1.add_widget(btn1)
                btn1.bind(on_press=lambda ab:self.addbookmark(dictresult[a]))
                self.ids.acc.add_widget(item1)
                self.cur+=4
            else:

                var=len(dictresult)-self.cur-1
                print(var)
                if var==1:
                    a=self.cur
                    txt=str("")
                    txt+="[b][color=87ceeb]"
                    txt+=str("Id:"+str(dictresult[a]['id'])+"\nName:"+str(dictresult[a]['name'])+"\nPrice:"+str(dictresult[a]['price'])+"\nAddress:"+str(dictresult[a]['address']))
                    txt+='[/color][/b]'
                    item=MouseWidget(source=imlist[1])
                    item1 = AccordionItem(title='Land %d' % (a+1),orientation='vertical')
                    item1.add_widget(item)
                    item1.add_widget(Button(text=txt,markup=True))

                    item1.add_widget(Button(text="Bookmark",size_hint_x=0.2,on_press=lambda ab:self.addbookmark(dictresult[a])))
                    self.ids.acc.add_widget(item1)
                elif var==2:
                    a=self.cur
                    txt=str("")
                    txt+="[b][color=87ceeb]"
                    txt+=str("Id:"+str(dictresult[a]['id'])+"\nName:"+str(dictresult[a]['name'])+"\nPrice:"+str(dictresult[a]['price'])+"\nAddress:"+str(dictresult[a]['address']))
                    txt+='[/color][/b]'
                    item = AccordionItem(title='Land %d' % (a+2),orientation='vertical')

                    item1=MouseWidget(source=imlist[0])
                    item.add_widget(item1)
                    item.add_widget(Button(text=txt,markup=True))
                    item.add_widget(Button(text="Bookmark",size_hint_x=0.2,on_press=lambda ab:self.addbookmark(dictresult[a])))
                    self.ids.acc.add_widget(item)
                    a+=1
                    txt=str("")
                    txt+="[b][color=87ceeb]"
                    print(a)
                    txt+=str("Id:"+str(dictresult[a]['id'])+"\nName:"+str(dictresult[a]['name'])+"\nPrice:"+str(dictresult[a]['price'])+"\nAddress:"+str(dictresult[a]['address']))
                    txt+='[/color][/b]'
                    item=MouseWidget(source=imlist[1])
                    item1 = AccordionItem(title='Land %d' % (a+1),orientation='vertical')
                    item1.add_widget(item)
                    item1.add_widget(Button(text=txt1,markup=True))
                    item1.add_widget(Button(text="Bookmark",size_hint_x=0.2,on_press=lambda ab:self.addbookmark(dictresult[a])))
                    self.ids.acc.add_widget(item)
                elif var==3:
                    a=self.cur
                    txt=str("")
                    txt+="[b][color=87ceeb]"
                    txt+=str("Id:"+str(dictresult[a]['id'])+"\nName:"+str(dictresult[a]['name'])+"\nPrice:"+str(dictresult[a]['price'])+"\nAddress:"+str(dictresult[a]['address']))
                    txt+='[/color][/b]'
                    item=MouseWidget(source=imlist[1])
                    item1 = AccordionItem(title='Land %d' % (a+1),orientation='vertical')
                    item1.add_widget(item)
                    item1.add_widget(Button(text=txt1,markup=True))

                    item1.add_widget(Button(text="Bookmark",size_hint_x=0.2,on_press=lambda ab:self.addbookmark(dictresult[a])))
                    self.ids.acc.add_widget(item)
                    a+=1
                    txt=str("")
                    txt+="[b][color=87ceeb]"
                    txt+=str("Id:"+str(dictresult[a]['id'])+"\nName:"+str(dictresult[a]['name'])+"\nPrice:"+str(dictresult[a]['price'])+"\nAddress:"+str(dictresult[a]['address']))
                    txt+='[/color][/b]'
                    item=MouseWidget(source=imlist[1])
                    item1 = AccordionItem(title='Land %d' % (a+1),orientation='vertical')
                    item1.add_widget(item)
                    item1.add_widget(Button(text=txt1,markup=True))
                    item1.add_widget(Button(text="Bookmark",size_hint_x=0.2,on_press=lambda ab:self.addbookmark(dictresult[a])))
                    self.ids.acc.add_widget(item)
                    a+=1
                    txt=str("")
                    txt+="[b][color=87ceeb]"
                    txt+=str("Id:"+str(dictresult[a]['id'])+"\nName:"+str(dictresult[a]['name'])+"\nPrice:"+str(dictresult[a]['price'])+"\nAddress:"+str(dictresult[a]['address']))
                    txt+='[/color][/b]'
                    item=MouseWidget(source=imlist[1])
                    item1 = AccordionItem(title='Land %d' % (a+1),orientation='vertical')
                    item1.add_widget(item)
                    item1.add_widget(Button(text=txt1,markup=True))
                    item1.add_widget(Button(text="Bookmark",size_hint_x=0.2,on_press=lambda ab:self.addbookmark(dictresult[a])))
                    self.ids.acc.add_widget(item)

                self.cur=len(dictresult)-1


    def prevland(self):
        global dictresult
        if(self.cur<=3):
            popup = Popup(title='Error!',content=Label(text='No More Lands!!'),size_hint=(None, None), size=(200, 200))
            popup.open()
            return
        elif(self.cur>3):
            self.cur-=4
            self.ids.acc.clear_widgets()
            for i in range(self.cur,self.cur+4):
                txt=str("")
                txt+="[b][color=87ceeb]"
                txt+=str("Id:"+str(dictresult[i]['id'])+"\nName:"+str(dictresult[i]['name'])+"\nPrice:"+str(dictresult[i]['price'])+"\nAddress:"+str(dictresult[i]['address']))
                txt+='[/color][/b]'
                item = AccordionItem(title='Land %d' % (i+1),orientation='vertical')
                item1=MouseWidget(source=imlist[i%4])
                item.add_widget(item1)
                item.add_widget(Button(text=txt,markup=True))
                item.add_widget(Button(text="Bookmark",size_hint_x=0.2))
                self.ids.acc.add_widget(item)
        else:
            self.cur=0
            self.ids.acc.clear_widgets()
            for i in range(self.cur,self.cur+4):
                txt=str("")
                txt+="[b][color=87ceeb]"
                txt+=str("Id:"+str(dictresult[i]['id'])+"\nName:"+str(dictresult[i]['name'])+"\nPrice:"+str(dictresult[i]['price'])+"\nAddress:"+str(dictresult[i]['address']))
                txt+='[/color][/b]'
                item = AccordionItem(title='Land %d' % (i+1),orientation='vertical')
                item1=MouseWidget(source=imlist[i%4])
                item.add_widget(item1)
                item.add_widget(Button(text=txt,markup=True))
                item.add_widget(Button(text="Bookmark",size_hint_x=0.2))
                self.ids.acc.add_widget(item)
            self.cur=3

    def gotofilter(self):
        self.ids.acc.clear_widgets()
        self.manager.current="filterpage"

    def clearbutton(self):
        self.ids.acc.clear_widgets()


    def sort1(self):
        str_signup='http://20.0.0.94:4000/land/getbyprice'
        headers = {'Content-type': 'application/x-www-form-urlencoded','Accept': 'text/plain'}
        Json_obj1_SignUp={'name':'karan'}
        params = urllib.parse.urlencode(Json_obj1_SignUp)
        req = UrlRequest(str_signup, on_success=self.got_json1, req_body=params,req_headers=headers)
    def got_json1(self,req,result):
        print(result)
        popup = Popup(title='Success',content=Label(text='Sorted'),size_hint=(None, None), size=(200, 200))
        # popup.open()
        self.showland(req, result)

    def sort2(self):
        str_signup='http://20.0.0.94:4000/land/getbyarea'
        headers = {'Content-type': 'application/x-www-form-urlencoded','Accept': 'text/plain'}
        Json_obj1_SignUp={'name':'karan'}
        params = urllib.parse.urlencode(Json_obj1_SignUp)
        req = UrlRequest(str_signup, on_success=self.got_json2, req_body=params,req_headers=headers)
    def got_json2(self,req,result):
        print(result)
        popup = Popup(title='Success',content=Label(text='Sorted'),size_hint=(None, None), size=(200, 200))
        # popup.open()
        self.showland(req, result)

    def logout(self):
        conn=sqlite3.connect("signup.db")
        c=conn.cursor()
        c.execute("DELETE from register")
        conn.commit()
        conn.close()
        self.ids.acc.clear_widgets()
        self.manager.current="login"
        self.cur=-1

    def openmap(self):

        str_signup='http://20.0.0.94:4000/land/getalllocation'
        headers = {'Content-type': 'application/x-www-form-urlencoded','Accept': 'text/plain'}
        Json_obj1_SignUp={'name':'karan'}
        params = urllib.parse.urlencode(Json_obj1_SignUp)
        req = UrlRequest(str_signup, on_success=self.startmap, req_body=params,req_headers=headers)

    def startmap(self,res,result):
        print(result['location'])
        mapview = ""
        for i in range(len(result['location'])):
            print(result['location'][i]['latitude'])
            if result['location'][i]['longitude'] and result['location'][i]['latitude']:
                if mapview == "":
                    mapview = MapView(zoom=11, lat=result['location'][i]['latitude'],lon=result['location'][i]['longitude'])
                mapview.add_marker(MapMarkerPopup(lat=result['location'][i]['latitude'],lon=result['location'][i]['longitude']))
        popup=Popup(content=mapview)
        popup.open()


    def closebutton(self):
        conn.commit()
        App.get_running_app().stop()
