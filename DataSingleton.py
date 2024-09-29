import pyodbc
class Databasesingleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Databasesingleton,cls).__new__(cls)
            cls._instance.connection = None
            cls._instance.cursor = None
        return cls._instance

    def __init__(self,connection_string):
        if self.connection is None:
            self.connection_string=connection_string
            self.connection = pyodbc.connect(self.connection_string)
            self.cursor = self.connection.cursor()

    def execute_query(self,query,params = None):
        if params:
            self.execute_query(query,params)
        else:
            self.execute_query(query)
        return self.cursor.fetchall()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
