import gspread
from oauth2client.service_account import ServiceAccountCredentials

def export_to_sheets(df, sheet_id):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "credentials.json", scope
    )
    client = gspread.authorize(creds)

    sheet = client.open_by_key(sheet_id)
    ws = sheet.sheet1
    ws.clear()
    ws.update([df.columns.tolist()] + df.values.tolist())
