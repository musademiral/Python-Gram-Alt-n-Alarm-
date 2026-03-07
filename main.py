import pygame
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

def playNotificationSount():
    pygame.init()
    pygame.mixer.music.load("ohnono.mp3")
    pygame.mixer.music.play()
    time.sleep(10)

istenen_fiyat = int(input("Lütfen Altının Altın Alarmı İçin Sınır Ekleyiniz: "))
parite_ismi = "Has Gram Altın"

if istenen_fiyat > borsa_data_alma():
    action= "long"
else:
    action= "short"

while True:
    fiyat = borsa_data_alma()
    if fiyat is not None:
        print(f"{parite_ismi} Alış fiyatı ----> {fiyat}")
        if action == "long" and istenen_fiyat <= fiyat:
                notification.notify(
                    title = "ALTIN HEDEFİNİZE ULAŞTI",

                    app_name = "Altın Sayacı",

                    message = f"Altın hedeflediğiniz {istenen_fiyat} değerine ulaştı!",

                    timeout= 20
                )
                playNotificationSount()
                break
        elif action == "short" and istenen_fiyat >= fiyat:
            notification.notify(
                title="ALTIN HEDEFİNİZE ULAŞTI",

                app_name="Altın Sayacı",

                message=f"Altın hedeflediğiniz {istenen_fiyat} değerine ulaştı!",

                timeout=20
            )
            playNotificationSount()
            break

        time.sleep(10)
    else:

        "Data alınamadı"
