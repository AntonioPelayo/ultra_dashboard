from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

def get_tables(db_url):
    """
    Returns the list of tables in the database.

    Args:
        db_url (str): The URL of the database.
    Returns:
        list: A list of table names in the database.
    """
    try:
        engine = create_engine(db_url)
        with engine.connect() as connection:
            result = connection.execute(text("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema='public';
            """))
            tables = [row[0] for row in result.fetchall()]
    except Exception as e:
        print(f"Error fetching tables: {e}")
        tables = []

    return tables

def test_connection(db_url):
    """
    Tests the connection to the database.
   
    Args:
        db_url (str): The URL of the database.
    Returns:
        bool: True if the connection is successful, False otherwise.
    """
    try:
        engine = create_engine(db_url)
        with engine.connect() as connection:
            return True
    except SQLAlchemyError as e:
        print(f"Connection failed: {e}")
        return False
