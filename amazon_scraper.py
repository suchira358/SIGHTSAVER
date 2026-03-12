import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0"
}

def amazon_price(product):

    url = f"https://www.amazon.in/s?k={product}"

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    price = soup.select_one(".a-price-whole")

    rating = soup.select_one(".a-icon-alt")

    if price:
        price = price.text
    else:
        price = "N/A"

    if rating:
        rating = rating.text
    else:
        rating = "N/A"

    return {
        "website": "Amazon",
        "price": price,
        "rating": rating
    }
