#Fecha: 25/04/2024
#Centro de Biotecnología Agropecuario
#Ficha: 2877795
#Aprendiz: Nicolás Agamez Melo


#Llamando a la libreria random
from random import*

#Definir los datos random de 1 a 100
dato1 = randint(0, 100)
dato2 = randint(0, 100)


#Definir la función saludo
def saludo():

#Input para que el usuario ingrese su nombre
    nombre = (input("Ingrese su nombre: "))
    print("-------------------------------------------------")
    print("Bienvenido", nombre, "a la ficha 2877795 ADSO :)")
    print("-------------------------------------------------")
    print("")

if __name__=="__main__":
    saludo()


#Definir una función sumar
def sumar():
#Retorna la suma
    return (dato1 + dato2)


#Definir una función restar
def restar():
#Retorna la resta
    return (dato1 - dato2)


#Definir una función multiplicar
def multi():
#Retorna el producto
    return (dato1 * dato2)


#Definir una función dividir
def divi():
#Retorna la división
   return (dato1 / dato2)


#Imprimiendo la suma
print("La suma de los números es: ", sumar())
print("**************************************")
print("")

#Imprimiendo la resta
print("La resta de los números es: ", restar())
print("**************************************")
print("")

#Imprimiendo el producto
print("El producto de los números es: ", multi())
print("**************************************")
print("")


#Condicional si algún dato es igual a cero
#Imprimiendo la división
if dato1 == 0:
   print("No se puede dividir entre cero")
   print("*************************************")
elif dato2 == 0:
   print("No se puede dividir entre cero")
   print("*************************************")
else:
   print("La división de los números es: ", divi())
   print("**************************************")


#Presentando los datos aleatorios escogidos
print(f"Los datos aleatorios fueron: {dato1} y {dato2}")
