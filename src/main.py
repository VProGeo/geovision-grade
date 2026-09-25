import cv2

# Підключення камери
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Камеру не знайдено")
    exit()

# Налаштування розпізнавання міток
dictionary = cv2.aruco.getPredefinedDictionary(
    cv2.aruco.DICT_4X4_50
)

detector = cv2.aruco.ArucoDetector(dictionary)

while True:
    success, frame = camera.read()

    if not success:
        break

    # Пошук міток
    corners, ids, rejected = detector.detectMarkers(frame)

    if ids is not None:
        cv2.aruco.drawDetectedMarkers(
            frame, corners, ids
        )

    cv2.imshow("GeoVision Grade", frame)

    # Натисни Q для виходу
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()