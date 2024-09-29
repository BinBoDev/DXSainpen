import  pandas as pd
import pyodbc
#connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER3\SQLEXPRESS};DATABASE={KhoUni};UID={sa};PWD={2911}'
#connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER3\SQLEXPRESS};DATABASE={KhoUni};UID={sa};PWD={2911}'


try:
    # Kết nối đến SQL Server
   #Driver={ODBC Driver 18 for SQL Server};Server=localhost;Database=TestDB;UID=sa;PWD=your_password;Encrypt=yes;TrustServerCertificate=yes;

    conn = pyodbc.connect("Driver={ODBC Driver 18 for SQL Server};Server=SERVER3\\SQLEXPRESS;Database=KhoUni;UID=sa;PWD=2911;Encrypt=yes;TrustServerCertificate=yes;")
    print("Kết nối thành công!")
    query = 'select [userName] from [dbo].[Account]'
    #df = pd.read_sql(query, conn)
    cursor =conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    # Đóng kết nối
    conn.close()
except Exception as e:
    print("Kết nối không thành công!")
    print(e)