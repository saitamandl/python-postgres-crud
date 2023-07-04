class ConnectionInfo(object):
    def __init__(self, database_type, database_name, database_user, database_password,
                database_host, database_port):
        self.database_type = database_type
        self.database_name = database_name
        self.database_user = database_user
        self.database_password = database_password
        self.database_host = database_host
        self.database_port = database_port

    def print_connection(self):
        print("Connection Info", self.database_type)

