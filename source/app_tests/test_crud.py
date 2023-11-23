import os
import unittest

from source.app.database_connection_info import DatabaseConnectionInfo
from source.app.crud import Crud


class TestCrud(unittest.TestCase):
    crud = None
    database_connection_info = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.database_connection_info = DatabaseConnectionInfo(database_type=os.environ.get('DATABASE_TYPE'),
                                                              database_name=os.environ.get('DATABASE_NAME'),
                                                              database_user=os.environ.get('DATABASE_USER'),
                                                              database_password=os.environ.get('DATABASE_PASSWORD'),
                                                              database_host=os.environ.get('DATABASE_HOST'),
                                                              database_port=os.environ.get('DATABASE_PORT'))
        cls.crud = Crud(cls.database_connection_info)
        last_e_id = cls.crud.get_last_value()[0]
        name = "eg_n_{}".format(last_e_id)
        username = "eg_un_{}".format(last_e_id)
        cls.crud.add_new_row(name=name, username=username)

    def test_insert_row(self):
        last_e_id = self.crud.get_last_value()[0]
        new_e_id = last_e_id + 1
        name = "eg_n_{}".format(new_e_id)
        username = "eg_un_{}".format(new_e_id)
        self.crud.add_new_row(name=name, username=username)
        row = self.crud.get_row_by_id(new_e_id)
        self.assertEqual(name, row[1])
        self.assertEqual(username, row[2])
        self.seq_flag = True

    def test_update_row(self):
        last_e_id = self.crud.get_last_value()[0]
        new_e_id = last_e_id + 1
        name = "eg_n_{}".format(new_e_id)
        username = "eg_un_{}".format(new_e_id)
        self.crud.add_new_row(name=name, username=username)
        name = "eg_n_{}".format(new_e_id)
        username = "eg_un_{}".format(new_e_id)
        self.crud.update_row(e_id=new_e_id, name=name, username=username)
        row = self.crud.get_row_by_id(new_e_id)
        self.assertEqual(name, row[1])
        self.assertEqual(username, row[2])
        self.seq_flag = True

    def test_delete_row(self):
        last_e_id = self.crud.get_last_value()[0]
        new_e_id = last_e_id + 1
        name = "eg_n_{}".format(new_e_id)
        username = "eg_un_{}".format(new_e_id)
        self.crud.add_new_row(name=name, username=username)
        self.crud.delete_row_by_id(e_id=new_e_id)
        row_count = self.crud.get_row_count(new_e_id)
        self.assertEqual(0, row_count)
        self.seq_flag = True

    def test_delete_all_rows(self):
        last_e_id = self.crud.get_last_value()[0]
        new_e_id = last_e_id + 1
        name = "eg_n_{}".format(new_e_id + 1)
        username = "eg_un_{}".format(new_e_id + 1)
        self.crud.add_new_row(name=name, username=username)
        self.crud.delete_all_rows()
        row_count = self.crud.get_row_count()
        self.assertEqual(0, row_count)
        self.seq_flag = True


if __name__ == '__main__':
    unittest.main()
