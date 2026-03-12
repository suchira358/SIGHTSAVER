import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0"
}

def myntra_price(product):

    url = f"https://www.myntra.com/{product}"

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    price = soup.select_one("span.pdp-price")

    rating = soup.select_one("div.index-overallRating")

    if price:
        price = price.text
    else:
        price = "N/A"

    if rating:
        rating = rating.text
    else:
        rating = "N/A"

    return {
        "website": "Myntra",
        "price": price,
        "rating": rating
    }
