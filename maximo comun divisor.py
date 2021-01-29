# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 16:15:55 2020

@author: HACKER
"""

def mcd(a,b): #definimos una funcion con dos parametros
    minimo = min (a,b)# lo primerpo que voy a realizar escalcular el minimo 
    maximo = max(a,b)# voy a calcular el numero maximo entre los parametros
        
    if minimo==0:# agrego la condicion si minimo es igual 0 retorno
        return maximo
    elif minimo ==1:# agrego otro condicion si minimo es igual a uno se retorna
        return 1
    else:# viene el caso recusrsivo, entonces
        return mcd(minimo,maximo % minimo)# retornamos el resultado de invocar recusrsivamente la funcion
    
print("el maximo comun divisor es")
print(mcd(4,12)) # ya no solicito los valores si no que lo hago de forma sintatico
print("el maximo comun divisor es")
print(mcd(20,10))
print("el maximo comun divisor es")
print(mcd(16,20))