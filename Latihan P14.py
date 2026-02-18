import cv2
import mediapipe as mp
mp_pose = mp.solutions.pose #inisiasi media pipe pose
pose = mp_pose.Pose()
mdraw = mp.solutions.drawing_utils
cap =  cv2.VideoCapture(0) #video dari webcam

while True:
    success, frame = cap.read()
    if not success:
        continue
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hasil = pose.process(imgRGB)
    if hasil.pose_landmarks:
        mdraw.draw_landmarks(frame, hasil.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        landmarks = hasil.pose_lanmarks.landmark

        left_shoulder = landmarks[11]
        left_wrist = landmarks[15]
        right_shoulder = landmarks[12]
        right_wrist = landmarks[16]

        status = "Tangan Tidak Terangkat"

        # Deteksi tangan kiri
        if left_wrist.y < left_shoulder.y:
            status = "Tangan Kiri Terangkat"

        # Deteksi tangan kanan
        if right_wrist.y < right_shoulder.y:
            status = "Tangan Kanan Terangkat"

        cv2.putText(frame, status, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 225, 0), 2)

    cv2.imshow("Deteksi Angkat Tangan", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()