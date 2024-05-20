from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file("front.kv")

class meuApp(App):
    def build(self):
        return GUI
    
meuApp().run()