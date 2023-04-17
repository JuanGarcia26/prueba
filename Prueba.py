while True:
    print("\nSeleccione una opción:")
    print("1. Buscar dispositivo por IP")
    print("2. Agregar dispositivo")
    print("3. Editar dispositivo")
    print("4. Agregar campus")
    print("5. Ver dispositivos")
    print("6. Borrar dispositivo")
    print("7. Mostrar Campus")
    print("8. Salir")
    option = input("Opción: ")
    if option == "1":
        # Pedir la dirección IP a buscar
        search_ip = input("Ingrese la dirección IP a buscar: ")
        # Leer el archivo "dispositivos.txt" y buscar la dirección IP
        found = False
        with open("dispositivos.txt", "r") as f:
            for line in f:
                device_info = line.strip().split(",")
                if device_info[2] == search_ip:
                    print(f"Dispositivo encontrado: {device_info[1]} ({device_info[0]})")
                    found = True
        if not found:
            print("Dispositivo no encontrado.")
    elif option == "2":
        print("¿Qué tipo de dispositivo desea agregar?")
        print("1. Dispositivo genérico")
        print("2. Router")
        print("3. Switch")
        device_type = input("Opción: ")
        # Solicitar el nombre del dispositivo
        device_name = input("Ingrese el nombre del dispositivo: ")
        # Solicitar la dirección IP del dispositivo
        device_ip = input("Ingrese la dirección IP del dispositivo: ")
        # Solicitar la VLAN del dispositivo
        vlan = input("Ingrese el número de VLAN del dispositivo: ")
        # Solicitar la capa a la que pertenece el dispositivo
        print("¿A qué capa pertenece el dispositivo?")
        print("1. Capa de acceso")
        print("2. Capa de distribución")
        print("3. Capa de core")
        layer = input("Opción: ")
        # Solicitar los servicios comprometidos del dispositivo
        compromised_services = input("¿Qué servicios están comprometidos en el dispositivo? (separe cada servicio con una coma): ")
        # Solicitar el campus al que pertenece el dispositivo
        campus = input("Ingrese el campus al que pertenece el dispositivo: ")
        if device_type == "1":
            # Código para agregar un dispositivo genérico
            print(f"Agregando dispositivo genérico con nombre {device_name}, IP {device_ip}, VLAN {vlan}, capa {layer}, servicios comprometidos {compromised_services} y perteneciente al campus {campus}...")
            with open("dispositivos.txt", "a") as f:
                f.write(f"{device_name},{device_ip},{vlan},{layer},{compromised_services},{campus}\n")
        elif device_type == "2":
            # Código para agregar un router
            print(f"Agregando router con nombre {device_name}, IP {device_ip}, VLAN {vlan}, capa {layer}, servicios comprometidos {compromised_services} y perteneciente al campus {campus}...")
            with open("dispositivos.txt", "a") as f:
                f.write(f"{device_name},{device_ip},{vlan},{layer},{compromised_services},{campus}\n")
        elif device_type == "3":
            # Código para agregar un switch
            print(f"Agregando switch con nombre {device_name}, IP {device_ip}, VLAN {vlan}, capa {layer}, servicios comprometidos {compromised_services} y perteneciente al campus {campus}...")
            with open("dispositivos.txt", "a") as f:
                f.write(f"{device_name},{device_ip},{vlan},{layer},{compromised_services},{campus}\n")
        else:
            # Opción inválida
            print("Opción inválida. Por favor, seleccione una opción válida.")
    elif option == "3":
        devices = []
        with open("dispositivos.txt", "r") as f:
            for line in f:
                device_info = line.strip().split(",")
                devices.append(device_info)
            print("Seleccione el dispositivo que desea editar:")
            for i, device in enumerate(devices):
                print(f"{i+1}. {device[1]} ({device[0]})")
            selected_device_index = input("Opción: ")
            if selected_device_index.isdigit() and int(selected_device_index) in range(1, len(devices)+1):
                selected_device = devices[int(selected_device_index)-1]
                print(f"Editando dispositivo {selected_device[1]} ({selected_device[0]})...")
                # Solicitar los nuevos valores para el dispositivo
                new_device_name = input("Ingrese el nuevo nombre del dispositivo: ")
                new_device_ip = input("Ingrese la nueva dirección IP del dispositivo: ")
                new_vlan = input("Ingrese el nuevo número de VLAN del dispositivo: ")
                new_layer = print("¿A qué capa pertenece el dispositivo?")
                print("¿A qué capa pertenece el dispositivo?")
                print("1. Capa de acceso")
                print("2. Capa de distribución")
                print("3. Capa de core")
                layer = input("Opción: ")
                new_compromised_services = input("¿Qué servicios están comprometidos en el dispositivo? (separe cada servicio con una coma): ")
                new_campus = input("Ingrese el campus al que pertenece el dispositivo: ")
                # Actualizar el archivo de dispositivos
                with open("dispositivos.txt", "r") as f:
                    lines = f.readlines()
                with open("dispositivos.txt", "w") as f:
                    for line in lines:
                        device_info = line.strip().split(",")
                        if device_info == selected_device:
                            f.write(f"{device_info[0]},{new_device_name},{new_device_ip},{new_vlan},{new_layer},{new_compromised_services},{new_campus}\n")
                        else:
                            f.write(line)
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
    elif option == "4":
        # Pedir los datos del campus
        campus_name = input("Ingrese el nombre del campus: ")
        campus_address = input("Ingrese la dirección del campus: ")
        campus_contact = input("Ingrese el número de contacto del campus: ")
        # Agregar el campus al archivo de campus
        with open("campus.txt", "a") as f:
            f.write(f"{campus_name},{campus_address},{campus_contact}\n")
        print(f"Campus '{campus_name}' agregado exitosamente.")
    elif option == "5":
        # Abrir el archivo de texto en modo lectura
        with open("dispositivos.txt", "r") as f:
            # Leer los datos del archivo línea por línea
            lines = f.readlines()
            # Si el archivo está vacío, mostrar un mensaje
            if not lines:
                print("No hay dispositivos registrados.")
            # Si el archivo no está vacío, mostrar los dispositivos
            else:
                print("Dispositivos registrados:")
                for line in lines:
                    # Separar los campos de cada dispositivo por coma
                    fields = line.strip().split(",")
                    # Mostrar los campos de cada dispositivo formateados
                    print(f"Nombre: {fields[0]}, IP: {fields[1]}, VLAN: {fields[2]}, Capa: {fields[3]}, Servicios comprometidos: {fields[4]}, Campus: {fields[5]}")

    elif option == "6":
        with open("dispositivos.txt", "r") as archivo:
            dispositivos = archivo.readlines()
        # Mostrar la lista de dispositivos
        print("Lista de dispositivos:")
        for i, dispositivo in enumerate(dispositivos):
            print(f"{i+1}. {dispositivo}")
        # Solicitar la opción al usuario
        opcion = input("Seleccione el número del dispositivo que desea eliminar (o presione enter para salir): ")
        if opcion:
            # Convertir la opción en un entero
            opcion = int(opcion)
            # Eliminar el dispositivo seleccionado de la lista
            if opcion > 0 and opcion <= len(dispositivos):
                dispositivo_eliminado = dispositivos.pop(opcion-1)
                print(f"El dispositivo {dispositivo_eliminado.strip()} ha sido eliminado.")
                # Guardar la lista actualizada en el archivo
                with open("dispositivos.txt", "w") as archivo:
                    archivo.writelines(dispositivos)
            else:
                print("Opción inválida.")
        else:
            print("Saliendo del programa.")
    elif option == "7":
        # Mostrar información de campus
        print("Mostrando información de campus...")
        with open("campus.txt", "r") as f:
            for line in f:
                campus_info = line.strip().split(",")
                print(f"Nombre: {campus_info[0]}, Dirección: {campus_info[1]}, Contacto: {campus_info[2]}")
    elif option == "8":
        # Salir del programa
        print("Saliendo del programa...")
        break
    else:
        # Opción inválida
        print("Opción inválida. Por favor, seleccione una opción válida.")
