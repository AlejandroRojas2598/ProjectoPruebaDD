import sys

dano = 0
vida = 0
armadura = 0
magia = 0

def enemigos_nivel1(numero_enemigo_aleatorio):
    #Caballero_Rebelde
    if numero_enemigo_aleatorio >= 1 and numero_enemigo_aleatorio < 25:
        enemigo = "Caballero Rebelde"
        dano = "2"
        vida = "8"
        armadura = "3"
        return enemigo,dano,vida,armadura
    #Arquero_Rebelde
    if numero_enemigo_aleatorio >= 25 and numero_enemigo_aleatorio < 50:
        enemigo = "Caballero Rebelde"
        dano = "2"
        vida = "8"
        armadura = "3"
        return enemigo,dano,vida,armadura
    
    if numero_enemigo_aleatorio >= 50 and numero_enemigo_aleatorio < 75:
        enemigo = "Caballero Rebelde"
        dano = "2"
        vida = "8"
        armadura = "3"
        return enemigo,dano,vida,armadura
    
    if numero_enemigo_aleatorio >= 75 and numero_enemigo_aleatorio < 100:
        enemigo = "Caballero Rebelde"
        dano = "2"
        vida = "8"
        armadura = "3"
        return enemigo,dano,vida,armadura