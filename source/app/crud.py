import sqlalchemy

from source.app.database_connect import DatabaseConnector
import datetime
import pytz


class Crud(object):
    def __init__(self, connection_info):
        self.database_connector = DatabaseConnector(connection_info)
        self.database_engine = self.database_connector.get_database_engine()

    def add_new_row(self, name, username):
        with self.database_engine.connect() as connection:
            connection.execute(sqlalchemy.text(
                "INSERT INTO e_crud (e_name, e_username, e_created_on) VALUES (:e_name, :e_username, :e_created_on);"),
                [{"e_name": name, "e_username": username,
                  "e_created_on": datetime.datetime.now(pytz.timezone('Europe/Berlin'))}])
            connection.commit()

    def get_all_rows(self):
        with self.database_engine.connect() as connection:
            result = connection.execute(sqlalchemy.text("SELECT * FROM e_crud;"))
            print(result.all())

    def get_last_value(self):
        with self.database_engine.connect() as connection:
            result = connection.execute(sqlalchemy.text("SELECT last_value FROM e_crud_e_id_seq;"))
            return result.one()

    def get_row_by_id(self, e_id):
        with self.database_engine.connect() as connection:
            result = connection.execute(sqlalchemy.text("SELECT * FROM e_crud WHERE e_id= :e_id;"), [{"e_id": e_id}])
            return result.one()

    def get_row_count(self, e_id=None):
        with self.database_engine.connect() as connection:
            if e_id is None:
                result = connection.execute(sqlalchemy.text("SELECT * FROM e_crud;"))
            else:
                result = connection.execute(sqlalchemy.text("SELECT * FROM e_crud WHERE e_id= :e_id;"),
                                            [{"e_id": e_id}])
            return result.rowcount

    def update_row(self, e_id, name, username):
        with self.database_engine.connect() as connection:
            connection.execute(sqlalchemy.text(
                "UPDATE e_crud SET e_name= :e_name, e_username= :e_username, e_updated_on= :e_updated_on "
                "WHERE e_id= :e_id;"),
                [{"e_id": e_id, "e_name": name, "e_username": username,
                  "e_updated_on": datetime.datetime.now(pytz.timezone('Europe/Berlin'))}])
            connection.commit()

    def delete_row_by_id(self, e_id):
        with self.database_engine.connect() as connection:
            connection.execute(sqlalchemy.text("DELETE FROM e_crud WHERE e_id= :e_id;"), [{"e_id": e_id}])
            connection.commit()

    def delete_all_rows(self):
        with self.database_engine.connect() as connection:
            connection.execute(sqlalchemy.text("DELETE FROM e_crud;"))
            connection.commit()
