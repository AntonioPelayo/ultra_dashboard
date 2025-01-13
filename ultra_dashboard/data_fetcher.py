import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

from ultra_dashboard.config import DATABASE_URL

DATABASE_ENGINE = create_engine(DATABASE_URL)

def execute_query(query):
    """
    Executes the given SQL query on the PostgreSQL database.

    Args:
        query (str): The SQL query to execute.
    Returns:
        pd.DataFrame: A DataFrame with the query results.
    """
    try:
        df = pd.read_sql(query, DATABASE_ENGINE)
    except SQLAlchemyError as e:
        print(f"Error fetching data: {e}")
        df = pd.DataFrame()
    return df

def get_finishers_per_year(race):
    """
    Fetches the number of finishers for each year from the PostgreSQL database.

    Args:
        race (str): The name of the race's table to query.
    Returns:
        pd.DataFrame: A DataFrame with columns "year" and "finishers".
    """
    if race == "WSER":
        table = "wser_historical_results"

    return execute_query(f"""
        SELECT year, COUNT(*) AS finishers
        FROM {table}
        WHERE time != '00:00:00'
        GROUP BY year
        ORDER BY year;
    """)


def get_winners_per_year(race):
    """
    Fetches the first place finisher for each year from the PostgreSQL database.

    Args:
        race (str): The name of the race's table to query.
    Returns:
        pd.DataFrame: A DataFrame with first place finisher data for each year.
    """
    if race == "WSER":
        table = "wser_historical_results"

    return execute_query(f"""
        SELECT *
        FROM {table}
        WHERE place = 1
        ORDER BY year;
    """)
