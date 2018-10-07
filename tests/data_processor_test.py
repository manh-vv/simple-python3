import unittest

from excel_tool.data_processor import group_by_sup_name, map_customer_code_name, worker_data_processor


class MyTestCase(unittest.TestCase):
    @unittest.skip
    def test_group_by_sup_name(self):
        group_by_sup_name()
        self.assertEqual(True, True)

    @unittest.skip
    def test_map_customer_code_name(self):
        map_customer_code_name()
        self.assertEqual(True, True)

    # @unittest.skip
    def test_worker_data_processor(self):
        worker_data_processor()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
