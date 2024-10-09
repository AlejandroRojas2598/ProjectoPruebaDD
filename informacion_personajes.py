import sys

clase = ""
dano = 0
vida = 0
armadura = 0
magia = 0


def personaje(seleccion_crear_personaje,nombre_usuario):
     if seleccion_crear_personaje == "Caballero" or seleccion_crear_personaje == "1":
          clase = "Caballero"
          dano = 5
          vida = 20
          armadura = 10
          #print(f"Nombre: {nombre_usuario} \nClase: {clase} \nDaño: {dano} \nVida: {vida} \nArmadura: {armadura}")
          return clase, dano, vida, armadura
          
     elif seleccion_crear_personaje == "Arquero" or seleccion_crear_personaje == "2":
          clase = "Arquero"
          dano = 8
          vida = 15
          armadura = 5
          #print(f"Nombre: {nombre_usuario} \nClase: {clase} \nDaño: {dano} \nVida: {vida} \nArmadura: {armadura}")
          return clase, vida, armadura
     
     elif seleccion_crear_personaje == "Mago" or seleccion_crear_personaje == "3":
          clase = "Mago"
          dano = 13
          vida = 10
          armadura = 3
          #print(f"Nombre: {nombre_usuario} \nClase: {clase} \nDaño: {dano} \nVida: {vida} \nArmadura: {armadura}")  
          return clase, vida, armadura
