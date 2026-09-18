# Driver Drowsiness and Distraction Detection System

**Author:** Shaurya Das  
**Registration ID:** 24BAC10028  
**Institution:** VIT Bhopal University  
**Platform:** VITyarthi - Build Your Own Project  

An end-to-end, real-time computer vision application designed to monitor driver attentiveness using facial landmark tracking, Eye Aspect Ratio (EAR) calculations, Mouth Aspect Ratio (MAR) metrics, and 3D head pose estimation.

---

## 1. Features
* **Drowsiness Monitoring:** Real-time analysis of eye closure dynamics using Eye Aspect Ratio (EAR) to detect microsleep events.
* **Yawn & Fatigue Tracking:** Mouth Aspect Ratio (MAR) evaluation to identify early signs of physical fatigue.
* **Head Pose & Distraction Estimation:** 3D facial orientation tracking (pitch, yaw, roll) to detect when a driver looks away from the road for $>2$ seconds.
* **Multi-Modal Warning System:** Instant visual bounding overlays via OpenCV and non-blocking auditory alarms using Pygame.
* **Session Telemetry:** Automatic local logging of fatigue and distraction timestamps in structured JSON/CSV format for post-trip analytics.

---

## 2. Technologies & Tools Used
* **Programming Language:** Python 3.10+
* **Computer Vision & ML:** OpenCV, MediaPipe
* **Data Processing:** NumPy, SciPy
* **Alert System:** Pygame, OpenCV GUI
* **Testing & Quality Assurance:** PyTest, Flake8

---

## 3. Repository Directory Structure
