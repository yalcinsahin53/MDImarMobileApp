import folium

# Harita oluşturma - başlangıç merkezi ve zoom seviyesi
map_center = [40.9234, 40.2234]  # Rize koordinatlarına yakın bir merkez noktası
zoom_level = 14

# Folium haritasını başlat
m = folium.Map(
    location=map_center, 
    zoom_start=zoom_level,
    tiles=None  # Varsayılan tile'ları kapatıyoruz
)

# Tile servisini ekle
tile_url = "https://cbs.rizeozelidare.gov.tr/geodataserver/api/v1/collections/TKGM_PARSEL/tiles/WebMercatorQuad/{z}/{x}/{y}?&access_token=pVPS0BjanTPwYePOECyb6DIu"
folium.TileLayer(
    tiles=tile_url,
    attr="Rize Özel İdare CBS",
    name="Parsel Tile Servisi"
).add_to(m)

# Katman kontrolü ekle
folium.LayerControl().add_to(m)

# Haritayı HTML dosyasına kaydet
output_file = "rize_parsel_map.html"
m.save(output_file)

print(f"Harita oluşturuldu ve {output_file} olarak kaydedildi.")
