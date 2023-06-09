# credits : https://www.learnpythonwithrune.org/how-to-scan-qr-codes-from-your-web-cam-in-3-steps/

# import the opencv library
import cv2

# define a video capture object
vid = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
cnt = 0

while True:
    # Capture the video frame by frame
    ret, frame = vid.read()
    data, bbox, straight_qrcode = detector.detectAndDecode(frame)
    if len(data) > 0:
        print(data)
        
    # Display the resulting frame
    cv2.imshow('frame', frame)
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if len(data) > 0:
        break
    
    cnt = cnt + 1
    if( cnt%10 == 0 ):
        print(cnt)
        
# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()
