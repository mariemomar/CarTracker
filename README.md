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

## Usage
1. Ensure you have the required YOLO model files.
2. Run the script:
```bash
python objectTracking.py
```
3. Press 'q' to exit the video.



