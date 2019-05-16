import ai2thor.controller
import cv2
import numpy as np

from getch import getch
from yolo_detect import yolo_detect

controller = ai2thor.controller.Controller()
controller.start()

# Kitchens: FloorPlan1 - FloorPlan30
# Living rooms: FloorPlan201 - FloorPlan230
# Bedrooms: FloorPlan301 - FloorPlan330
# Bathrooms: FloorPLan401 - FloorPlan430

controller.reset('FloorPlan3')
event = controller.step(dict(
    action='Initialize',
    gridSize=0.25,
    renderImage=True,
    renderDepthImage=True,
    renderClassImage=True,
    renderObjectImage=True
))

rotationCorner = 30

while True:
    key = getch()
    print(key)

    if key == 'q':
        break
    elif key == 'w':
        event = controller.step(dict(action='MoveAhead'))
    elif key == 'a':
        event = controller.step(dict(action='MoveLeft'))
    elif key == 's':
        event = controller.step(dict(action='MoveBack'))
    elif key == 'd':
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

    yolo_detect(event.cv2image())
