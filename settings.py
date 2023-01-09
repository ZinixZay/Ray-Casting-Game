import math
from paths import IMAGES_PATH

# general
SIZE_SCREEN = WIDTH, HEIGHT = 1200, 800
HALF_WIDTH, HALF_HEIGHT = WIDTH // 2, HEIGHT // 2
DOUBLE_WIDTH, DOUBLE_HEIGHT = WIDTH * 2, HEIGHT * 2
TILE = 100
FPS = 60
SENSITIVITY = 0.002

# ray casting
FOV = math.pi / 4
HALF_FOV = FOV / 2
NUM_RAYS = 400
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 2.8 * DIST * TILE
SCALE = WIDTH // NUM_RAYS
DOUBLE_PI = math.pi * 2
CENTER_RAY = NUM_RAYS // 2 - 1
FAKE_RAYS = 100
FAKE_RAYS_RANGE = NUM_RAYS - 1 + 2 * FAKE_RAYS

# map
WORLD_SIZE = WORLD_WIDTH, WORLD_HEIGHT = 27, 18
WORLD_SIZE_TILE = WORLD_WIDTH_TILE, WORLD_HEIGHT_TILE = WORLD_WIDTH * TILE, WORLD_HEIGHT * TILE

# map generator
GENERATE_RATE = {
    1: 28,
    2: 28,
    3: 28,
    4: 8,
    5: 8,
}
INTENSIVE = 15

# textures
TEXTURE_WIDTH, TEXTURE_HEIGHT = 1200, 1200
HALF_TEXTURE_HEIGHT = TEXTURE_HEIGHT // 2
TEXTURE_SCALE = TEXTURE_WIDTH // TILE
TEXTURES = {
    0: IMAGES_PATH + '\\walls\\wall0.png',
    1: IMAGES_PATH + '\\walls\\wall1.png',
    2: IMAGES_PATH + '\\walls\\wall2.png',
    3: IMAGES_PATH + '\\walls\\wall3.png',
    4: IMAGES_PATH + '\\walls\\wall4.png',
    5: IMAGES_PATH + '\\walls\\wall5.png',
    'S': IMAGES_PATH + '\\sky\\skyf.png',
    'F': IMAGES_PATH + '\\sky\\floor.png',
}

TEXTURES_INTERFACE = {
    'interface': IMAGES_PATH + '\\interface\\interface.png',
    'button': IMAGES_PATH + '\\interface\\button.png',
    'active_button': IMAGES_PATH + '\\interface\\active_button.png',
    'background': IMAGES_PATH + '\\interface\\background.png',
    'minimap_background': IMAGES_PATH + '\\interface\\minimap.png',
    'player_point': IMAGES_PATH + '\\interface\\player_point.png',
    'points': IMAGES_PATH + '\\interface\\points.png',
    'points_background': IMAGES_PATH + '\\interface\\points_background.png',
    'bullet': IMAGES_PATH + '\\interface\\bullet.png',
}

# drawing
MARGIN = 10
MINIMAP_SIZE = MINIMAP_WIDTH, MINIMAP_HEIGHT = 190, 206
HALF_MINIMAP_WIDTH, HALF_MINIMAP_HEIGHT = MINIMAP_WIDTH//2, MINIMAP_HEIGHT//2
GAMEINFO_SIZE = GAMEINFO_WIDTH, GAMEINFO_HEIGHT = 440, 217
MINIMAP_TILE = 20
MINIMAP_SCALE = TILE // MINIMAP_TILE
MINIMAP_POS = (MARGIN+6, HEIGHT-220-MARGIN+6)
GAMEINFO_POS = (WIDTH-MARGIN-440, HEIGHT-220-MARGIN)
FPS_POS = (MARGIN, GAMEINFO_HEIGHT-26)
HEALTH_POINTS_POS = (MARGIN + 385, HEIGHT - 100 - MARGIN)
HEALTH_POINTS_TEXT_POS = (MARGIN + 385, HEIGHT - 120 - MARGIN)
ARMOR_POINTS_POS = (MARGIN + 445, HEIGHT - 45 - MARGIN)
ARMOR_POINTS_TEXT_POS = (MARGIN + 445, HEIGHT - 65 - MARGIN)
WEAPON_BULLET_POS = (MARGIN + HALF_WIDTH + 76, HEIGHT - 95 - MARGIN)
WEAPON_NAME_TEXT_POS = (MARGIN + HALF_WIDTH + 56, HEIGHT - 120 - MARGIN)
WEAPON_BULLET_NUMBER_POS = (MARGIN + HALF_WIDTH + 104, HEIGHT - 88 - MARGIN)


MAP_WALLS_COLOR = (71, 231, 255, 80)
INTERFACE_COLOR = (24, 27, 33)
EMPTY_COLOR = (0, 0, 0, 0)
BLACK = (0, 0, 0)
DARK_GRAY = (12, 12, 12)
LIGHT_GRAY = (182, 182, 180)
LIGHT_GRAY2 = (232, 232, 230)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 80, 0)
PURPLE = (120, 0, 120)
SKY_BLUE = (0, 186, 255)
YELLOW = (220, 220, 0)

# entities
ENTITIES_PARAM = {
    'test_entity': {
        'sprites': [IMAGES_PATH+'entities\\test_entity\\default\\0.png'],
        'viewing_angles': None,
        'angle': None,
        'shift': 0.4,
        'scale': 1,
        'animation': [],
        'animation_dist': 800,
        'animation_speed': 0,
        'blocked': False,
        'side': 20
    },
    'test_entity_anim': {
        'sprites': [IMAGES_PATH+'entities\\test_entity_anim\\default\\0.png'],
        'viewing_angles': None,
        'angle': None,
        'shift': 0,
        'scale': 1,
        'animation': [f'{IMAGES_PATH}entities\\test_entity_anim\\animation\\{path}.png' for path in range(4)],
        'animation_dist': 400,
        'animation_speed': 20,
        'blocked': True,
        'side': 100
    },
    'test_angle': {
        'sprites': [f'{IMAGES_PATH}entities\\test_angle\\default\\{path}.png' for path in range(8)],
        'viewing_angles': True,
        'angle': 90,
        'shift': 0,
        'scale': 1,
        'animation': [],
        'animation_dist': 400,
        'animation_speed': 20,
        'blocked': True,
        'side': 40
    }
}
