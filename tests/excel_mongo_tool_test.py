import unittest

from excel_tool.excel_mongo_tool import *

collection_test = client['tests']['test']


class MyTestCase(unittest.TestCase):
    def test_mongo_connection(self):
        client.server_info()
        self.assertEqual(True, True)

    def test_mongo_delete(self):
        obj = {
            '_id': 'test_id',
            'test': 'test insert'
        }

        collection_test.delete_one(obj)

        self.assertEqual(True, True)

    def test_mongo_insert(self):
        obj = {
            '_id': 'test_id',
            'test': 'test insert'
        }

        collection_test.insert_one(obj)

        self.assertEqual(True, True)

    def test_get_sub_name(self):
        sup_names = get_all_sup_name()
        print(f'---- sub_names: {sup_names}')
        self.assertEqual(True, True)

    def test_customer_code_name_mapping(self):
        customer_code = 'customer_code_xxx'
        customer_name = 'customer_name_xxx'

        ccdb = db[map_customer_code_name_db]
        ccdb.delete_one({'_id': customer_code})
        ccdb.insert_one({
            '_id': customer_code,
            'customer_name': customer_name
        })

        customer_name_n = customer_code_name_mapping(customer_code)
        self.assertEqual(customer_name_n, customer_name)


if __name__ == '__main__':
    unittest.main()
