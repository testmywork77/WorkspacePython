import xlrd


workbook = xlrd.open_workbook("DataFile_XLSX.xlsx")
sheet = workbook.sheet_by_name("Sheet1")

rows = sheet.nrows  # Rows count
print(f"Rows count: {rows}")

cols = sheet.ncols  # Columns count
print(f"Columns count: {cols}")

for curr_row in range(1, rows):
    userName = sheet.cell_value(curr_row, 0)
    password = sheet.cell_value(curr_row,1)
    print(f"UserName: {userName}, Password: {password}")

