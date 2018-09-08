from openpyxl import load_workbook

resource_folder = '../resources'
input_folder = f'{resource_folder}/input'


# read incentive and update data in memory
def read_incentive(incentive_file_path):
    sup_group = dict()

    col_sup_name = 'H'
    col_customer_code = 'B'
    col_month_name = 'A'

    row_data_start = 2
    row_data_end = 44

    incentive_wb = load_workbook(incentive_file_path, data_only=True)
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
        cur_month = str(sheet_ranges[f'{col_month_name}{row_num}'].value).lower()

        # E is `Doanh so`
        # F is `Thue Vat`
        data = (sheet_ranges[f'E{row_num}'].value, sheet_ranges[f'F{row_num}'].value)

        if sup_name not in sup_group:
            sup_group[sup_name] = dict()

        month_group = sup_group[sup_name]
        if cur_month not in month_group:
            month_group[cur_month] = dict()

        customer_group = month_group[cur_month]
        if customer_code not in customer_group:
            customer_group[customer_code] = []

        customer_group[customer_code].append(data)

        if row_num >= row_data_end:
            break

    # validate
    if row_num == row_data_end:
        print('---- reach end -- finish collect and grouping data')
    else:
        print('---- reading data fail: may missing row')
        raise Exception(f'reading data fail: expected {row_data_end} but get {row_num}')

    return sup_group

# test incentive
# rs = read_incentive(f'{input_folder}/Incentive 2017 carry FW to 2018.xlsx')
# print('rs', rs)
