import xlwt

wb = xlwt.Workbook()
sheet = wb.add_sheet('Movies')
sheet.write(0, 0, 'Html Movie Title')

wb.save('movies.xlsx')