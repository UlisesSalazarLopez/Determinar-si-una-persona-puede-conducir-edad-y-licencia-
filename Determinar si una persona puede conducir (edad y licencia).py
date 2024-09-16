def puede_conducir():
    edad = int(input("Introduce tu edad: "))
    tiene_licencia = input("¿Tienes licencia de conducir? (s/n): ")

    if edad >= 18 and tiene_licencia.lower() == 's':
        print("Puedes conducir.")
    else:
        print("No puedes conducir.")
        
puede_conducir()
