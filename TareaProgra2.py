# Programa que determina el resultado de la siguiente operacion matematica usando funciones
# Autor: Javier Vargas   Seccion: 3031A   CI: 28.745.677    Area: Programacion II

def my_fuction():
    a = 3               # Primer valor 
    b = 7               # Segundo valor
    c = 10              # Tercer valor
    def my_other_fuction():
        d =  ((a+b)**c) / ((c-a)**(b+a))    # Operacion 
        return d                           # Me retorna el valor que obtiene d 
    return my_other_fuction()    
print(my_fuction())    