import unittest

from excel_tool.create_file_from_template import create_file_by_sup_name, create_quarter_by_sup_name
from excel_tool.utils import is_file_there, delete_file


class MyTestCase(unittest.TestCase):
    def test_create_file_by_sup_name(self):
        file = create_file_by_sup_name("template1.xlsx", "manhvu", "jan")
        self.assertEqual(is_file_there(file), True)
        delete_file(file)

    def test_create_quarter_by_sup_name(self):
        file = create_quarter_by_sup_name("template_incentive.xlsx", "manhvu")
        self.assertEqual(is_file_there(file), True)
        delete_file(file)


if __name__ == '__main__':
    unittest.main()
