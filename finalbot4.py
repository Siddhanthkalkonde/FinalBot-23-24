import cv2
import argparse
import numpy as np
from ultralytics import YOLO
from realsense_depth import *
import supervision as sv
import math
from finalbot_arduino import *
import time

motor_controller = Cytron_driver()

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="YOLOv8 live")
    parser.add_argument(
        "--webcam-resolution",
        default=[700, 700],
        nargs=2,
        type=int
    )
    args = parser.parse_args()
    return args

def find_average_rgb(image, detections):
    boxes = detections.xyxy[:, :4].astype(int)
    average_rgb_values = [] 
    
    for box in boxes:
        roi = image[box[1]:box[3], box[0]:box[2]]
        average_rgb = np.mean(roi, axis=(0, 1))
        average_rgb_values.append(average_rgb)

    return np.mean(average_rgb_values, axis=0)

def count_bounding_boxes(detections):
    boxes = detections.xyxy[:, :4].astype(int)
    return int(len(boxes))

def get_color_region(x, width):
    third_width = width // 3
    if 0 <= x < third_width:
        return "Blue"
    elif third_width <= x < 2 * third_width:
        return "Green"
    else:
        return "Red"

def calculate_midpoint(box):
    x1, y1, x2, y2 = box
    return ((x1 + x2) // 2, (y1 + y2) // 2)

def track_closest_object(frame, model, box_annotator, depth_frame):
    result = model(frame)[0]
    detections = sv.Detections.from_yolov8(result)

    frame = box_annotator.annotate(
        scene=frame,
        detections=detections,
    )

    closest_distance = float('inf')
    closest_box = None
    closest_box_midpoint = None

    for box in detections.xyxy[:, :4].astype(int):
        box_center_x = (box[0] + box[2]) // 2
        color_region = get_color_region(box_center_x, frame.shape[1])
        print(f"Object detected in the {color_region} region")

        # Calculate the midpoint of the bounding box
        box_midpoint = calculate_midpoint(box)
        print("Midpoint of bounding box:", box_midpoint)

        # Calculate distance from the midpoint using depth information
        distance = depth_frame[box_midpoint[1], box_midpoint[0]]
        print(f"Distance: {distance}")

        # Check if this object is closer than the previously tracked closest object
        if distance < closest_distance:
            closest_distance = distance
            closest_box = box
            closest_box_midpoint = box_midpoint

    if closest_box is not None:
        # Perform movement control based on the closest object
        angle = calculate_angle(frame, closest_box_midpoint)
        print("Angle =", angle)

        if angle > 15:
            motor_controller.angle_M(0, 0.3)  # Rotate right
        elif angle < -15:
            motor_controller.angle_M(1, 0.3)  # Rotate left
        elif -15 <= angle <= 15:
            motor_controller.forward(0.3)  # Move forward
        else:
            motor_controller.stop(0)  # Stop if the angle logic doesn't satisfy

        # Display annotations on the frame
        draw_annotations(frame, closest_box_midpoint, closest_distance, angle)

    return frame


def perform_detection(frame, model, box_annotator, depth_frame):
    result = model(frame)[0]
    detections = sv.Detections.from_yolov8(result)

    frame = box_annotator.annotate(
        scene=frame,
        detections=detections,
    )

    global num_boxes
    num_boxes = count_bounding_boxes(detections)
    print("Number of Bounding Boxes:", num_boxes)

    height, width, _ = frame.shape
   
    third_width = width // 3

    # Draw Cartesian plane with unit markings
    draw_cartesian_plane(frame)

    for box in detections.xyxy[:, :4].astype(int):
        box_center_x = (box[0] + box[2]) // 2
        color_region = get_color_region(box_center_x, width)
        print(f"Object detected in the {color_region} region")

        color_code = 0 if color_region == 'Green' else 1 if color_region == 'Blue' else 2

        box_midpoint = calculate_midpoint(box)
        print("Midpoint of bounding box:", box_midpoint)




        
        angle = calculate_angle(frame , box_midpoint)
        print("Angle = ", angle)

        if num_boxes > 0 :
            turn =0
            motor_controller.move_trigno(0.3 , turn , angle + 3.1413/4)
        else : 
            turn = 1
            motor_controller.move_trigno(0.126 , turn , angle + 3.1413/4)

        # Calculate distance from origin to midpoint
        distance_to_midpoint = calculate_distance(point, box_midpoint)
        print("mid point distance: " , distance_to_midpoint)


                # Calculate distance from the midpoint using depth information
        distance = depth_frame[box_midpoint[1], box_midpoint[0]]
        print(f"Distance: {distance}")
        if distance<650:
            motor_controller.ir_in()
            
            

         
        # Draw line from origin to midpoint if distance is less than threshold (e.g., 100 pixels)
        if distance_to_midpoint < 100:
            plot_line_from_origin(frame, box_midpoint)
        if distance_to_midpoint< 400:
            motor_controller.stop(0)

        
        # Display the distance and angle on the frame
        cv2.putText(frame, "{:.2f}mm".format(distance_to_midpoint), (box_midpoint[0], box_midpoint[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
        cv2.putText(frame, "{:.2f} degrees".format(angle), (box_midpoint[0], box_midpoint[1] + 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

    # Draw a red circle at the reference point
    cv2.circle(frame, point, 4, (0, 0, 255), -1)

    # Calculate distance from the reference point using depth information
    distance = depth_frame[point[1], point[0]]
    print("distance : ", distance)

    # Display the distance of the reference point on the frame
    cv2.putText(frame, "{}mm".format(distance), (point[0], point[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

    cv2.line(frame, (third_width, 0), (third_width, height), (255, 0, 0), 2)  # Blue
    cv2.line(frame, (2 * third_width, 0), (2 * third_width, height), (0, 255, 0), 2)  # Green

    return frame


def draw_annotations(frame, midpoint, distance, angle):
    # Draw line from origin to midpoint
    plot_line_from_origin(frame, midpoint)

    # Draw circle at the midpoint of the bounding box
    cv2.circle(frame, midpoint, 4, (0, 255, 0), -1)

    # Display the distance and angle on the frame
    cv2.putText(frame, "{:.2f}mm".format(distance), (midpoint[0], midpoint[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2,
                (0, 0, 0), 2)
    cv2.putText(frame, "{:.2f} degrees".format(angle), (midpoint[0], midpoint[1] + 20), cv2.FONT_HERSHEY_PLAIN, 2,
                (0, 0, 0), 2)

def calculate_angle(frame, midpoint):
    # Calculate the angle between the y-axis and the line from origin to the midpoint
    origin_x, origin_y = frame.shape[1] // 2, frame.shape[0] - 1
    angle_radians = math.atan2(origin_x - midpoint[0], origin_y - midpoint[1])
    angle_degrees = math.degrees(angle_radians)
    return angle_degrees

def plot_line_from_origin(frame, midpoint):
    # Draw a line from origin to the midpoint
    height, width, _ = frame.shape
    origin = (width // 2, height)
    cv2.line(frame, origin, midpoint, (255, 0, 0), 2)

def get_quadrant(midpoint):
    x, y = midpoint
    # Check the x and y coordinates of the midpoint to determine the quadrant
    if x >= 320 and y >= 240:
        return "First Quadrant"
    elif x < 320 and y >= 240:
        return "Second Quadrant"
    elif x < 320 and y < 240:
        return "Third Quadrant"
    else:
        return "Fourth Quadrant"

def detection_output():
    args = parse_arguments()
    frame_width, frame_height = args.webcam_resolution

    dc = DepthCamera()

    model = YOLO("/home/sid/trial/trained_models/V82.pt")
    
    box_annotator = sv.BoxAnnotator(
        thickness=2,
        text_thickness=2,   
        text_scale=1
    )

    while True:
        ret, depth_frame, color_frame = dc.get_frame()

        color_frame = track_closest_object(color_frame, model, box_annotator, depth_frame)
        
        cv2.imshow("detections", color_frame)
        # cv2.imshow("depth", depth_frame)

        if (cv2.waitKey(30) == 27):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    detection_output()
