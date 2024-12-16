from kivy.config import Config

# Farklı çözünürlükleri test etmek için pencere boyutunu ayarla
Config.set('graphics', 'width', '360')   # Genişlik (örnek: telefon çözünürlüğü)
Config.set('graphics', 'height', '640')  # Yükseklik (örnek: telefon çözünürlüğü)
Config.set('graphics', 'resizable', True)  # Pencereyi yeniden boyutlandırılabilir yap

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout  
from kivymd.uix.appbar import MDTopAppBar, MDBottomAppBar
from kivy.lang import Builder  # .kv dosyasını manuel yüklemek için
from kivy_garden.mapview import MapView
from kivy_garden.mapview import MapView, MapSource, MapLayer
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
import requests
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.core.image import Image as CoreImage
from io import BytesIO
from pyproj import Transformer

# .kv dosyasını manuel olarak yükle
Builder.load_file('main.kv')

class ExportMapLayer(MapLayer):
    def __init__(self, url_template, bbox, width=512, height=512, **kwargs):
        super().__init__(**kwargs)
        self.url_template = url_template
        self.bbox = bbox
        self.width = width
        self.height = height

    def reposition(self):
        mapview = self.parent
        if not mapview:
            return

        self.canvas.clear()
        with self.canvas:
            Color(1, 1, 1, 1)  # Şeffaflık
            export_url = self.url_template.format(
                bbox=self.bbox,
                width=self.width,
                height=self.height,
                dpi=96,
                format="png"
            )
            print(f"Export URL: {export_url}")  # Hata ayıklama için URL'yi yazdır
        try:
            response = requests.get(export_url)
            response.raise_for_status()
            print(f"Görüntü boyutu: {len(response.content)} byte")
            image_data = BytesIO(response.content)
            export_image = CoreImage(image_data, ext="png")
            Rectangle(
                texture=export_image.texture,
                pos=(0, 0),
                size=(self.width, self.height),
            )
        except Exception as e:
            print(f"Hata: {e}, Export URL: {export_url}")


class MainScreen(MDBoxLayout):
    def build(self):
        mapview = MapView()
        return mapview

class MapApp(MDApp):


    def menu_open(self):
        service_data = [
            {"name": "EsriWorldImagery", "url": "https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"},
            {"name": "OpenStreetMap", "url": "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"},
            {"name": "EsriTopographic", "url": "https://services.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}"},
        ]

        menu_items = [
            {
                "text": service["name"],
                "on_release": lambda x=service: self.menu_callback(x),
            } for service in service_data
        ]
        MDDropdownMenu(
            caller=self.root.ids.btnLayer,
            items=menu_items,
            width= max([len(service['name']) for service in service_data]) * dp(10) # Responsive bir genişlik çarpanı
        ).open()

    def menu_callback(self, service):
        print(f"Seçilen harita: {service['name']}, URL: {service['url']}")
        # Harita URL'sini MapView'da güncelle
        map_area = self.root.ids.map_area
        for child in map_area.children:
            if isinstance(child, MapView):
                child.map_source = MapSource(
                    url=service['url'],
                    attribution="Custom Map",
                    min_zoom=1,
                    max_zoom=19,
                )
                return
        print("MapView bileşeni bulunamadı veya uygun değil.")

    def build(self):
        self.title="İmar Durumu Sorgulama"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Olive"  # "Purple", "Red"

        main_screen = MainScreen()

        mapview = MapView()

        # EPSG:32637 -> EPSG:4326 dönüşümü
        transformer = Transformer.from_crs("EPSG:32637", "EPSG:4326")
        bbox_utm = [612841.8968000002, 4493659.852399999, 692499.5865000002, 4577079.430400001]  # Örnek EPSG:32637 bbox değerleri
        min_lon, min_lat = transformer.transform(bbox_utm[0], bbox_utm[1])
        max_lon, max_lat = transformer.transform(bbox_utm[2], bbox_utm[3])
        bbox = f"{min_lon},{min_lat},{max_lon},{max_lat}"

        # Rize KYA ek katmanı ekleniyor
        rize_kya_layer = ExportMapLayer(
            url_template="https://cbs.rizeozelidare.gov.tr/server/rest/services/IDARE/KYA/MapServer/export?bbox={bbox}&size={width},{height}&dpi=96&format=png&f=image&sr=3857",
            bbox=bbox,  # Dönüştürülmüş EPSG:4326 bbox değerleri
            width=1024,
            height=1024
        )
        mapview.add_layer(rize_kya_layer)
        main_screen.add_widget(mapview)

        return main_screen

if __name__ == "__main__":
    MapApp().run()
