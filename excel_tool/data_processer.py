import pprint

import excel_tool.excel_mongo_tool as db
import excel_tool.utils as utils


# Group by sup name
def group_by_sup_name():
    sup_names = db.get_all_sup_name()
    for sup_name in sup_names:
        sup_name = utils.normalize_name(sup_name)
        print(f'---- sup_name: {sup_name}')

    pipeline = [
        {
            "$sort": {"sup_name": 1, "customer_code": 1, "month": 1}
        }
    ]
    g_sub_name = db.excel_data.aggregate(pipeline)
    for d in g_sub_name:
        pprint.pprint(d)
