import cv2

class AlertSystem:
    def __init__(self, ear_threshold=0.22, mar_threshold=0.6, consecutive_frames=15):
        self.EAR_THRESHOLD = ear_threshold
        self.MAR_THRESHOLD = mar_threshold
        self.CONSECUTIVE_FRAMES = consecutive_frames
        self.frame_counter = 0

    def evaluate(self, frame, avg_ear, mar):
        if avg_ear is None:
            cv2.putText(frame, "NO FACE DETECTED", (30, 40), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            return frame

        # Check for Drowsiness
        if avg_ear < self.EAR_THRESHOLD:
            self.frame_counter += 1
            if self.frame_counter >= self.CONSECUTIVE_FRAMES:
                cv2.putText(frame, "ALERT: DROWSINESS DETECTED!", (30, 40), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
        else:
            self.frame_counter = 0

        # Check for Yawning
        if mar > self.MAR_THRESHOLD:
            cv2.putText(frame, "WARNING: YAWNING DETECTED", (30, 80), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

        # Display Metrics on Screen
        cv2.putText(frame, f"EAR: {avg_ear:.2f}", (30, h_pos := frame.shape[0] - 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.putText(frame, f"MAR: {mar:.2f}", (30, h_pos + 25), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        return frame