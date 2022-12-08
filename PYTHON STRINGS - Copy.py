
SQL ALCHEMY CONNECTION STRING

db_con =r'mssql://@localhost\SQLEXPRESS/ReportsAutomation_K?driver=ODBC Driver 17 for SQL Server' 

connection = sa.create_engine(db_con).connect()



PYODBC CONNECTION STRING

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=localhost\SQLEXPRESS;'
                      'Database=ReportsAutomation_K;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
