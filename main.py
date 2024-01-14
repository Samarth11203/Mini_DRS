import os
from save_frames import save_frames
from annotate_frames import annotate_frames
from create_final_video import create_final_video

def main():
    # Input video path
    input_video_path = 'input_1.mp4'

    # Directory paths
    frames_dir = 'frames/'
    annotated_frames_dir = 'annotated_frames/'
    output_video_path = 'output_video.mp4'

    # Step 1: Save frames from the input video
    print("Saving the frames from the given input video.")
    save_frames(input_video_path, frames_dir)
    print("Frames saved in the folder './frames'.")

    # Step 2: Annotate frames
    print("Saving the annotated frames.")
    annotate_frames(frames_dir, annotated_frames_dir)
    print("Annotated frames saved in the folder './annotated_frames'")

    # Step 3: Create final video
    print("Creating the final output video")
    create_final_video(annotated_frames_dir, output_video_path)
    print("Output video created by the name output_video.mp4")

    # Optional: Clean up temporary directories
    # Uncomment the following lines if you want to delete the frames and annotated_frames directories
    # os.rmdir(frames_dir)
    # os.rmdir(annotated_frames_dir)

if __name__ == "__main__":
    main()
