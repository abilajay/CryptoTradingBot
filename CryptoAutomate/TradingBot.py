from CryptoAutomate.SheetRead import Read
from CryptoAutomate.GetCurrentMarket import CurrentMarket
SheetRead = Read()
CurrentMarket = CurrentMarket()

sheetCurrency = SheetRead.currencyRead()

while True:
    currencyPrice = CurrentMarket.getCurrentPriceStatus()
    result = CurrentMarket.pct_change(sheetCurrency[0], currencyPrice[0])
    print(result)
    if result > 0.5:
        print("actions")