import cv2 as cv
#video is the variable i have declared and VideoCapture reads the video and 0 there means inbuilt webcam
cap = cv.VideoCapture("Players.mp4")
while(True):
    ret, frame = cap.read()
    cv.imshow("Frame", frame)
    if cv.waitKey(1) & 0xFF == ord("e"):
        break

        cap.release()
        cv.destroyAllWindows()
