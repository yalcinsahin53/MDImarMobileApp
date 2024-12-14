from kivy.config import Config

# Farklı çözünürlükleri test etmek için pencere boyutunu ayarla
Config.set('graphics', 'width', '360')   # Genişlik (örnek: telefon çözünürlüğü)
Config.set('graphics', 'height', '640')  # Yükseklik (örnek: telefon çözünürlüğü)
Config.set('graphics', 'resizable', True)  # Pencereyi yeniden boyutlandırılabilir yap

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder  # .kv dosyasını manuel olarak yüklemek için
from kivy_garden.mapview import MapView, MapLayer
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock

# .kv dosyasını manuel olarak yükle
Builder.load_file('main.kv')

class WMSLayer(MapLayer):
    def __init__(self, wms_url, layer_name, **kwargs):
        super().__init__(**kwargs)
        self.wms_url = wms_url
        self.layer_name = layer_name

    def reposition(self):
        self.draw_wms()

    def draw_wms(self):
        map_view = self.parent
        if not map_view:
            return

        # MapView'ın BBox değerlerini dinamik olarak al
        xmin, ymin, xmax, ymax = map_view.get_bbox()

        # WMS URL oluşturma
        tile_url = (
            f"{self.wms_url}?service=WMS&request=GetMap&layers={self.layer_name}&"
            f"bbox={xmin},{ymin},{xmax},{ymax}&width=512&height=512&"
            f"srs=EPSG:3857&format=image/png&transparent=true"
        )

        # Katmanı çiz
        with self.canvas:
            self.canvas.clear()
            Color(1, 1, 1, 1)
            Rectangle(source=tile_url, pos=map_view.pos, size=map_view.size)

class MainScreen(MDBoxLayout):
    pass

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
            width=max([len(service['name']) for service in service_data]) * 10
        ).open()

    def menu_callback(self, service):
        print(f"Seçilen harita: {service['name']}, URL: {service['url']}")
        map_view = self.root.ids.map_view
        map_view.map_source = service['url']

    def add_overlay_layers(self):
        overlay_layers = [
            {"name": "KYA Servisi", "url": "https://cbs.rizeozelidare.gov.tr/server/services/IDARE/KYA/MapServer/WMSServer", "layer_name": "0"},
            {"name": "TKGM Servisi", "url": "https://cbs.rizeozelidare.gov.tr/server/services/IDARE/TKGM/MapServer/WMSServer", "layer_name": "0"}
        ]

        map_view = self.root.ids.map_view
        for overlay in overlay_layers:
            layer = WMSLayer(wms_url=overlay['url'], layer_name=overlay['layer_name'])
            map_view.add_layer(layer)

    def build(self):
        self.title = "İmar Durumu Sorgulama"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Olive"

        screen = MainScreen()
        Clock.schedule_once(lambda dt: self.add_overlay_layers())
        return screen

if __name__ == "__main__":
    MapApp().run()
