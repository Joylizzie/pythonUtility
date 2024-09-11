print(__package__)
from pathlib import Path
import unittest
import src.pathoperation.create_folder as pro 
import src.processcsv.processcsv as pcsv

class TestCreatefolder(unittest.TestCase):
    def test_folder_creation(self):
        base_dir = Path(__file__).resolve().parent
        folder = 'test_data' 
        pro.create_folder_if_needed(base_dir, folder)
        test_path = Path('/home/lizzie/project/pythonUtility/tests/tests_data')
        self.assertTrue(test_path)

    def test_unique_items(self):
        base_dir = Path(__file__).resolve().parent
        in_filename = 'data/rawdata/new_ROI.csv'
        out_folder = 'test_data/processedData'
        cols=['BATCH TYPE']
        pcsv.unique_items(base_dir=base_dir, in_filename=in_filename, out_folder=out_folder, cols=cols)
        
    def test_foo(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()