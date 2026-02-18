import cv2
import mediapipe as mp
mp_pose =mp.solutions.pose
# Inisiasi Media Pipe Pose
pose = mp_pose.Pose()
cap = cv2.VideoCapture(0) # Video dari webcam

while True:
    success, frame = cap.read() #pembacaan image
    imgrgb= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #konversi warna dari bgr ke rgb
    hasil = pose.process(imgrgb) #ekstraksi dari image
    if hasil.pose_landmarks:
        print ("terdeteksi")
    else:
        print ("tidak terdeteksi")

    cv2.imshow ("webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() # Tutup webcam jendela tampilan saat q ditekan
cv2.destroyAllWindows()