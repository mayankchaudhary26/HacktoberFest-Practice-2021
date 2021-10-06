import numpy as np
import cv2 as cv

def click_event(event, x, y, flags, param) :
	if event == cv.EVENT_LBUTTONDOWN :
		blue = img[y, x, 0]
		green = img[y, x, 1]
		red = img[y, x, 2]
		imageColor = np.zeros([300, 300, 3], np.uint8)
		imageColor[:] = [blue, green, red]
		cv.imshow("BGR Colors: ", imageColor)
img = cv.imread("Color-Balls-2.jpg")
# insert an image of your choice here above

cv.setMouseCallback("Image", click_event)

cv.waitKey()
cv.destroyAllWindows()
