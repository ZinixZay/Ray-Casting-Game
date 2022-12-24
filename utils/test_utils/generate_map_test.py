from utils.generate_map import MapGenerator


def pretty_print_map(_map):
    for row in _map:
        for col in row:
            if col == 0:
                print(' ', end='')
            elif col == 5:
                print('@', end='')
            else:
                print('█', end='')
        print()


gr = MapGenerator(16, 24)
gr.generate()
print('TEST GENERATE 10*15')
pretty_print_map(gr.map)
