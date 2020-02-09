#Aquí solicito al usuario que escriba una cadena de caracteres y lo guardo en la variable cadena
cadena = input("Escribe una cadena de caracteres: ")
#Aquí guardo la cadena pero borrando los espacios que el usuario haya escrito
cadenan = cadena.replace(" ","")
#Verifico si la cadena sin espacios es igual a la cadena sin espacios invertida
if cadenan[::-1] == cadenan:
    print("¡Es un palíndromo!")
else:
    print('No es un palíndromo')

