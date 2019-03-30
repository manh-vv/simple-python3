# group sup_name customer_code_month
group_sup_cc_m_db = 'c_group_sup_cc_m'
c_group_by_year = 'c_group_by_year'
set_sup_name_db = 'c_set_sup_name'
map_customer_code_name_db = 'c_map_customer_code_name'

template_description = {
    'template_sheet_name': 'customer_name',
    'sheet_title_col': 'A1',
    'inventory_num_col': 'B2',
    'inventory_num_prefix': '0119HCM-',  # tobe updated
    'percent_col': 'G46',
    'row_start': 5,
    'available_rows': 40,
}

# Input
data_input = {
    'import_new': False,
    'data_file_name': 'data_book2.xlsx',
    'data_range': ('A', 2, 4311),
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
    'percent_file_name': 'phan_tram_1.xlsx',
    'working_months': [
        ('dec', 'H')
    ],
    'percent_file_des': {
        'row_data_start': 2,
        'row_data_end': 81,
        'col_sup_name': 'E',
        'col_customer_code': 'B',
    },
    'current_month': 'Jan',
    'enable_export_incentive': False,
    'quarter_month_start': 1
}
