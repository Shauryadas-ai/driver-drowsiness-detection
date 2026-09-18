import cv2
import numpy as np
import mediapipe as mp

class DrowsinessDetector:
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        
        # Landmark indices for Left Eye, Right Eye, and Mouth
        self.LEFT_EYE_IDX = [362, 385, 387, 263, 373, 380]
        self.RIGHT_EYE_IDX = [33, 160, 158, 133, 153, 144]
        self.MOUTH_IDX = [61, 81, 13, 312, 291, 402, 14, 178]

    def process_frame(self, frame):
        h, w, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_frame)
        
        if not results.multi_face_landmarks:
            return None, None, None
        
        landmarks = results.multi_face_landmarks[0].landmark
        
        # Extract pixel coordinates
        left_eye = np.array([(landmarks[idx].x * w, landmarks[idx].y * h) for idx in self.LEFT_EYE_IDX])
        right_eye = np.array([(landmarks[idx].x * w, landmarks[idx].y * h) for idx in self.RIGHT_EYE_IDX])
        mouth = np.array([(landmarks[idx].x * w, landmarks[idx].y * h) for idx in self.MOUTH_IDX])
        
        return left_eye, right_eye, mouth