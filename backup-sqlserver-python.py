import pyodbc

server = 'your_server'
database = 'your_database'
username = 'your_username'
password = 'your_password'
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
path = 'your_path'
file = 'file_name.bak'
execute(f"BACKUP DATABASE [{database}] TO DISK = '{path}{file}'")
cnxn.close()
print('done')
