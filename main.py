from functools import partial
from typing import OrderedDict
import kivy
from kivy.uix.button import Button
from speech_detector import spech_detector
kivy.require('2.0.0') 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
import threading
from kivy.properties import StringProperty


class MainScreen(BoxLayout):
    screenText = StringProperty()
    def __init__(self, **kwargs):
        super(MainScreen,self).__init__(**kwargs)
        self.screenText = 'Speech to Mouse'
        layout = BoxLayout(orientation='vertical')
        bottomLayout = BoxLayout(orientation='horizontal')
        l = Label(text=self.screenText,font_size='75sp') 
        btn2 = Button(text='            Begin\n Speech Recognition',font_size='20sp',size_hint =(.5, .25))
        btn2.bind(on_press=self.callback)
        TextList = Label(text='Command List:\n Mouse Up/Move Up\n Mouse Down/Move Down\n Mouse Left/Move Left\n Mouse Right/Move Right\n Stop\n Exit Program\n')
        anchorLayout = AnchorLayout(anchor_x='center', anchor_y='center')
        anchorLayout.add_widget(btn2)
        bottomLayout.add_widget(anchorLayout)
        bottomLayout.add_widget(TextList)
       
        layout.add_widget(l)
        layout.add_widget(bottomLayout)
        self.bind(screenText = partial(self.screen_text_changed,l))
        self.add_widget(layout)

    def screen_text_changed(self,label,mainScreen,screentext):
        label.text = screentext
    
    def callback_thread(self):
        
        for text in spech_detector():
            self.screenText = text
    
    def callback(self,instance):
        threading.Thread(target=self.callback_thread,daemon=True).start()            
class MyApp(App):

     
    def build(self):
        return MainScreen()
        

 

if __name__ == '__main__':
    MyApp().run()