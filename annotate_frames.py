import cv2
import os
import numpy as np

def annotate_frames(frames_dir, annotated_frames_dir):
    # Create annotated frames directory if it doesn't exist
    os.makedirs(annotated_frames_dir, exist_ok=True)

    for frame_filename in os.listdir(frames_dir):
        frame_path = os.path.join(frames_dir, frame_filename)
        frame = cv2.imread(frame_path)

        # Your annotation logic here (using the example color segmentation)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_red = np.array([160, 50, 50])
        upper_red = np.array([180, 255, 255])
        mask = cv2.inRange(hsv, lower_red, upper_red)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > 100:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        annotated_frame_path = os.path.join(annotated_frames_dir, frame_filename)
        cv2.imwrite(annotated_frame_path, frame)
