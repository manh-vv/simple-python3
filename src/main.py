from excel_tool.mysql_workbook import execute_export

resource_folder = '/Users/manhvu/mworks/python3/simple-python3/src/resources/input'


def file_input(file_name):
    return f'{resource_folder}/{file_name}'


if __name__ == '__main__':
    execute_export()

