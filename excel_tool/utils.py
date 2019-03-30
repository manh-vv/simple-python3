import os
from slugify import slugify
from excel_tool.MonthEnum import MonthEnum


def delete_file(path):
    return os.remove(path)


def is_file_there(path):
    return os.path.exists(path)


# input folder
def file_input_path(file_name):
    return f'{os.getcwd()}/resources/input/{file_name}'


# output folder
def make_folder(path):
    if not is_file_there(path):
        os.makedirs(path)


# output folder
def file_output_path(file_name):
    output_folder = f'{os.getcwd()}/resources/output'
    make_folder(output_folder)

    return f'{output_folder}/{file_name}'


# normalize name
def normalize_name(s, length=256):
    return slugify(s)[-length:]


# month name
def month_to_num(month_name):
    month_name = month_name.capitalize()
    month_enum = MonthEnum[month_name]
    if month_enum:
        return month_enum.value

    raise Exception(f'month name [{month_name}] does not exist')

# month num
def num_to_month(month_num):
    month_enum = MonthEnum(month_num)
    if month_enum:
        return month_enum.name

    raise Exception(f'month num [{month_num}] does not exist')
