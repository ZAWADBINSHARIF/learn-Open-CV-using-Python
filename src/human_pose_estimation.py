import cv2 as cv
import mediapipe as mp
import time

mpPose = mp.solutions.pose
mpDraw = mp.solutions.drawing_utils
pose = mpPose.Pose()

cap = cv.VideoCapture("resources/human_dance.mp4")

pTime = 0

while True:
    success, img = cap.read();
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    print(results.pose_landmarks)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks)

        if results.pose_landmarks:
            mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
            for id, lm in enumerate(results.pose_landmarks.landmark):
                h, w, c = img.shape
                print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                cv.circle(img, (cx, cy), 5, (255, 0, 0), cv.FILLED)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv.putText(img, str(int(fps)), (64, 64), cv.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
    img = cv.resize(img, (640, 980))
    cv.imshow("Image", img)

    cv.waitKey(1)