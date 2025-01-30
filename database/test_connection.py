import os
import sys

from utils import test_connection

def main():
    if len(sys.argv) == 1:
        db_url = os.getenv("DATABASE_URL")
    if len(sys.argv) == 2:
        db_url = sys.argv[1]
    else:
        print("Usage: python database/test_connection.py <optional: db_url>")
        sys.exit(1)

    print("Testing database connection...")
    if test_connection(db_url):
        print("Connection successful.")

if __name__ == "__main__":
    main()
