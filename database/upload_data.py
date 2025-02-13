import argparse
import pandas as pd

from utils import create_table, table_exists, upload_data_to_table

def main():
    parser = argparse.ArgumentParser(description="Upload csv data to a new or existing table in the database.")
    parser.add_argument("db_url", help="The URL of the database.")
    parser.add_argument("table_name", help="The name of the table to create.")
    parser.add_argument("csv_file_path", help="The path to the CSV file containing the data.")
    parser.add_argument("--r", action="store_true", help="Replace the table instead of appending.")
    args = parser.parse_args()

    try:
        df = pd.read_csv(args.csv_file_path)
    except FileNotFoundError:
        print(f"CSV file '{args.csv_file_path}' not found.")
        return

    table_exists = table_exists(args.db_url, args.table_name)

    if not table_exists:
        print(f"Table {args.table_name} does not exist. Creating table...")
        if not create_table(args.db_url, args.table_name):
            print(f"Error creating table {args.table_name}.")
            return
        print(f"Table {args.table_name} created successfully.")

    if upload_data_to_table(args.db_url, args.table_name, df, replace=args.r):
        print("Data uploaded successfully.")

if __name__ == "__main__":
    main()
