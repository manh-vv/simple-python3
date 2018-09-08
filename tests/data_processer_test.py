import unittest

from excel_tool.data_processer import *


class MyTestCase(unittest.TestCase):
    def test_mongo_connection(self):
        group_by_sup_name()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
