from openpyxl import load_workbook
from slugify import slugify
from shutil import copyfile

wb = load_workbook(filename='data_book.xlsx', data_only=True)
sheet_ranges = wb['final T11']

# our data range is: A2, J988
# data_range = sheet_ranges['A2':'J988']

# group by SUP name
sup_group = dict()
# get column J, and fill out sup_group by sup_name=[row_num]
row_num = 0
for sup_name_cell in sheet_ranges['J']:
    row_num = sup_name_cell.row
    if row_num < 2:
        continue

    sup_name = sup_name_cell.value

    # read customer name
    customer_name = sheet_ranges[f'E{row_num}'].value.strip()

    if sup_name in sup_group:
        # check if customer name is in dictionary then add row_num
        if customer_name in sup_group[sup_name]:
            sup_group[sup_name][customer_name].append(row_num)

        # else create new key of customer name then add row_num
        else:
            sup_group[sup_name][customer_name] = [row_num]
    else:
        # create customer dictionary to group customer by name
        customer_group = sup_group[sup_name] = dict()
        customer_group[customer_name] = [row_num]

# validate
if row_num == 988:
    print('---- reach end -- finish collect and grouping data')
else:
    print('---- reading data fail: may missing row')


def get_valid_sheet_name(s):
    return slugify(s)[-30:]


def get_valid_filename(s):
    return slugify(s)


def create_file_by_sup_name(sup_name):
    file_name = get_valid_filename(sup_name)
    _file = f'output/{file_name}.xlsx'
    copyfile('template.xlsx', _file)
    return _file


read_cols = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
template_sheet_name = 'customer_name'

# available rows in template now is 26
available_rows = 26
# we need to insert more rows so data can fit in

for sup_name, customer_group in sup_group.items():
    print(sup_name)
    # for each sup_name create new excel file from template
    new_file = create_file_by_sup_name(sup_name)
    nwb = load_workbook(filename=new_file)

    for customer_name, row_num_list in customer_group.items():
        print(''.ljust(10, '-'), ' ', customer_name)
        # for each customer name create new sheet name from template
        c_sheet = nwb.copy_worksheet(nwb[template_sheet_name])
        c_sheet.title = get_valid_sheet_name(customer_name)

        # then fill related values to the sheet
        # we will fill from row 5
        # need inserting more rows
        will_fill_row_count = len(row_num_list)
        if will_fill_row_count > available_rows:
            c_sheet.insert_rows(29, will_fill_row_count - available_rows + 2)

        row_index = 5
        for row_num in row_num_list:
            for col_name in read_cols:
                c_sheet[f'{col_name}{row_index}'] = sheet_ranges[f'{col_name}{row_num}'].value

            row_index = row_index + 1

        print(f'---- fill out {row_index - 4}rows')

    # remove template sheet
    nwb.remove(nwb[template_sheet_name])

    # saving
    nwb.save(new_file)
