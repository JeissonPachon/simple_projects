## Este programa va a calcular el valor total de la cuenta incluyendo la propina que el usuario desee

count = int(input("Por favor ingresa el valor total de la cuenta: "))
print("1. 15%")
print("2. 18%")
print("3. 20%")
print("4. Personalizado")
print("5. Salir")
percentage = input("Por favor ingresa el porcentaje de propina (1-5): ")

def firts_percent():
    percent = count * 0.15
    cuenta_total = percent + count
    print(f'''El precio con la propina del 15% es de {cuenta_total} \n 
          Ten en cuenta valor de la cuenta {count} \n
          Valor de la propina {percent}''')


def second_percent():
    percent = count * 0.18
    cuenta_total = percent + count
    print(f'''El precio con la propina del 18% es de {cuenta_total} \n 
          Ten en cuenta valor de la cuenta {count} \n
          Valor de la propina {percent}''')

def third_percen():
    percent = count * 0.20
    cuenta_total = percent + count
    print(f'''El precio con la propina del 20% es de {cuenta_total} \n 
          Ten en cuenta valor de la cuenta {count} \n
          Valor de la propina {percent}''')

def perso_percent():
    porcentaje = int(input("Ingresa el valor del porcentaje de propina que deseas dar: "))
    porcentaje_deci = porcentaje / 100
    percent = count * porcentaje_deci
    cuenta_total = percent + count
    print(f'''El precio con la propina del {porcentaje}% es de {cuenta_total} \n 
          Ten en cuenta valor de la cuenta {count} \n
          Valor de la propina {percent}''')
    
while percentage != "5":
    if percentage == "1":
        firts_percent()
    elif percentage == "2":
        second_percent()
    elif percentage == "3":
        third_percen()
    elif percentage == "4":
        perso_percent()
    else:
        print("El numero ingresado no es valido")
    print("Selecciona una opcion nuevamente")
    print("1. 15%")
    print("2. 18%")
    print("3. 20%")
    print("4. Personalizado")
    print("5. Salir")
    percentage = input("Por favor ingresa el porcentaje de propina (1-5): ")