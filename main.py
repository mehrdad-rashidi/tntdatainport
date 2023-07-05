from file.Excel import Excel
from database import MysqlDatabase
from database import MysqlCRUD
from file import FileUtils

"""
    TNTIran Api for Import Voucher of Goods To Database of Portal
      1. Connect to TNTIran mail server
      2. Read the UNSEEN emailServer
      3. Download the attachment Excel
      4. Read the Excel file use Panda Library and Transform the data and import to Dataframe
      5. import the data to Mysql database in to part

"""
myFile = Excel('C:/Users/Mehrdad/Desktop/coalpublic2013.xlsx')
sheets = myFile.sheet_name
print(sheets)
for sheet in sheets:
    df = myFile.read_sheet(sheet)
    print(df.head())
    print('loc is 3 : ', df.loc[3][0], type(df.loc[3]))
db = MysqlDatabase.MysqlDatabase('localhost', 'root', 'Aa123456@', 'tnt')
crud = MysqlCRUD.MysqlCRUD(db)
result = crud.get_column('tb_agent')
# print(result)
# print(type(result))
result1 = crud.get_schema_name('tb_agent')
# print(result)
# print(type(result))
data = [124, 2, 'test2', '124@tnt.com']
crud.save('tb_agent', data)

file_directory = FileUtils.FileUtils('C:/Download')
file, directory = file_directory.list_file()
print(file)
print(directory)
myFile2 = Excel(file[0])
sheets2 = myFile2.sheet_name
print(sheets2)
path, file_name = file_directory.create_file('Script', 'sql', 'C:/Download')
del_path = file_directory.delete_file('Script.sql', 'C:/Download')
print(path, file_name)
print(f'delete file : {del_path}')
