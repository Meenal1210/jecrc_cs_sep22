#import cv2
#loc= r'C:\Users\Meenal Jain\Desktop\JECRC Logo.png'
#im = cv2.imread(loc)
#print(im.shape)
#cv2.imshow('image', im)
#cv2.waitKey(0)

import webbrowser
import cv2
cam=cv2.VideoCapture(0)
from mediapipe import solutions as sol
mph = sol.hands
mpdraw = sol.drawing_utils
mpstyle = sol.drawing_styles
hand_conn = mpstyle.get_default_hand_connections_style
hand_im = mpstyle.get_default_hand_landmarks_style
hand_detect = mph.Hands()

old_value=0
while True:
    r,im=cam.read()
    if r == True:
        # print(im.shape)
        im=cv2.flip(im,1)
        results = hand_detect.process(im)
        counter = 0
        if results.multi_hand_landmarks:
            for gesture in results.multi_hand_landmarks:
                mpdraw.draw_landmarks(
                    im, gesture, mph.HAND_CONNECTIONS, hand_im(), hand_conn()
                )
                if gesture.landmark[8].y < gesture.landmark[5].y:
                    counter +=1
                if gesture.landmark[12].y < gesture.landmark[9].y:
                    counter +=1
                if gesture.landmark[16].y < gesture.landmark[13].y:
                    counter +=1
                if gesture.landmark[20].y < gesture.landmark[17].y:
                    counter +=1
        print(counter)
        if counter == 1 and old_value != counter:
            webbrowser.open('www.flipkart.com/search?q=oneplus')
            old_value = counter
        cv2.imshow('image',im)
        if cv2.waitKey(1) == ord('a'):
            break
cam.release()
cv2.destroyAllWindows()







