import xlrd

workbook = 'workbook2.xlsx'

book1 = xlrd.open_workbook(workbook)

first_sheet = book1.sheet_by_index(0)


first_shift =0
second_shift = 0

for row in range(1,first_sheet.nrows):
    if float(first_sheet.cell(row,0).value) >= .375 and float(first_sheet.cell(row,0).value) <= .5:
        first_shift = first_shift + (first_sheet.cell(row,2).value)
    else:
        pass


for row in range(1,first_sheet.nrows):
    if float(first_sheet.cell(row,0).value) > .5 and float(first_sheet.cell(row,0).value) <= (17/24):
        second_shift = second_shift + (first_sheet.cell(row,2).value)
    else:
        pass

print(first_shift)
print(second_shift)
