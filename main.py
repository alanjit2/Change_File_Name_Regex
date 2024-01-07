import os # To split file name and exention and extract the file names from the file path
from rename_files import parse_file_name # Renames the actual file
from add_to_excel import display_in_excel # Adds file names to xlsx spreadsheet

if __name__ == '__main__':
    number_of_chars = 8
    old_file_name_list =[]
    new_file_name_list = []

    directory = "C:\PWP2022\PWP2022"
    # iterate over Images in the directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            # Function sends back two lists
            old_file_name_list, new_file_name_list = parse_file_name(f, number_of_chars, "ALAN",  old_file_name_list, new_file_name_list)
    display_in_excel(old_file_name_list, new_file_name_list)