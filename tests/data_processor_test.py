import unittest

from excel_tool.data_processor import *


class MyTestCase(unittest.TestCase):
    # def test_group_by_sup_name(self):
    #     group_by_sup_name()
    #     self.assertEqual(True, True)
    #
    # def test_drop_sup_collection(self):
    #     drop_sup_collection()
    #     self.assertEqual(True, True)
    #
    # def test_create_processing_data_database(self):
    #     create_processing_data_database()
    #     self.assertEqual(True, True)
    #
    # def test_map_customer_code_name(self):
    #     map_customer_code_name()
    #     self.assertEqual(True, True)

    def test_worker_data_processor(self):
        worker_data_processor()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
