from utils import create_table, drop_table, table_exists

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Create a table in the database and upload data.")
    parser.add_argument("db_url", help="The URL of the database.")
    parser.add_argument("table_name", help="The name of the table to create.")
    parser.add_argument("--c", action="store_true", help="Create a new table.")
    parser.add_argument("--d", action="store_true", help="Drop an existing table.")
    args = parser.parse_args()

    if not args.c and not args.d:
        print("Please specify either --c or --d (create or drop).")

        if table_exists(args.db_url, args.table_name):
            print(f"Table {args.table_name} already exists.")
        else:
            print(f"Table {args.table_name} does not exist.")

            print(f"Creating new table: {args.table_name}...")
            if create_table(args.db_url, args.table_name):
                print(f"Table {args.table_name} created successfully.")
    elif args.c and args.d:
        print("Please specify only one of --c or --d.")

        if table_exists(args.db_url, args.table_name):
            print(f"Table {args.table_name} already exists.")
        else:
            print(f"Table {args.table_name} does not exist.")
    elif args.c and create_table(args.db_url, args.table_name):
        print(f"Table {args.table_name} created successfully.")
    elif args.d and drop_table(args.db_url, args.table_name):
        print(f"Table {args.table_name} dropped successfully.")

if __name__ == "__main__":
    main()
