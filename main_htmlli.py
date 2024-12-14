from kivy.config import Config

# Farklı çözünürlükleri test etmek için pencere boyutunu ayarla
Config.set('graphics', 'width', '360')   # Genişlik (örnek: telefon çözünürlüğü)
Config.set('graphics', 'height', '640')  # Yükseklik (örnek: telefon çözünürlüğü)
Config.set('graphics', 'resizable', True)  # Pencereyi yeniden boyutlandırılabilir yap

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder  # .kv dosyasını manuel yüklemek için
from kivy_garden.mapview import MapView
from kivy_garden.webview import WebView
from kivy.clock import Clock
import os

# .kv dosyasını manuel olarak yükle
Builder.load_file('main.kv')

class MainScreen(MDBoxLayout):
    pass

class MapApp(MDApp):

    def build(self):
        self.title = "İmar Durumu Sorgulama"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Olive"

        screen = MainScreen()
        Clock.schedule_once(self.load_webview)
        return screen

    def load_webview(self, *args):
        # WebView için bir HTML dosyası oluşturuyoruz
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Harita Görselleştirme</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <script src="https://js.arcgis.com/4.21/"></script>
            <style>
                html, body, #map {
                    padding: 0;
                    margin: 0;
                    height: 100%;
                    width: 100%;
                }
            </style>
        </head>
        <body>
            <div id="map"></div>
            <script>
                require(["esri/Map", "esri/views/MapView", "esri/layers/MapImageLayer"], function(Map, MapView, MapImageLayer) {
                    var map = new Map({
                        basemap: "streets"
                    });

                    var kyaLayer = new MapImageLayer({
                        url: "https://cbs.rizeozelidare.gov.tr/server/rest/services/IDARE/KYA/MapServer"
                    });

                    var tkgmLayer = new MapImageLayer({
                        url: "https://cbs.rizeozelidare.gov.tr/server/rest/services/IDARE/TKGM/MapServer"
                    });

                    map.add(kyaLayer);
                    map.add(tkgmLayer);

                    var view = new MapView({
                        container: "map",
                        map: map,
                        center: [41.0, 41.0], // Harita merkezi (Rize koordinatları örnek)
                        zoom: 10
                    });
                });
            </script>
        </body>
        </html>
        """

        # HTML dosyasını kaydet
        html_file = os.path.join(os.getcwd(), "map.html")
        with open(html_file, "w") as f:
            f.write(html_content)

        # WebView kullanarak HTML'yi yükle
        webview = WebView()
        webview.url = f"file://{html_file}"

        # Ana ekran üzerine ekle
        self.root.add_widget(webview)

if __name__ == "__main__":
    MapApp().run()
