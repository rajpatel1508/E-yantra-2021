import cv2
import numpy as np
image = cv2.imread(r"C:\Users\Satvik\Desktop\Untitled-3-01.png")
dimensions = image.shape
print(dimensions)
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
cv2.imshow("Original", image)
berries_dictionary = {}
berries = ["Strawberry", "Blueberry", "Lemon"]

	##############	ADD YOUR CODE HERE	##############
berries_dictionary = {berries[0]:[], berries[1]:[], berries[2]:[]}
graypic=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
cv2.imshow("gray", graypic)
ret,thresh=cv2.threshold(graypic,0,255,cv2.THRESH_BINARY)
cv2.imshow("thresh", thresh)
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
m=len(contours)

for i in range(0,m):
	contour=contours[i]
	approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
	cv2.drawContours(image, [contour], 0, (0, 255, 0), 5)
	M = cv2.moments(contour)
	if M['m00'] != 0.0:
		X = int(M['m10']/M['m00'])
		Y = int(M['m01']/M['m00'])
	
	cv2.putText(image, str(X), (X, Y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
	print(X,Y)
	print(image[Y,X,0],image[Y,X,1],image[Y,X,2])

	if (image[Y,X,0]>128 and image[Y,X,0]<=255 and image[Y,X,1]<=255 and image[Y,X,1]>128 and image[Y,X,2]<127):
		berries_dictionary["Lemon"].append(tuple([X,Y]))
	elif(image[Y,X,2]<=255 and image[Y,X,2]>128 and image[Y,X,1]<127 and image[Y,X,0]<127):
		berries_dictionary["Blueberry"].append(tuple([X,Y]))
	elif(image[X,Y,2]<127 and image[X,Y,1]<127 and image[X,Y,0]<=255 and image[X,Y,0]>128):
		berries_dictionary["Strawberry"].append(tuple([X,Y]))

cv2.imshow("shapes", image)
print(berries_dictionary)
cv2.waitKey(0)
    
    
