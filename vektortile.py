from kivy_garden.mapview import MapView, MapSource
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class CustomMapSource(MapSource):
    def __init__(self, **kwargs):
        # Özel MapSource tanımlaması
        super().__init__(
            url="https://cbs.rizeozelidare.gov.tr/geodataserver/api/v1/collections/TKGM_PARSEL/tiles/WebMercatorQuad/{z}/{x}/{y}?&access_token=pVPS0BjanTPwYePOECyb6DIu",
            cache_key="custom_tile",
            tile_size=256,  # Tile boyutu (genellikle 256x256 pikseldir)
            image_ext="png",  # Resim formatı
            attribution="© Rize Özel İdare",
        )

class CustomMapView(MapView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.map_source = CustomMapSource()  # Özel MapSource'u kullanıyoruz
        self.zoom = 14  # Başlangıç zoom seviyesi
        self.lat = 41.0245  # Başlangıç enlem
        self.lon = 40.5234  # Başlangıç boylam

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        self.map_view = CustomMapView()
        layout.add_widget(self.map_view)
        return layout

if __name__ == "__main__":
    MainApp().run()
