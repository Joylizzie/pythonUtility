from pathlib import Path

def create_folder_if_needed(base_dir, folder):
    """ If a new folder doesn\'t exist, create the folder

    :param base_dir: parent directory where the folder to be created
    :type base_dir: str
    :param folder: The new folder name 
    :type folder: str
    """
   
    if not Path.exists(base_dir/folder):
        Path.mkdir(base_dir/folder)

def create_folder_for_file_if_needed(path_file):
    """Given a file with it's path, if the directory for this file doesn't exist,
    created the directory

    :param path_file: the file name and it's directory to reside
    :type path_file: str
    """

    path_name = Path.absolute(path_file)
    create_folder_if_needed(path_name)
