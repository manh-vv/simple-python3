from slugify import slugify
from shutil import copyfile
import os

output_folder = f'{os.getcwd()}/resources/output'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)


def get_valid_sheet_name(s):
    return slugify(s)[-30:]


def get_valid_filename(s):
    return slugify(s)


def create_file_by_sup_name(file_template_path, sup_name, cur_month):
    file_name = get_valid_filename(sup_name)
    _file = f'{output_folder}/{cur_month}_{file_name}.xlsx'

    copyfile(file_template_path, _file)
    return _file
