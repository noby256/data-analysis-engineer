import psycopg2


class SqlHandler:

    def drop_table(self):
        self._connect()
        cur = self.conn.cursor()
        cur.execute('''DROP TABLE eur_base;''')
        self._disconnect()

    def create_table(self, column_names):
        self._connect()
        cur = self.conn.cursor()
        query = '''
        CREATE TABLE eur_base(
        id SERIAL,
        date DATE,
        {}
        );
        '''.format(column_names)
        cur.execute(query)
        self.conn.commit()
        cur.close()
        # cur.execute('SELECT * FROM notes')
        self._disconnect()

    def copy_csv_into_table(self, script_path):
        self._connect()
        cur = self.conn.cursor()
        cur.execute('''
        COPY eur_base
        FROM '{}/eurofxref-hist.csv' DELIMITER ',' CSV HEADER;
        '''.format(script_path))
        cur.close()
        self._disconnect()

    def _connect(self):
        self.conn = psycopg2.connect(user="dbuser1",
                                     password="dbuser1",
                                     host="127.0.0.1",
                                     port="5432",
                                     database="testdb")
        self.conn.autocommit=True
        # "host=localhost dbname=testdb user=dbuser1 password=dbuser1")

    def _disconnect(self):
        if self.conn:
            self.conn.close()
            print("PostgreSQL connection is closed")



