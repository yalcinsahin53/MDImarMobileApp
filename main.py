from kivy.config import Config

# Farklı çözünürlükleri test etmek için pencere boyutunu ayarla
Config.set('graphics', 'width', '360')   # Genişlik (örnek: telefon çözünürlüğü)
Config.set('graphics', 'height', '640')  # Yükseklik (örnek: telefon çözünürlüğü)
Config.set('graphics', 'resizable', True)  # Pencereyi yeniden boyutlandırılabilir yap



from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout  
from kivymd.uix.appbar import MDTopAppBar
from kivymd.uix.appbar import MDBottomAppBar
from kivy.lang import Builder  # .kv dosyasını manuel yüklemek için
from kivy_garden.mapview import MapView
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp


# .kv dosyasını manuel olarak yükle
Builder.load_file('main.kv')

class MainScreen(MDBoxLayout):
    def build(self):
        mapview = MapView()
        return mapview

class MapApp(MDApp):

    def menu_open(self):
        menu_items = [
            {
                "text": f"Item {i}",
                "on_release": lambda x=f"Item {i}": self.menu_callback(x),
            } for i in range(5)
        ]
        MDDropdownMenu(
            caller=self.root.ids.btnLayer,
            items=menu_items,
        ).open()

    def menu_callback(self, text_item):
        print(text_item)

    def build(self):
        self.title="İmar Durumu Sorgulama"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Olive"  # "Purple", "Red"
        return MainScreen()

if __name__ == "__main__":
    MapApp().run()
