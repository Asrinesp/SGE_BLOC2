import  connect

def read_reg():
    conn = connect.connection()
    cursor = conn.cursor()

    sql_read = "SELECT * FROM clients"

    cursor.execute(sql_read)
    conn.commit()

    results = cursor.fetchall()

    print(results[4])

read_reg()