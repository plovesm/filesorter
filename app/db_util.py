# Copyright 2017
# Author Paul Ottley

import sqlite3
from objects import FSfile

from datetime import date


class DatabaseUtil:

    def __init__(self):
        self.conn = None

    @staticmethod
    def open_connection(name="test.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES):
        conn = sqlite3.connect(name, detect_types)
        c = conn.cursor()
        print("Opened database successfully")
        return conn, c

    @staticmethod
    def create_files_table(c, table_name="Files",):
        c.execute('''DROP TABLE IF EXISTS ?;''', table_name)
        c.execute('''CREATE TABLE IF NOT EXISTS FILES
                         (  ID INTEGER PRIMARY KEY NOT NULL,
                            FILENAME TEXT NOT NULL,
                            DATE_TAKEN DATETIME,
                            FILE_TYPE TEXT,
                            SRC_DIR VARCHAR(50),
                            TGT_DIR VARCHAR(50));''')
        return True

    @staticmethod
    def insert_record(c, file=FSfile()):
        c.execute('''INSERT INTO FILES (FILENAME, DATE_TAKEN, FILE_TYPE, SRC_DIR, TGT_DIR) VALUES (?, ?, ?, ?, ?);''',
                  (file.get_filename(), file.get_date_taken(), file.get_type(), file.get_src_dir(), file.get_tgt_dir()))
        DatabaseUtil.commit_transaction(c.connection)
        return True

    @staticmethod
    def read_all_records(c):
        c.execute("SELECT * FROM FILES;")
        return c.fetchall();

    @staticmethod
    def read_first_record(c):
        c.execute("SELECT * FROM FILES;")
        return c.fetchone();

    @staticmethod
    def read_one_record(c, fields_values=[{'FILENAME' : 'frog.jpg'}]):
        select_script = "SELECT * FROM FILES WHERE ("
        for x in fields_values.keys():
            select_script += "{0} = {1}".format(x, fields_values[x])
            if x.index() < len(fields_values.keys())-1:
                select_script += ","
        select_script += ");"
        c.execute(select_script)

    # Update
    @staticmethod
    def update_record(c, date_taken, filename):
        c.execute('''UPDATE FILES SET (?) TO (?) WHEre ? = ?''', ("DATE_TAKEN", date_taken, "FILENAME", filename))
        DatabaseUtil.commit_transaction(c.connection)

        return True

    # Delete
    @staticmethod
    def delete_record(c, id):
        c.execute('''DELETE from FILES WHERE ID = ?''', id)
        DatabaseUtil.commit_transaction(c.connection)
        return True

    @staticmethod
    def commit_transaction(connection):
        connection.commit()

    @staticmethod
    def close_connection(connection):
        connection.close()
