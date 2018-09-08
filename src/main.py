import os
from excel_tool.mysql_workbook import execute_export
from excel_tool.excel_mongo_tool import *
from excel_tool.excel_read_data_book import read_work_book
from excel_tool.create_file_from_template import create_file_by_sup_name
import pprint
from openpyxl import load_workbook



def file_input(file_name):
    return f'{os.getcwd()}/resources/input/{file_name}'


if __name__ == '__main__':
    # file_path = file_input('data_book.xlsx')
    # file_template_path = file_input('template1.xlsx')
    # print('File input:\n', file_path, '\n', file_template_path)
    #
    # config = {
    #     'import_new': False,
    #     'file_path': file_path,
    #     'data_range': ('A', 6, 6079),
    #     'sheet_name': 'Sheet1',
    #     'data_col': {
    #         'month': 'A',
    #         'customer_code': 'C',
    #         'customer_name': 'D',
    #         'sup_name': 'X',
    #         'net_sale': 'Q',
    #         'vat_sale': 'R',
    #     },
    #
    #     'sheet_template_name': 'customer_name'
    # }
    #
    # worker_excel_mongodb(config)
    #
    # n = 0
    # agg = quarter_inventory();
    # for item in agg:
    #     n += 1
    #     if n > 2:
    #         break
    #
    #     pprint.pprint(item)

    # export quarter inventory
    execute_export()

