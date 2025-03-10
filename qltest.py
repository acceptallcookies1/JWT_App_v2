import sqlite3

def vulnerable_query(user_input):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # 🚨 SQL Injection Vulnerability (unsafe user input)
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    cursor.execute(query)  # ❌ This is unsafe!

    return cursor.fetchall()

user_input = input("Enter username: ")
print(vulnerable_query(user_input))
