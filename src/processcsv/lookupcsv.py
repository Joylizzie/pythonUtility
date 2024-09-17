import csv
from typing import List
from collections import defaultdict
from pathlib import Path

def differs(f1,key_cols_1,val_col_1, f2, key_cols_2, val_col_2, f3, f4, f5):
    """Find the items:
     1. Both in f1 and f2 and write to f3,
     2. In f1 but not in f2 and write to f4,
     3. In f2 but not in f1 and write to f5"""
    dict_val_1 = dict_val(f1, key_cols_1, val_col_1)
    dict_val_2 = dict_val(f2, key_cols_2, val_col_2)
    f_3= open(f3, 'w+')
    f_4 = open(f4, 'w')
    f_5 = open(f5, 'w')
    
    for k_1, v_1 in dict_val_1.items():
        if k_1 in dict_val_2.keys():
            v_2 = dict_val_2[k_1]
            f_3.write(str(k_1) + ',' + str(v_1) + '#'  + str(v_2) + '\n')
        else:
            f_4.write(str(k_1) + ',' + str(v_1)  + '\n')
    f_3.close()
    f_4.close()
    
    for k_2, v_2 in dict_val_2.items():
        if k_2 not in dict_val_1.keys():
            f_5.write(str(k_2) + ',' + str(v_2) + '\n')
    f_5.close()
            


            


def dict_val(f, key_cols:(str), val_col:str):
    """Form  a new dictionary which the key is predefined in key_cols
    and value is from val_col"""
    dict_ = defaultdict(list)
    with open (f, 'r', encoding="utf-8", newline='') as read_obj:
        csv_reader = csv.DictReader(read_obj)
        headers = csv_reader.fieldnames
        i = 0
        for row_dict in csv_reader:
            #i += 1
            #if i > 20000:
            #   break
            key = tuple(row_dict[key_col] for key_col in key_cols)
            val = row_dict[val_col]
            dict_[key].append(val)
    return dict_


