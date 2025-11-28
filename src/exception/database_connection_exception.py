class DatabaseConnectionException(Exception):
    def __init__(self,message="Database Connection Error"):
        super().__init__(message)