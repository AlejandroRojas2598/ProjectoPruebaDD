import sys
import logging
import random
from informacion_personajes import personaje
from informacion_enemigos import enemigos_nivel1


lista_personaje = []
inventario_personaje = []
dinero_personaje = 0

#Inicio
mensaje_inicio = "Para iniciar la aventura presiona 1"
print(mensaje_inicio)
iniciar = input()
#Fin inicio 

#Bienvenida personaje
mensaje_bienvenida =  "¿Cuál es tú nombre?"
print(mensaje_bienvenida)
nombre_usuario = input()
mensaje_bienvenida_2 = "Mucho gusto " + nombre_usuario + ", te encuentras en un mundo donde la esperanza se ha esfumado..."
mensaje_bienvenida_3 = "En este mundo tus decisiones forman parte importante en el desarrollo de la historia"
print(mensaje_bienvenida_2)
input()
#Fin bienvenida

#Crear personaje
print(mensaje_bienvenida_3)
mensaje_crear_personaje = "Antes de empezar tu aventura, necesitamos crearte un personaje."
print(mensaje_crear_personaje)                   
input()
mensaje_crear_personaje_2 = "Por el momento te podemos ofrecer 3 clases: \n 1.- Caballero \n 2.- Arquero \n 3.- Mago"
print(mensaje_crear_personaje_2)
seleccion_crear_personaje = input("Selecciona a tu personaje: \n")
personaje_creado = personaje(seleccion_crear_personaje,nombre_usuario)
clase_personaje, dano_personaje, vida_personaje, armadura_personaje = personaje(seleccion_crear_personaje,nombre_usuario)
print(f"Nombre: {nombre_usuario} \nClase: {clase_personaje} \nDaño: {dano_personaje} \nVida: {vida_personaje} \nArmadura: {armadura_personaje}")
#Fin crear personaje

#Inicio Tutorial
mensaje_tutorial_1 = "Antes de empezar tu gran aventura es necesario aprender lo básico."
mensaje_tutorial_2 = "En está aventura te encontraras con un mundo lleno de sorpresas."
mensaje_tutorial_3 = "Hola"

print(mensaje_tutorial_1)
input()
print(mensaje_tutorial_2)
input()
print(mensaje_tutorial_3)

numero_enemigo_aleatorio = random.randint(1, 100)
enemigo_escogido = enemigos_nivel1(numero_enemigo_aleatorio)

tipo_enemigo, dano_enemigo, vida_enemigo, armadura_enemigo = enemigos_nivel1(numero_enemigo_aleatorio)

print(tipo_enemigo,numero_enemigo_aleatorio)

#Empezar Juego
#while vida_personaje >= 1:
#    print("Game Over")