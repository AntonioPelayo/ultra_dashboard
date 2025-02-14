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

### Insert data
# ./venv/bin/python database/upload_data.py $DATABASE_URL <table_name> <path_to_csv> <optional: --r(eplace)>

### List tables
# ./venv/bin/python database/list_tables.py <optional: DB_URL>
# ./venv/bin/python database/list_tables.py $DATABASE_URL


## Web app
### Development with auto reload
# ./venv/bin/python -m ultra_dashboard.app

### Heroku deployment
# ./venv/bin/python -m gunicorn ultra_dashboard.app:server -b 127.0.0.1:8050


# Unset the environment variables
unset $(grep -v '^#' .env | sed -E 's/(.*)=.*/\1/' | xargs)
