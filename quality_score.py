def calculate_quality(price, rating):

    try:
        price = float(price.replace(",", "").replace("₹", ""))
        rating = float(rating.split()[0])
    except:
        return 0

    score = (rating * 10) / price

    return score
