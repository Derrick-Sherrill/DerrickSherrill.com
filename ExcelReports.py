import xlrd

ExcelSheet1 = 'YoutubeExcelSheet.xlsx'
ExcelSheet2 = 'YoutubeExcelSheet_2.xlsx'

Book1 = xlrd.open_workbook(ExcelSheet1)
Book2 = xlrd.open_workbook(ExcelSheet2)

first_sheet = Book1.sheet_by_index(0)
second_sheet = Book2.sheet_by_index(0)


i =0
total =0

for row in range(first_sheet.nrows):
    if str(first_sheet.cell(row,1).value) == "Key Lime":
        i = i +1
        total = total + (first_sheet.cell(row,2).value)
    else:
        pass

for row in range(second_sheet.nrows):
    if str(first_sheet.cell(row,1).value) == "Key Lime":
        i = i +1
        total = total + (second_sheet.cell(row,2).value)
    else:
        pass

print(i)
print(total)

print(total/i)
