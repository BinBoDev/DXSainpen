import  pyodbc
class DBSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DBSingleton, cls).__new__(cls)
            cls._instance.connection = None
        return cls._instance

    def connect(self, connection_string):
        if self.connection is None:
            self.connection = pyodbc.connect(connection_string)
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None

