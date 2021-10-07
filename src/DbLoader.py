'''
    Python module for database connection (POSTGRESQL)
'''

import psycopg2 
import json

class DbLoader:

    def __init__(self, host, port, dbname, user, password):
        
        # postgres
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password

    def connectDB(self):
        
        # connection information
        conn = 'host = {host} port = {port} dbname = {dbname} user = {user} password = {password}'.format(
            host = self.host,
            port = self.port,
            dbname = self.dbname,
            user = self.user,
            password = self.password
        )

        # establish connection
        print(conn)
        self.db = psycopg2.connect(conn)
        self.cur = self.db.cursor()
    
    def view_connDB(self):

        sql = 'SELECT VERSION()'        
        self.cur.execute(sql)
        result = self.cur.fetchone()
        self.db.close()

        return result

    def view_table(self):
        
        sql = """SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"""
        self.cur.execute(sql)
        result = self.cur.fetchall()
        
        cols = ('tbl_name',)
        tbl_list = []

        if len(result) == 0:
            print('There is no data')
        else:
            for rows in result:
                tbl_list.append(dict(zip(cols, rows)))

        # return json output
        return json.dumps(tbl_list)

