import requests
import json
import os

def geoip_lookup(ip):
    """
    Mengambil data lokasi IP dari API ipinfo.io
    """
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url, timeout=5)  # request ke API
    data = response.json()  # ubah ke dict (Python object)
    return data

if __name__ == "__main__":
    ip = input("Masukkan IP atau hostname: ")
    data = geoip_lookup(ip)

    # Print hasil ke layar
    print("\n=== Hasil GeoIP ===")
    print(json.dumps(data, indent=4))

    # Simpan ke file JSON
    os.makedirs("sample_output", exist_ok=True)
    with open("sample_output/geoip_result.json", "w") as f:
        json.dump(data, f, indent=4)

    print("\nHasil disimpan ke sample_output/geoip_result.json ✅")
