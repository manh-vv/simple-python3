from openpyxl import load_workbook

resource_folder = '../resources'
input_folder = f'{resource_folder}/input'

working_months = [
    ('aug', 'H')
]


# read incentive and update data in memory
#
# sup_name
# -------- customer-code -- jan-v -- feb-v ...
#
def read_percent(file_path):
    sup_group = dict()

    col_sup_name = 'D'
    col_customer_code = 'B'

    row_data_start = 2
    row_data_end = 86

    incentive_wb = load_workbook(file_path, data_only=True)
    sheet_ranges = incentive_wb['Sheet1']
    row_num = 0

    for sup_name_cell in sheet_ranges[col_sup_name]:
        row_num = sup_name_cell.row
        if row_num < row_data_start:
            continue

        sup_name = sup_name_cell.value

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

# test read percent
# rs = read_percent(f'{input_folder}/phan tram.xlsx')
# print('rs', rs)
