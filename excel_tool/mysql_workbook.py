from csv import reader

from .excel_export import export_quarter_inventory


def parse_int(s):
    res = int(eval(str(s)))
    if type(res) == int:
        return res


def read_data(has_header=True):
    file_path = '/Users/manhvu/mworks/python3/simple-python3/src/resources/input/quarter_inventory.csv'
    csv_file = open(file_path, encoding="utf-8", newline='\n')

    sup_group = dict()
    count = 0
    try:
        spam_reader = reader(csv_file, delimiter=',', quotechar='"')
        for row in spam_reader:
            count += 1

            if has_header and count == 1:
                continue

            sup_name = row[0]
            cur_month = row[1]
            customer_code = row[2]
            sales = parse_int(row[3])
            vat = parse_int(row[4])

            if sup_name not in sup_group:
                sup_group[sup_name] = dict()

            customer_group = sup_group[sup_name]
            if customer_code not in customer_group:
                customer_group[customer_code] = dict()

            month_group = customer_group[customer_code]
            if cur_month not in month_group:
                month_group[cur_month] = (sales, vat, row[5])
            else:
                Exception(f'month exist ?? [{cur_month}]')

    except Exception as e:
        print(e)
    finally:
        csv_file.close()

    return sup_group


# print out
def execute_export():
    sup_group = read_data()

    for sup in sup_group.items():
        print('---- sup = ', sup)
        break

    export_quarter_inventory('quarter_inventory_template.xlsx', 'Sheet1', sup_group)
