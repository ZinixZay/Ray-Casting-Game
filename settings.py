import math

SIZE_SCREEN = WIDTH, HEIGHT = 1200, 800
HALF_WIDTH, HALF_HEIGHT = WIDTH // 2, HEIGHT // 2
DOUBLE_WIDTH, DOUBLE_HEIGHT = WIDTH * 2, HEIGHT * 2
TILE = 100
FPS = 60
SENSITIVITY = 0.002


FOV = math.pi / 4
HALF_FOV = FOV / 2
NUM_RAYS = 400
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 2.8 * DIST * TILE
SCALE = WIDTH // NUM_RAYS
DOUBLE_PI = math.pi * 2

TEXTURE_WIDTH, TEXTURE_HEIGHT = 1200, 1200
HALF_TEXTURE_HEIGHT = TEXTURE_HEIGHT // 2
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

WORLD_WIDTH, WORLD_HEIGHT = 24, 16

# WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# RED = (220, 0, 0)
# GREEN = (0, 80, 0)
# BLUE = (0, 0, 255)
DARK_GRAY = (12, 12, 12)
# PURPLE = (120, 0, 120)
# SKY_BLUE = (0, 186, 255)
# YELLOW = (220, 220, 0)
