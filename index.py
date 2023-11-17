import sqlite3

# Simulated config file or a settings module
CONFIG = {
    "default_table": "users",
    "default_column": "username"
}

def get_data_by_config_value(value):
    query = "SELECT * FROM ? WHERE ? = ?"

    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute(query, (CONFIG["default_table"], CONFIG["default_column"], value))
    result = cursor.fetchall()
    connection.close()

    return result

# Test
print(get_data_by_config_value("admin"))