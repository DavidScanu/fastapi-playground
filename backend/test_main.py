import psycopg
from unittest import TestCase, main

from database import get_db_uri

class TestDatabase(TestCase):
    # Vérifier connection à la base de données
    def test_connection(self):

        DB_URI = get_db_uri()
        self.assertIsNotNone(DB_URI)

        with psycopg.connect(conninfo=DB_URI) as conn:
            self.assertIsInstance(conn, psycopg.Connection)

if __name__  == '__main__':
    main(verbosity=2)