import connect

def update_reg():
    conn = connect.connection()
    cursor = conn.cursor()

    sql_update = '''
    UPDATE clients
    SET teléfono_cliente=100100999
    WHERE nombre_cliente = 'Estefania'
    '''

    cursor.execute(sql_update)
    conn.commit()

    cursor.close()
    conn.close()

    return {"Update successfully"}