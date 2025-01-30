import os
import sys

from utils import get_tables

def main():
    if len(sys.argv) == 1:
        db_url = os.getenv("DATABASE_URL")
    elif len(sys.argv) == 2:
        db_url = sys.argv[1]
    else:
        print("Usage: python database/list_tables.py <optional: db_url>")
        sys.exit(1)

    print("Getting tables...")
    tables = get_tables(db_url)
    print("-------")
    for table in tables:
        print(table)
    print("-------------")
    print("End of tables")

if __name__ == "__main__":
    main()
