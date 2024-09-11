from pathlib import Path
from create_folder import create_folder_if_needed

def main(base_dir, folder):
    create_folder_if_needed(base_dir, folder)

if __name__ == '__main__':
    base_dir = Path(__file__).resolve().parents[1]
    folder = 'data/ProcessedData'
    main(base_dir, folder)