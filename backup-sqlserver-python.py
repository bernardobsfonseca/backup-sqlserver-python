import pyodbc

server = 'Your server'
database = 'Your database'
username = 'Your username'
password = 'Your password'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+
                      ';DATABASE=MASTER;UID='+username+';PWD='+password)
cnxn.autocommit = True

def execute(cmd):
    cursor = cnxn.cursor()
    cursor.execute(cmd)
    while cursor.nextset():
        pass
    cursor.close()

print('backing up...')
directory = 'Your path'
arq = f'name_arquive.bak'
execute(f"BACKUP DATABASE [{database}] TO DISK = '{directory}{arq}'")
cnxn.close()
print('done')