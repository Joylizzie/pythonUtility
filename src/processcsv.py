from typing import List
import csv
from os import path
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


def unique_items(base_dir, in_pathfilename, out_folder, cols=None):
    """Find unique items in a column in a csv file if  column name(s) specified;
    if no column(s) specified, provide csv file with unique items for every column."""
    if not Path(base_dir/out_folder).exists():
        Path.mkdir(base_dir/out_folder)
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
                

def sum_group_by_col(base_dir, in_pathfilename, out_folder, filename, group_by:List[str]):
    """Sum a column which normally is 'amount' with predefined conditions, the conditions are normally 
    values in one or more columns."""
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

        for k, v in res_dic.items():
            line_dict = {}
            for idx, column in enumerate(group_by):
                line_dict[column] = k[idx]
            line_dict['TOTAL_AMOUNT'] = v
            writer.writerow(line_dict)


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent
    in_filename = 'data/rawdata/new_ROI.csv'
    out_folder = 'data/processedData'
    #cols = ['PAY METHOD','BATCH TYPE']
    cols = []
    unique_items(base_dir, in_filename, out_folder, cols=cols)
    group_by = ['BATCH TYPE','ORIGINATION VENDOR', 'PAY METHOD', 'CURRENCY TYPE']
    out_filename = 'aa_groupsums.csv'
    sum_group_by_col(base_dir, in_filename,out_folder, out_filename, group_by