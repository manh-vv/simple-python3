from openpyxl import load_workbook


def read_sheet(file_path, sheet_name):
    print('file path:', file_path)
    wb = load_workbook(file_path, data_only=True)
    ws = wb[sheet_name]

    for row in ws.rows:
        for cell in row:
            print(cell.value)
