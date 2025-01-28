import requests

url = "https://cbs.rizeozelidare.gov.tr/geodataserver/api/v1/collections/TKGM_PARSEL/tiles/WebMercatorQuad/14/8923/12417?&access_token=pVPS0BjanTPwYePOECyb6DIu"

response = requests.get(url)

if response.status_code == 200:
    print(f"Content-Type: {response.headers['Content-Type']}")
    print(f"Yanıt uzunluğu: {len(response.content)} bayt")
    with open("response_sample.bin", "wb") as f:
        f.write(response.content)  # Yanıtı bir dosyaya kaydet
else:
    print(f"Hata: {response.status_code}, {response.text}")
