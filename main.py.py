import cv2
import numpy as np
from src.detector import DrowsinessDetector
from src.metrics import calculate_ear, calculate_mar
from src.alert_system import AlertSystem

def main():
    cap = cv2.VideoCapture(0)
    detector = DrowsinessDetector()
    alert = AlertSystem()

    print("Starting Driver Drowsiness Detection... Press 'q' to exit.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        left_eye, right_eye, mouth = detector.process_frame(frame)

        if left_eye is not None:
            left_ear = calculate_ear(left_eye)
            right_ear = calculate_ear(right_eye)
            avg_ear = (left_ear + right_ear) / 2.0
            mar = calculate_mar(mouth)
        else:
            avg_ear, mar = None, None

        annotated_frame = alert.evaluate(frame, avg_ear, mar)
        cv2.imshow("Driver Drowsiness System - VIT Bhopal", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()