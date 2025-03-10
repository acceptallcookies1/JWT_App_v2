import pymysql

def vulnerable_query(user_input):
    conn = pymysql.connect(host='localhost', user='root', password='root', database='testdb')
    cursor = conn.cursor()

    # 🚨 This is vulnerable (CodeQL should detect this)
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    cursor.execute(query)  # ❌ Unsafe SQL execution

    return cursor.fetchall()

user_input = input("Enter username: ")
print(vulnerable_query(user_input))
