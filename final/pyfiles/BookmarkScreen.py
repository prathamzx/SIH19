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
Item=[]

class BookmarkScreen(Screen,BoxLayout):

    def clearbutton(self):
        self.ids.acc.clear_widgets()
    cur=-1;
    def showbookmarks(self):
        self.cur=-1
        self.ids.acc.clear_widgets()
        conn=sqlite3.connect("signup.db")
        c=conn.cursor()
        user =(list(c.execute("Select * from register")))
        conn.commit()
        c.close()
        if len(user) :
            self.userToken = user[0][0]
        str_signup='http://20.0.0.94:4000/bookmark/getall'
        headers = {'Content-type': 'application/x-www-form-urlencoded','Accept': 'text/plain'}
        Json_obj1_SignUp={'userToken' :self.userToken}
        params = urllib.parse.urlencode(Json_obj1_SignUp)
        req = UrlRequest(str_signup, on_success=self.showIt, req_body=params,req_headers=headers)
        
    def deletebookmarks(self):
        self.ids.acc.clear_widgets()

    def showIt(self, res, result):
        print(result)
        dictresult=result['bookmarks']
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
                conn=sqlite3.connect("signup.db")
                c=conn.cursor()
                x=list(c.execute("select * from register"))
                print(x)
                tok=x[0][0]
                #item.add_widget(Button(text="Bookmark",size_hint_x=0.2,on_press=lambda a:self.addbookmark(tok,dictresult[0]['id'])))
                self.ids.acc.add_widget(item)
            elif len(dictresult)==2:
                txt=str("")
                txt+="[b][color=87ceeb]"
                txt+=str("Id:"+str(dictresult[0]['id'])+"\nName:"+str(dictresult[0]['name'])+"\nPrice:"+str(dictresult[0]['price'])+"\nAddress:"+str(dictresult[0]['address']))
                txt+='[/color][/b]'
                item = AccordionItem(title='Land %d' % (1),orientation='vertical')
                item.add_widget(Button(text=txt,markup=True))
                conn=sqlite3.connect("signup.db")
                c=conn.cursor()
                x=list(c.execute("select * from register"))
                print(x)
                tok=x[0][0]
                #item.add_widget(Button(text="Bookmark",size_hint_x=0.2,on_press=lambda a:self.addbookmark(tok,dictresult[0]['id'])))
                self.ids.acc.add_widget(item)
                txt=str("")
                txt+="[b][color=87ceeb]"
                txt+=str("Id:"+str(dictresult[1]['id'])+"\nName:"+str(dictresult[1]['name'])+"\nPrice:"+str(dictresult[1]['price'])+"\nAddress:"+str(dictresult[1]['address']))
                txt+='[/color][/b]'
                item = AccordionItem(title='Land %d' % (2),orientation='vertical')
                item.add_widget(Button(text=txt,markup=True))
                conn=sqlite3.connect("signup.db")
                c=conn.cursor()
                x=list(c.execute("select * from register"))
                print(x)
                tok=x[0][0]
                #item.add_widget(Button(text="Bookmark",size_hint_x=0.2,on_press=lambda a:self.addbookmark(tok,dictresult[1]['id'])))
                self.ids.acc.add_widget(item)
            elif len(dictresult)==3:
                txt=str("")
                txt+="[b][color=87ceeb]"
                txt+=str("Id:"+str(dictresult[0]['id'])+"\nName:"+str(dictresult[0]['name'])+"\nPrice:"+str(dictresult[0]['price'])+"\nAddress:"+str(dictresult[0]['address']))
                txt+='[/color][/b]'
                item = AccordionItem(title='Land %d' % (1),orientation='vertical')
                item.add_widget(Button(text=txt,markup=True))
                conn=sqlite3.connect("signup.db")
                c=conn.cursor()
                x=list(c.execute("select * from register"))
                print(x)
                tok=x[0][0]
                #item.add_widget(Button(text="Bookmark",size_hint_x=0.2,on_press=lambda a:self.addbookmark(tok,dictresult[0]['id'])))
                self.ids.acc.add_widget(item)
                txt=str("")
                txt+="[b][color=87ceeb]"
                txt+=str("Id:"+str(dictresult[1]['id'])+"\nName:"+str(dictresult[1]['name'])+"\nPrice:"+str(dictresult[1]['price'])+"\nAddress:"+str(dictresult[1]['address']))
                txt+='[/color][/b]'
                item = AccordionItem(title='Land %d' % (2),orientation='vertical')
                item.add_widget(Button(text=txt,markup=True))
                conn=sqlite3.connect("signup.db")
                c=conn.cursor()
                x=list(c.execute("select * from register"))
                print(x)
                tok=x[0][0]
                #item.add_widget(Button(text="Bookmark",size_hint_x=0.2,on_press=lambda a:self.addbookmark(tok,dictresult[1]['id'])))
                self.ids.acc.add_widget(item)
                txt=str("")
                txt+="[b][color=87ceeb]"
                txt+=str("Id:"+str(dictresult[2]['id'])+"\nName:"+str(dictresult[2]['name'])+"\nPrice:"+str(dictresult[2]['price'])+"\nAddress:"+str(dictresult[2]['address']))
                txt+='[/color][/b]'
                item = AccordionItem(title='Land %d' % (3),orientation='vertical')
                item.add_widget(Button(text=txt,markup=True))
                conn=sqlite3.connect("signup.db")
                c=conn.cursor()
                x=list(c.execute("select * from register"))
                print(x)
                tok=x[0][0]
                #item.add_widget(Button(text="Bookmark",size_hint_x=0.2,on_press=lambda a:self.addbookmark(tok,dictresult[2]['id'])))
                self.ids.acc.add_widget(item)
        else:
                txt=str("")
                txt+="[b][color=87ceeb]"
                txt+=str("Id:"+str(dictresult[0]['id'])+"\nName:"+str(dictresult[0]['name'])+"\nPrice:"+str(dictresult[0]['price'])+"\nAddress:"+str(dictresult[0]['address']))
                txt+='[/color][/b]'
                item = AccordionItem(title='Land %d' % (1),orientation='vertical')

                item.add_widget(Button(text=txt,markup=True))
                conn=sqlite3.connect("signup.db")
                c=conn.cursor()
                x=list(c.execute("select * from register"))
                print(x)
                tok=x[0][0]
                #item.add_widget(Button(text="Bookmark",size_hint_x=0.2,on_press=lambda a:self.addbookmark(tok,dictresult[0]['id'])))
                self.ids.acc.add_widget(item)
                txt=str("")
                txt+="[b][color=87ceeb]"
                txt+=str("Id:"+str(dictresult[1]['id'])+"\nName:"+str(dictresult[1]['name'])+"\nPrice:"+str(dictresult[1]['price'])+"\nAddress:"+str(dictresult[1]['address']))
                txt+='[/color][/b]'
                item = AccordionItem(title='Land %d' % (2),orientation='vertical')

                item.add_widget(Button(text=txt,markup=True))
                conn=sqlite3.connect("signup.db")
                c=conn.cursor()
                x=list(c.execute("select * from register"))
                print(dictresult[1]['id'])
                tok=x[0][0]
                #item.add_widget(Button(text="Bookmark",size_hint_x=0.2,on_press=lambda a:self.addbookmark(tok,dictresult[1]['id'])))
                self.ids.acc.add_widget(item)
                txt=str("")
                txt+="[b][color=87ceeb]"
                txt+=str("Id:"+str(dictresult[2]['id'])+"\nName:"+str(dictresult[2]['name'])+"\nPrice:"+str(dictresult[2]['price'])+"\nAddress:"+str(dictresult[2]['address']))
                txt+='[/color][/b]'
                item = AccordionItem(title='Land %d' % (3),orientation='vertical')

                item.add_widget(Button(text=txt,markup=True))
                conn=sqlite3.connect("signup.db")
                c=conn.cursor()
                x=list(c.execute("select * from register"))
                print("sadfgh")
                tok=x[0][0]
                #item.add_widget(Button(text="Bookmark",size_hint_x=0.2,on_press=lambda a:self.addbookmark(tok,dictresult[2]['id'])))
                self.ids.acc.add_widget(item)
                txt=str("")
                txt+="[b][color=87ceeb]"
                txt+=str("Id:"+str(dictresult[3]['id'])+"\nName:"+str(dictresult[3]['name'])+"\nPrice:"+str(dictresult[3]['price'])+"\nAddress:"+str(dictresult[3]['address']))
                txt+='[/color][/b]'
                item = AccordionItem(title='Land %d' % (4),orientation='vertical')

                item.add_widget(Button(text=txt,markup=True))
                conn=sqlite3.connect("signup.db")
                c=conn.cursor()
                x=list(c.execute("select * from register"))
                print(x)
                tok=x[0][0]
                #item.add_widget(Button(text="Bookmark",size_hint_x=0.2,on_press=lambda a:self.addbookmark(tok,dictresult[3]['id'])))
                self.ids.acc.add_widget(item)
                self.cur+=4

        # conn=sqlite3.connect("signup.db")
        # c=conn.cursor()
        # fetchlist=list(c.execute("select * from bookmarks"))
        # #print(fetchlist)
        # conn.commit()
        # c.close()
        # AllLands=[]
        # for lands in fetchlist:
        #     if(lands[0]==use):
        #       AllLands.append(lands)
        # if(len(AllLands)<4):
        #     self.cur=len(AllLands)-1
        #     for i in range(len(AllLands)):
        #         txt=str("")
        #         txt+="[b][color=87ceeb]"
        #         txt+=str(AllLands[i][0]+"\n "+AllLands[i][1]+"\n"+AllLands[i][2]+"\n"+AllLands[i][3])
        #         txt+='[/color][/b]'
        #         item = AccordionItem(title='Land %d' % (i+1),orientation='vertical')
        #         item.add_widget(Button(text=txt,markup=True))
        #         self.ids.acc.add_widget(item)
        #
        # else:
        #     for i in range(4):
        #         txt=str("")
        #         txt+="[b][color=87ceeb]"
        #         txt+=str(AllLands[i][0]+"\n "+AllLands[i][1]+"\n"+AllLands[i][2]+"\n"+AllLands[i][3])
        #         txt+='[/color][/b]'
        #         item = AccordionItem(title='Land %d' % (i+1),orientation='vertical')
        #         item.add_widget(Button(text=txt,markup=True))
        #         self.ids.acc.add_widget(item)
        #     self.cur+=4


    # def nextland(self):
    #     conn=sqlite3.connect("signup.db")
    #     c=conn1.cursor()
    #     fetchlist=list(c.execute("select * from bookmarks"))
    #    #print(fetchlist)
    #     conn.commit()
    #     c.close()
    #     AllLands=[]
    #     for lands in fetchlist:
    #         if(lands[0]==use ):
    #           AllLands.append(lands)
    #     if(len(AllLands)==self.cur+1):
    #         popup = Popup(title='Error!',content=Label(text='No More Lands!!'),size_hint=(None, None), size=(200, 200))
    #         popup.open()
    #         return
    #     else:
    #         self.ids.acc.clear_widgets()
    #         if(len(AllLands)-1-self.cur>=4):
    #             for i in range(self.cur+1,self.cur+5):
    #                 txt=str("")
    #                 txt+="[b][color=87ceeb]"
    #                 txt+=str(AllLands[i][0]+"\n "+AllLands[i][1]+"\n"+AllLands[i][2]+"\n"+AllLands[i][3])
    #                 txt+='[/color][/b]'
    #                 item = AccordionItem(title='Land %d' % (i+1),orientation='vertical')
    #                 item.add_widget(Button(text=txt,markup=True))
    #                 self.ids.acc.add_widget(item)
    #             self.cur+=4
    #         else:
    #             for i in range(self.cur+1,len(AllLands)):
    #                 txt=str("")
    #                 txt+="[b][color=87ceeb]"
    #                 txt+=str(AllLands[i][0]+"\n "+AllLands[i][1]+"\n"+AllLands[i][2]+"\n"+AllLands[i][3])
    #                 txt+='[/color][/b]'
    #                 item = AccordionItem(title='Land %d' % (i+1),orientation='vertical')
    #                 item.add_widget(Button(text=txt,markup=True))
    #                 self.ids.acc.add_widget(item)
    #             self.cur=len(AllLands)-1
    #
    #
    #
    # def prevland(self):
    #     conn=sqlite3.connect("signup.db")
    #     c=conn1.cursor()
    #     fetchlist=list(c.execute("select * from bookmarks"))
    #    #print(fetchlist)
    #     conn.commit()
    #     c.close()
    #     AllLands=[]
    #     for lands in fetchlist:
    #         if(lands[0]==use):
    #           AllLands.append(lands)
    #     if(self.cur<=3):
    #         popup = Popup(title='Error!',content=Label(text='No More Lands!!'),size_hint=(None, None), size=(200, 200))
    #         popup.open()
    #         return
    #     elif(self.cur>=3):
    #         self.cur-=411111111
    #         self.ids.acc.clear_widgets()
    #         for i in range(self.cur,self.cur+4):
    #             txt=str("")
    #             txt+="[b][color=87ceeb]"
    #             txt+=str(AllLands[i][0]+"\n "+AllLands[i][1]+"\n"+AllLands[i][2]+"\n"+AllLands[i][3])
    #             txt+='[/color][/b]'
    #             item = AccordionItem(title='Land %d' % (i+1),orientation='vertical')
    #             item.add_widget(Button(text=txt,markup=True))
    #             self.ids.acc.add_widget(item)
    #     else:
    #         self.cur=0
    #         self.ids.acc.clear_widgets()
    #         for i in range(self.cur,self.cur+4):
    #             txt=str("")
    #             txt+="[b][color=87ceeb]"
    #             txt+=str(AllLands[i][0]+"\n "+AllLands[i][1]+"\n"+AllLands[i][2]+"\n"+AllLands[i][3])
    #             txt+='[/color][/b]'
    #             item = AccordionItem(title='Land %d' % (i+1),orientation='vertical')
    #             item.add_widget(Button(text=txt,markup=True))
    #             self.ids.acc.add_widget(item)
    #         self.cur=3
    # def deletebookmarks(self):
    #     conn=sqlite3.connect("signup.db")
    #     c=conn1.cursor()
    #     c.execute("DELETE from bookmarks WHERE User='"+use+"';")
    #     conn.commit()
    #     c.close()
