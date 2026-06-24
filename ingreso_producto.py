inventario = {}
def menu():
   print("\n --- inventario ---")
   print("1. añadir producto")
   print("2. actualizar  stock")
   print("3. eliminar producto")
   print("4. salir")
def obtener_float(mensaje):
   while True:
      try:
        valor = float(input(mensaje))
        if valor >= 0:
           return valor
        print("por favor, ingrese un número mayor o igual a 0.")
      except ValueError:
         print("Entrada invalida. Por favor, ingrese un numero")

         
def añadir_producto():
    while True:
       nombre = input("\n nombre de producto: ").strip().capitalize()
       if nombre in inventario:
          print("¡producto ya existente, intente de nuevo!")
       else:
          break
    precio = obtener_float("precio del producto: ")
    stock = obtener_float("stock inicial ")
    inventario[nombre] = {"precio": precio, "stock": stock}
    print(f"¡Producto '{nombre}' añadido con exito!")

def actualizar_stock():
    nombre = input("\nNombre del producto a actualizar: ").strip().title()
    if nombre not in inventario:
        print("El producto no existe en el inventario.")
    else:
        print(f"Stock actual: {inventario[nombre]['stock']}")
        nuevo_stock = obtener_float("Nuevo stock (debe ser mayor a 0): ")
        inventario[nombre]['stock'] = nuevo_stock
        print(f"¡Stock actualizado a {nuevo_stock} para {nombre}!")

def eliminar_producto():
    nombre = input("\nNombre del producto a eliminar: ").strip().title()
    if nombre in inventario:
        del inventario[nombre]
        print(f"¡Producto '{nombre}' eliminado del inventario!")
    else:
        print("El producto no existe en el inventari")

while True:
   menu()
   opcion = input("\nSelecione una opcion(1-4: )")

   if opcion == '1':
      añadir_producto()
   elif opcion == '2':
      actualizar_stock()
   elif opcion == '3':
      eliminar_producto()
   elif opcion == '4':
      print("\nSaliendo del inventario")
      break
   else:
      print("\nopcion no valida, intente de nuevo (ingrese 1-4)")
