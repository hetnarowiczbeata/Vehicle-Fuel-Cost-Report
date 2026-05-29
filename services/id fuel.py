import requests
def get_product_id():
    products_id=[]
    for product_id in range(1, 100):
        try:
            url = (
                f"https://tool.orlen.pl/api/wholesalefuelprices/ByProduct"f"?productId={product_id}"f"&from=2026-01-01"f"&to=2026-05-29")
            response = requests.get(url)

            if response.status_code != 200:
                continue
            products_id.append(product_id)

        except Exception as e:
            print(e)
    return products_id
print(get_product_id())