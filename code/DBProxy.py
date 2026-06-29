from dbm import sqlite3


# -*- coding: utf-8 -*-
import sqlite3

class DBProxy:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.connection.execute('''
            CREATE TABLE IF NOT EXISTS dados (
                name TEXT,
                score INTEGER,
                date TEXT
            )
        ''')

    def save(self, score_dict: dict):
        self.connection.execute('INSERT INTO dados (name, score, date) VALUES (:name, :score, :date)', score_dict)
        self.connection.commit()

    def retrieve_top10(self):
        return self.connection.execute('SELECT * FROM dados ORDER BY score DESC LIMIT 10').fetchall()

    def close(self):
        return self.connection.close()
