import psycopg
from unittest import TestCase, main
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# DEFINE THE DATABASE CREDENTIALS
user = os.environ['DB_USER']
password = os.environ['DB_PASS']
host = os.environ['DB_HOST']
port = os.environ['DB_PORT']
database = os.environ['DB_NAME']


db_url = f"postgresql://{user}:{password}@{host}:{port}/{database}"

print(db_url)

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