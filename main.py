from kivy.config import Config

# Farklı çözünürlükleri test etmek için pencere boyutunu ayarla
Config.set('graphics', 'width', '360')   # Genişlik (örnek: telefon çözünürlüğü)
Config.set('graphics', 'height', '640')  # Yükseklik (örnek: telefon çözünürlüğü)
Config.set('graphics', 'resizable', True)  # Pencereyi yeniden boyutlandırılabilir yap

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout    
from kivy.lang import Builder  # .kv dosyasını manuel yüklemek için
from kivy_garden.mapview import MapView

# .kv dosyasını manuel olarak yükle
Builder.load_file('main.kv')

class MainScreen(MDBoxLayout):
    def build(self):
        mapview = MapView()
        return mapview


class MapApp(MDApp):
    def build(self):
        return MainScreen()

if __name__ == "__main__":
    MapApp().run()
