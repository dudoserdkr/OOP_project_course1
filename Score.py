from Coin import Coin
from Tablet import Tablet






class Score:
    def __init__(self):
        self.observer_score_points = 0

    def update_score(self, new_score):
        self.observer_score_points = new_score
        print(f"Отримано оновлення score_points: {self.observer_score_points}")


