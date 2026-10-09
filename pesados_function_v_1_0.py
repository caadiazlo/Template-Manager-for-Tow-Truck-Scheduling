# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 17:05:09 2026

@author: Carlos
"""

def pesados():
    pesados_data={
        "N_Llantas": input("Número llantas (ENTERO): "),
        "Rescate": input("Rescate: "),
        "Ancho": input("Ancho: "),
        "Largo": input("Largo: "),
        "Alto": input("Alto: "),
        "Cap_Carga": input("Capacidad carga: "),
        "Tipo_Carga": input("Tipo carga: "),
        "Descargado": input("Descargado: "),
        "Carroceria": input("Tipo carrocería: "),
        "Bloqueo": input("Bloqueo: "),
        "Adap_Grua": input("Adaptación grúa gancho: "),
        "Recomendacion": input("Recomendación: "),
        "Whatsapp": input("WhatsApp de envío de datos: ")
    }
    print() # tratar de eliminar esta línea
   
    return pesados_data
