import os


current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'settings.txt')


settings_arr = []

with open(file_path, 'r') as f:
    for line in f:
        line = line.split('=')
        settings_arr += [int(line[1])]

CELL_SIZE, DELAY = settings_arr

ANIMATION_STEP_SIZE = CELL_SIZE // 10
ANIMATION_STEP = CELL_SIZE // ANIMATION_STEP_SIZE  # 10

# Напишу українською, щоб всі зрозуміли, використовуємо CELL_SIZE, DELAY кратні 2