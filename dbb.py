from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel 
from kivymd.uix.list import TwoLineListItem,ThreeLineListItem
from kivy.uix.scrollview import ScrollView
from kivymd.uix.button import MDIconButton, MDRectangleFlatButton,MDFloatingActionButton 
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager,FadeTransition
import base64,hashlib,os,zlib,json
from kivymd.uix.dialog import MDDialog
from kivy.uix.popup import Popup
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.label import Label
from kivymd.uix.textfield import TextInput
from kivymd.uix.toolbar import MDToolbar

class Database:
    def __init__(self):
        self.dic = matter
        
    def createdic(self):
        self.database=json.dumps({"Name":str(matter[0]),"Matric No":str(matter[2]),"Department":str(matter[1]),"Gender":str(matter[3]),"Age":str(matter[4]),"Address":str(matter[5])})
    def savedata(self):
        try:
            if os.path.exists(base_path + '/database.json'):
                with open(base_path + '/database.json','a') as e:
                    e.write('\n')
                    e.write(self.database)
            else:
                with open(base_path + '/database.json','w') as e:
                    e.write('\n')
                    e.write(self.database)
        except Exception as ex:
            print(ex)
            

def readDatabase_Createwidget(path):
    info_list=[]
    if os.path.exists(path + '/database.json'):
        with open(path + '/database.json','r') as e:
            for dic in e:
                
                dic=json.loads(dic)
                info_list.append(dic)
        widget_list=[]
        for i in info_list:
            widg = ThreeLineListItem(text=Scramble(i['Name']).unscramble(),secondary_text=Scramble(i['Matric No']).unscramble(),tertiary_text=Scramble(i['Department']).unscramble())
            widget_list.append(widg)
        return widget_list
    else:
        return []
        
class Scramble:
    def __init__(self,word) :
        self.word = bytes(word,'utf-8')
    def scramble(self):
        return base64.urlsafe_b64encode(zlib.compress(self.word,9))
    def unscramble(self):
        return zlib.decompress(base64.urlsafe_b64decode(self.word))

class Screen1(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.litem = TwoLineListItem()
        base_path = os.getcwd() + '/stRecords/'
        #if os.path.exists(base_path):
           # pass
        #else:
           # os.system(f'mkdir {base_path}')
       # print(base_path)
        icbn = MDFloatingActionButton(icon='plus',pos_hint={'bottom':1,'right':1},on_press=self.of)
        tooltop = Tops()
        main=MDBoxLayout(orientation='vertical',pos_hint={'top':1})
        #main.add_widget(tooltop)
        self.add_widget(tooltop)
        
        
        
        scroll = ScrollView()
        scroll.add_widget(self.litem)
        self.add_widget(scroll)
        self.add_widget(icbn)
        self.form = FormField()
    def of(self,instance):
        self.form.open()
        
    pass

class FormField(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (.5,.38)
        self.pos_hint = {'center_x':.5,'center_y':.5}
        self.title = 'Student Information'
        self.main = MDBoxLayout(orientation='vertical')
        namein = MDBoxLayout(orientation='horizontal')
        namein.add_widget(Label(text='Name',font_size='12sp',halign='left'))
        self.named = TextInput(multiline=False)
        namein.add_widget(self.named)
        matin = MDBoxLayout(orientation='horizontal')
        matin.add_widget(Label(text='Matric No',font_size='12sp',halign='left'))
        self.mat = TextInput(multiline=False)
        matin.add_widget(self.mat)
        deptin = MDBoxLayout(orientation='horizontal')
        deptin.add_widget(Label(text='Department',font_size='12sp',halign='left'))
        self.dept = TextInput(multiline=False)
        deptin.add_widget(self.dept)
        agein = MDBoxLayout(orientation='horizontal')
        agein.add_widget(Label(text='Age',font_size='12sp',halign='left'))
        self.age = TextInput(multiline=False)
        agein.add_widget(self.age)
        genin = MDBoxLayout(orientation='horizontal')
        genin.add_widget(Label(text='Gender',font_size='12sp',halign='left'))
        self.gender = TextInput(multiline=False)
        genin.add_widget(self.gender)
        addin = MDBoxLayout(orientation='horizontal')
        addin.add_widget(Label(text='Address Info',font_size='12sp',halign='left'))
        self.addr = TextInput(multiline=False)
        addin.add_widget(self.addr)
        wids = [namein,matin,deptin,genin,agein,addin]
        for i in wids:
            self.main.add_widget(i)
        self.main.add_widget(MDRectangleFlatButton(text='Submit',on_press=self.submit))
        self.add_widget(self.main)
    def submit(self,obj):
        self.info =[self.named.text,self.dept.text,self.mat.text,self.gender.text,self.age.text,self.addr.text]
        for i in range(len(self.info)):
            try:
                self.info[i]=str(i)
                self.info[i] = Scramble(self.info[i]).scramble()
            except Exception as e:
                print(e)
        global matter 
        matter = self.info
        bigobj = Database()
        bigobj.createdic()
        bigobj.savedata()
        self.dismiss()
            
class Tops(MDToolbar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.opposite_colors = True 
        self.pos_hint ={'top':1}
        self.elevation =20

class Db(MDApp):
    scrambler = Scramble
    def build(self):
        self.on_start = self.started
        self.theme_cls.primary_palette='Blue'
        self.sc = Screen1()
        self.root = ScreenManager(transition=FadeTransition())
        self.root.add_widget(self.sc)
    def started(self):
        global base_path
        base_path = os.getcwd() + '\\stRecords\\'
        if os.path.exists(base_path):
            pass
        else:
            os.system(f'mkdir {base_path}')
        print(base_path)
        lists=readDatabase_Createwidget(base_path)
        for i in lists:
            self.sc.litem.add_widget(i)
        return super().build()
Db().run()