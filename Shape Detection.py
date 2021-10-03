import cv2

link = r'folder\filename.jpeg'
img = cv2.imread(link)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, threshold = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(
	threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i = 0
liobj = []

for contour in contours:
    
    Area = cv2.contourArea(contour)
    if Area > 2000:

        if i == 0:
            i = 1                
            continue
        approx = cv2.approxPolyDP(
            contour, 0.01 * cv2.arcLength(contour, False), False)

        M = cv2.moments(contour)
        if M['m00'] != 0.0:
            x = int(M['m10']/M['m00'])
            y = int(M['m01']/M['m00'])
            
        i+=1
        if i%2 == 1:
            liobj.append([x,y])
        else:
            pass
        if len(approx) == 3:
            cv2.drawContours(img, [contour], 0, (0, 0, 255), 1)
            cv2.putText(img, 'Triangle', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        elif len(approx) == 4:
            cv2.drawContours(img, [contour], 0, (0,255, 255), 1)
            cv2.putText(img, 'Quadrilateral', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255, 255), 2)
            
        elif len(approx) == 5:
            cv2.drawContours(img, [contour], 0, (0, 255,0), 1)
            cv2.putText(img, 'Pentagon', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0, 255),2)
        elif len(approx) == 6:
            cv2.drawContours(img, [contour], 0, (0, 0, 255), 1)
            cv2.putText(img, 'Hexagon', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        elif len(approx) == 8:
            cv2.drawContours(img, [contour],0, (255,0,0), 1)
            cv2.putText(img, 'Octagon', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0,0 ), 2)    
        else:
            cv2.drawContours(img, [contour], 0, ( 255, 255,0), 1)
            cv2.putText(img, 'circle', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, ( 255, 255,0), 2)

cv2.imshow('shapes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()import cv2

link = r'folder\filename.jpeg'
img = cv2.imread(link)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, threshold = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(
	threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i = 0
liobj = []

for contour in contours:
    
    Area = cv2.contourArea(contour)
    if Area > 2000:

        if i == 0:
            i = 1                
            continue
        approx = cv2.approxPolyDP(
            contour, 0.01 * cv2.arcLength(contour, False), False)

        M = cv2.moments(contour)
        if M['m00'] != 0.0:
            x = int(M['m10']/M['m00'])
            y = int(M['m01']/M['m00'])
            
        i+=1
        if i%2 == 1:
            liobj.append([x,y])
        else:
            pass
        if len(approx) == 3:
            cv2.drawContours(img, [contour], 0, (0, 0, 255), 1)
            cv2.putText(img, 'Triangle', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        elif len(approx) == 4:
            cv2.drawContours(img, [contour], 0, (0,255, 255), 1)
            cv2.putText(img, 'Quadrilateral', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255, 255), 2)
            
        elif len(approx) == 5:
            cv2.drawContours(img, [contour], 0, (0, 255,0), 1)
            cv2.putText(img, 'Pentagon', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0, 255),2)
        elif len(approx) == 6:
            cv2.drawContours(img, [contour], 0, (0, 0, 255), 1)
            cv2.putText(img, 'Hexagon', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        elif len(approx) == 8:
            cv2.drawContours(img, [contour],0, (255,0,0), 1)
            cv2.putText(img, 'Octagon', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0,0 ), 2)    
        else:
            cv2.drawContours(img, [contour], 0, ( 255, 255,0), 1)
            cv2.putText(img, 'circle', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, ( 255, 255,0), 2)

cv2.imshow('shapes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
