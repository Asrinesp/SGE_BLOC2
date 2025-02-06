import  connect

def read_reg():
    conn = connect.connection()
    cursor = conn.cursor()

    sql_read = "SELECT * FROM clients"

    cursor.execute(sql_read)
    conn.commit()

    results = cursor.fetchall()

    print(results[9])
    print(results[9][3])
    print(results[14])
    print(results[14][1])
    print(results[19])
    print(results[19][4])

read_reg()