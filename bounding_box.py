# -*- coding: utf-8 -*-
"""Bounding Box.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17juc3SmMlFZCGNeIwTqjVXz_Y0xRM8Wl
"""

!pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
!pip install imageai --upgrade

from imageai.Detection import VideoObjectDetection
import os
import time
import torch

# Start timing
start_time = time.time()

# Set the execution path
execution_path = os.getcwd()


def forFrame(frame_number, output_array, output_count):
    print("FOR FRAME " , frame_number)
    print("Output for each object : ", output_array)
    print("Output count for unique objects : ", output_count)
    print("------------END OF A FRAME --------------")

def forSeconds(second_number, output_arrays, count_arrays, average_output_count):
    print("SECOND : ", second_number)
    print("Array for the outputs of each frame ", output_arrays)
    print("Array for output count for unique objects in each frame : ", count_arrays)
    print("Output average count for unique objects in the last second: ", average_output_count)
    print("------------END OF A SECOND --------------")

def forMinute(minute_number, output_arrays, count_arrays, average_output_count):
    print("MINUTE : ", minute_number)
    print("Array for the outputs of each frame ", output_arrays)
    print("Array for output count for unique objects in each frame : ", count_arrays)
    print("Output average count for unique objects in the last minute: ", average_output_count)
    print("------------END OF A MINUTE --------------")



video_detector = VideoObjectDetection()
video_detector.setModelTypeAsTinyYOLOv3()
video_detector.setModelPath(os.path.join(execution_path, "tiny-yolov3.pt"))
video_detector.loadModel()

video_detector.detectObjectsFromVideo(
    input_file_path=os.path.join(execution_path, "video2.mp4"),
    output_file_path=os.path.join(execution_path, "car_yolo_tiny"),
    frames_per_second=10,
    per_second_function=forSeconds,
    per_frame_function=forFrame,
    per_minute_function=forMinute,
    minimum_percentage_probability=30
)
# End timing and calculate the duration
end_time = time.time()
execution_duration = end_time - start_time

# print("Video saved at:", output_file_path)
print("Time taken to run the code:", execution_duration, "seconds")