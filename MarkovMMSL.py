#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 19:19:17 2020

@author: aymen
"""

import math

# initilaisation des parametres utilises dans les formules de little 
Ns = 0
Nf = 0
Ts = 0
Tf = 0
s = 0
Lambda = 0
Mu = 0
Ro = 0
L = 0

# obtention du parametre a calculer
print("Veuillez donner le nombre de serveurs s = ")
s = int(input())
print("Veuillez donner la longueur de la file d'attente L = ")
L = int(input())
if(L < s):
    print("ERREUR : L < S, cas impossible !")
else:
    print("Veuillez donner le taux d'arrivee des clients Lambda = ")
    Lambda = int(input())
    print("Veuillez donner le duree de service Mu = ")
    Mu = int(input())
    print("Que voulez vous calculez ?")
    print("1/ Nombre moyen des clients dans le systeme")
    print("2/ Nombre moyen des clients dans la file")
    print("3/ Temps d'attente moyen dans le systeme")
    print("4/ Temps d'attente moyen dans la file")
    parametre = int(input())
    Ro = Lambda / (s * Mu)
    u = Lambda / Mu
    
    # definition des fonction de calcul des proba
    def P0():
        somme = 0
        temp = 0
        if(s == u):
            for i in range (0, s):
                somme = somme + (s ** i) / math.factorial(i)
            temp = somme + ((s ** s) / math.factorial(s))(L - s + 1)
        else:
            for i in range (0, s):
                somme = somme + (u ** i) / math.factorial(i)
            temp = somme + ((u ** s) / math.factorial(s)) * (1 - (u / s)**(L - s + 1))/(1 - u / s)
        return 1 / temp
        
    def Pl():
        return (P0() * u ** s)/(math.factorial(s) * s ** (L-s))
    
    def P(k):
        if(1 <= k) and (k <= s):
            return ((u ** k) / math.factorial(k)) * P0()
        elif(k >= s) and (k <= L):
            return ((u ** k) / (math.factorial(s) * s ** (k - s)))  * P0()
        
    def Nf():
        if(Ro == 1):
            Nf = P0() * ((s ** s) / math.factorial(s)) * (L - s)(L - s + 1)/(2)
        else:
            Nf1 = 0
            Nf2 = 0
            Nf1 = (P0() * ((s * Ro) ** s) * Ro) / (math.factorial(s) * (1 - Ro) ** 2)
            Nf2 = 1 - (Ro ** (L - s + 1)) - (1 - Ro) * (L - s + 1) * Ro ** (L - s)
            Nf = Nf1 * Nf2
        return Nf
    
    # calcul des parametres
    if(Ro >= 1):
        print("ERREUR : Regime stationnaire n'existe pas !")
    else:
        if parametre == 1:
            print("Calcul du nombre moyen des clients dans le systeme...")
            Nf = Nf()
            Ns = Nf + Lambda * (1 - Pl()) / Mu
            print(Ns)
        elif parametre == 2:
            print(Ns)
            print("Calcul du nombre moyen des clients dans la file...")
            Nf = Nf()
            print(Nf)
        elif parametre == 3:
            print("Calcul du temps d'attente moyen dans le systeme...")
            Nf = Nf()
            Ns = Nf + Lambda * (1 - Pl()) / Mu
            Ts = Ns / (Lambda * (1 - Pl()))
            print(Ts)
        elif parametre == 4:
            print("Calcul du temps d'attente moyen dans la file...")
            Nf = Nf()
            Tf = Nf / (Lambda * (1 - Pl()))
            print(Tf)