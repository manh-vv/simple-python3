import excel_tool.excel_mongo_tool as db

from excel_tool.export_month_stats import export_month_stats

# Group by sup name
from excel_tool.variables import group_sup_cc_m_db, map_customer_code_name_db, set_sup_name_db


def group_by_sup_name():
    pipeline = [
        {
            "$group": {
                "_id": {
                    "sup_name": "$sup_name",
                    "month": "$month",
                    "customer_code": "$customer_code"
                },
                "items": {
                    "$push": "$$CURRENT"
                }
            }
        },
        {
            "$out": group_sup_cc_m_db
        }
    ]

    db.excel_data.aggregate(pipeline)


# Map customer code name
def map_customer_code_name():
    pipeline = [
        {
            "$group": {
                "_id": "$customer_code",
                "customer_name": {"$first": "$customer_name"}
            }
        },
        {
            "$out": map_customer_code_name_db
        }
    ]

    db.excel_data.aggregate(pipeline)


# Set sup name
def set_sup_name():
    pipeline = [
        {
            "$group": {
                "_id": "$sup_name"
            }
        },
        {
            "$out": set_sup_name_db
        }
    ]

    db.excel_data.aggregate(pipeline)


# output statistic by month
# py -m unittest tests/data_processor_test.py
#
def export_out1():
    for data in db.db[group_sup_cc_m_db].find():
        # pprint.pprint(data)
        export_month_stats(data)


def worker_data_processor():
    export_out1()
