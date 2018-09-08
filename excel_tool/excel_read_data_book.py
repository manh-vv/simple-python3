from openpyxl import load_workbook


def read_work_book(handler, file_path, data_range=('A', 6, 7), sheet_name='Sheet1'):
    wb = load_workbook(filename=file_path, data_only=True)
    ws = wb[sheet_name]

    for cell in ws[data_range[0]]:
        if cell.row < data_range[1]:
            continue
        elif cell.row > data_range[2]:
            break

        handler(ws, cell.row)
