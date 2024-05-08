settings_arr = []

with open('settings.txt', 'r') as f:
    for line in f:
        line = line.split('=')
        settings_arr += [int(line[1])]

CELL_SIZE, DELAY = settings_arr
