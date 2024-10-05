import csv
from pathlib import Path
import logging
from pythonUtility.pathoperation.createfolder import create_folder_if_needed

logger = logging.getLogger(__name__)

def unique_items(base_dir, in_pathfilename, out_folder, cols=None):
    """Find unique items in a column in a csv file if  column name(s) specified;
    if no column(s) specified, provide csv file with unique items for every column.
    
    
    :param base_dir: parent directory of the csv file
    :type base_dir: str
    :param in_pathfilename: the path within the basedir and the csv file name
    :type in_pathfilename: str
    :param out_folder: dir for output files
    :type out_folder: str
    :param cols: the columns which need to find their unique items
    :type cols: List, optional
    """
 
    # if not Path(base_dir/out_folder).exists():
    #     Path.mkdir(base_dir/out_folder)
    create_folder_if_needed(base_dir,out_folder)
    with open (base_dir/in_pathfilename, newline='') as read_object:
        rawdata_reader = csv.DictReader(read_object)
        #print(rawdata_reader.fieldnames)
        unique_dic = {}
        for row in rawdata_reader:
            for k, v in row.items():
                if k not in unique_dic:
                    unique_dic[k] = set()
                unique_dic[k].add(v)
    fieldnames = rawdata_reader.fieldnames
    if not cols:
        cols = fieldnames
    for col in cols:
        if col not in fieldnames:
            logger.error
        with open(Path.joinpath(base_dir, out_folder,f'{col}.csv'), 'w+', newline='') as write_obj:
            fieldnames = [f'{col}']
            writer = csv.DictWriter(write_obj, fieldnames=fieldnames)
            writer.writeheader()
            for x in unique_dic[col]:
                writer.writerow({col:x})
                
# divide by 100. By dividing 100, convert the processed numbers to original numbers
def divid_100(number):
    return round(number / 100, 2)
