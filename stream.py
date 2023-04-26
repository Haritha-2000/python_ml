#we can run python file using python stream(file name)
import cv2
#define a video caputure object
vid = cv2.VideoCapture(0)
while True:
    # capture the videoframe

    ret, img = vid.read()
    image = cv2.putText(img, 'Welcome to AI ML class', (150,250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 6, cv2.LINE_AA)
    # Display the resulting frame

    cv2.imshow('Live video', image)
    # the "q" button is set as the quitiing button may use any other deisred button of your choice

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

# after the loop relaese the cap object

vid.release()
cv2.destroyAllWindows()


