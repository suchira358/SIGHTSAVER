def meesho_price(product):

    url = f"https://www.meesho.com/search?q={product}"

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    price = soup.select_one("h5")

    rating = soup.select_one("span")

    if price:
        price = price.text
    else:
        price = "N/A"

    if rating:
        rating = rating.text
    else:
        rating = "N/A"

    return {
        "website": "Meesho",
        "price": price,
        "rating": rating
    }
