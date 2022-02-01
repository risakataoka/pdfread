import csv
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from pdfminer.high_level import extract_text
import os


currnt_dir = os.getcwd()
file_path = currnt_dir + '/経費請求書.pdf'

texts = extract_text(file_path).split()
for text in texts:
    print(text)

# (1) Google Spread Sheetsにアクセス


def connect_gspread(jsonf, key):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        jsonf, scope)
    gc = gspread.authorize(credentials)
    SPREADSHEET_KEY = key
    worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1
    return worksheet


# ここでjsonfile名と2-2で用意したkeyを入力
jsonf = "pdfread-339913-a265476a532d.json"
spread_sheet_key = "1ZGYiRPcoPpsMq8pjFuMqfhh7gAXxfZEAHz4YxGe_L6g"
ws = connect_gspread(jsonf, spread_sheet_key)

counter = 0

for text in texts:
    counter += 1
    ws.update_cell(counter, 1, text)
