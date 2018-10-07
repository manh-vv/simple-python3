from shutil import copyfile

from excel_tool.utils import file_input_path, file_output_path, normalize_name, make_folder


def create_file_by_sup_name(file_template_name, sup_name, cur_month):
    file_name = normalize_name(sup_name)

    folder_name = 'out1'
    make_folder(file_output_path(folder_name))
    _file = file_output_path(f'{folder_name}/{cur_month}_{file_name}.xlsx')

    copyfile(file_input_path(file_template_name), _file)
    return _file


def create_quarter_by_sup_name(file_template_name, sup_name):
    file_name = normalize_name(sup_name)

    folder_name = 'quarter'
    make_folder(file_output_path(folder_name))
    _file = file_output_path(f'{folder_name}/{file_name}.xlsx')

    copyfile(file_input_path(file_template_name), _file)
    return _file
