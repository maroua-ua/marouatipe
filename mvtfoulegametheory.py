#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 13:57:53 2022

@author: maroua
"""

import numpy as np
import random as rd
import math
import matplotlib.pyplot as plt
import time
n=20
longueur=5
strat = ["D","C"] # Defector and cooperator
r = 0.4
v0= 1.31
DistanceDeSecurité=0.8
porte=[0,0]

def init_plot(l):
    Xs = [l[i][0] for i in range(len(l))]
    Ys = [l[i][1] for i in range(len(l))]
    Ss = [l[i][2]*100 for i in range(len(l))]
    # print("len: ",len(l))
    # print("len: ",len(l[0]))
    x = np.array(Xs)
    y = np.array(Ys)
    s = np.array(Ss)
    plt.scatter(x, y)
    plt.xticks(np.arange(0, 5, 1))
    plt.yticks(np.arange(0, 5, 1))
    plt.xlim(0,5)
    plt.ylim(0,5)
    plt.show()
    time.sleep(0.1)
    plt.close()
    plt.clf()

    # time.sleep(0.1)
    
    
def positionInitiale():
    l=[]
    for i in range (n):
        x=rd.uniform(0.5,longueur)
        y=rd.uniform(0.5,longueur)
        poid= rd.randint(60, 120)
        l.append([x,y,rd.choice(strat),poid])
    print(l)
    return l  

def distancePorte(a):#distance de la porte
    return ((a[0]-porte[0])**2+(a[1]-porte[1])**2)**(1/2)

def distance(a,b):#distance entre a et b
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**(1/2)

def Direction(Agent):
    
    
    direction_x=porte[0]-Agent[0];
    direction_y=porte[1] -Agent[1]
    return np.array([direction_x/math.sqrt(direction_x**2+direction_y**2),direction_y/math.sqrt(direction_x**2+direction_y**2)])


def angle (x,y):#angle entre deux points
    idk=(x[1]-y[1])/(x[0]-y[0])
    return np.arctan(idk)

def angles (l): #angles avec la porte
    return [angle(l[i],porte) for i in range (len(l))]

def DansZoneSec(i):
    res = [i]
    for j in range(n):
        if i != j :
            if distance(pos[i],pos[j]) < DistanceDeSecurité :
                res.append(j)
    return res

def LargeDefectors(lst) :
    res=[]
    for i in lst :
        verif = True
        x  = pos[i]
        if pos[i][2] == "D" :
            for j in lst :
                if i != j:
                    y = pos[j]
                    if (y[3] >= x[3] + 10) or (y[2] == "C" and y[3] >= x[3] - 10):
                        verif = False
            if verif :
                res.append(i)
        return res
    
def defectors(lst) :
    res =[]
    for i in lst :
        if pos[i][2] == "D" :
            res.append(i)
    return res
            
            
def IsWinner (i):
    proche = DansZoneSec(i)
    Cd = 0
    Cc = 0
    LargeDef = LargeDefectors(proche)
    Def = defectors(proche)
    if len(proche) == 1:
        return i
    for x in proche :
        if pos[i][2] == "D" :
            Cd += 1
        else :
            Cc += 1
    if Cd > 1 :
        if len(LargeDef) == 1 :
            return LargeDef[0]
        elif len(LargeDef) > 1 :
            return rd.choice(LargeDef)
        elif len(LargeDef) == 0 :
            return rd.choice(Def)
    elif Cd == 1 and Cc >= 1 :
        return Def[0]
    else :
        return rd.choice(proche)
            
            
def main ():
    pos
    temps=0
    i=0
    print (pos)
    # while not finished :
    while len(pos)!=0:
        print("list :",pos)
        for i in range(len(pos)):
            if i == IsWinner(i) :
                (x0,y0) = Direction(pos[i])
                pos[i][0] = pos[i][0] + x0*v0*0.5
                pos[i][1] = pos[i][1] + y0*v0*0.5
        temps=temps+0.5
        # print("somme dist:",sommeDesDistances(l))
        init_plot(pos)
        i=0
        
        while i<len(pos):
            if distancePorte(pos[i])<0.4:
                print(i, "was removed")
                pos.pop(i)
                print(pos)
            else:
                i=i+1
    return temps
    
#main

pos = positionInitiale()
t = main()
if __name__ == '__main__':
    print(main())

print("le temps est", t," secondes")








