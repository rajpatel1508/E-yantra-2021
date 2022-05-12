'''
*****************************************************************************************
*
*        		===============================================
*           		Berryminator (BM) Theme (eYRC 2021-22)
*        		===============================================
*
*  This script is to implement Task 1A of Berryminator(BM) Theme (eYRC 2021-22).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''

# Team ID:			BM_1270
# Author List:		Soham Das, Satvik Raj Patel, Ayush Kumar
# Filename:			task_1a.py
# Functions:		detect_shapes
# 					[ Comma separated list of functions in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv, os)                ##
##############################################################
import cv2
import numpy as np
import os
##############################################################

################# ADD UTILITY FUNCTIONS HERE #################





##############################################################

def detect_shapes(frame):

	"""
	Purpose:
	---
	This function takes the image as an argument and returns a nested list
	containing details of colored (non-white) shapes in that image

	Input Arguments:
	---
	`img` :	[ numpy array ]
			numpy array of image returned by cv2 library

	Returns:
	---
	`detected_shapes` : [ list ]
			nested list containing details of colored (non-white) 
			shapes present in image
	
	Example call:
	---
	shapes = detect_shapes(img)
	"""    
	detected_shapes = []

	##############	ADD YOUR CODE HERE	##############
	#lower and upper bounds of each color in hsv space
	lower = {'Red':([0, 50, 80]), 'Green':([50, 50, 120]), 'Blue':([100, 150, 0]), 'Orange':([10, 50, 50])} #assign new item lower['blue'] = (93, 10, 0)
	upper = {'Red':([10,255,255]), 'Green':([70, 255, 255]), 'Blue':([120,255,255]), 'Orange':([20,255,255])}

	#BGR tuple of each color 
	colors = {'red':(0,0,255), 'green':(0,255,0), 'blue':(255,0,0), 'orange':(0,140,255)}

	

	frame2 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	#plt.imshow(frame)
	#plt.imshow(frame2)
	

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	#plt.imshow(hsv)

	mlist=[]
	clist=[]
	ks=[]

	for (key, value) in upper.items():
		kernel = np.ones((2,2),np.uint8)
		mask = cv2.inRange(hsv, np.array(lower[key]), np.array(upper[key]))
		mlist.append(mask)
		cnts,hei = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		
		for r in cnts:
			if len(cnts)>=1:
				clist.append(r)
				#print(key)
				ks.append(key)
			
	#print(ks)
	
		
	for i,cnt in enumerate(clist):
			approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
			
			
			
			M = cv2.moments(cnt)
			if M['m00'] != 0.0:
				cX = int(M['m10']/M['m00'])
				cY = int(M['m01']/M['m00'])
		
			if len(approx) == 3:
				shape_name="Triangle"
				
			elif len(approx) == 4:
				x, y , w, h = cv2.boundingRect(approx)
				aspectRatio = w/h
				
				if aspectRatio < 1.05:
					shape_name="Square"

				else:
					shape_name="Rectangle"

				
				
			elif len(approx) == 5:
				shape_name= "Pentagon"
			
			#elif 6 < len(approx) < 15:
				#cv2.putText(res, "Ellipse", (x, y), font, 1, (255,255,255))
			
			else:
				shape_name="Circle"
			shape=[ks[i],shape_name,(cX,cY)]
			detected_shapes.append(shape)
	
	
	 


	##################################################
	
	return detected_shapes

def get_labeled_image(img, detected_shapes):
	######### YOU ARE NOT ALLOWED TO MAKE CHANGES TO THIS FUNCTION #########
	"""
	Purpose:
	---
	This function takes the image and the detected shapes list as an argument
	and returns a labelled image

	Input Arguments:
	---
	`img` :	[ numpy array ]
			numpy array of image returned by cv2 library

	`detected_shapes` : [ list ]
			nested list containing details of colored (non-white) 
			shapes present in image

	Returns:
	---
	`img` :	[ numpy array ]
			labelled image
	
	Example call:
	---
	img = get_labeled_image(img, detected_shapes)
	"""
	######### YOU ARE NOT ALLOWED TO MAKE CHANGES TO THIS FUNCTION #########    

	for detected in detected_shapes:
		colour = detected[0]
		shape = detected[1]
		coordinates = detected[2]
		cv2.putText(img, str((colour, shape)),coordinates, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
	return img

if __name__ == '__main__':
	
	# path directory of images in 'test_images' folder
	img_dir_path = 'test_images/'

	# path to 'test_image_1.png' image file
	file_num = 1
	img_file_path = img_dir_path + 'test_image_' + str(file_num) + '.png'
	
	# read image using opencv
	img = cv2.imread(img_file_path)
	
	print('\n============================================')
	print('\nFor test_image_' + str(file_num) + '.png')
	
	# detect shape properties from image
	detected_shapes = detect_shapes(img)
	print(detected_shapes)
	
	# display image with labeled shapes
	img = get_labeled_image(img, detected_shapes)
	cv2.imshow("labeled_image", img)
	cv2.waitKey(2000)
	cv2.destroyAllWindows()
	
	choice = input('\nDo you want to run your script on all test images ? => "y" or "n": ')
	
	if choice == 'y':

		for file_num in range(1, 16):
			
			# path to test image file
			img_file_path = img_dir_path + 'test_image_' + str(file_num) + '.png'
			
			# read image using opencv
			img = cv2.imread(img_file_path)
	
			print('\n============================================')
			print('\nFor test_image_' + str(file_num) + '.png')
			
			# detect shape properties from image
			detected_shapes = detect_shapes(img)
			print(detected_shapes)
			
			# display image with labeled shapes
			img = get_labeled_image(img, detected_shapes)
			cv2.imshow("labeled_image", img)
			cv2.waitKey(2000)
			cv2.destroyAllWindows()


