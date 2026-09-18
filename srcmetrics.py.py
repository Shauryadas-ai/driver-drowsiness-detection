import numpy as np

def calculate_ear(eye_landmarks):
    """
    Computes the Eye Aspect Ratio (EAR) given 6 facial landmark points for an eye.
    """
    # Vertical landmark distances
    a = np.linalg.norm(eye_landmarks[1] - eye_landmarks[5])
    b = np.linalg.norm(eye_landmarks[2] - eye_landmarks[4])
    # Horizontal landmark distance
    c = np.linalg.norm(eye_landmarks[0] - eye_landmarks[3])
    
    if c == 0:
        return 0.0
    
    ear = (a + b) / (2.0 * c)
    return ear

def calculate_mar(mouth_landmarks):
    """
    Computes the Mouth Aspect Ratio (MAR) to detect yawning.
    """
    # Vertical mouth landmark distances
    a = np.linalg.norm(mouth_landmarks[1] - mouth_landmarks[7])
    b = np.linalg.norm(mouth_landmarks[2] - mouth_landmarks[6])
    c = np.linalg.norm(mouth_landmarks[3] - mouth_landmarks[5])
    # Horizontal mouth landmark distance
    d = np.linalg.norm(mouth_landmarks[0] - mouth_landmarks[4])
    
    if d == 0:
        return 0.0
    
    mar = (a + b + c) / (2.0 * d)
    return mar