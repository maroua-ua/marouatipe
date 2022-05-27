import numpy as np
import random as rd

# Map settings
dt=0.1
n=8
sizeX=50.
sizeY=sizeX
doors = [	((0,0),np.array([0.,0.])),
			((0,0),np.array([sizeX,sizeY]))
		]    #R P              X     Y





# Actor settings
# actorSize= lambda : rd.uniform(1.8, 2.2)
actorSize= lambda : rd.choice([1.8, 1.9, 2.0, 2.1, 2.2]) #cleaner console output
actorWeight=actorSize
pos = np.array([np.array([rd.uniform(0.0, sizeX), rd.uniform(0.0, sizeY)]) for i in range(n)])
spd = np.array([0.1,0.1])
actors = [[(actorSize(),actorWeight()),pos[i],spd] for i in range(n)]

# Actor Accessors
def actor_size(a):
	return a[0][0]

def actor_weight(a):
	return a[0][1]

def actor_pos(a):		#actor position vector
	return a[1]
def actor_x(a):			#actor x
	return actor_pos(a)[0]
def actor_y(a):			#actor y
	return actor_pos(a)[1]

def actor_v(a): 		#actor speed vector
	return a[2]
def actor_vx(a): 		#actor x speed
	return actor_v(a)[0]
def actor_vy(a): 		#actor y speed
	return actor_v(a)[1]
def actor_v_mag(a): 	#actor speed
	return np.linalg.norm(actor_v(a))






# Functions
def distance_pos(a,b): #distance between pos vectors
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

def weight(a,b): #combined weight of 2 actors
	return actor_weight(a)+actor_weight(b)

def collision(a,b): #collision between actors
	return distance(a,b) < size(a,b)

# Detect Actor Collisions
def actor_collisions(actors):
	out=[]
	for i, a in enumerate(actors):
		for j, b in enumerate(actors):
			if j<=i:
				continue
			if collision(a,b):
				out.append((i,j))
	return out

# Detect Actors at Doors
def door_collisions(actors,doors):
	out=[]
	for i, a in enumerate(actors):
		for b in doors:
			if collision(a,b):
				out.append(i)
	return out

# Remove Actors at Doors
def solve_door_collisions(actors, collisions):
	collisions.sort(reverse=True) #if we remove the lower index first, it changes the indices of those above
	for c in collisions:
		del actors[c]

def solve_actor_collisions(actors, collisions):
	for i,j in collisions:
		a,b= actors[i],actors[j]
		axe = a[1]-b[1]/np.linalg.norm(a[1]-b[1])
		amt = size(a,b) - distance(a,b)
		actors[i][1] = a[1] + axe * amt * actor_weight(b)/weight(a,b)
		actors[j][1] = b[1] - axe * amt * actor_weight(a)/weight(a,b)


def update_actor_speeds(actors):
	for a in actors:
		speed = np.linalg.norm(a[2])
		door_factor=1 	*	 (actor_size(a)/actor_weight(a))
		drag_factor= 0.1 *	 (actor_size(a)+actor_weight(a)) * speed**2
		
		door = closestDoor(a)
		doordir = (door[1]-actor_pos(a))/np.linalg.norm(door[1]-actor_pos(a))
		dragdir = -1 * a[2]/speed

		acc_door = door_factor * doordir 	# size/weight in director of door
		acc_drag = drag_factor * dragdir 	# -(size+weight) * speed**2
		
		a[2] = a[2]+(acc_door+acc_drag)*dt

def update_actor_positions(actors):
	for a in actors:
		a[1] = a[1] + a[2]*dt






# Main
import os
import time
import matplotlib.pyplot as plt

while(actors):
	os.system('clear')
	for a in actors:
		print(a)

	dc = door_collisions(actors,doors)
	solve_door_collisions(actors,dc)

	ac = actor_collisions(actors)
	solve_actor_collisions(actors,ac)


	update_actor_speeds(actors)
	update_actor_positions(actors)

	time.sleep(dt)