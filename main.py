import os

from excel_tool.excel_mongo_tool import worker_excel_mongodb


def file_input(file_name):
    return f'{os.getcwd()}/resources/input/{file_name}'


def import_data_to_mongo(import_new=True):
    file_path = file_input('data_book.xlsx')
    file_template_path = file_input('template1.xlsx')
    print('File input:\n', file_path, '\n', file_template_path)

    config = {
        'import_new': import_new,
        'file_path': file_path,
        'data_range': ('A', 2, 2271),
        'sheet_name': 'Sheet1',
        'data_col': {
            'month': 'A',
            'customer_code': 'C',
            'customer_name': 'D',
            'sup_name': 'X',
            'net_sale': 'Q',
            'vat_sale': 'R',
        },

        'sheet_template_name': 'customer_name'
    }

    worker_excel_mongodb(config)


if __name__ == '__main__':
    print("Hello from python")

    import_data_to_mongo()

    # n = 0
    # agg = quarter_inventory()
    # for item in agg:
    #     n += 1
    #     if n > 2:
    #         break
    #
    #     pprint.pprint(item)

    # export quarter inventory
    # execute_export()
