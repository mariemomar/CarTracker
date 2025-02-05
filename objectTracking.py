import cv2 
import numpy as np
from object_detection import ObjectDetection
import math

od = ObjectDetection()  #

cap = cv2.VideoCapture('IMG_2451.MP4')
count = 0

center_points_prev_frame = []
tracking_objects = {}
track_id = 0  

ROI_Y_START = 150 

while True:
    ret, frame = cap.read()
    if not ret:
        break

    
    roi = frame[ROI_Y_START:, :]  

    center_points_current_frame = []  
    count += 1

    
    (class_ids, scores, boxes) = od.detect(roi)  

    for box in boxes:
        x, y, w, h = box
        cx = int((x + x + w) / 2)
        cy = int((y + y + h) / 2)

        
        cy += ROI_Y_START  

        center_points_current_frame.append((cx, cy))  
        cv2.rectangle(frame, (x, y + ROI_Y_START), (x + w, y + h + ROI_Y_START), (0, 255, 0), 2)

    print("Prev frame centers:", center_points_prev_frame)
    print("Current frame centers:", center_points_current_frame)

    
    if count <= 2: # the fisrt 2 frames 
        for pt in center_points_current_frame:
            for pt2 in center_points_prev_frame: 
                distance = math.hypot(pt2[0] - pt[0], pt2[1] - pt[1])
                if distance < 20:
                    tracking_objects[track_id] = pt 
                    track_id += 1
    else:
        tracking_objects_copy = tracking_objects.copy()
        center_points_current_frame_copy = center_points_current_frame.copy()
        for object_id, pt2 in tracking_objects_copy.items():
            object_exists = False 
            for pt in center_points_current_frame_copy:
                distance = math.hypot(pt2[0] - pt[0], pt2[1] - pt[1])
                if distance < 20:
                    tracking_objects[object_id] = pt
                    object_exists = True
                    if pt in center_points_current_frame:
                        center_points_current_frame.remove(pt) # the current frame now has only the objects tracked before
                    break

            if not object_exists: # if the object is not found in the current frame, remove it from the tracking objects
                tracking_objects.pop(object_id)

        # add new ids
        for pt in center_points_current_frame:
            tracking_objects[track_id] = pt
            track_id += 1

    
    for object_id, pt in tracking_objects.items():
        cv2.circle(frame, pt, 5, (0, 0, 255), -1)
        cv2.putText(frame, str(object_id), (pt[0], pt[1] - 7), 0, 1, (0, 0, 255), 2)

    print("Tracking objects:", tracking_objects)
    # print("Frame size:", frame.shape)

   
    cv2.imshow('Full Frame with ROI Tracking', frame)

    center_points_prev_frame = center_points_current_frame.copy()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# for object tracking we detect the center of the object detected and then 
# we compare its position with the next frame to see if it has moved or not
# store the current position of the object and compare it with the next frame 
# calculate the distance betweeen the point on the current frame and the point on the prev frame
# if the distance is greater than a certain threshold then the object has moved and we update the position
# hypot ( prev x - current x  , prev y - current y) = sqrt(x^2 + y^2)
