import math

## Geometry
NODE_SIZE = 0.01  # (NODE = NODE_SIZE * NODE_SIZE * THICKNESS)
THICKNESS = 1

CANVAS_SIZE_X = 0.5
CANVAS_SIZE_Y = 1

TIME = 0.3
TIME_SLICE = 0.001

# Resize
CXN = math.ceil(CANVAS_SIZE_X / NODE_SIZE)
CYN = math.ceil(CANVAS_SIZE_Y / NODE_SIZE)
TN = math.ceil(TIME / TIME_SLICE)
CANVAS_SIZE_X = CXN * NODE_SIZE
CANVAS_SIZE_Y = CYN * NODE_SIZE
TIME = TN * TIME_SLICE

## Heat transfer coefficient
h = 10
k = 5
rho = 20
cp = 10

## Temperatures
T_inf = 25
T_base = 60
