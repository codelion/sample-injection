import sqlite3

# Simulated config file or a settings module
CONFIG = {
    "default_table": "users",
    "default_column": "username"
}

def get_data_by_config_value(value):
    # This might look suspicious due to string concatenation with values from CONFIG.
    query = "SELECT * FROM " + CONFIG["default_table"] + " WHERE " + CONFIG["default_column"] + " = '" + value + "'"

    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()

    query_2 = "SELECT * FROM users WHERE id = " + str(user_id)

    connection_2 = sqlite3.connect("database.db")
    cursor_2 = connection_2.cursor()
    cursor_2.execute(query_2)
    result = cursor_2.fetchall()
    connection_2.close()

    return result

# Test
print(get_data_by_config_value("admin"))

#nothing here
