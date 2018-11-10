import urllib.parse

from bson.objectid import ObjectId
from pymongo import MongoClient

from excel_tool.excel_read_data_book import read_work_book
from excel_tool.utils import file_input_path
from excel_tool.variables import map_customer_code_name_db

username = urllib.parse.quote_plus('root')
password = urllib.parse.quote_plus('manhvu@1')

client = MongoClient('mongodb://%s:%s@localhost:27017/' % (username, password))
db = client['data_book']
collection_name = 'excel_data'
excel_data = db[collection_name]


def quarter_inventory():
    pipeline = [
        {
            "$sort": {"sup_name": 1, "customer_code": 1, "month": 1}
        },
        {
            "$group": {
                "_id": {
                    "sup_name": "$sup_name",
                    "month": "$month",
                    "customer_code": "$customer_code"
                },

                "totalNetSale": {"$sum": "$net_sale"}
            }
        }
    ]

    return excel_data.aggregate(pipeline)


def get_all_sup_name(sup_name_col="sup_name"):
    return excel_data.distinct(sup_name_col)


def insert_into_db(obj):
    return excel_data.insert_one(obj).inserted_id


def query_db(post_id):
    return excel_data.find_one({"_id": ObjectId(post_id)})


def delete_all():
    db.drop_collection(collection_name)


def customer_code_name_mapping(customer_code):
    cc = db[map_customer_code_name_db].find_one({'_id': customer_code})

    if not cc:
        raise Exception(f'can not find customer code: {customer_code}')

    return cc.get('customer_name')


def worker_excel_mongodb(config):
    if not config['import_new']:
        print(f'---- check import_new value {config["import_new"]}')
        return

    print('erase old data')
    delete_all()

    # read config
    file_path = file_input_path(config['data_file_name'])
    data_range = config['data_range']
    sheet_name = config['sheet_name']
    data_col = config['data_col']

    # prepare document
    def row_reader(work_sheet, row_idx):
        obj = {}
        for name, col_name in data_col.items():
            obj[name] = work_sheet[f'{col_name}{row_idx}'].value
            if isinstance(obj[name], str):
                obj[name] = obj[name].strip()

        # insert document to mongodb
        insert_into_db(obj)

    # read excel file
    print('transferring data from excel to mongodb')
    read_work_book(row_reader, file_path, data_range, sheet_name)

    print('worker_excel_mongodb done')
