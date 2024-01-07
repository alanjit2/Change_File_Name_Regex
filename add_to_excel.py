import xlsxwriter

def display_in_excel(old_file_name_list, new_file_name_list):
    workbook = xlsxwriter.Workbook("Old_New_File_Names.xlsx")
    sheet = workbook.add_worksheet('Sheet1')
    sheet.write(0,0,"Old File Name")
    sheet.write(0,1,"New File Name")
    counter = 0
    row = 1
    for file_name in old_file_name_list:
        sheet.write(row, 0, file_name)
        sheet.write(row, 1, new_file_name_list[counter])
        row += 1
        counter += 1

    workbook.close()