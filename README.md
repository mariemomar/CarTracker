# CarTracker

CarTracker is a simple vehicle tracking system that detects and tracks cars on the road using computer vision. It assigns unique IDs to vehicles and monitors their movement within a selected region of interest (ROI).

## Features
- Detects vehicles using YOLO
- Tracks vehicles and assigns unique IDs
- Focuses tracking on a specific ROI while displaying the full frame

## Requirements
- Python 3
- OpenCV
- YOLO model files

## Installation
```bash
pip install opencv-python numpy
```
download the yolov4.weights file by clicking the link
[download yolov4.weights](https://objects.githubusercontent.com/github-production-release-asset-2e65be/75388965/749e43d0-8605-436f-b26c-12ee01c2a265?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20250205%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250205T015847Z&X-Amz-Expires=300&X-Amz-Signature=9dee1d5bde22b83771c886f84c3248d87723e32d9a2e91c5f989166eedfe717f&X-Amz-SignedHeaders=host&response-content-disposition=attachment%3B%20filename%3Dyolov4.weights&response-content-type=application%2Foctet-stream)

and move it to the directory dnn_models

## Usage
1. Ensure you have the required YOLO model files.
2. Run the script:
```bash
python objectTracking.py
```
3. Press 'q' to exit the video.



