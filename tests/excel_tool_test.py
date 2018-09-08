import unittest

import excel_tool.excel_tool as excel_tool


class MyTestCase(unittest.TestCase):
    def test_something(self):
        excel_tool.worker_excel_tool()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
