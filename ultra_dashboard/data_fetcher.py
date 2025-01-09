import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

from ultra_dashboard.config import DATABASE_URL

def get_finishers_per_year(race):
    """
    Fetches the number of finishers for each year from the PostgreSQL database.

    Returns:
        pd.DataFrame: A DataFrame with columns "year" and "finishers".
    """
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL environment variable not set.")

    engine = create_engine(DATABASE_URL)

    if race == "WSER":
        table = "wser_historical_results"

    query = f"""
        SELECT year, COUNT(*) AS finishers
        FROM {table}
        WHERE time != '00:00:00'
        GROUP BY year
        ORDER BY year;
    """

    try:
        df = pd.read_sql(query, engine)
        return df
    except SQLAlchemyError as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame(columns=["year", "finishers"])

def get_winners_per_year(race):
    """
    Fetches the first place finisher for each year from the PostgreSQL database.

    Returns:
        pd.DataFrame: A DataFrame with first place finisher data for each year.
    """
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL environment variable not set.")

    engine = create_engine(DATABASE_URL)

    if race == "WSER":
        table = "wser_historical_results"

    query = f"""
        SELECT *
        FROM {table}
        WHERE place = 1
        ORDER BY year;
    """

    try:
        df = pd.read_sql(query, engine)
        return df
    except SQLAlchemyError as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame(columns=["year", "finishers"])
