import cv2
import time
Vidpath = "H:\PROJECT\Alphabets\\"
VidCap = "VidCap\\"
VidSmall = "VidSmall\\"
vidext = ".mp4"
#.........................playing Videos..................#
def VideoPlay(bet):
    if bet.isupper():
        Vidbet = Vidpath+VidCap+bet+vidext 
    if bet.islower():
        Vidbet = Vidpath+VidSmall+bet+vidext 
    cap = cv2.VideoCapture(Vidbet)
    while cap.isOpened():
        ret,frame = cap.read()
        if not ret:
            break
        time.sleep(0.06)
        cv2.imshow(bet,frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
