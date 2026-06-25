#definimos la variable que actuara como dicionario
inventario = {}

#creamos un menu inicial
def menu():
   print("\n --- inventario ---")
   print("1. añadir producto")
   print("2. actualizar  stock")
   print("3. eliminar producto")
   print("4. salir")

#determinamos el valor numerico a positivo atra vez de while
def obtener_float(mensaje):
   while True:
#usamos la funcion try-except para bloquear los errores ineperados
      try:
        valor = float(input(mensaje))
        if valor >= 0:
           return valor
        print("por favor, ingrese un número mayor o igual a 0.")
      except ValueError:
         print("Entrada invalida. Por favor, ingrese un numero")

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
    precio = obtener_float("precio del producto: ")
    stock = obtener_float("stock inicial ")
#guardamos en el diccionario (inventario)
   inventario[nombre] = {"precio": precio, "stock": stock} 
    print(f"¡Producto '{nombre}' añadido con exito!") 

#para actualizar el inventario
def actualizar_stock():
   #solicitamos el nombre del producto a actualizar
    nombre = input("\nNombre del producto a actualizar: ").strip().title()
    if nombre not in inventario:
        print("El producto no existe en el inventario.")
    else:
   
   #muestra el stock actual
        print(f"Stock actual: {inventario[nombre]['stock']}") 
        nuevo_stock = obtener_float("Nuevo stock (debe ser mayor a 0): ")
       
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
        print("El producto no existe en el inventari")

#si todose en cuentra en orden el codigo deberia funcionar correctamente 
while True:
   menu()
   opcion = input("\nSelecione una opcion(1-4: )")

   if opcion == '1':
      añadir_producto()
   elif opcion == '2':
      actualizar_stock()
   elif opcion == '3':
      eliminar_producto()
#para poner fin al codigo solo hay que apretar la opcion '4' y el codigo se cerrera 
   elif opcion == '4':
      print("\nSaliendo del inventario")
      break
   else:
      print("\nopcion no valida, intente de nuevo (ingrese 1-4)")
