import csv
import fileinput

def remove_q(f, col=None):
    """Remove ' from the begining of a string in given columns
    save in temp file and overwrite the same file later."""
    with fileinput.input(f, inplace=True, mode='r') as f:
        reader = csv.DictReader(f)
        print(",".join(reader.fieldnames))  # print back the headers
        i = 0
        for row_dict in reader:
            i += 1
            if i > 10:
                break
            if row_dict[col].startswith("''"):
                row_dict[col] = row_dict[col][2:]
                print(','.join([col, row_dict[col]]))

