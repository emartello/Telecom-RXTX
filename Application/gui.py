import pySerial
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.config import Config

Config.read('config.ini')

class frmPrincipal(BoxLayout):
    def __init__(self, **kwargs):
        super(frmPrincipal, self).__init__(**kwargs)
        self.orientation='horizontal'
        self.spacing=10
        self.btn1 = Button(text='LIGA', size=(200, 100), size_hint=(None, None))
        self.btn2 = Button(text='DESLIGA', size=(200, 100), size_hint=(None, None))
        self.add_widget(self.btn1)
        self.add_widget(self.btn2)
        self.add_widget(Label(text='LED'))

class MyApp(App):
    def build(self):
        return frmPrincipal()

if __name__ == '__main__':
    MyApp().run()