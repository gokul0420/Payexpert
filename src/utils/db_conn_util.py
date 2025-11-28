import mysql.connector
from exception.database_connection_exception import DatabaseConnectionException
from utils.db_property_util import DbPropertyUtil


class DbConnUtil:
    @staticmethod
    def get_connection():
        try:
            params=DbPropertyUtil.get_connection_params()
            conn=mysql.connector.connect(
                host=params["host"],
                user=params["user"],
                password=params["password"],
                database=params["database"],
            )
            return conn
        
        except mysql.connector.Error as e:
            raise DatabaseConnectionException(f"Failed to connect to database :{e}")