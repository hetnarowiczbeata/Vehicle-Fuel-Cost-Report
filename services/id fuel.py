import requests

for product_id in range(1, 100):
    try:
        url = (
            f"https://tool.orlen.pl/api/wholesalefuelprices/ByProduct"f"?productId={product_id}"f"&from=2026-01-01"f"&to=2026-05-29")
        response = requests.get(url)

        if response.status_code != 200:
            continue

        if not response.text.strip():
            continue

        data = response.json()

        if data:
            print(product_id, data[0]["productName"])

    except Exception as e:
        print(f"ID {product_id}: {e}")