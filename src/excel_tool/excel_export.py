from openpyxl import load_workbook
from slugify import slugify
from os import path, makedirs
from .excel_tool_helper import month_to_num, get_customer_name

input_folder = '/Users/manhvu/mworks/python3/simple-python3/src/resources/input'
output_folder = '/Users/manhvu/mworks/python3/simple-python3/src/resources/output'


def ensure_dir(file_path):
    directory = path.dirname(file_path)
    if not path.exists(directory):
        makedirs(directory)

    return file_path


def get_valid_sheet_name(s):
    return slugify(s)[-30:]


def get_valid_filename(s):
    return slugify(s)


def create_file_by_sup_name(output_f, sup_name):
    file_name = get_valid_filename(f'{sup_name}')
    _file = f'{output_f}/{file_name}.xlsx'

    return _file


def print_data(_c_sheet, _customer_code, _data, _row):
    _c_sheet[f'H{_row}'] = _data[0]  # doanh so
    _c_sheet[f'I{_row}'] = _data[1]  # thue
    _c_sheet['B5'] = _c_sheet['B6'] = _c_sheet['B7'] = _data[2]  # region
    _c_sheet['D5'] = _c_sheet['D6'] = _c_sheet['D7'] = _customer_code
    _c_sheet['E5'] = _c_sheet['E6'] = _c_sheet['E7'] = get_customer_name(_customer_code)


def export_quarter_inventory(template_name, template_sheet_name, sup_group):
    output_path = ensure_dir(f'{output_folder}/quarter_inventory')

    row_map = {
        1: 5,
        2: 6,
        3: 7
    }

    for sup_name, customer_group in sup_group.items():
        nwb = load_workbook(filename=f'{input_folder}/{template_name}')

        for customer_code, month_group in customer_group.items():
            c_sheet = nwb.copy_worksheet(nwb[template_sheet_name])
            c_sheet.title = get_valid_sheet_name(get_customer_name(customer_code))

            for cur_month, data in month_group.items():
                month_num = month_to_num(cur_month)
                if month_num in row_map:
                    print_data(c_sheet, customer_code, data, row_map[month_num])

        # remove template sheet
        nwb.remove(nwb[template_sheet_name])

        # saving
        new_file = create_file_by_sup_name(output_path, sup_name)
        nwb.save(new_file)
        nwb.close()
