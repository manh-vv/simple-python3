# group sup_name customer_code_month
group_sup_cc_m_db = 'c_group_sup_cc_m'
set_sup_name_db = 'c_set_sup_name'
map_customer_code_name_db = 'c_map_customer_code_name'

template_description = {
    'template_sheet_name': 'customer_name',
    'sheet_title_col': 'A1',
    'percent_col': 'G46',
    'available_rows': 40,
}

# Input
data_input = {
    'import_new': False,
    'data_file_name': 'data_book2.xlsx',
    'data_range': ('A', 2, 1637),
    'sheet_name': 'Sheet1',
    'data_col': {
        'month': 'A',
        'customer_code': 'C',
        'customer_name': 'D',
        'sup_name': 'X',
        'net_sale': 'Q',
        'vat_sale': 'R',
        'District': 'F',
        'Region': 'B',
        'Date': 'S',
    },
    'percent_file_name': 'phan_tram_10.xlsx',
    'working_months': [
        ('oct', 'H')
    ],
    'percent_file_des': {
        'row_data_start': 2,
        'row_data_end': 58,
        'col_sup_name': 'D',
        'col_customer_code': 'B',
    },
    'current_month': 'Oct',
    'enable_export_incentive': False
}
