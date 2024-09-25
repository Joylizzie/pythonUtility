print(__package__)
from pathlib import Path

from pythonutility.processcsv import unique_items
print(f'cwd = {Path.cwd()}')
import unittest
from pythonutility.pathoperation import create_folder as pro
from pythonutility.processcsv import lookupcsv, sanitize

class TestCreatefolder(unittest.TestCase):
    def test_folder_creation(self):
        base_dir = Path(__file__).resolve().parent
        folder = 'test_data' 
        pro.create_folder_if_needed(base_dir, folder)
        test_path = Path('/home/lizzie/project/pythonUtility/tests/tests_data')
        self.assertTrue(test_path)

    def test_sanitize(self):
        f = "/home/lizzie/project/pythonUtility/data/rawdata/sep_2_1.csv"
        cols = 'Vantiv Payment ID'
        sanitize.remove_q(f, cols)
        self.assertEqual(1, 1)


    def test_unique_items(self):
        base_dir = Path(__file__).resolve().parent
        in_filename = 'data/rawdata/new_ROI.csv'
        out_folder = 'test_data/processedData'
        cols=['BATCH TYPE']
        unique_items.unique_items(base_dir=base_dir, in_filename=in_filename, out_folder=out_folder, cols=cols)
        
    def test_lookupcsv(self):
        f = "/home/lizzie/project/pythonUtility/data/rawdata/sep_1.csv"
        dict = lookupcsv.dict_val(f, 'PAY PROCESSOR ID', 'NET AMOUNT')
        self.assertEqual(1, 1)

    def test_differ(self):
        f1 = "/home/lizzie/project/pythonUtility/data/rawdata/sep_1.csv"
        f2 = "/home/lizzie/project/pythonUtility/data/rawdata/sep_2.csv"
        lookupcsv.differs(f1,
                        ('PAY PROCESSOR ID','CURRENCY TYPE'),
                        'NET AMOUNT',
                        f2,
                        ('Vantiv Payment ID','Settlement Currency'),
                        ' Net Amount ',
                         "/home/lizzie/project/pythonUtility/data/rawdata/sep_3.txt",
                         "/home/lizzie/project/pythonUtility/data/rawdata/sep_4.txt",
                         "/home/lizzie/project/pythonUtility/data/rawdata/sep_5.txt"
                        )
        self.assertEqual(1, 1)

    def test_foo(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()