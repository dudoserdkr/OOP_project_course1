import tkinter as tk

from Score import Score


class VisualScore(Score, tk.Frame):
    def __init__(self, master=None):
        Score.__init__(self)
        tk.Frame.__init__(self, master)
        self.pack(fill=tk.BOTH, expand=True)
        self.score_var = tk.StringVar(value=str(self.observer_score_points))
        self.score_label = tk.Label(self, height=2, textvariable=self.score_var, anchor="w", font=("Helvetica", 10))
        self.score_label.pack(fill=tk.BOTH, expand=True, padx=(20, 0))

    def update_score(self, new_score):
        self.score_var.set(str(new_score))

