import psycopg
from unittest import TestCase, main

# DEFINE THE DATABASE CREDENTIALS
user = 'testuser'
password = 'testpwd'
host = 'localhost'
port = 5432
database = 'vectordb'


class TestDatabase(TestCase):
    # Vérifier connection à la base de données
    def test_connection(self):

        # DB_PSY_URI = st.secrets.DB_PSY_URI
        db_url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
        print(db_url)
        self.assertIsNotNone(db_url)

        with psycopg.connect(conninfo=db_url) as conn:
            self.assertIsInstance(conn, psycopg.Connection)

if __name__  == '__main__':
    main(verbosity=2)