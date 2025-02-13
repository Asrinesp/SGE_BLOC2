import  connect

def delete_reg():
    conn = connect.connection()
    cursor = conn.cursor()

    sql_delete = '''
    DELETE FROM clients
    WHERE nombre_cliente = 'Aleix'
    '''

    cursor.execute(sql_delete)
    conn.commit()

    conn.close()
    cursor.close()
    return {"Delete successfully"}