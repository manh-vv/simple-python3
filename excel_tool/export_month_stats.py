from excel_tool.excel_mongo_tool import customer_code_name_mapping
from excel_tool.read_percent import find_percent
from excel_tool.utils import normalize_name, month_to_num
from excel_tool.variables import template_description


def export_month_stats(sup_name, cur_month, data, current_book):
    template_sheet_name = template_description['template_sheet_name']
    sheet_title_col = template_description['sheet_title_col']
    percent_col = template_description['percent_col']
    available_rows = template_description['available_rows']

    _id = data.get('_id')
    items = data.get('items')

    customer_code = _id.get('customer_code')

    # create new sheet for customer name
    customer_name = customer_code_name_mapping(customer_code)
    work_sheet_source = current_book[template_sheet_name]
    c_sheet = current_book.copy_worksheet(work_sheet_source)
    c_sheet.title = normalize_name(customer_name, 30)

    # fill value to sheet title
    month_num = month_to_num(cur_month)
    c_sheet[sheet_title_col] = f'Bảng kê chi tiết doanh số, chiết khấu thương mại Tháng {month_num}.2018'
    c_sheet[percent_col] = find_percent(sup_name, cur_month, customer_code)

    # then fill related values to the sheet
    # we will fill from row 5
    # need inserting more rows
    will_fill_row_count = len(items)
    # print(f'customer_name={customer_name} have {will_fill_row_count} items')
    if will_fill_row_count > available_rows:
        c_sheet.insert_rows(available_rows - 2, will_fill_row_count - available_rows + 5)

    row_index = 5
    for item in items:
        c_sheet[f'B{row_index}'] = item.get('Region')  # Khu Vực
        c_sheet[f'C{row_index}'] = item.get('District')  # Tỉnh/Thành
        c_sheet[f'D{row_index}'] = item.get('customer_code')  # Mã khách hàng
        c_sheet[f'E{row_index}'] = item.get('customer_name')  # Tên khách hàng
        c_sheet[f'G{row_index}'] = item.get('Date')  # Ngày hóa đơn
        c_sheet[f'H{row_index}'] = item.get('net_sale')  # Doanh số
        c_sheet[f'I{row_index}'] = item.get('vat_sale')  # Thuế VAT

        row_index = row_index + 1
