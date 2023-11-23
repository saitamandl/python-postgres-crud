import urllib.parse as url_parse
import sqlalchemy


class DatabaseConnector(object):
    def __init__(self, connection_info):
        self.database_type = connection_info.database_type
        self.database_name = connection_info.database_name
        self.database_user = connection_info.database_user
        self.database_password = connection_info.database_password
        self.database_host = connection_info.database_host
        self.database_port = connection_info.database_port

    def get_database_engine(self):
        connection_string = "{}://{}:{}@{}:{}/{}". \
            format(self.database_type,
                   self.database_user, url_parse.quote(self.database_password),
                   self.database_host, self.database_port,
                   self.database_name)
        return sqlalchemy.create_engine(connection_string)