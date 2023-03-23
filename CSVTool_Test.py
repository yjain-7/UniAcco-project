import unittest
import os
import csv
from CSVTool import CSVTool

class TestCSVTool(unittest.TestCase):
    def setUp(self):
        self.tool = CSVTool()
        self.file = 'test_data.csv'
        with open(self.file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['name', 'age', 'gender'])
            writer.writerow(['Alice', '25', 'F'])
            writer.writerow(['Bob', '30', 'M'])
            writer.writerow(['Charlie', '35', 'M'])
    
    def tearDown(self):
        os.remove(self.file)

    def test_load(self):
        self.tool.load(self.file)
        self.assertEqual(len(self.tool.data), 3)

    def test_count(self):
        self.tool.load(self.file)
        self.assertEqual(self.tool.count(), 3)

    def test_mean(self):
        self.tool.load(self.file)
        self.assertAlmostEqual(self.tool.mean('age'), 30.0)

    def test_filter(self):
        self.tool.load(self.file)
        filtered_value = self.tool.filter('gender', 'F')
        self.assertEqual(len(filtered_value), 1)
        self.assertEqual(filtered_value,[{'name': 'Alice', 'age': '25', 'gender': 'F'}])

    def test_std_dev(self):
        self.tool.load(self.file)
        self.assertEqual(int(self.tool.std_dev('age')), 4)

if __name__ == '__main__':
    unittest.main()
