from app.connection_info import ConnectionInfo
from app.crud import Crud

if __name__ == '__main__':
    print('Application started')
    connection_info = ConnectionInfo(database_type="postgresql",
                                     database_name="py_pg_crud",
                                     database_user="safeguard",
                                     database_password="&j#n59^%V38bGN@y!4zV7B2B5",
                                     database_host="localhost",
                                     database_port="5001")
    crud = Crud(connection_info)
    crud.add_new_row()
    print("done")
# PDQwx7JNchhN2AbkAXf39jrRy