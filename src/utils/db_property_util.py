import configparser

class DbPropertyUtil:

    @staticmethod
    def get_connection_params(property_file: str = "db.properties"):
        config=configparser.ConfigParser()
        read_files=config.read(property_file)
        if not read_files or "mysql" not in config:
            raise Exception("MySQL configuration not found in db.properties")
        return config["mysql"]
