from price_scraper import amazon_price, flipkart_price, myntra_price, meesho_price
from quality_score import calculate_quality

def compare(product):

    results = []

    results.append(amazon_price(product))
    results.append(flipkart_price(product))
    results.append(myntra_price(product))
    results.append(meesho_price(product))

    for r in results:
        r["score"] = calculate_quality(r["price"], r["rating"])

    best = max(results, key=lambda x: x["score"])

    return best, results
