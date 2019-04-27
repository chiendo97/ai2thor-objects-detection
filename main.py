from threading import Thread

import threading
import time
import cv2
import numpy as np

from getch import getch
from yolo_detect import yolo_detect

import ai2thor.controller

controller = ai2thor.controller.Controller()

controller.start()


rotationCorner = 45

input_array = []


def input():
    while True:
        input = getch()
        input_array.append(input)
        if input == 'q':
            break


def read_and_process():
    event = controller.reset('FloorPlan227')
    event = controller.step(dict(
        action='Initialize',
        gridSize=0.25,
        cameraY=0.75,
        qualitySetting='MediumCloseFitShadows',
        renderImage=True, renderDepthImage=True, renderClassImage=True, renderObjectImage=True))

    print('ready to read input')

    while True:
        if len(input_array) > 0:
            key = input_array.pop()
            del input_array[:]
            if key == 'q':
                break
            elif key == 'w':
                for _ in range(1):
                    event = controller.step(dict(action='MoveAhead'))
            elif key == 'a':
                for _ in range(1):
                    event = controller.step(dict(action='MoveLeft'))
            elif key == 's':
                for _ in range(1):
                    event = controller.step(dict(action='MoveBack'))
            elif key == 'd':
                for _ in range(1):
                    event = controller.step(dict(action='MoveRight'))
            elif key == 'h':
                y = event.metadata['agent']['rotation']['y']
                event = controller.step(
                    dict(action='Rotate', rotation=y - rotationCorner))
            elif key == 'l':
                y = event.metadata['agent']['rotation']['y']
                event = controller.step(
                    dict(action='Rotate', rotation=y + rotationCorner))
            elif key == 'j':
                event = controller.step(dict(action='LookDown'))
            elif key == 'k':
                event = controller.step(dict(action='LookUp'))
            elif key == 'r':
                cv2.imread(event.frame)
                # yolo_detect(event.frame)
                # cv2.imshow('demo', event.frame)
                # cv2.waitKey(0)


def process_image(event):
    cv2.imshow('demo', event.frame)


try:

    t = time.time()
    t1 = threading.Thread(target=input)
    t2 = threading.Thread(target=read_and_process)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('done in ', time.time() - t)

except:
    print('error')
