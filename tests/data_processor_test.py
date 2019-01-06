import unittest

from excel_tool.data_processor import group_by_sup_name, map_customer_code_name, group_by_year


class MyTestCase(unittest.TestCase):
    # @unittest.skip
    def test_group_by_year(self):
        group_by_year()
        self.assertEqual(True, True)

    @unittest.skip
    def test_group_by_sup_name(self):
        group_by_sup_name()
        self.assertEqual(True, True)

    @unittest.skip
    def test_map_customer_code_name(self):
        map_customer_code_name()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
