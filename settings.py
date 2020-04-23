import math

## Geometry
NODE_SIZE = 0.002  # (NODE = NODE_SIZE * NODE_SIZE * THICKNESS)
THICKNESS = 0.002

CANVAS_SIZE_X = 0.5
CANVAS_SIZE_Y = 0.5

# CANVAS_SIZE_X = 0.1
# CANVAS_SIZE_Y = 0.5

# Constraints
MAX_FIN_NODE = 7150

TIME = 0.2
TIME_SLICE = 0.002

# For steady
MAX_ERROR_TOLERANCE = 0.01

# For transient
ANIMATION_FRAME_MILLISECOND = 10

# Resize
CXN = math.ceil(CANVAS_SIZE_X / NODE_SIZE)
CYN = math.ceil(CANVAS_SIZE_Y / NODE_SIZE)
TN = math.ceil(TIME / TIME_SLICE)
CANVAS_SIZE_X = CXN * NODE_SIZE
CANVAS_SIZE_Y = CYN * NODE_SIZE
TIME = TN * TIME_SLICE

## Heat transfer coefficient
h = 3.4785

# Copper
k = 401
rho = 8944
cp = 376.812

## Temperatures
T_inf = 17.955
T_base = 35.13


A_base = 0.002 * 0.1
