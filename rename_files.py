import os # To split file name and exention and extract the file names from the file path
import re # To remove the prefix and identify the numbers
from check_dupe_in_list import check_duplicate # To check for dupilicates and re-edit the file name

def parse_file_name(fpath, number_of_chars, first_name, old_file_name_list, new_fname_list):
    prefix ="PWP2024_"
    zero_pad = '0' * (number_of_chars)
    file_name_with_ext = os.path.basename(fpath)
    old_file_name_list.append(file_name_with_ext)
    file_name, file_extension = os.path.splitext(file_name_with_ext)

    # Can be matched either by digits, underscores, or two underscores
    match_double_underscore = (re.search("__", file_name))
    if match_double_underscore is not None:
        start = match_double_underscore.start()
        length = match_double_underscore.regs[0][1]
        # String Splicing to isolate numbers, which identify the file and to add the name suffix
        right_len = len(file_name)
        numeric_part = file_name[length:right_len]
    else:
        match_underscore = (re.search("_", file_name))
        if match_underscore is not None:
            start = match_underscore.start()
            length = match_underscore.regs[0][1]
            right_len = len(file_name)
            numeric_part = file_name[length:right_len]
        else:
            match = (re.search(r'\d+', file_name_with_ext))
            if match is not None:
                start = match.start()
                length = match.regs[0][1]
                right_len = length - start
                numeric_part = file_name[start:length]
                numeric_part = re.findall(r'\d+', file_name_with_ext)


    numeric_part_str = ''.join(numeric_part)
    numeric_part_str = zero_pad + numeric_part_str
    # Padding
    numeric_part_str = numeric_part_str[-number_of_chars:]

    file_name_standardized = check_duplicate(prefix,numeric_part_str,first_name,file_extension,new_fname_list)
    new_fname_list.append(file_name_standardized)
    return old_file_name_list, new_fname_list

