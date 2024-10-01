from DataSingleton import DBSingleton
db = DBSingleton()
conn = db.connect("Driver={ODBC Driver 18 for SQL Server};Server=SERVER3\\SQLEXPRESS;Database=KhoUni;UID=sa;PWD=2911;Encrypt=yes;TrustServerCertificate=yes;")
cursor = conn.cursor()
cursor.execute("select * from Account")
for row in cursor.fetchall():
    print(row)
