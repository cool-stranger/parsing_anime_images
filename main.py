from urllib.parse import urlparse
from bs4 import BeautifulSoup
import os
import lxml
import requests


def this_page(url):
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, "lxml")
    url_s = soup.find("ul", class_="wallpapers__list").find_all("a", class_="wallpapers__link")
    links = []
    for i in url_s:
        link = i.get("href")
        links.append(f"{url_base}{link}")
        download_image(links[-1])


def download_image(link, num_of_photo=[0]):

    req = requests.get(link)
    soup = BeautifulSoup(req.text, "lxml")
    src = soup.find("img", class_="wallpaper__image")
    img = requests.get(src.get("src"), headers=headers)
    name_of_file = os.path.basename(img.url).split("_")
    del name_of_file[-1]
    del name_of_file[-1]
    name_of_file = " ".join(name_of_file)
    with open(f"images/{str(name_of_file)}.jpg", "wb") as file:
        file.write(img.content)
    num_of_photo[0] += 1


headers = {
     "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v2081887232276297082 t1191530496833852085",
     "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8"
}
url_base = "https://wallpaperscraft.ru"
url_page = "https://wallpaperscraft.ru/catalog/anime/page"
if __name__ == "__main__":
    number_of_page = 1
    while True:
        this_page(url_page + str(number_of_page))
        number_of_page += 1     

