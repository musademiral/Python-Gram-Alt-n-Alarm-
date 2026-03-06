import requests
import time

from plyer import notification

def borsa_data_alma():
    response = requests.get("https://finance.truncgil.com/api/gold-rates")

    if response.status_code == 200:
        data = response.json()
        fiyat = data["Rates"]["GRA"]["Buying"]
        return fiyat
    else:
        return None

istenen_fiyat = int(input("Lütfen Altının Altın Alarmı İçin Sınır Ekleyiniz: "))
parite_ismi = "Has Gram Altın"

while True:
    fiyat = borsa_data_alma()
    if fiyat is not None:
        print(f"{parite_ismi} Alış fiyatı ----> {fiyat}")
        if fiyat >= istenen_fiyat:
                notification.notify(
                    title = "ALTIN HEDEFİNİZE ULAŞTI",

                    app_name = "Altın Sayacı",

                    message = f"Altın hedeflediğiniz {istenen_fiyat} değerinin üstünde!",

                    timeout= 20
                )
                break
        time.sleep(10)
    else:

        "Data alınamadı"

