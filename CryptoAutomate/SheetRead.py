import json
from googleapiclient.discovery import build
from google.oauth2 import service_account

class Read():

    def currencyRead(self):

        SERVICE_ACCOUNT_FILE = "E:\CryptoProject\Resources\keys.json"
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        # The ID spreadsheet.
        SAMPLE_SPREADSHEET_ID = '1KO1jRZEbS71U7lkHPXpDBlWKnkDkyNjxw1Guaxablkw'
        service = build('sheets', 'v4', credentials=creds)
        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="Sheet1!A1:B6").execute()
        values = result.get('values', [])

        # dict = {
        #     "BTC":1,
        #     "USDT":2,
        #     "WRX":3,
        #     "ETH":4,
        #     "TRX":5
        #      }
        # i = dict.get(currency)

        sheetCurrency = []
        i = 1
        while i <= 5:
            sheetCurrency.append(float(values[i][1]))
            i += 1
        return sheetCurrency



