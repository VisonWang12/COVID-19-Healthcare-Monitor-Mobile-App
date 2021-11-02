from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.textinput import TextInput
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
KV = '''
#:import MapView kivy.garden.mapview.MapView
<ContentNavigationDrawer>:

    ScrollView:

        MDList:

            Image:
                id: avatar
                size_hint: None, None
                size: "56dp", "56dp"
                source: "images.jpg"
            MDLabel:
                text: "Alvin Lee"
                font_style: "Button"
                size_hint_y: None
                height: self.texture_size[1]

            MDLabel:
                text: "alvinlee060706@gmail.com"
                font_style: "Caption"
                size_hint_y: None
                height: self.texture_size[1]
            OneLineIconListItem:
                text: "Profile"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"
                IconLeftWidget:
                    icon: 'account'
                    

            OneLineIconListItem:
                text: "Maps"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"
                IconLeftWidget:
                    icon: 'google-maps'
            
            OneLineIconListItem:
                text: "Score"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 4"
                IconLeftWidget:
                    icon: 'scoreboard'
            
            OneLineIconListItem:
                text: "Contant with Developer"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 3"
                IconLeftWidget:
                    icon: 'forum'
                    
            OneLineIconListItem:
                text: "Chat"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 6"
                IconLeftWidget:
                    icon: 'chat'
                    
            
            OneLineIconListItem:
                text: "Virtual Doctor"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 7"
                IconLeftWidget:
                    icon: 'doctor'
                
            OneLineIconListItem:
                text: "Log Out"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "login"
                IconLeftWidget:
                    icon: 'logout'
                    

Screen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "COVID Health Service"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    NavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "COVID Health Care Service"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                    MDBottomNavigation:
                        panel_color: 0, .7, 1, 1


                        MDBottomNavigationItem:
                            name: 'screen 1'
                            text: 'Info'
                            icon: 'information-variant'

                            MDLabel:
                                text: "Thank you for using this App! It is the first version of COVID-19 Health Service App"
                                font_style: "Caption"
                                size_hint_y: 1.58
                                height: self.texture_size[1]
                            
                            MDLabel:
                                text: "You may find a few bugs in this App. if you find it, please let me know. "
                                font_style: "Caption"
                                size_hint_y: 1.45
                                height: self.texture_size[1]
                             
                            MDLabel:
                                text: "You can contact me in 'Contact with developer'"
                                font_style: "Caption"
                                size_hint_y: 1.22
                                height: self.texture_size[1]
                
                    
                Widget:
            
            Screen:
                name: "scr 1"
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "COVID Health Service"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                   
                    Image:
                        id: avatar
                        size_hint: None, None
                        size: "56dp", "56dp"
                        source: "images.jpg"
                    MDLabel:
                        text: "Username: Alvin Lee"
                        font_style: "Button"
                        size_hint_y: 0.3
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Email: alvinlee060706@gmail.com"
                        font_style: "Caption"
                        size_hint_y: 0.3
                        height: self.texture_size[1]
                    MDLabel:
                        text: "Age: 14"
                        font_style: "Caption"
                        size_hint_y: 0.3
                        height: self.texture_size[1]
                    MDLabel:
                        text: "Country: China"
                        font_style: "Caption"
                        size_hint_y: 0.3
                        height: self.texture_size[1]
                    MDLabel:
                        text: "COVID-19 Condition: Less Than 10%"
                        font_style: "Caption"
                        size_hint_y: 0.3
                        height: self.texture_size[1]
                    MDLabel:
                        text: "Cellphone: +1 326-578429"
                        font_style: "Caption"
                        size_hint_y: 0.3
                        height: self.texture_size[1]
                    MDLabel:
                        text: "Emergency Contact: +86 137-5587-6651"
                        font_style: "Caption"
                        size_hint_y: 0.3
                        height: self.texture_size[1]
                    MDLabel:
                        text: "If you have any question about this App, "
                        font_style: "Caption"
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDLabel:
                        text: "Please Contact Me: "
                        font_style: "Caption"
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDLabel:
                        text: "WeChat: AlvinLee200676"
                        font_style: "Caption"
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDLabel:
                        text: "Alvin Lee"
                        font_style: "Caption"
                        size_hint_y: 1
                        height: self.texture_size[1]
                    MDBottomNavigation:
                        panel_color: 0, .7, 1, 1
                        
                        MDBottomNavigationItem:
                            name: 'screen 1'
                            text: 'Info'
                            icon: 'information-variant'
                            MDLabel:
                                text: ' '
                                halign: 'center'
                        
                Widget:

            Screen:
                name: "scr 2"
                MapView:
                    lat: 10
                    lon: 10
                    zoom: 5
                    on_lat:
                        print('lat', self.lat)
                    on_lon:
                        print('lon', self.lon)
                    MapMarkerPopup:
                        lat: 11
                        lon: 11
                        Button:
                            on_release:
                                #root.center_on(14, 14)
                                print(root.get_bbox())
                
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Maps"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                        
                    Widget:
            Screen:
                name: "scr 4"
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "About Test"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                    
                    MDLabel:
                        text: "It is a test which will help you better know your health and protect yourself"
                        font_style: "Caption"
                        size_hint_y: 0.3
                        height: self.texture_size[1]
                        
                    MDLabel:
                        text: "It will take you a few minutes to answer these question"
                        font_style: "Caption"
                        size_hint_y: 0.3
                        height: self.texture_size[1]
                    MDLabel:
                        text: "0-60: Terrible(You should go to hospital)"
                        font_style: "Caption"
                        size_hint_y: 0.3
                        height: self.texture_size[1]
                    MDLabel:
                        text: "60-80 Just Fine(You may have some healthy problem which is not serious)"
                        font_style: "Caption"
                        size_hint_y: 0.3
                        height: self.texture_size[1]
                    MDLabel:
                        text: "80-100 Very Healthy(You do not have any healthy problem, only thing you need to do is wearing masks"
                        font_style: "Caption"
                        size_hint_y: 0.3
                        height: self.texture_size[1]
                    
                    MDLabel:
                        text: "1. Do you have any medication?"
                        font_style: "Caption"
                        size_hint_y: 0.3
                        height: self.texture_size[1]
                    GridLayout:
                        cols: 1
                        TextInput:
                            id: username
                            size_hint: (.2, None)
                            height: 40
                            multiline:False
                    MDLabel:
                        text: "2. Do you have fever or cough in the last 2 weeks?(Yes/No)"
                        font_style: "Caption"
                        size_hint_y: 0.5
                        height: self.texture_size[1]
                    MDLabel:
                        text: "Yes"
                        font_style: "Caption"
                        size_hint_y: None
                        height: self.texture_size[1]
                    Button:
                        text: "0+"
                        size_hint: 0.3, 0.5
                        background_color: (0.7, 0.0, 0.0, 1.0)
                        on_press: entry.text += self.text
                    MDLabel:
                        text: "No"
                        font_style: "Caption"
                        size_hint_y: None
                        height: self.texture_size[1]
                    Button:
                        text: "10+"
                        size_hint: 0.3, 0.5
                        background_color: (0.7, 0.0, 0.0, 1.0)
                        on_press: entry.text += self.text
                    
                    MDLabel:
                        text: "3. Before using this app, did you wear mask when you go out?(Yes/No)"
                        font_style: "Caption"
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDLabel:
                        text: "Yes"
                        font_style: "Caption"
                        size_hint_y: None
                        height: self.texture_size[1]
                    Button:
                        text: "35+"
                        size_hint: 0.3, 0.5
                        background_color: (0.7, 0.0, 0.0, 1.0)
                        on_press: entry.text += self.text
                    MDLabel:
                        text: "No"
                        font_style: "Caption"
                        size_hint_y: None
                        height: self.texture_size[1]
                    Button:
                        text: "10+"
                        size_hint: 0.3, 0.5
                        background_color: (0.7, 0.0, 0.0, 1.0)
                        on_press: entry.text += self.text
                    MDLabel:
                        text: "4. Did your family member ever get COVID-19 infection?(Yes/No)"
                        font_style: "Caption"
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDLabel:
                        text: "Yes"
                        font_style: "Caption"
                        size_hint_y: None
                        height: self.texture_size[1]
                    Button:
                        text: "10+"
                        size_hint: 0.3, 0.5
                        background_color: (0.7, 0.0, 0.0, 1.0)
                        on_press: entry.text += self.text
                    MDLabel:
                        text: "No"
                        font_style: "Caption"
                        size_hint_y: None
                        height: self.texture_size[1]
                    Button:
                        text: "35+"
                        size_hint: 0.3, 0.5
                        background_color: (0.7, 0.0, 0.0, 1.0)
                        on_press: entry.text += self.text
                    MDLabel:
                        text: "6. Did you stay in NYC, NJ, CA before in 2020?(Yes/No)"
                        font_style: "Caption"
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDLabel:
                        text: "Yes"
                        font_style: "Caption"
                        size_hint_y: None
                        height: self.texture_size[1]
                    Button:
                        text: "30"
                        size_hint: 0.3, 0.5
                        background_color: (0.7, 0.0, 0.0, 1.0)
                        on_press: entry.text += self.text
                    MDLabel:
                        text: "No"
                        font_style: "Caption"
                        size_hint_y: None
                        height: self.texture_size[1]
                    Button:
                        text: "10"
                        size_hint: 0.3, 0.5
                        background_color: (0.7, 0.0, 0.0, 1.0)
                        on_press: entry.text += self.text
                    MDLabel:
                        text: "Alvin Lee"
                        font_style: "Caption"
                        size_hint_y: 1
                        height: self.texture_size[1]
                    
                    Button:
                        text: "Submit"
                        size_hint: 0.3, 0.5
                        background_color: (0.7, 0.0, 0.0, 1.0)
                        on_press: 
                            
  
                    BoxLayout:
                        TextInput:
                            id: entry
                            font_size: 32
                            multiline: False

                            
                Widget:
            Screen:
                name: "scr 3"
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "COVID Health Service"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                    Image:
                        id: avatar
                        size_hint: None, None
                        size: "56dp", "56dp"
                        source: "images.jpg"
                    MDLabel:
                        text: "If you have any question about this App, "
                        font_style: "Caption"
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDLabel:
                        ext: "Please Contact Me: "
                        font_style: "Caption"
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDLabel:
                        text: "Alvin Lee"
                        font_style: "Button"
                        size_hint_y: 0.3
                        height: self.texture_size[1]
                    
                    MDLabel:
                        text: "Email: alvinlee060706@gmail.com"
                        font_style: "Caption"
                        size_hint_y: 0.3
                        height: self.texture_size[1]
                   
                    MDLabel:
                        text: "Country: China"
                        font_style: "Caption"
                        size_hint_y: 0.3
                        height: self.texture_size[1]
                    
                    MDLabel:
                        text: "Cellphone: +86 17849524759"
                        font_style: "Caption"
                        size_hint_y: 0.3
                        height: self.texture_size[1]
                    
                    
                    
                    MDLabel:
                        text: "WeChat: AlvinLee200676"
                        font_style: "Caption"
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDLabel:
                        text: "Alvin Lee"
                        font_style: "Caption"
                        size_hint_y: 1
                        height: self.texture_size[1]
                        
                MDLabel:
                    text: " "
                    halign: "center"
            Screen:
                name: "scr 6"
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "COVID Health Service"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                    MDLabel:
                        text: "Email Address: "
                        font_style: "Caption"
                        size_hint_y: None
                        height: self.texture_size[1]
                    GridLayout:
                        cols: 1
                        TextInput:
                            id: email
                            size_hint: (None, None)
                            width: 300
                            height: 40
                            multiline:False
                    MDLabel:
                        text: "Title: "
                        font_style: "Caption"
                        size_hint_y: None
                        height: self.texture_size[1]
                    GridLayout:
                        cols: 1
                        TextInput:
                            id: title
                            size_hint: (.2, None)
                            multiline:False
                    MDLabel:
                        text: "Content: "
                        font_style: "Caption"
                        size_hint_y: None
                        height: self.texture_size[1]
                    GridLayout:
                        cols: 1
                        TextInput:
                            id: email
                            size_hint: (.2, None)
                            multiline:False
                    Button:
                        text: "Send"
                        size_hint: 0.3, 0.5
                        background_color: (0.7, 0.0, 0.0, 1.0)
            
                      
            Screen:
                name: "scr 7"
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Virtual Doctor"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                   
                    Image:
                        id: avatar
                        size_hint: None, None
                        size: "56dp", "56dp"
                        source: "3141452.jpg"
                    MDLabel:
                        text: "Name: ZhongWei Chen"
                        font_style: "Button"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Hospital: Affiliated Hospital of Qingdao Binhai University"
                        font_style: "Caption"
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDLabel:
                        text: "Country: China"
                        font_style: "Caption"
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDLabel:
                        text: "Introduction: Chief physician, professor, master tutor, bachelor degree. Good at the diagnosis and treatment of diabetes and various acute and chronic complications, as well as the diagnosis and treatment of various cerebrovascular diseases in the acute and recovery phases, epilepsy, motor neuron disease, tremor paralysis, nervous system infection, and neurodegenerative diseases . From 1985 to 2003, he worked in the Department of Neurology at Tiemei Group General Hospital of Liaoning Province. In 1990, he studied neurology at Beijing Medical University. Since 2003, he has been engaged in neuroendocrine research and diagnosis and treatment of diabetes complications. In 2008, he studied at Tokyo Medical College, Japan. ."
                        font_style: "Caption"
                        size_hint_y: None
                        height: self.texture_size[1]
                    Image:
                        id: avatar
                        size_hint: None, None
                        size: "56dp", "56dp"
                        source: "85763821.jpg"
                    MDLabel:
                        text: "Name: YunXiao Zhang"
                        font_style: "Button"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Hospital: The First Affiliated Hospital of Xingtai Medical College"
                        font_style: "Caption"
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDLabel:
                        text: "Country: China"
                        font_style: "Caption"
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDLabel:
                        text: "Introduction: Chief physician, graduated in clinical medicine, good at diagnosis and treatment of leukemia, lymphoma, myeloma and various anemias, and works in the First Affiliated Hospital of Xingtai Medical College."
                        font_style: "Caption"
                        size_hint_y: None
                        height: self.texture_size[1]
                    Widget:
                    
            Screen:
                name: "login"
                BoxLayout:
                    orientation: 'vertical' 
                    canvas.before:
                        Rectangle:
                            pos:self.pos
                            size:self.size
                            source: "maskl.jpg"
                    GridLayout:
                        cols:1
                        size: root.width - 200, root.height - 200

                        GridLayout:
                            cols:2

                            Label:
                                text:"Name: "

                            TextInput:
                                id: name
                                multiline:False

                            Label:
                                text:"Email: "

                            TextInput:
                                id: email
                                multiline:False

                            Label:
                                text:"Password: "

                            TextInput:
                                id: password
                                multiline:False
                                password: "True"
                                password_mask: "*"
                            Button:
                                background_color: (1.0, 0.0, 0.0, 1.0)
                                text: "Log In"
                                on_release:
                                    app.root.current = "scr 1"

                            Button:
                                background_color: (1.0, 0.0, 0.0, 1.0)
                                text: "Create Account"
                                on_release: 
                                    app.root.current = "register"
                                WindowManager:
                                    Register:
                                    
                                Widget:

        MDNavigationDrawer: 
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
                            
                            
<Register>
    name: "register"
    
                   
                
                   
                  
'''
class Register(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class CalGridLayout(GridLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class CalculatorApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
        

CalculatorApp().run()
