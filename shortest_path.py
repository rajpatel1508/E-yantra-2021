
import os, sys
import traceback
import math
import time
import sys

shortest_path_list = []
def isvalid(list):
	if list[0] < 0 or list[0] > 8 or list[1] < 0 or list[1] > 11:
		return False
	return True

def distance(source, destination):
	dist = math.sqrt((source[0] - destination[0])**2 + (source[1] - destination[1])**2)
	return dist

def shortest_path(source,destination,shortest):
	"""
	Purpose:
	---
	This function should be used to find the shortest path on the given floor between the destination and source co-ordinates.
	"""
	if source == destination:
		shortest_path_list.append(shortest)
		return True
	dist = distance(source,destination)
	s1 = (source[0]+1,source[1])
	s2 = (source[0],source[1]+1)
	s3 = (source[0]-1,source[1])
	s4 = (source[0],source[1]-1)
	x = False

	if isvalid(s1):
		dist1 = distance(s1,destination)
		if dist1 < dist:
			temp = shortest.copy()
			temp.append(s1)
			x = shortest_path(s1,destination,temp)

	if x:
		return True

	if isvalid(s2):
		dist1 = distance(s2,destination)
		if dist1 < dist:
			temp = shortest.copy()
			temp.append(s2)
			x = shortest_path(s2,destination,temp)

	if x:
		return True

	if isvalid(s3):
		dist1 = distance(s3,destination)
		if dist1 < dist:
			temp = shortest.copy()
			temp.append(s3)
			x = shortest_path(s3,destination,temp)

	if x:
		return True

	if isvalid(s4):
		dist1 = distance(s4,destination)
		if dist1 < dist:
			temp = shortest.copy()
			temp.append(s4)
			x = shortest_path(s4,destination,temp)

	if x:
		return True

	return False

if __name__ == "__main__":
    source = (2,2)
    destination = (0,0)
    shortest =[]
    shortest_path(source,destination,shortest)
    print(shortest_path_list)
