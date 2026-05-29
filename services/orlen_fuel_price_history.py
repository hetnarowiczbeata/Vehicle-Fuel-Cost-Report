import requests
from datetime import datetime

DATE = datetime.today().strftime('%Y-%m-%d')
API_URL = f'https://tool.orlen.pl/api/wholesalefuelprices/ByProduct?productId=41&from=2026-01-01&to={DATE}'
response = requests.get(API_URL)
data = response.json()
fuel_history=[]
for item in data:
    fuel_history.append({

        'date':item['publishFrom'][:10],
        'Product':item['value']})
print(fuel_history)