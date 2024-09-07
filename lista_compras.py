lista_compras = []

while True:

    print("\nMenú:")
    print("1. Agregar artículo")
    print("2. Eliminar artículo")
    print("3. Mostrar lista")
    print("4. Salir")
    

    opcion = input("Elige una opción (1-4): ")
    
    if opcion == '1':
     
        articulo = input("Introduce el nombre del artículo a agregar: ")
        lista_compras.append(articulo)
        print(f"Artículo '{articulo}' agregado a la lista.")
        
    elif opcion == '2':
       
        if lista_compras:
           
            print("Lista actual:")
            for idx, item in enumerate(lista_compras):
                print(f"{idx}. {item}")
                
           
            try:
                indice = int(input("Introduce el índice del artículo a eliminar: "))
                if 0 <= indice < len(lista_compras):
                    eliminado = lista_compras.pop(indice)
                    print(f"Artículo '{eliminado}' eliminado de la lista.")
                else:
                    print("Índice fuera de rango.")
            except ValueError:
                print("Por favor, introduce un número válido.")
        else:
            print("La lista está vacía.")
            
    elif opcion == '3':
       
        if lista_compras:
            print("Lista de compras:")
            for item in lista_compras:
                print(f"- {item}")
        else:
            print("La lista está vacía.")
            
    elif opcion == '4':
        
        print("¡Gracias por usar la lista de compras!")
        break
        
    else:
        print("Opción no válida. Por favor, elige una opción entre 1 y 4.")