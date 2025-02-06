# SGE_BLOC2

![primer_print.png](IMG/primer_print.png)
En esta imagen se muestra un print utilizando la funcion de connect. Se puede ver que la conexion ha sido establecia por el usuatio "user" a la base de datos "all_penjat"

![captura_bae_de_datos_con_datos.png](IMG/captura_bae_de_datos_con_datos.png)

En esta imagen se puede comprobar qu ay he podidio ingresar los datos de los clientes a la base de datos.

Para conseguir esto he tenido que crear las tablas con este codigo:

![img.png](IMG/creador_tablas.png)

Una vez se han creado las tablas solo he tenido que tener mi csv con los datos preparados y iniciar el primero codigo de estos dos:

![img.png](IMG/csv_to_dict.png)
![img.png](IMG/dict_to_db.png)

Aqui se puede ver como he podido crear un registro nuevo con la funcion de "create_registre"
![create_registre.png](IMG/create_registre.png)

Aqui podemos ver un print simple de read_registre
![print_read_reg.png](IMG/print_read_reg.png)

Este es el read_reg pero especificando una fila (la fila 4 en este caso)
![read_reg_4.png](IMG/read_reg_4.png)

Este es el read_reg pero especificando fila y columna (en este caso es la fila 4, igual que el anterior y la columna 4)
![read_reg_4-4.png](IMG/read_reg_4-4.png)

Aqui estan los siguientes datos:
- Les dades de l’Andreu
- El correu de l’Andreu
- Les dades de la Vivian
- La direcció de la Vivian
- Les dades de l’Albert
- La data de cumpleanys de l’Albert
![actividad_print_read_reg.png](IMG/actividad_print_read_reg.png)

Aqui podemos ver la tabla de datos ordenada de manera que se entiende mejor que es cada dato
![tabla_datos_registros.png](IMG/tabla_datos_registros.png)

Aqui podemos ver como con el update_reg se han cambiado los numeros de telefono de estos 3 clientes
![telefonos_cambiados.png](IMG/telefonos_cambiados.png)