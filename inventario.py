from almacenaje import base_de_productos
# Arriba lo que hice fue llamar al otro archivo que contiene la "base de de datos" desde aqui podemos visualizar
# que productos pueda tener el inventario


# Aqui con la funcion def ver_inventario(): podemos ver si todos los productos registrados estan almacenados o
# puedan esatr vacios
def ver_inventario():
    print("\n--- INVENTARIO ACTUAL ---")

    if not base_de_productos: #con esta condicion podemos verificar si el diccionario esta vacio o no
        print("El INVENTARIO ESTA VASIO")
        return # el return nos sirve para finalizar la instruccion de la funcion
 # con estos 2 print mostramos los "Titulos o nombres" de los productos ya existentes
    print(f"{'Producto':<20}{'Precio':>10}{'Stock':>8}")
    print("-" * 45)
# con el for recorremos el diccionario lo q hacemos con items().es obtener la clave y el valor de cada elemento
    for nombres, almacenaje in base_de_productos.items():
          print(f"{nombres:<20} ${almacenaje['precio']:>9.2f}{almacenaje['stock']:>8}")
# Aui podemos ver la cantidad de productos que ya tenemos o existen
    print(f"\n  Total de preoductos: {len(base_de_productos)}")


# Con esta funcion lo q hacemos es poder permitir realizar busquedas de los productos por sus nombres
def buscar_producto():
    print("\n ---BUSCAR PRODUCTOS---")
# aqui solicitamos el nombre para buscar el producto. Utilizamos .strip() para eliminar los
# espacios en blanco al inicio y al final del texto
    name = input("Nombre del producto a buscar: ").strip()
# esta condicion valida que el usuario que el usuario realmente haya ingresado alguna letra o nombre
 # para buscarlo
    if not name:
        print("Error ingrese un nombre para buscar")
        return # De igual manera finaliza la instruccion de la funcion
# Aqui usamos una validacion de diccionario para realizar la busqueda ignorando las letras
# MAYUSCULAS y minusculas
    resultado = {
        n: d for n, d in base_de_productos.items()
        if name.lower() in n.lower()
    }
# Aqui revisamos si el nombre que ingreso existe
    if not resultado:
        print(f"No se encontro ningun producto con el nombrer de {name}.")
# Aqui mostramos el producto de la busqueda existente
    print(f"\n Rsultados de {name}:")
# Finalmente mostramos los resultados con su nombre,precio y stock
    for a, almacenaje in resultado.items():
        print(f"\nNombre: {a}")
        print(f"Precio: ${almacenaje['precio']:.2f}")
        print(f"Stock :{almacenaje['stock']} unidades")