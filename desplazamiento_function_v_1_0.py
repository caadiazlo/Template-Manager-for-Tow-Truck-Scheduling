# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 16:35:40 2026

@author: Carlos
"""

# Función para desplazamiento

def desplazamiento(final):
    print("Desplazamiento: \n1.Si\n2.No\n")
    desplaz=int(input("Opc: "))
    if desplaz == 1:
        print("Mismo destino grúa: \n1.Si\n2.No\n")
        mismo_dest=int(input("Opc: "))
        if mismo_dest != 1:
            final={
                "City_Dest": input("Ciudad destino: "),
                "Dir_Dest": input("Dirección destino: "),
                "Bar_Dest": input("Barrio destino: ")
                }
            final["City_Dest"]=final["City_Dest"].title()
            final["Bar_Dest"]=final["Bar_Dest"].title()
        
        final["N_Personas"]= input("Número personas: ")
        final["Maletas"]= input("Tiene maletas: ")
        final["T_Maletas"]= input("Tamaño maletas: ")
        final["Mascotas"]= input("Tiene mascotas: ")
        final["T_Mascotas"]= input("Tamaño mascotas :")
        
    final["Si"]=str(desplaz)
    
    print() # tratar de eliminar esta línea
    
    return final