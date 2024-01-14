
# Mini DRS

This project is designed for cricket enthusiasts, developers, and computer vision enthusiasts interested in understanding and implementing a basic cricket ball tracking system using computer vision techniques. The project provides a modularized approach to the process, allowing users to save frames from an input video, annotate frames by detecting a cricket ball, and create a final video with annotated frames.

Who It's For:

- Cricket Enthusiasts: Individuals interested in exploring computer vision applications in cricket analysis and ball tracking.
- Developers: Those looking to understand and implement computer vision concepts, especially related to object detection in sports scenarios.
- Computer Vision Enthusiasts: Individuals keen on experimenting with basic computer vision techniques and exploring their applications in real-world scenarios.
Note: The project serves as a starting point and can be extended for more sophisticated ball tracking applications with additional enhancements and optimizations.


## Features

- Frame Extraction: Save frames from the input video to analyze and process individual frames.
- Ball Annotation: Utilize color segmentation and contour detection to annotate frames by identifying and marking the cricket ball.
- Final Video Creation: Compile annotated frames into a final video, providing a visual representation of ball tracking.




## Cloning the repo

```bash
  git clone https://github.com/Samarth11203/Mini_DRS.git
```
```bash
  cd Mini_DRS
```
## Install Dependencies

```bash
  pip install -r requirements.txt
```
## Run the main script

```bash
  python main.py
```

This script will perform the following steps:

- Save frames from the input video (input_1.mp4) to the frames directory.
- Annotate frames by detecting the cricket ball and save them to the annotated_frames directory.
- Create the final video (output_video.mp4) using the annotated frames.
## Notes

- This is a basic example, and you may need to fine-tune the parameters based on your specific video and cricket ball characteristics.
- Feel free to customize the code to enhance the accuracy of ball detection.
## Customization

- To use your own input video, replace `input_1.mp4` with your video file in `main.py`.
- Adjust the color segmentation parameters for ball detection in `annotate_frames.py` based on your cricket ball color.
