from utils.generate_map import MapGenerator


def pretty_print_map(_map):
    for row in _map:
        [print(' ' if col == 0 else '█', end='') for col in row]
        print()


gr = MapGenerator(10, 15)
gr.generate()
print('TEST GENERATE 10*15')
pretty_print_map(gr.map)
