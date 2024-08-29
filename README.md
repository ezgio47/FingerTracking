# FingerTracking

Dieses Projekt verwendet Hand-Tracking-Technologie zur Erkennung und Zählung der Finger in einem Live-Feed von deiner Kamera. Es besteht aus zwei Hauptkomponenten:

- **`finger.py`**: Das Hauptskript zur Durchführung der Handerkennung und zur Anzeige der Anzahl der Finger.
- **`HandTrackingModule.py`**: Ein Modul zur Implementierung der Handverfolgung und Erkennung mit Mediapipe.

## Installation

1. **Repository klonen:**

   ```bash
   git clone git@github.com:dein-username/FingerTracking.git
   cd FingerTracking
2. **Abhängigkeiten installieren:**

   ```bash
   pip install opencv-python mediapipe

## Verwendung

1. **Starten des Hand-Tracking-Skripts:**

   ```bash
   python finger.py

2. **Wie es funktioniert:**

   ```bash
   Kamera: Das Skript verwendet die Kamera deines Computers, um ein Live-Feed anzuzeigen.
   Handverfolgung: HandTrackingModule.py nutzt Mediapipe, um Hände im Bild zu erkennen.
   Fingerzählung: Die Anzahl der Finger wird im Terminal angezeigt.

3. **Fehlerbehebung:**
   ```bash
   Kamera nicht erkannt: Stelle sicher, dass keine anderen Anwendungen auf die Kamera zugreifen und dass die Kamera ordnungsgemäß funktioniert.
