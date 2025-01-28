from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy_garden.mapview import MapView, MapMarker


# .kv dosyasını manuel olarak yükle
Builder.load_file('mainqwen.kv')

class MapScreen(Screen):
    def __init__(self, **kwargs):
        super(MapScreen, self).__init__(**kwargs)

class MapApp(MDApp):
    def build(self):
        return MapScreen()

if __name__ == '__main__':
    MapApp().run()