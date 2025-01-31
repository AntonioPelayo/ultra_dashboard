# Load environment variables from .env
export $(grep -v '^#' .env | xargs)


# Run Python
## Database
### Test connection
# ./venv/bin/python database/test_connection.py <optional: DB_URL>
# ./venv/bin/python database/test_connection.py $DATABASE_URL

### Create table
# ./venv/bin/python database/create_or_drop_table.py $DATABASE_URL <table_name> <optional: --c or --d>
# ./venv/bin/python database/create_or_drop_table.py $DATABASE_URL temp_table

### List tables
# ./venv/bin/python database/list_tables.py <optional: DB_URL>
# ./venv/bin/python database/list_tables.py $DATABASE_URL


## Web app
### TODO: list commands


# Unset the environment variables
unset $(grep -v '^#' .env | sed -E 's/(.*)=.*/\1/' | xargs)
