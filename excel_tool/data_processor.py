import excel_tool.excel_mongo_tool as db
import excel_tool.utils as utils
import re
import pprint

sup_name_db = 'c_sup_name'
c_sup_prefix = 'sup_'


# Group by sup name
def group_by_sup_name():
    pipeline = [
        {
            "$group": {
                "_id": "$sup_name",
                "items": {
                    "$push": "$$CURRENT"
                }
            }
        },
        {
            "$out": sup_name_db
        }
    ]

    db.excel_data.aggregate(pipeline)


# drop_sup_collection
def drop_sup_collection():
    c_sup_reg = re.compile('^' + c_sup_prefix)

    for c in db.db.list_collection_names():
        if c_sup_reg.match(c):
            db.db.drop_collection(c)


# create new database for processing data
def create_processing_data_database():
    for sup in db.db[sup_name_db].find():
        sup_name = utils.normalize_name(sup.get('_id'))
        c_name = f'{c_sup_prefix}{sup_name}'
        db.db[c_name].insert_many(sup.get('items'))


def worker_data_processor():
    group_by_sup_name()
    drop_sup_collection()
    create_processing_data_database()
