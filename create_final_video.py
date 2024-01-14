import cv2
import os

def create_final_video(annotated_frames_dir, output_video_path):
    frames = []
    for frame_filename in sorted(os.listdir(annotated_frames_dir)):
        frame_path = os.path.join(annotated_frames_dir, frame_filename)
        frame = cv2.imread(frame_path)
        frames.append(frame)

    height, width, _ = frames[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, 20.0, (width, height))

    for frame in frames:
        out.write(frame)

    out.release()
