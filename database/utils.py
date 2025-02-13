from sqlalchemy import (
    create_engine,
    text,
    Column,
    Float,
    Integer,
    Interval,
    String,
    Table,
    MetaData
)
from sqlalchemy.exc import SQLAlchemyError

metadata = MetaData()

def race_table_schema(table_name):
    """
    Defines the schema for race result tables.

    Args:
        table_name (str): The name of the table.

    Returns:
        Table: A SQLAlchemy Table object representing the race table schema.
    """
    return Table(
        table_name, metadata,
        Column('event_id', Integer),
        Column('place', Integer),
        Column('first_name', String(100), nullable=False),
        Column('last_name', String(100), nullable=False),
        Column('full_name', String(100), nullable=False),
        Column('city', String(100)),
        Column('state', String(5)), # Country code for international
        Column('age', Integer, nullable=False),
        Column('division', String(3)),
        Column('division_place', Integer),
        Column('time', Interval),
        Column('time_seconds', Float),
        Column('runner_rank', Float),
        Column('athlete_url', String(150)),
        Column('year', Integer, nullable=False),
    )

def create_table(db_url, table_name):
    """
    Creates a new table in the database.

    Args:
        db_url (str): The URL of the database.
        table_name (str): The name of the table to create.
    Returns:
        bool: True if the table was created successfully, False otherwise.
    """
    try:
        _ = race_table_schema(table_name)
        metadata.create_all(create_engine(db_url))
        return True
    except SQLAlchemyError as e:
        print(f"Error creating table: {e}")
        return False

def drop_table(db_url, table_name):
    """
    Drops a table from the database.

    Args:
        db_url (str): The URL of the database.
        table_name (str): The name of the table to drop.
    Returns:
        bool: True if the table was dropped successfully, False otherwise.
    """
    try:
        table = race_table_schema(table_name)
        table.drop(create_engine(db_url))
        return True
    except SQLAlchemyError as e:
        print(f"Error dropping table: {e}")
        return False

def get_tables(db_url):
    """
    Returns the list of tables in the database.

    Args:
        db_url (str): The URL of the database.
    Returns:
        list: A list of table names in the database.
    """
    try:
        with create_engine(db_url).connect() as connection:
            result = connection.execute(text("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema='public';
            """))
            return [row[0] for row in result.fetchall()]
    except Exception as e:
        print(f"Error fetching tables: {e}")
        return []

def table_exists(db_url, table_name):
    """
    Checks if a table exists in the database.

    Args:
        db_url (str): The URL of the database.
        table_name (str): The name of the table to check.
    Returns:
        bool: True if the table exists, False otherwise.
    """
    return table_name in get_tables(db_url)

def test_connection(db_url):
    """
    Tests the connection to the database.

    Args:
        db_url (str): The URL of the database.
    Returns:
        bool: True if the connection is successful, False otherwise.
    """
    try:
        with create_engine(db_url).connect() as connection:
            return True
    except SQLAlchemyError as e:
        print(f"Connection failed: {e}")
        return False

def upload_data_to_table(db_url, table_name, df, replace=False):
    """
    Uploads data to a table in the database.

    Args:
        db_url (str): The URL of the database.
        table_name (str): The name of the table to upload data to.
        df (DataFrame): The data to upload.
        replace (bool): Whether to replace the data to the table or append.
    Returns:
        bool: True if the data was uploaded successfully, False otherwise.
    """
    try:
        df.to_sql(
            table_name,
            create_engine(db_url),
            if_exists='replace' if replace else 'append',
            index=False
        )
        return True
    except SQLAlchemyError as e:
        print(f"Error uploading data to table: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
