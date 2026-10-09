# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 10:36:19 2026

@author: Carlos
"""
# Importar función pesados:

import pesados_function_v_1_0 as pesados
import desplazamiento_function_v_1_0 as desplaz

#Función de ingreso de datos:

def datos_inicio():
    asegurado_intro={
        "Nombre": input("Nombre: "),
        "Motivo0": input("Motivo: "),
        "Celular1": input("Celular 1: "),
        "Celular2": input("Celular 2: "),
        "Cedula": input("Cedula: "),
        "Correo": input("Correo: "),
        "Placa": input("Placa: ")
    }
    
    #asegurado={llaves: valores.title() for llaves, valores in asegurado_intro.items() }
    
    asegurado_intro["Nombre"]=asegurado_intro["Nombre"].title()
    asegurado_intro["Placa"]=asegurado_intro["Placa"].upper()
    
    print()
    
    return asegurado_intro


def datos_tipif(datos):
    print("Datos Tipificación:\n",datos["Cedula"],"\n",datos["Nombre"],"\n",datos["Celular1"],"\n",datos["Placa"])


def origen():
    origen_serv={
        "City_Origen": input("Ciudad origen: "),
        "Dir_Origen": input("Dirección origen: "),
        "Bar_Origen": input("Barrio origen: ")
    }
    origen_serv["City_Origen"]=origen_serv["City_Origen"].title()
    origen_serv["Bar_Origen"]=origen_serv["Bar_Origen"].title()
    
    return origen_serv

def dest():
    dest_serv={
        "City_Dest": input("Ciudad destino: "),
        "Dir_Dest": input("Dirección destino: "),
        "Bar_Dest": input("Barrio destino: ")
    }
    dest_serv["City_Dest"]=dest_serv["City_Dest"].title()
    dest_serv["Bar_Dest"]=dest_serv["Bar_Dest"].title()
    
    print()
    
    return dest_serv

def sal_datos (datos):
    print("Nombre: ", datos["Nombre"])
    print("Celular: ",datos["Celular1"],datos["Celular2"])
    print("Cedula: ",datos["Cedula"])
    print("Correo: ",datos["Correo"])
    print("Placa: ",datos["Placa"],"\n")
    print("Motivo: ",datos["Motivo0"],"\n")
    
def sal_origen(origen):
    print("Ciudad origen: ",origen["City_Origen"])
    print("Dirección origen: ",origen["Dir_Origen"])
    print("Barrio origen: ",origen["Bar_Origen"])
    
def sal_dest(dest):
    print("Ciudad destino: ",dest["City_Dest"])
    print("Dirección destino: ",dest["Dir_Dest"])
    print("Barrio destino: ",dest["Bar_Dest"],"\n")

def livianos():
    livianos_data={
        "Llanta_Rueda": input("Llantas ruedan: "),
        "Sotano": input("Sótano o Parq. Alto: "),
        "Maniobra": input("Maniobra: "),
        "Automatico": input("Automático: "),
        "Blindaje": input("Blindaje: "),
        "Destino_Hora": input("Destino reciben cualquier hora: "),
        "Fecha": input("Fecha: "),
        "Hora": input("Hora: ")
    }
    print() # Tratar de eliminar esta línea
    
    return livianos_data

def sal_livianos(livi_data):
    print("Llantas ruedan: ", livi_data["Llanta_Rueda"])
    print("Sótano o Parq. Alto: ",livi_data["Sotano"])
    print("Maniobra: ",livi_data["Maniobra"])
    print("Automatico: ",livi_data["Automatico"])
    print("Blindaje: ",livi_data["Blindaje"])
    print("Destino reciben a cualquier hora: ",livi_data["Destino_Hora"])
    print("Fecha: ",livi_data["Fecha"])
    print("Hora: ",livi_data["Hora"],"\n")
    
def sal_pesados(pesa_data):
    print("Número de llantas : ", pesa_data["N_Llantas"])
    print("Rescate: ",pesa_data["Rescate"])
    print("Ancho(m): ",pesa_data["Ancho"])
    print("Largo(m): ",pesa_data["Largo"])
    print("Alto(m): ",pesa_data["Alto"])
    print("Capacidad carga: ",pesa_data["Cap_Carga"])
    print("Tipo de carga: ",pesa_data["Tipo_Carga"])
    print("Descargado: ",pesa_data["Descargado"])
    print("Tipo de carrocería: ",pesa_data["Carroceria"])
    print("Presenta algún bloqueo: ",pesa_data["Bloqueo"])
    print("Adaptación grúa de gancho: ",pesa_data["Adap_Grua"])
    print("Recomendación: ",pesa_data["Recomendacion"])
    print("WhatsApp de envió de datos: ",pesa_data["Whatsapp"],"\n")
    
def sal_desplazamiento(origen,dest):
    print("Ciudad origen: ",origen["City_Origen"])
    print("Dirección origen: ",origen["Dir_Origen"])
    print("Barrio origen: ",origen["Bar_Origen"])
    print("Ciudad destino: ",dest["City_Dest"])
    print("Dirección destino: ",dest["Dir_Dest"])
    print("Barrio destino: ",dest["Bar_Dest"],"\n")
    print("Número personas: ",dest["N_Personas"])
    print("Tiene maletas: ",dest["Maletas"])
    print("Tamaño maletas: ",dest["T_Maletas"])
    print("Tiene mascotas: ",dest["Mascotas"])
    print("Tamaño mascotas: ",dest["T_Mascotas"],"\n")
    
def indefinido(origen,destino):
    if origen["Dir_Origen"] == "indef":
        origen["Dir_Origen"]= input("Ubicación origen: ")
    if destino["Dir_Dest"] == "indef":
        destino["Dir_Dest"]= input("Ubicación destino: ")
    
    ubicaciones={"Origen": origen["Dir_Origen"],"Destino": destino["Dir_Dest"]}
    
    return ubicaciones
    
turno=1
asegurados=1


while turno != 555:
    
    print("Asegurado No: ",asegurados,"\n")
    datos_ini=datos_inicio()
    datos_tipif(datos_ini)
    
    print()
    poliza=input("Póliza: ")
    print()
    print("Opciones de servicio:\n")
    print("""          1.Vehículo Liviano
          2.Vehículo Pesado
          3.Conductor Elegido
          4.Paso Corriente - Carro Taller
          5.Cambio Llanta - Carro Taller
          6.Cerrajería - Carro Taller
          7.Suministro Combustible - Carro Taller
          8.Conductor Profesional
          9.Información o Rellamada""")
    
    opcion=int(input("Ingresa opción: "))
    print()
    match opcion:
        case 1:
            motivo= input("Motivo: ")
            origins=origen()
            destiny=dest()
            livi=livianos()
            whatsapp=input("WhatsApp envío datos: ")
            print()
            if origins["Dir_Origen"] == "indef" or destiny["Dir_Dest"] == "indef":
                dir_transitorio=indefinido(origins,destiny)
                origins["Dir_Origen"]=dir_transitorio["Origen"]
                destiny["Dir_Dest"]=dir_transitorio["Destino"]
            
            desp=desplaz.desplazamiento(destiny)
            print("-----------------------------")
            datos_ini["Motivo0"]=motivo
            sal_datos(datos_ini)
            sal_origen(origins)
            sal_dest(destiny)
            sal_livianos(livi)
            print("WhatsApp envío datos: ",whatsapp,"\n")
            desplazo=int(desp["Si"])
            if desplazo == 1:
                print("Desplazamiento: \n")
                sal_desplazamiento(origins, desp)
            print("-----------------------------")
            
        case 2:
            motivo= input("Motivo: ")
            origins=origen()
            destiny=dest()
            livi=livianos()
            pesa=pesados.pesados()
            whatsapp=input("WhatsApp envío datos: ")
            print()
            if origins["Dir_Origen"] == "indef" or destiny["Dir_Dest"] == "indef":
                dir_transitorio=indefinido(origins,destiny)
                origins["Dir_Origen"]=dir_transitorio["Origen"]
                destiny["Dir_Dest"]=dir_transitorio["Destino"]
            
            desp=desplaz.desplazamiento(destiny)
            print("-----------------------------")
            datos_ini["Motivo0"]=motivo
            sal_datos(datos_ini)
            sal_origen(origins)
            sal_dest(destiny)
            sal_livianos(livi)
            sal_pesados(pesa)
            print("WhatsApp envío datos: ",whatsapp,"\n")
            desplazo=int(desp["Si"])
            if desplazo == 1:
                print("Desplazamiento: \n")
                sal_desplazamiento(origins, desp)
            print("-----------------------------")
        
        case _:
            print("otra opción")
            
    asegurados+=1
    turno=int(input("Ingresa 555 para terminar el turno: "))

print("FIN DEL TURNO")







