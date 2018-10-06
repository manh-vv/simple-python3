import unittest

from excel_tool.utils import *


class MyTestCase(unittest.TestCase):
    def test_normalize_name(self):
        name = 'hello from / pagoda \\'

        n1 = normalize_name(name)
        n2 = normalize_name(name, 6)

        self.assertEqual(n1, 'hello-from-pagoda')
        self.assertEqual(n2, 'pagoda')

    def test_month_name(self):
        self.assertEqual(month_to_num('Jan'), 1)
        self.assertEqual(month_to_num('JAn'), 1)
        self.assertEqual(month_to_num('jaN'), 1)
        self.assertEqual(month_to_num('JAN'), 1)
        self.assertEqual(month_to_num('jAN'), 1)

        self.assertEqual(month_to_num('jan'), 1)
        self.assertEqual(month_to_num('feb'), 2)
        self.assertEqual(month_to_num('mar'), 3)
        self.assertEqual(month_to_num('apr'), 4)
        self.assertEqual(month_to_num('may'), 5)
        self.assertEqual(month_to_num('jun'), 6)
        self.assertEqual(month_to_num('jul'), 7)
        self.assertEqual(month_to_num('aug'), 8)
        self.assertEqual(month_to_num('sep'), 9)
        self.assertEqual(month_to_num('oct'), 10)
        self.assertEqual(month_to_num('nov'), 11)
        self.assertEqual(month_to_num('dec'), 12)

        with self.assertRaises(Exception):
            month_to_num('de')

    def test_is_file_there(self):
        self.assertEqual(is_file_there(file_input_path("data_book.xlsx")), True)


if __name__ == '__main__':
    unittest.main()
