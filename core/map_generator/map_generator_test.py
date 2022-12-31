from map_generator import MapGenerator


def pretty_print_map(_map):
    for row in _map:
        for col in row:
            if col == 0:
                print(' ', end='')
            else:
                print('█', end='')
        print()


gr = MapGenerator(24, 11)
gr.generate()
print('TEST GENERATE 24*16')
pretty_print_map(gr.map)