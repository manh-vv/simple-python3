from openpyxl import load_workbook

from excel_tool.utils import file_input_path
from excel_tool.variables import data_input

resource_folder = '../resources'
input_folder = f'{resource_folder}/input'

working_months = data_input['working_months']


# read incentive and update data in memory
#
# sup_name
# -------- customer-code -- jan-v -- feb-v ...
#
def read_percent(file_path):
    sup_group = dict()

    percent_file_des = data_input['percent_file_des']
    col_sup_name = percent_file_des['col_sup_name']
    col_customer_code = percent_file_des['col_customer_code']

    row_data_start = percent_file_des['row_data_start']
    row_data_end = percent_file_des['row_data_end']

    incentive_wb = load_workbook(file_path, data_only=True)
    sheet_ranges = incentive_wb['Sheet1']
    row_num = 0

    for sup_name_cell in sheet_ranges[col_sup_name]:
        row_num = sup_name_cell.row
        if row_num < row_data_start:
            continue

        sup_name = sup_name_cell.value
        sup_name = sup_name.strip()

        # read customer name
        customer_code = sheet_ranges[f'{col_customer_code}{row_num}'].value

        # read month
        if sup_name not in sup_group:
            sup_group[sup_name] = dict()

        for t in working_months:
            m = t[0]
            col = t[1]
            month_group = sup_group[sup_name]
            if m not in month_group:
                month_group[m] = dict()

            customer_group = month_group[m]

            percent_value = sheet_ranges[f'{col}{row_num}'].value
            if percent_value is not None:
                customer_group[customer_code] = percent_value

        if row_num >= row_data_end:
            break

    # validate
    if row_num == row_data_end:
        print('---- reach end -- finish collect and grouping data')
    else:
        print('---- reading data fail: may missing row')
        raise Exception(f'reading data fail: expected {row_data_end} but get {row_num}')

    return sup_group


month_percent = read_percent(file_input_path(data_input['percent_file_name']))


def find_percent(_sup_name, _cur_month, _customer_code):
    if _sup_name not in month_percent:
        return 0

    if _cur_month not in month_percent[_sup_name]:
        return 0

    if _customer_code not in month_percent[_sup_name][_cur_month]:
        return 0

    return month_percent[_sup_name][_cur_month][_customer_code]
