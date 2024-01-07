# Check for duplicates during a name change
# If there are duplicates, it will add another letter of the name at the end of the numbers

def check_duplicate(prefix, numeric_part_str, first_name, file_extension, list):
    name_pos = 0
    not_duplicate = 0
    new_name = prefix  + numeric_part_str + first_name[name_pos] + "_" + first_name + file_extension
    while not_duplicate == 0:
        if new_name not in list:
            not_duplicate = 1
            return new_name
        else:
            name_pos = name_pos + 1
            new_name = prefix + numeric_part_str + first_name[0:name_pos] + "_" + first_name + file_extension
            not_duplicate = 0