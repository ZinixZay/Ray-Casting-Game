import math
from paths import IMAGES_PATH, WALLS_TEXTURES_PATH, SKY_TEXTURES_PATH, INTERFACE_TEXTURES_PATH, ENTITY_TEXTURES_PATH

# general
SIZE_SCREEN = WIDTH, HEIGHT = 1200, 800
HALF_WIDTH, HALF_HEIGHT = WIDTH // 2, HEIGHT // 2
DOUBLE_WIDTH, DOUBLE_HEIGHT = WIDTH * 2, HEIGHT * 2
TILE = 100
HALF_TILE = TILE//2
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
    0: WALLS_TEXTURES_PATH + 'wall0.png',
    1: WALLS_TEXTURES_PATH + 'wall1.png',
    2: WALLS_TEXTURES_PATH + 'wall2.png',
    3: WALLS_TEXTURES_PATH + 'wall3.png',
    4: WALLS_TEXTURES_PATH + 'wall4.png',
    5: WALLS_TEXTURES_PATH + 'wall5.png',
    'S': SKY_TEXTURES_PATH + 'skyf.png',
    'F': SKY_TEXTURES_PATH + 'floor.png',
}

TEXTURES_INTERFACE = {
    'interface': INTERFACE_TEXTURES_PATH + 'interface.png',
    'button': INTERFACE_TEXTURES_PATH + 'button.png',
    'active_button': INTERFACE_TEXTURES_PATH + 'active_button.png',
    'background': INTERFACE_TEXTURES_PATH + 'background.png',
    'background_pause': INTERFACE_TEXTURES_PATH + 'background_pause.png',
    'minimap_background': INTERFACE_TEXTURES_PATH + 'minimap.png',
    'player_point': INTERFACE_TEXTURES_PATH + 'player_point.png',
    'points': INTERFACE_TEXTURES_PATH + 'points.png',
    'points_background': INTERFACE_TEXTURES_PATH + 'points_background.png',
    'bullet': INTERFACE_TEXTURES_PATH + 'bullet.png',
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
WEAPON_NAME_CENTER_TEXT_POS = (MARGIN + HALF_WIDTH + 125, HEIGHT - 120 - MARGIN)
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
        'type': 'static',
        'sprites': [IMAGES_PATH+'entities\\test_entity\\default\\0.png'],
        'viewing_angles': None,
        'angle': None,
        'shift': 0.4,
        'scale': (1, 1),
        'animation': [],
        'death_animation': [],
        'animation_dist': 800,
        'animation_speed': 0,
        'blocked': False,
        'side': 20,
        'action_dist': 50,
        'heath_point': -1,
        'action_animation': [],
        'damage': 0,
        'speed': 0
    },
    'test_entity_anim': {
        'type': 'static',
        'sprites': [IMAGES_PATH+'entities\\test_entity_anim\\default\\0.png'],
        'viewing_angles': None,
        'angle': None,
        'shift': 0,
        'scale': (1, 1),
        'animation': [f'{IMAGES_PATH}entities\\test_entity_anim\\animation\\{path}.png' for path in range(4)],
        'death_animation': [],
        'animation_dist': 400,
        'animation_speed': 20,
        'blocked': True,
        'side': 100,
        'action_dist': 50,
        'heath_point': -1,
        'action_animation': [],
        'damage': 0,
        'speed': 0
    },
    'test_angle': {
        'type': 'static',
        'sprites': [f'{IMAGES_PATH}entities\\test_angle\\default\\{path}.png' for path in range(8)],
        'viewing_angles': True,
        'angle': 90,
        'shift': 0,
        'scale': (1, 1),
        'animation': [],
        'death_animation': [f'{IMAGES_PATH}entities\\test_entity_anim\\animation\\{path}.png' for path in range(4)],
        'animation_dist': 400,
        'animation_speed': 20,
        'blocked': True,
        'side': 40,
        'action_dist': 50,
        'heath_point': 100,
        'action_animation': [],
        'damage': 0,
        'speed': 0
    },
    'test_npc': {
        'type': 'npc',
        'sprites': [f'{IMAGES_PATH}entities\\test_nps\\default\\{path}.png' for path in range(8)],
        'animation': [f'{IMAGES_PATH}entities\\test_nps\\animation\\{path}.png' for path in range(4)],
        'death_animation': [f'{IMAGES_PATH}entities\\test_nps\\death\\{path}.png' for path in range(11)],
        'action_animation': [f'{IMAGES_PATH}entities\\test_nps\\action\\{path}.png' for path in range(6)],
        'viewing_angles': True,
        'angle': 0,
        'shift': 0.0,
        'scale': (0.5, 1),
        'side': 50,
        'dead_shift': 0.6,
        'animation_dist': 800,
        'animation_speed': 10,
        'action_dist': 110,
        'blocked': True,
        'heath_point': 100,
        'damage': 20,
        'speed': 2
    },
}

HEALTH_PACK = {
    'name': 'heath pack',
    'sprites': [ENTITY_TEXTURES_PATH+'heath_pack\\default\\0.png'],
    'viewing_angles': None,
    'angle': None,
    'shift': 0,
    'scale': (0, 0),
    'animation': [],
    'animation_dist': 800,
    'animation_speed': 0,
    'blocked': False,
    'side': 20,
    'heath_point': -1
}

WEAPONS_PARAM = {
    'test_weapon': {
        'name': 'SRM-8900',
        'base_sprite': IMAGES_PATH+'\\weapons\\test_weapon\\shotgun\\base\\0.png',
        'exhausted_sprite': IMAGES_PATH+'\\weapons\\test_weapon\\shotgun\\base\\1.png',
        'miniature': IMAGES_PATH+'\\weapons\\test_weapon\\miniature\\0.png',
        'numbers_bullets': 100,
        'gun_magazine': 10,
        'animation_shot': [f'{IMAGES_PATH}weapons\\test_weapon\\shotgun\\shot\\{path}.png' for path in range(10)],
        'animation_shot_speed': 4,
        'shot_length': 40,
        'damage': 55
    }
}
