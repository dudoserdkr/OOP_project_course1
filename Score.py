






class Score:
    VISUAL_SCORE = 0
    def __init__(self):
        self.observer_score_points = 0
        self.listeners = []

    def update_score(self, new_score):
        self.observer_score_points = new_score
        print(f"Отримано оновлення score_points: {self.observer_score_points}")
        self.notify_listeners()

    def register_listener(self, listener):
        if listener not in self.listeners:
            self.listeners.append(listener)
            listener.update_score(self.observer_score_points)
    def unregister_listener(self, listener):
        self.listeners.remove(listener)

    def notify_listeners(self):
        for listener in self.listeners:
            listener.update_score(self.observer_score_points)

