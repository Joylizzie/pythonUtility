from typing import List
import csv
from os import path
from pathlib import Path


def unique_items(in_pathfilename, out_path, col=None):
    """Find unique items in a column in a csv file if the column name specified;
      if no column specified, provide csv file with unique items for every column."""
    with open (in_pathfilename, newline='') as read_object:
        rawdata_reader = csv.DictReader(read_object)

        unique_dic = {}
        for row in rawdata_reader:
            for k, v in row.items():
                if k not in unique_dic:
                    unique_dic[k] = set()
                unique_dic[k].add(v)

        for k in unique_dic.keys():
            if col is None:
                with open (f'{out_path/k}.csv','w+', newline='') as write_obj:
                    fieldnames = [f'{k}']
                    writer = csv.DictWriter(write_obj, fieldnames=fieldnames)
                    writer.writeheader()
                    for x in unique_dic[k]:
                        writer.writerow({k:x})
            with open (f'{out_path/k}.csv','w+', newline='') as write_obj:
                fieldnames = [f'{k}']
                writer = csv.DictWriter(write_obj, fieldnames=fieldnames)
                writer.writeheader()
                for x in unique_dic[k]:
                    writer.writerow({k:x})
                

def sum_group_by_col(in_pathfilename, out_path,filename, group_by:List[str]):
    """Sum a column normally is amount with predefined conditions, the conditions are normally 
    values in one or more columns."""
    with open (in_pathfilename, newline='') as read_object:
        rawdata_reader = csv.DictReader(read_object)
        # rows group by columns in tup defined
        res_dic = {}
        for row in rawdata_reader:
            k = tuple([row[column] for column in group_by])
            if k not in res_dic:
                res_dic[k] = 0
            res_dic[k] += float(row['NET AMOUNT'])

    with open (f'{out_path}/{filename}','w+', newline='') as write_obj:
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
    BASE_DIR = Path(__file__).resolve().parent.parent
    in_filename = 'rawdata/new_ROI.csv'
    out_path = 'processedData'
    print(unique_items(BASE_DIR/in_filename, BASE_DIR/out_path), col='BATCH TYPE')
    #print(unique_items(BASE_DIR/filename, BASE_DIR/out_path))
    group_by = ['BATCH LOCK DATE','BATCH TYPE','ORIGINATION VENDOR', 'PAY METHOD', 'CURRENCY TYPE']
    out_filename = 'aa_groupsums.csv'
    sum_group_by_col(BASE_DIR/in_filename,out_path, out_filename,group_by)