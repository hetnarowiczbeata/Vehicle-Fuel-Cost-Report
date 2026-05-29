import requests
from datetime import datetime

DATE=datetime.today().strftime('%Y-%m-%d')
API_URL=f'https://tool.orlen.pl/api/wholesalefuelprices/ByProduct?productId=41&from=2026-01-01&to={DATE}'

response = requests.get(API_URL)
data = response.json()
print(data)