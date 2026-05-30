from services.excel_core import save_to_excel
from services.orlen_fuel_price_history import pobierz_historie_cen



df=pobierz_historie_cen()
save_to_excel(df,"historia_cen_paliw.xlsx")
print("Plik zapisany")