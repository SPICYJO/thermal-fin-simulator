import math

## Geometry
NODE_SIZE = 0.1
THICKNESS = 0.1

CANVAS_SIZE_X = 100
CANVAS_SIZE_Y = 100

TIME = 100
TIME_SLICE = 0.1

# Resize
CXN = math.ceil(CANVAS_SIZE_X / NODE_SIZE)
CYN = math.ceil(CANVAS_SIZE_Y / NODE_SIZE)
TN = math.ceil(CANVAS_SIZE_X / NODE_SIZE)
CANVAS_SIZE_X = CXN * NODE_SIZE
CANVAS_SIZE_Y = CYN * NODE_SIZE
TIME = TN * TIME_SLICE

## Heat transfer coefficient
h = 10
k = 5