#este es el diccionario vacio donde integraremos todos los datos del inventario de la tienda y donde podremos tambien consultar, agregar o eliminar datos.
inventario = {}

#validacion de precio

def obtener_precio():
    while True:
        try:
            precio = float(input("ingrese el precio correspondiente: "))
        
            if precio < 0:
                print("el precio no pude ser negativo.")

            else:
                return precio
    
        except ValueError:
            print("error! debe ingresar un numero.")


#validacion de stock
def obtener_stock():
    while True:
        try:
            stock = int(input("ingrese el stock: "))

            if stock < 0:
                print("el stock debe ser un numero positivo.")
        
            else:
                return stock
    
        except ValueError:
            print("error! debes ingresar un numero valido.")


# Aqui con la funcion def ver_inventario(): podemos ver si todos los productos registrados estan almacenados o puedan estar vacios
def ver_inventario():
    print("\n--- INVENTARIO ACTUAL ---")

    if not inventario: #con esta condicion podemos verificar si el diccionario esta vacio o no
        print("El INVENTARIO ESTA VACIO")
        return # el return nos sirve para finalizar la instruccion de la funcion
 # con estos 2 print mostramos los "Titulos o nombres" de los productos ya existentes
    print(f"{'Producto':<20}{'Precio':>10}{'Stock':>8}")
    print("-" * 45)
# con el for recorremos el diccionario lo q hacemos con items().es obtener la clave y el valor de cada elemento
    for nombres, almacenaje in inventario.items():
          print(f"{nombres:<20} ${almacenaje['precio']:>9.2f}{almacenaje['stock']:>8}")
# Aui podemos ver la cantidad de productos que ya tenemos o existen
    print(f"\n  Total de preoductos: {len(inventario)}")


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
        n: d for n, d in inventario.items()
        if name.lower() in n.lower()
    }
# Aqui revisamos si el nombre que ingreso existe
    if not resultado:
        print(f"No se encontro ningun producto con el nombrer de {name}.")
        return
# Finalmente mostramos los resultados con su nombre,precio y stock

    for a, almacenaje in resultado.items():
        print(f"\nNombre: {a}")
        print(f"Precio: ${almacenaje['precio']:.2f}")
        print(f"Stock :{almacenaje['stock']} unidades")



#añadimos el producto al inventario (diccionario)         
def añadir_producto():
    while True:
#solicitamos el nombre del producto
       nombre = input("\n nombre de producto: ").strip().capitalize() 
#verficamos que no exita ya un dato con ese nombre
       if nombre in inventario: 
          print("¡producto ya existente, intente de nuevo!") 
       else:
          break
#solicitamos que ingrese los datos del producto si no existia antes
    precio = obtener_precio()
    stock = obtener_stock()
#guardamos en el diccionario (inventario)
    inventario[nombre] = {"precio": precio, "stock": stock}
    print(f"¡Producto '{nombre}' añadido con exito!") 

#para actualizar el inventario
def actualizar_stock():
   #solicitamos el nombre del producto a actualizar
    nombre = input("\n  Nombre del producto a actualizar: ").strip().title()
    if nombre not in inventario:
        print("El producto no existe en el inventario.")
    else:
   
   #muestra el stock actual
        print(f"Stock actual: {inventario[nombre]['stock']}") 
        nuevo_stock = obtener_stock()
       
   #pide un nuevo stock y lo actualiza
        inventario[nombre]['stock'] = nuevo_stock
        print(f"¡Stock actualizado a {nuevo_stock} para {nombre}!")

#para eliminar el imventario
def eliminar_producto():
#solicitamos el nombre del producto a borra
    nombre = input("\nNombre del producto a eliminar: ").strip().title()
#si el producto existe sera borrado   
    if nombre in inventario:
        del inventario[nombre]
        print(f"¡Producto '{nombre}' eliminado del inventario!")
    else:
         print("El producto no existe en el inventario")

#si todose en cuentra en orden el codigo deberia funcionar correctamente

#menu principal

while True:
    print ("\n-----MENÚ PRINCIPAL-----")
    print ("1. ver inventario ")
    print ("2. añadir producto ")
    print ("3. actualizar stock ")
    print ("4. eliminar producto ")
    print ("5. buscar producto ")
    print ("6. salir ")

#el try permite corroborar y asegurarnos que el programa no se caiga en caso de que el usuario ingrese otro caracter y pueda volver a preguntar de nuevo.
    try:
        opcion = int(input("ingrese una opcion: "))
    except ValueError:
        print("error!, debe ingresar un número.")
        continue

#el if permite encasillar la opcion que eligio el usario y que entre a un sub bucle dentro de la opcion
    if opcion == 1:
        ver_inventario()

    elif opcion == 2:
        añadir_producto()

    elif opcion == 3:
        actualizar_stock()
    
    elif opcion == 4:
        eliminar_producto()
    
    elif opcion == 5:
        buscar_producto()

    elif opcion == 6:
        print ("saliendo del sistema, Hasta pronto!......")
        break

    else:
        print("error! opcion no valida...")