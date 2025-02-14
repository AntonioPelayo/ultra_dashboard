import argparse
import os
import sys

from utils import get_tables

def main():
    parser = argparse.ArgumentParser(description="List all tables in the database.")
    parser.add_argument(
        "db_url",
        nargs="?",
        default=os.getenv("DATABASE_URL"),
        help="The database URL (defaults to the DATABASE_URL environment variable)"
    )
    args = parser.parse_args()

    if not args.db_url:
        print("Error: No database URL provided and DATABASE_URL environment variable is not set.")
        sys.exit(1)

    print("Getting tables in database...")
    tables = get_tables(args.db_url)
    print("-"*40)
    for table in tables:
        print(table)
    print("-"*40)
    print("End of tables")

if __name__ == "__main__":
    main()
