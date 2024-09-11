from pathlib import Path

def create_folder_if_needed(base_dir, folder):
    """If a new folder doesn\'t exist, create the folder"""
    if not Path.exists(base_dir/folder):
        Path.mkdir(base_dir/folder)

def create_folder_for_file_if_needed(path_file):
    path_name = Path.absolute(path_file)
    create_folder_if_needed(path_name)

if __name__ == '__main__':
    base_dir = Path(__file__).resolve().parents[1]
    folder = 'data/processedData'
    create_folder_if_needed(base_dir, folder)