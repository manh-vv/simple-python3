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


if __name__ == '__main__':
    unittest.main()
