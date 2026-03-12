def flipkart_price(product):

    url = f"https://www.flipkart.com/search?q={product}"

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    price = soup.select_one("._30jeq3")

    rating = soup.select_one("._3LWZlK")

    if price:
        price = price.text
    else:
        price = "N/A"

    if rating:
        rating = rating.text
    else:
        rating = "N/A"

    return {
        "website": "Flipkart",
        "price": price,
        "rating": rating
    }
