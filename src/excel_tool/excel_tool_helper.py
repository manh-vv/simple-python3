from csv import reader

file_path = '/Users/manhvu/mworks/python3/simple-python3/src/resources/input/customer_code.csv'
csv_file = open(file_path, encoding="utf-8", newline='\n')

customer_code_map = dict()
spam_reader = reader(csv_file, delimiter=',', quotechar='"')
for row in spam_reader:
    customer_code_map[row[0]] = row[1]

csv_file.close()


def get_customer_name(customer_code):
    return customer_code_map[customer_code]


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

    raise Exception(f'month name [{month_name}] not exist')

# print("Jan", month_to_num('Jan'))
# print("JAn", month_to_num('JAn'))
# print("jaN", month_to_num('jaN'))
# print("JAN", month_to_num('JAN'))
# print("jAN", month_to_num('jAN'))
#
# print("jan", month_to_num('jan'))
# print("feb", month_to_num('feb'))
# print("mar", month_to_num('mar'))
# print("apr", month_to_num('apr'))
# print("may", month_to_num('may'))
# print("jun", month_to_num('jun'))
# print("jul", month_to_num('jul'))
# print("aug", month_to_num('aug'))
# print("sep", month_to_num('sep'))
# print("oct", month_to_num('oct'))
# print("nov", month_to_num('nov'))
# print("dec", month_to_num('dec'))
#
# print("dec", month_to_num('de'))
