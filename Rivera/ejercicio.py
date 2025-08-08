tareas = []

while True:
    print("MENÚ TO-DO LIST")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como hecha")
    print("4. Salir")
    
    opcion = int(input("Elige una opción (1-4): "))

    if opcion == 1:
        nueva_tarea = input("Escribe la tarea que deseas agregar: ")
        tareas.append(nueva_tarea)
        print("Tarea agregada \n")
    
    elif opcion == 2:
        if len(tareas) == 0:
            print("No tienes tareas aún")
        else:
            print("Tus tareas son:")
            for i in range(len(tareas)):
                print(str(i + 1) + ". " + tareas[i])
        input("\n Presiona Enter para volver")
    
    elif opcion == 3:
        if len(tareas) == 0:
            print("No hay tareas para marcar como hechas")
        else:
            print("Selecciona la tarea a marcar como hecha:")
            for i in range(len(tareas)):
                print(str(i + 1) + ". " + tareas[i])
            num = int(input("Número de tarea: "))
            if 1 <= num <= len(tareas):
                tareas[num - 1] = "[HECHA] " + tareas[num - 1]
                print("Tarea marcada como hecha.")
            else:
                print("Número inválido")
        input("\nPresiona Enter para volver")
    
    elif opcion == 4:
        print("Saliendo")
        break
    
    else:
        print("Opción no válida, pareces Alejo.\n")