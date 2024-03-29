
SQL ALCHEMY CONNECTION STRING

db_con =r'mssql://@localhost\SQLEXPRESS/ReportsAutomation_K?driver=ODBC Driver 17 for SQL Server' 

connection = sa.create_engine(db_con).connect()



PYODBC CONNECTION STRING

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=localhost\SQLEXPRESS;'
                      'Database=ReportsAutomation_K;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()


SQL

1. SET ANSI_NULLS ON:

When ANSI_NULLS is ON, a SELECT statement that uses WHERE column_name = NULL returns zero rows even if there are null values in column_name.According to ANSI(American National Standard Institute) any comparison or calculation performed with NULL is NULL. NULL is neither a string nor a number nor zero.It is simply NOT DEFINED.So, When I do SET ANSI_NULLS ON; I am simply telling SQL SERVER to follow the standard of ANSI.

When ANSI_NULLS is set to ON. ‘=’ operator is not able to identify NULL. This is the standard of ANSI that any comparison with NULL is always NULL. So you will never ever get a result for this. To find NULL in a column we use Keyword ‘IS NULL’.

2. SET QUOTED_IDENTIFIER ON:

In simple words, when you do SET QUOTED_IDENTIFIER ON you can use SQL identifier or reserved keywords in SQL as user-defined objects. It must be defined within double quotation marks & hence the name QUOTED_IDENTIFIER.

Consider a situation where you want your column name be ‘Identity’. But Identity is a keyword for SQL Server. How it will differentiate between a user referred Identitiy Or T-SQL referred Identity.This is where Quoted Idenfiers come in handy.


HTML:

spaces
<p>This is a &nbsp; regular space.</p>
<p>This is a &ensp; two spaces gap.</p>
<p>This is a &emsp; four spaces gap.</p>

LOVE PDF CODE


def love_pdf(input_files, path):

    public_key = 'project_public_ac0742b921677dca3282dd80a88374ba_umNAm40803ab085e17039c60cb640577709a5'

    # importing the ilovepdf api

    # creating a ILovePdf object
    ilovepdf = ILovePdf(public_key, verify_ssl=True)

    # assigning a new split tasky
    task = ilovepdf.new_task('merge')

    # adding the pdf file to the task
    for file in input_files:
        task.add_file(file)

    # setting the output folder directory
    # if no folder exist it will create one
    task.set_output_folder(path)

    # execute the task
    task.execute()

    # download the task
    task.download()

    # delete the task
    task.delete_current_task()

