import sqlite3

# Simulated config file or a settings module
CONFIG = {
    "default_table": "users",
    "default_column": "username"
}

def get_data_by_config_value(value, user_id):
    query = "SELECT * FROM ? WHERE ? = ?"
    params = (CONFIG["default_table"], CONFIG["default_column"], value)

    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    connection.close()

    query_2 = "SELECT * FROM users WHERE id = ?"
    params_2 = (user_id,)

    connection_2 = sqlite3.connect("database.db")
    cursor_2 = connection_2.cursor()
    cursor_2.execute(query_2, params_2)
    result_2 = cursor_2.fetchall()
    connection_2.close()

    return result, result_2

# Test
print(get_data_by_config_value("admin", 1))
#nothing here