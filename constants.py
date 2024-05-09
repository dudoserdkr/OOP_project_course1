settings_arr = []

with open('settings.txt', 'r') as f:
    for line in f:
        line = line.split('=')
        settings_arr += [int(line[1])]

CELL_SIZE, DELAY = settings_arr

ANIMATION_STEP_SIZE = 2
ANIMATION_STEP = CELL_SIZE // ANIMATION_STEP_SIZE  # 10

# Напишу українською, щоб всі зрозуміли, використовуємо CELL_SIZE, DELAY кратні 2