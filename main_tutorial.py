from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.appbar import MDTopAppBar 

class Example(MDApp):
    def build(self):
        return Builder.load_file("main_tutorial.kv")


Example().run()