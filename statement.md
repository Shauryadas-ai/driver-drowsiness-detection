# Problem Statement & System Scope

**Project:** AI-Powered Real-Time Driver Drowsiness and Distraction Detection System  
**Student Name:** Shaurya Das  
**Registration ID:** 24BAC10028  
**Institution:** VIT Bhopal University  

---

## 1. Problem Statement
Driver drowsiness and distraction are major contributors to road accidents globally. According to highway safety reports, momentary lapses in driver attention due to fatigue, mobile phone usage, or looking away from the road drastically increase collision risks. Existing high-end vehicle monitoring systems are expensive and proprietary. There is a need for an accessible, low-latency, real-time computer vision system that monitors driver attentiveness via a standard webcam and generates instant warnings to prevent accidents.

## 2. Project Scope
The system operates as an edge-deployable computer vision application that captures live video frames from an in-cabin camera. The functional scope includes:
* **Facial Landmark Extraction:** Detecting facial boundaries, eye region dynamics, and mouth posture in real time.
* **Drowsiness Monitoring:** Calculating the Eye Aspect Ratio (EAR) and monitoring yawn frequency via Mouth Aspect Ratio (MAR) over consecutive frame windows.
* **Distraction & Head Pose Estimation:** Computing pitch, yaw, and roll angles of the driver's head to detect off-road gaze direction.
* **Alert Mechanism:** Triggering visual overlays and auditory alarms upon detecting fatigue or prolonged distraction.

## 3. Target Users
* **Commercial Fleet Operators:** Managing long-haul truck drivers to minimize fleet accident risks.
* **Everyday Motorists:** Individual drivers seeking an affordable safety accessory using a smartphone or onboard webcam.
* **Ride-Hailing Platforms:** Monitoring driver fatigue during extended shifts to ensure passenger safety.

## 4. High-Level Features
* **Real-time Video Processing:** Low-latency frame analysis operating at $\ge 30$ FPS on standard hardware.
* **Eye Aspect Ratio (EAR) Thresholding:** Automatic detection of closed eyes or prolonged blinking.
* **Head Pose Dynamics:** Real-time facial orientation tracking to identify when a driver looks away from the road for $>2$ seconds.
* **Multi-Modal Warning System:** Instant visual notifications on screen and sound cues for immediate feedback.
* **Session Logging & Analytics:** Storing metrics locally for post-trip driving behavior analysis.