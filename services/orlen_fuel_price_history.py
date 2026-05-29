import requests
from datetime import datetime
from utils.tools import price_per_liter
import pandas as pd
DATE = datetime.today().strftime('%Y-%m-%d')
API_URL_95 = f'https://tool.orlen.pl/api/wholesalefuelprices/ByProduct?productId=41&from=2026-01-01&to={DATE}'
response = requests.get(API_URL_95)
data = response.json()
fuel_history=[]
for item in data:
    fuel_history.append({

        'date':item.get('publishFrom')[:10],
        'Product':item.get('productName'),
        'Price':price_per_liter(item.get('value'))
    })
dffuel=pd.DataFrame(fuel_history)
print(dffuel['Product'].unique())