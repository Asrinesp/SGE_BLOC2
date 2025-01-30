import connect

# Fucion para crear un registro a la base de detos con una consulta preparada
def create_reg():

    #Crear la conexion y guardarlo en la variable conn
    conn = connect.connection()

    #Crear un cursor con la conexion guardada en la variable conn
    cursor = conn.cursor()

    #Consulta preparada con %s
    sql_create = "INSERT INTO Clients (nombre_cliente, dirección_cliente, teléfono_cliente, correo_electrónico_cliente, fecha_cumpleaños) VALUES (%s, %s, %s, %s, %s)"

    #Valor a añadir, en orden, en los %s de VALUES de la consulta preparada
    values = ('Roger', 'carrer el que sigui', '678113452', 'correu@correu.com', '12_09_1999')

    #Enviar la consulta preaparada con los valores utilizados en el cursor
    cursor.execute(sql_create, values)
    #Hacer las modificacions en la DB segun execute()
    conn.commit()

    #Cerrar conexion
    conn.close()
    cursor.close()
