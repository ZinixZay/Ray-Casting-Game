import pygame

from paths import IMAGES_PATH

ENTITIES_PARAM = {
    'test_entity': {
        'sprite': IMAGES_PATH+'entities\\test_entity\\default\\0.png',
        'viewing_angles': None,
        'shift': 0.4,
        'scale': 1,
        'animation': [],
        'animation_dist': 800,
        'animation_speed': 0,
        'blocked': True,
    },
    'test_entity_anim': {
        'sprite': IMAGES_PATH+'entities\\test_entity_anim\\default\\0.png',
        'viewing_angles': None,
        'shift': 0,
        'scale': 1,
        'animation': [f'{IMAGES_PATH}entities\\test_entity_anim\\animation\\{path}.png' for path in range(4)],
        'animation_dist': 400,
        'animation_speed': 20,
        'blocked': True,
    },
    'test_angle': {
        'sprite': [f'{IMAGES_PATH}entities\\test_angle\\default\\{path}.png' for path in range(8)],
        'viewing_angles': True,
        'shift': 0,
        'scale': 1,
        'animation': [],
        'animation_dist': 400,
        'animation_speed': 20,
        'blocked': True,
    }
}
