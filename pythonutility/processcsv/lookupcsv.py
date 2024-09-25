import csv
from typing import List
from collections import defaultdict
from pathlib import Path


def differs(f1:str,key_cols_1:List[str],val_col_1, f2, key_cols_2, val_col_2, f3, f4, f5):

    """compare two csv files - file1 and file2, with selected columns. 
        write the items exist in both files to a csv file - f2,
        write the items exist in f1 not in f2 to f4,
        write the items exist in f2 not in f1 to f5

    :param f1: a file - f1 to be compared
    :type f1: str
    :param key_cols_1: the column's names which are selected to be compared
    :type key_cols_1: a list of string
    :param val_col_1: the value to be compared, mostly 'amount'
    :type val_col_1: could be numeric or any
    :param f2:The file -f2 to compare to the above file - f1
    :type f2: str
    :param key_cols_2:  the column's names which are selected to be compared
    :type key_cols_2: a list of string
    :param val_col_2: could be numeric or anythe value to be compared, mostly 'amount'
    :type val_col_2: could be numeric or any
    :param f3: the items exist in both files
    :type f3: str
    :param f4: the items in f1 not in f2
    :type f4: str
    :param f5: the items in f2 not in f1
    :type f5: str
    """
    
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
    """Populate a new dictionary from a csv file with predefined columns 

    :param f: source csv file 
    :type f: csv
    :param key_cols:The columns selected for the new dictionary's key
    :type key_cols: a tuple of str
    :param val_col: the column selected foe the new dictioary's value
    :type val_col: could be anyt, mostly will be float
    :return: a dictionary with selected columns of key and value
    :rtype: dict
    """

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
