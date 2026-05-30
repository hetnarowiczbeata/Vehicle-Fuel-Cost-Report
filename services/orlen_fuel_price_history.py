import requests
from datetime import datetime
from utils.tools import price_per_liter
from id_fuel import get_product_id
import pandas as pd
import openpyxl

def pobierz_historie_cen():
    DATE = datetime.today().strftime('%Y-%m-%d')
    fuel_history = []
    for product_id in get_product_id():
        URL_LIST=[]
        API_URL= f'https://tool.orlen.pl/api/wholesalefuelprices/ByProduct?productId={product_id}&from=2026-01-01&to={DATE}'
        URL_LIST.append(API_URL)
        for api_item in URL_LIST:
            response = requests.get(API_URL)
            data = response.json()
            for item in data:
               fuel_history.append({
                 'date':item.get('publishFrom')[:10],
                  'Product':item.get('productName'),
                   'Price':price_per_liter(item.get('value'))
                        })

    return pd.DataFrame(fuel_history)