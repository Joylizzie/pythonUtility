from pathlib import Path
from processcsv import processcsv as procs
from pathoperation.create_folder import create_folder_if_needed

def main(base_dir, in_pathfilename,outfolder):
    #create_folder_if_needed(base_dir, folder)
    #procs.(base_dir, in_pathfilename, outfolder)
    pass

if __name__ == '__main__':
    base_dir = Path(__file__).resolve().parents[1]
    in_pathfilename = 'data/rawdata/sep_1.csv'
    folder = 'data/ProcessedData'
    main(base_dir, in_pathfilename,folder)