import cv2
import HandTrackingModule as htm

# Kamera-Einstellungen
wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)  # Verwende die erste Kamera
cap.set(3, wCam)
cap.set(4, hCam)

# Initialisiere das Hand-Tracking-Modul
detector = htm.HandTrackingModule()

# Lade die Overlay-Bilder und überprüfe, ob sie erfolgreich geladen wurden
overlayList = []
for i in range(5):
    img_path = f'path_to_image_{i}.png'
    img = cv2.imread(img_path)
    if img is not None:
        overlayList.append(img)
    else:
        print(f"Fehler beim Laden des Bildes: {img_path}")

# Definiere die tipIds für die Finger-Spitzen
tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    if not success:
        print("Fehler beim Lesen des Kamerabildes.")
        break

    # Hände finden und markieren
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    
    if lmList:
        fingers = []
        # Überprüfe den Daumen
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        # Überprüfe die anderen Finger
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 1][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        totalFingers = fingers.count(1)
        
        if 0 <= totalFingers - 1 < len(overlayList):
            try:
                h, w, c = overlayList[totalFingers - 1].shape
                # Overlay anwenden
                img[0:h, 0:w] = overlayList[totalFingers - 1]
                cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
            except Exception as e:
                print(f"Fehler beim Anwenden des Overlays: {e}")
        else:
            print(f"TotalFingers {totalFingers} out of range for overlayList")
        
    else:
        print("Keine Hand erkannt.")

    # Zeige das Bild an
    cv2.imshow("Image", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Freigabe der Kamera und Schließen aller Fenster
cap.release()
cv2.destroyAllWindows()



