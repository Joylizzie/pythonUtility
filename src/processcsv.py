from typing import List
import csv
from os import path
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


def unique_items(base_dir, in_pathfilename, out_folder, cols:List[str]):
    """Find unique items in a column in a csv file if the column name specified;
      if no column(s) specified, provide csv file with unique items for every column."""
    with open (base_dir/in_pathfilename, newline='') as read_object:
        rawdata_reader = csv.DictReader(read_object)

        unique_dic = {}
        for row in rawdata_reader:
            for k, v in row.items():
                if k not in unique_dic:
                    unique_dic[k] = set()
                unique_dic[k].add(v)

        if not Path(base_dir/out_folder).exists():
            Path.mkdir(base_dir/out_folder)
        original_columns_header = unique_dic.keys()
        if len(cols) == 0:
            original_columns_header = unique_items  
            cols = original_columns_header
        else:
            for k in cols:
                if k not in original_columns_header:
                    logger.error(f'KeyError! The provided column name does\'t exist, omitted')
                    break
        for k in cols:
            with open(Path.joinpath(base_dir, out_folder,f'{k}.csv'), 'w+', newline='') as write_obj:
                fieldnames = [f'{k}']
                writer = csv.DictWriter(write_obj, fieldnames=fieldnames)
                writer.writeheader()
                for x in unique_dic[k]:
                    writer.writerow({k:x})
            # else:
            #     for col in cols:
            #         if col in columns:
            #             with open(Path.joinpath(base_dir, out_folder, f'{col}.csv'), 'w+', newline='') as write_obj:
            #                 fieldnames = [f'{col}']
            #                 writer = csv.DictWriter(write_obj, fieldnames=fieldnames)
            #                 writer.writeheader()
            #                 for x in unique_dic[col]:
            #                     writer.writerow({col:x})
            #         else:
            #             logger.warning(f'The provided column name does\'t exist, omitted')
            #             continue
                    
            
        # for k   in unique_dic.keys():
        #     if col is None:
        #         with open (f'{out_path/k}.csv','w+', newline='') as write_obj:
        #             fieldnames = [f'{k}']
        #             writer = csv.DictWriter(write_obj, fieldnames=fieldnames)
        #             writer.writeheader()
        #             for x in unique_dic[k]:
        #                 writer.writerow({k:x})
        #     with open (f'{out_path/k}.csv','w+', newline='') as write_obj:
        #         fieldnames = [f'{k}']
        #         writer = csv.DictWriter(write_obj, fieldnames=fieldnames)
        #         writer.writeheader()
        #         for x in unique_dic[k]:
        #             writer.writerow({k:x})
                

def sum_group_by_col(base_dir, in_pathfilename, out_folder, filename, group_by:List[str]):
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
    cols = []
    cols = ['BATCH TYPE']
    unique_items(base_dir, in_filename, out_folder, cols=cols)
    group_by = ['BATCH TYPE','ORIGINATION VENDOR', 'PAY METHOD', 'CURRENCY TYPE']
    out_filename = 'aa_groupsums.csv'
    sum_group_by_col(base_dir, in_filename,out_folder, out_filename, group_by)