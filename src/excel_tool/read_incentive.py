from openpyxl import load_workbook

resource_folder = '../resources'
input_folder = f'{resource_folder}/input'


# read incentive and update data in memory
def read_incentive_and_update_memory_data(incentive_file_path, memory_data):
    col_sup_name = 'H'
    col_customer_code = 'B'
    col_month_name = 'A'

    row_data_start = 6
    row_data_end = 44

    read_cols = ['']

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
        cur_month = sheet_ranges[f'{col_month_name}{row_num}'].value

        # test
        print("data:", sup_name, customer_code, cur_month)

        if row_num >= row_data_end:
            break

    # validate
    if row_num == row_data_end:
        print('---- reach end -- finish collect and grouping data')
    else:
        print('---- reading data fail: may missing row')
        raise Exception(f'reading data fail: expected {row_data_end} but get {row_num}')


read_incentive_and_update_memory_data(f'{input_folder}/Incentive 2017 carry FW to 2018.xlsx', dict())
