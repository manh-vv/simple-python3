from excel_tool.excel_mongo_tool import customer_code_name_mapping, db
from excel_tool.utils import normalize_name, month_to_num
from excel_tool.variables import template_description, map_customer_code_name_db


def export_quarter_stats(current_book, items):
    customer_code_group = {}
    for item in items:
        customer_code = item.get('customer_code')
        # group by customer code
        if customer_code not in customer_code_group:
            customer_code_group[customer_code] = {}

        item_month = item.get('month')
        customer_code_group[customer_code][item_month] = item

    for customer_code, month_items in customer_code_group.items():
        # print(f'---- customer_code: {customer_code}, item count: {len(month_items)}')

        # create new sheet for customer name
        customer_name = customer_code_name_mapping(customer_code)
        work_sheet_source = current_book[template_description['template_sheet_name']]
        c_sheet = current_book.copy_worksheet(work_sheet_source)
        c_sheet.title = normalize_name(customer_name, 30)

        cc = db[map_customer_code_name_db].find_one({'_id': customer_code})
        if not cc:
            raise Exception(f'can not find customer code: {customer_code}')

        for idx in range(5, 8):
            c_sheet[f'B{idx}'] = cc.get('Region')
            c_sheet[f'C{idx}'] = cc.get('District')
            c_sheet[f'D{idx}'] = customer_code
            c_sheet[f'E{idx}'] = cc.get('customer_name')

        for month, m_item in month_items.items():
            if month_to_num(month) == 7:
                c_sheet['H5'] = m_item.get('sum_net_sale')
            if month_to_num(month) == 8:
                c_sheet['H6'] = m_item.get('sum_net_sale')
            if month_to_num(month) == 9:
                c_sheet['H7'] = m_item.get('sum_net_sale')
