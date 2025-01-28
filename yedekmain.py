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
from kivymd.uix.menu import MDDropdownMenu
from kivy_garden.mapview import MapView, MapLayer, MapMarker, MapSource
from kivy.graphics import Color, Line
import requests
import json
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivymd.uix.navigationdrawer import (
    MDNavigationDrawerItem, MDNavigationDrawerItemTrailingText
    )

# .kv dosyasını manuel olarak yükle
Builder.load_file('main.kv')

class CustomTileLayer(MapLayer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tile_service = "https://cbs.rizeozelidare.gov.tr/geodataserver/api/v1/collections/TKGM_PARSEL/tiles/WebMercatorQuad/{z}/{x}/{y}?&access_token=pVPS0BjanTPwYePOECyb6DIu"

    def reposition(self):
        self.canvas.clear()
        mapview = self.parent
        if not mapview:
            return
        zoom = int(mapview.zoom)
        min_x = int(mapview.lon) - 2
        max_x = int(mapview.lon) + 2
        min_y = int(mapview.lat) - 2
        max_y = int(mapview.lat) + 2
        for x in range(min_x, max_x):
            for y in range(min_y, max_y):
                tile = self.tile_service.format(z=zoom, x=x, y=y)
                with self.canvas:
                    Color(1, 1, 1, 0.8)
                    Line(points=[x, y, x + 1, y + 1])

class MainScreen(MDBoxLayout):
    def build(self):
        mapview = MapView()
        mapview.add_layer(CustomTileLayer())
        return mapview

class MapApp(MDApp):

    selected_item = StringProperty("")  # Seçili olan öğeyi takip et
    def menu_open(self):
        service_data = [
            {"name": "EsriWorldImagery", "url": "https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"},
            {"name": "EsriBasemap", "url": "https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}"},
            {"name": "EsriTopograpyMap", "url": "http://services.arcgisonline.com/ArcGIS/rest/services/Elevation/World_Hillshade/MapServer/tile/{z}/{y}/{x}"},
            {"name": "OpenStreetMap", "url": "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"},
            {"name": "OpenTopoMaps", "url": "https://tile.opentopomap.org/{z}/{x}/{y}.png"},
            {"name": "GoogleSatallite", "url": "http://mt0.google.com/vt/lyrs=y&hl=en&x={x}&y={y}&z={z}"},
            {"name": "GoogleMaps", "url": "https://mt1.google.com/vt/lyrs=r&x={x}&y={y}&z={z}"},
            {"name": "GoogleRoads", "url": "https://mt1.google.com/vt/lyrs=h&x={x}&y={y}&z={z}"},
            {"name": "GoogleSatalliteHybrid", "url": "https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}"},            
        ]

        menu_items = [
            {
                "text": service["name"],
                "on_release": lambda x=service: self.menu_callback(x),
                "theme_text_color": "Custom",
                "text_color": self.get_item_color(service["name"]),
            } for service in service_data
        ]
        MDDropdownMenu(
            caller=self.root.ids.btnLayer,
            items=menu_items,
            width= max([len(service['name']) for service in service_data]) * dp(10) # Responsive bir genişlik çarpanı
        ).open()


    def get_item_color(self, name):
        # Seçili olan öğe ise koyu renk
        if name == self.selected_item:
            return [0, 0, 0, 1]  # Siyah renk (koyu)
        return [0.2, 0.2, 0.2, 1]  # Diğer öğeler için gri renk
    
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

        return MainScreen()

if __name__ == "__main__":
    MapApp().run()
