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


def read_and_process():
    event = controller.reset('FloorPlan227')
    event = controller.step(dict(
        action='Initialize',
        gridSize=0.25,
        # cameraY=0.75,
        # qualitySetting='MediumCloseFitShadows',
        # renderImage=True,
        renderDepthImage=True,
        renderClassImage=True,
        renderObjectImage=True
    ))

    while True:
        key = getch()

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
            frame = event.cv2image()
            cv2.imwrite('sense.jpg', frame)
            image = cv2.imread('sense.jpg')
            cv2.imshow("object detection", image)
            cv2.waitKey()


if __name__ == '__main__':

    read_and_process()
