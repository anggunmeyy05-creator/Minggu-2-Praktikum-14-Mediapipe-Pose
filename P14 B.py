import cv2
import mediapipe as mp
mp_pose = mp.solutions.pose #inisiasi media pipe pose
pose = mp_pose.Pose()
mdraw = mp.solutions.drawing_utils
cap =  cv2.VideoCapture(0) #video dari webcam

while True:
    success, frame = cap.read() #pembacaan image
    imgRGB= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #konversi warna dari bgr ke rgb
    hasil = pose.process(imgRGB) #ekstraksi dari image
    if hasil.pose_landmarks:
        mdraw.draw_landmarks(frame, hasil.pose_landmarks, mp_pose.POSE_CONNECTIONS) #menggambar koneksi landmark
    for id, lm in enumerate(hasil.pose_landmarks.landmark):
        print(id, lm.x, lm.y) #ekstraksi id, posisi x, posisi y

    cv2.imshow("webcam", frame)
    cv2.waitKey(10)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Tutup webcam dan jendela tampilan saat q ditekan
cap.release()
cv2.destroyAllWindows()