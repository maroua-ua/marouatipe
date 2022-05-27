import numpy as np
import random as rd
import time
import matplotlib.pyplot as plt

# Map settings
dt=0.01
n=8
sizeX=50.
sizeY=sizeX
doors = [	((0,0),np.array([0.,0.])),
			((0,0),np.array([sizeX,sizeY]))
		]    #R P   X     Y

# Actor settings
actorSize=2.
actorWeight=actorSize
pos = np.array([np.array([rd.uniform(0.0, sizeX), rd.uniform(0.0, sizeY)]) for i in range(n)])
spd = np.array([0.1,0.1])
actors = [[(actorSize,actorWeight),pos[i],spd] for i in range(n)]


# Functions
def distance_pos(a,b): #distance between pos tuples
	return ((a[0]-b[0])**2+(a[1]-b[1])**2)**(1/2)

def distance(a,b): #distance between actors
	return distance_pos(a[1],b[1])

def closestDoor(a):
	door=doors[0]
	dist=sizeX**2 #bigger than any used distance
	for i,d in enumerate(doors):
		ad = distance(a,d)
		if ad < dist:
			door=doors[i]
			dist=ad
	return door

def size(a,b): #combined size of actors
	return a[0][0]+b[0][0]

def collision(a,b): #collision between
	return distance(a,b) < size(a,b)

def actor_collisions(actors):
	out=[]
	for i, a in enumerate(actors):
		for j, b in enumerate(actors):
			if j<=i:
				continue
			if collision(a,b):
				out.append((i,j))
	return out

def door_collisions(actors,doors):
	out=[]
	for i, a in enumerate(actors):
		for b in doors:
			if collision(a,b):
				out.append(i)
	return out

def solve_door_collisions(actors, collisions):
	collisions.sort(reverse=True)
	for c in collisions:
		del actors[c]

def solve_actor_collisions(actors, collisions):
	pass


def update_actor_speeds(actors):
	for a in actors:
		speed = np.linalg.norm(a[2])
		door_factor=1 	*	 (a[0][0]/a[0][1])
		drag_factor= 0.1 *	 (a[0][0]+a[0][1]) * speed**2
		
		door = closestDoor(a)
		doordir = (door[1]-a[1])/np.linalg.norm(door[1]-a[1])
		dragdir = -1 * a[2]/speed

		acc_door = door_factor * doordir 	# size/weight in director of door
		acc_drag = drag_factor * dragdir 	# -(size+weight) * speed**2
		
		a[2] = a[2]+(acc_door+acc_drag)*dt

def update_actor_positions(actors):
	for a in actors:
		a[1] = a[1] + a[2]*dt


# Main
import os
while(actors):
	os.system('clear')
	for a in actors:
		print(a)

	dc = door_collisions(actors,doors)
	solve_door_collisions(actors,dc)


	update_actor_speeds(actors)
	update_actor_positions(actors)
	time.sleep(dt)