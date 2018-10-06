import os

from slugify import slugify


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
    month_name = month_name.lower()

    if month_name == 'jan':
        return 1
    if month_name == 'feb':
        return 2
    if month_name == 'mar':
        return 3
    if month_name == 'apr':
        return 4
    if month_name == 'may':
        return 5
    if month_name == 'jun':
        return 6
    if month_name == 'jul':
        return 7
    if month_name == 'aug':
        return 8
    if month_name == 'sep':
        return 9
    if month_name == 'oct':
        return 10
    if month_name == 'nov':
        return 11
    if month_name == 'dec':
        return 12

    raise Exception(f'month name [{month_name}] does not exist')
