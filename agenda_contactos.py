print("Aqui podras guardar tus contactos")

lista = []

while(True):
    print("Aqui podras agregar editar o eliminar contactos escoge una opcion")
    print("1. Ver contactos.")
    print("2. Agregar un nuevo contacto.")
    print("3. Editar un contacto.")
    print("4. Eliminar un contacto.")
    print("5. Salir")
    opcion = input("Escoge la opcion (1-2-3-4-5)")

    if(opcion == "1"):
        print(lista)
    elif(opcion == "2"):
        name = input("Ingresa el nombre del contacto: ")
        phone = input("Ingresa el numero de telefono: ")
        email = input("Ingresa el email del contacto: ")
        dictionary = {"nombre": name, "telefono": phone, "correo": email}

        lista.append(dictionary)
    elif(opcion == "3"):
        for indice, contacto in enumerate(lista):
                print(f"{indice}. {contacto['nombre']}, {contacto['telefono']}, {contacto['correo']}")
        edit = int(input("Ingresa el indice del contacto que deseas editar: "))
        
        print("Ingresa los datos de contacto nuevos")
        newname = input("Ingresa el nuevo nombre del contacto: ")
        newphone = input("Ingresa el nuevo numero de telefono: ")
        newemail = input("Ingresa el nuevo email del contacto: ")
        lista[edit]["nombre"] = newname
        lista[edit]["telefono"] = newphone
        lista[edit]["correo"] = newemail
    elif(opcion == "4"):
        for indice, contacto in enumerate(lista):
            print(f"{indice}. {contacto['nombre']}, {contacto['telefono']}, {contacto['correo']}")
        delete = int(input("Ingresa el indice del contacto que deseas eliminar: "))

        lista.pop(delete)
    elif(opcion == "5"):
        break
    else:
        print("Opcion incorrecta intenta nuevamente")