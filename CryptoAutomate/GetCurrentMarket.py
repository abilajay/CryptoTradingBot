import requests

class CurrentMarket():
    def getCurrentPriceStatus(self):
        url = "https://api.wazirx.com/api/v2/tickers"
        response = requests.get(url)
        responseBody = response.json()
        currencyPrice = []
        currencyPrice.append(float(responseBody["btcinr"]["last"]))
        currencyPrice.append(float(responseBody["usdtinr"]["last"]))
        currencyPrice.append(float(responseBody["wrxinr"]["last"]))
        currencyPrice.append(float(responseBody["ethinr"]["last"]))
        currencyPrice.append(float(responseBody["trxinr"]["last"]))
        return currencyPrice

    def pct_change(self, first, second):
        diff = second - first
        change = 0
        try:
            if diff > 0:
                change = (diff / first) * 100
            elif diff < 0:
                diff = first - second
                change = -((diff / first) * 100)
        except ZeroDivisionError:
            return float('inf')
        return change







