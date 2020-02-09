#Primero declaro una variable n con el número dado 
n=100000
#Ahora guardo ese valor como cadena en una nueva variable 
nc = str(n)


#Aquí entro a un bucle que verifica si la cadena guardada en nc es un palíndromo
while nc != nc[::-1]:
    #Una vez entrando al bucle le resto uno a n 
    n = n-1
    #Guardo nuevamente este valor como cadena para poder invertirlo
    nc = str(n)
    #Aquí invierto la cadena y la guardo como un entero
    n1 = int(nc[::-1])
    #Se realiza el producto del número n con su número "espejo"
    n2 = n*n1
    #Aquí guardo el resultado del producto como cadena
    nc = str(n2)

    
#En esta parte solo imprimo los números que generan el palíndromo y el palíndromo generado    
print(n," x ",n1, " = ", nc)
