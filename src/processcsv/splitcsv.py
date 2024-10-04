import csv
from collections import defaultdict
from pathlib import Path
#from pythonutility.pathoperation.createfolder import create_folder_if_needed
from pathoperation.createfolder import create_folder_if_needed


def split_csv(in_file:str, split_folder, out_file_name, delete_infile=True):
    """split a csv file with a header into different csv files based on the value in the 
    first column. 

    :param in_file: the csv file to be split
    :type in_file: str
    :param split_folder: directory to hold the split files
    :type split_folder: str
    :param out_file_name: the file name to hold content of the csv file with 
            same values in first column
    :type out_file_name: str
    """

    result = defaultdict(list)
    with open(in_file, "r", encoding="utf-8", newline="") as csv_r:
        # unpack the header and data from csv read object
        _header, *data = csv.reader(csv_r)
    for row in data:
        result[row[0]].append(row)

    for k, v in result.items():
        create_folder_if_needed(f"{split_folder}/{k}")
        with open(
            f"{split_folder}/{k}/{out_file_name}", "w", newline="", encoding="utf-8"
        ) as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(_header)
            csv.writer.writerows(v)
    if delete_infile:
        Path.unlink(in_file)
