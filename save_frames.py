import cv2
import os

def save_frames(input_video_path, frames_dir):
    # Create frames directory if it doesn't exist
    os.makedirs(frames_dir, exist_ok=True)

    cap = cv2.VideoCapture(input_video_path)
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_path = os.path.join(frames_dir, f'frame_{frame_count:04d}.jpg')
        cv2.imwrite(frame_path, frame)

        frame_count += 1

    cap.release()
