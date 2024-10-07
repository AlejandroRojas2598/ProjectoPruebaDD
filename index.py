import sys
import logging
from informacion_personajes import personaje


lista_personaje = []
inventario_personaje = []
dinero_personaje = []

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
#Fin crear personaje

#Inicio Tutorial
mensaje_tutorial_1 = "Antes de empezar tu gran aventura es necesario aprender lo básico."
mensaje_tutorial_2 = "En está aventura te encontraras con un mundo lleno de sorpresas."
mensaje_tutorial_3 = "Hola"





#Empezar Juego
#while vida_personaje>=1:
#    print("Game Over")