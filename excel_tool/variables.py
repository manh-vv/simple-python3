from excel_tool.MonthEnum import MonthEnum

# group sup_name customer_code_month
group_sup_cc_m_db = 'c_group_sup_cc_m'
c_group_by_year = 'c_group_by_year'
set_sup_name_db = 'c_set_sup_name'
map_customer_code_name_db = 'c_map_customer_code_name'

# current working month
month_enum = MonthEnum.Feb # to be updated
# current year
current_year = '2019' # to be updated

def sheet_title_text(moth_num):
    return f'Bảng kê chi tiết doanh số, chiết khấu thương mại Tháng {moth_num}.{current_year}'


template_description = {
    'template_sheet_name': 'customer_name',
    'sheet_title_col': 'A1',
    'inventory_num_col': 'B2',
    'inventory_num_prefix': f'{str(month_enum.value).zfill(2)}{current_year[2:]}HCM-',
    'inventory_num_col2': 'B3',
    'inventory_num_prefix2': f'EUCERIN/HCM/{month_enum.value}-{current_year}',
    'percent_col': 'G46',
    'row_start': 5,
    'available_rows': 40,
}

# Input
data_input = {
    'import_new': False, # to be updated
    'data_file_name': 'data_book2.xlsx', # to be updated
    'data_range': ('A', 2, 4311), # to be updated
    'sheet_name': 'Sheet1',
    'data_col': {
        'month': 'A',
        'Region': 'B',
        'customer_code': 'C',
        'customer_name': 'D',
        'sup_name': 'T',
        'net_sale': 'Q',
        'vat_sale': 'R',
        'District': 'F',
        'Date': 'S',
    },
    'percent_file_name': f'phan_tram_{month_enum.value}.xlsx',
    'working_months': [
        (month_enum.name.lower(), 'H')
    ],
    'percent_file_des': {
        'row_data_start': 2, # to be updated
        'row_data_end': 71, # to be updated
        'col_sup_name': 'E',
        'col_customer_code': 'B',
    },
    'current_month': month_enum.name,
    'enable_export_incentive': False, # to be updated
    'quarter_month_start': 1,  # to be updated
}
