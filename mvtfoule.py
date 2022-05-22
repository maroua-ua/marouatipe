import numpy as np
import random as rd
import math
import matplotlib.pyplot as plt
import time
n=8
pi=np.pi

def init_plot(l):
    Xs = [l[i][0] for i in range(len(l))]
    Ys = [l[i][1] for i in range(len(l))]
    Ss = [l[i][2]*100 for i in range(len(l))]
    # print("len: ",len(l))
    # print("len: ",len(l[0]))
    x = np.array(Xs)
    y = np.array(Ys)
    s = np.array(Ss)
    plt.scatter(x, y, s=s)
    plt.xticks(np.arange(0, 20, 5))
    plt.yticks(np.arange(0, 20, 5))
    plt.xlim(0,20)
    plt.ylim(0,20)
    plt.show()
    time.sleep(0.1)
    plt.close()
    plt.clf()

    # time.sleep(0.1)



def positionInitiale(n):
    l=[]
    for i in range (n):
        x=rd.randint(1,20)
        y=rd.randint(1,20)
        r = 2
        poid= rd.randint(30, 100)
        l.append([x,y,r,poid])
    print(l)
    return l
porte=[0,0]

def distance(a):#distance de la porte
    return ((a[0]-porte[0])**2+(a[1]-porte[1])**2)**(1/2)

def distance2(a,b):#distance entre a et b
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**(1/2)

def isSafe(a,b):
    dist = distance2(a,b)
    som = a[2]+b[2]
    print("isSafe:dist=",dist," somme:",som)
    print(som <= dist)
    return (som <= dist)

'''def safeForAll(l,temp,i):
    for pos,agent in enumerate(l):
        if pos != i and isSafe(temp,agent)==False:
            return False
    return True
'''
# def A(l):
#     res= []
#     for i in range (len(l)):
#         for j in  range (len(l)):
#             res.append(distance_(l[i],l[j]))
#     return res
#
# def safer (l):
#     for i in l:
#         for j in range (len(l)):
#             if not isSafe(l[i],l[j]) and l[i][1][2]>l[j][1][2]:

def sommeDesDistances (l):
    n,r=len(l),0
    for i in range (n):
        r+= distance(l[i])
    return r

def angle (a,b):
    idk=(a[1]-b[1])/(a[0]-b[0])
    return np.arctan(idk)

def angles (l):
    return [angle(l[i],porte) for i in range (len(l))]

def toutesnulles (l):
    b=True
    for i in range (len(l)):
        if distance(l[i])!=0:
            b=False
    return b

def ListeDesCollisions (l):
    res=[]
    for i in l :
        for j in l:
            if not isSafe (i,j) and i!=j:
                res.append([i,j])
    return res

def main ():
    n=10
    l=positionInitiale(n)
    temps=0
    i=0
    finished=False
    print (l)
    # while not finished :
    while len(l)!=0:
        print("list :",l)
        for i in range(len(l)):
            a,b = distance(l[i]),angle(l[i],porte)
            lc=ListeDesCollisions(l)
            if i not in lc:
            # print("distance: ",a)
                print("long: ", l[i])
                l[i] = [max(a*math.cos(b)-math.cos(b),0),max(a*math.sin(b)-math.sin(b),0),l[i][2],l[i][3]]
            else :
                pass
            '''for j in range(len(l)):
                if not isSafe(l[i],l[j]) and (l[i][3] > l[j][3]) and i!=j: 
                    c,d = distance2(l[j],porte),angle(l[j],porte)
                    l[i] = [max(c*math.cos(d-(180/20)),0),max(c*math.sin(d-(180/20)),0),l[j][2],l[j][3]]
          '''
            
               
          
        temps=temps+0.5
        # print("somme dist:",sommeDesDistances(l))
        init_plot(l)
        i=0
        
        while i<len(l):
            if distance(l[i])<1:
                print(i, "was removed")
                l.pop(i)
                print(l)
            else:
                i=i+1

        if sommeDesDistances(l)==0:
            finished=True
    return temps

if __name__ == '__main__':
    print(main())

'''if safeForAll(l, temp, i) == True:
    l[i] = [a*math.cos(b)-math.cos(b),a*math.sin(b)-math.sin(b),l[i][2]]
    print("long: ",l[i])
else:
    print(i,"skipped")
    print(l[i]," , ",temp)
       
  '''      