class Score:
    VISUAL_SCORE = 0
    observer_score_points = 0

    def __init__(self):
        self.listeners = []

    def update_score(self, new_score):
        Score.observer_score_points = new_score
        print(f"Got new score_points: {Score.observer_score_points}")
        self.notify_listeners()

    def register_listener(self, listener):
        if listener not in self.listeners:
            self.listeners.append(listener)
            listener.update_score(Score.observer_score_points)

    def notify_listeners(self):
        for listener in self.listeners:
            listener.update_score(Score.observer_score_points)
