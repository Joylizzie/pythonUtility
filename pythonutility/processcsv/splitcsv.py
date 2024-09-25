import csv
from collections import defaultdict
from pathlib import Path
from pathoperation.createfolder import create_folder_if_needed

def split_csv(in_file:str, split_folder, out_file_name):
    """split a csv file by the first column, and write to a new folder and new file name which is the
    one of unique value of the first column

    :param in_file: the csv file to be split
    :type in_file: str
    :param split_folder: directory to hold the splited file
    :type split_folder: str
    :param out_file_name: the file name to hold context of the csv file with same vaalue in first column
    :type out_file_name: str
    """
    result = defaultdict(list)
    with open(in_file, "r", encoding="utf-8", newline="") as csv_r:
        # unpack the header and data from csv read object
        _header, *data = csv.reader(csv_r)
    for a, *b in data:
        # unpack the first column and the rest columns from above data
        result[a].append([a, *b])

    for k, v in result.items():
        create_folder_if_needed(f"{split_folder}/{k}")
        with open(
            f"{split_folder}/{k}/{out_file_name}", "w", newline="", encoding="utf-8"
        ) as f:
            write = csv.writer(f)
            write.writerows([_header, *v])
    Path.unlink(in_file)
