import xlsxwriter 
 
workbook = xlsxwriter.Workbook('sample.xlsx') 
 
worksheet = workbook.add_worksheet() 

worksheet.write('A1', 'Hello..') 
worksheet.write('B1', 'Parth') 
worksheet.write('C1', 'For') 
worksheet.write('D1', 'Jadar') 
 
workbook.close() 
