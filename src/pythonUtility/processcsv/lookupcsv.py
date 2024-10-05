import csv
from typing import List
from collections import defaultdict
from pathlib import Path


def differs(f1:str,key_cols_1:List[str],val_col_1: any, \
            f2:str, key_cols_2:List[str], val_col_2:any, \
                f3:str, f4:str, f5:str):
    """Compare two csv files - file1 and file2, with selected columns. 
        write the items exist in both files to a csv file f3
        write the items exist in f1 not in f2 to f4,
        write the items exist in f2 not in f1 to f5

    :param f1: source csv file 
    :type f1: str
    :param key_cols_1: the column's names which are selected to be compared
    :type key_cols_1: List[str]
    :param val_col_1: the value to be compared, mostly 'amount'
    :type val_col_1: float or any
    :param f2: target csv file to be compared with f1
    :type f2: str
    :param key_cols_2: the column's names which are selected to be compared
    :type key_cols_2: List[str]
    :param val_col_2: the value to be compared, mostly 'amount'
    :type val_col_2: float or any
    :param f3: csv file to hold items both in f1 and f2
    :type f3: str
    :param f4: items in f1 not in f2
    :type f4: str
    :param f5: items in f2 not in f1
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

def dict_val(f:str, key_cols:(str), val_col:any):
    """Populate a new dictionary from a csv file with predefined columns 

    :param f: the source csv file
    :type f: str
    :param key_cols: the columns selected to form the dictionary's key
    :type key_cols: a tuple of str
    :param val_col: the value to be compared, mostly 'amount'
    :type val_col: float or any
    :return: a dictionary with a tuple of columns as key and value as the val_col
    :rtype: dictionary
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

    """Populate a new dictionary from a csv file with predefined columns 

    :param f: 
    :type f: str
    :param key_cols:The columns selected for the new dictionary's key
    :type key_cols: a tuple of str
    :param val_col: the column selected foe the new dictioary's value
    :type val_col: could be anyt, mostly will be float
    :return: a dictionary with selected columns of key and value
    :rtype: dict
    """