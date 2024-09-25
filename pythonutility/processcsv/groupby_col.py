from typing import List
import csv
from pathlib import Path

def group_by_col_sum(base_dir:str, in_pathfilename:str, out_folder:str, filename:str, group_by:List[str]):
    """Sum a column which normally is 'amount' with predefined conditions, the conditions are normally 
    values in one or more columns.
    :param base_dir: parent directory of the file
    :type base_dir: str
    :param in_pathfilename: the csv file to be group by, directory plus file name
    :type in_pathfilename: str
    :param out_folder: the processed csv file to be saved
    :type out_folder: str
    :param filename: the processed csv file name
    :type filename: str
    :param group_by: a list of columns as grouped by conditions
    :type group_by: List[str]
    """

    with open (in_pathfilename, newline='') as read_object:
        rawdata_reader = csv.DictReader(read_object)
        # rows group by columns in tup defined
        res_dict = {}
        for row in rawdata_reader:
            k = tuple([row[column] for column in group_by])
            if k not in res_dict:
                res_dict[k] = 0
            res_dict[k] += float(row['NET AMOUNT'])

    if not Path(base_dir/out_folder).exists():
        Path.mkdir({base_dir}/{out_folder})
    with open (base_dir/out_folder/filename,'w+', newline='') as write_obj:
        fieldnames = group_by.copy()
        fieldnames.append('TOTAL_AMOUNT')
        writer = csv.DictWriter(write_obj, fieldnames=fieldnames)
        writer.writeheader()

        for k, v in res_dict.items():
            line_dict = {}
            for idx, column in enumerate(group_by):
                line_dict[column] = k[idx]
            line_dict['TOTAL_AMOUNT'] = v
            writer.writerow(line_dict)