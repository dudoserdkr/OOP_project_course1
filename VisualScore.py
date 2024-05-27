import tkinter as tk
from PIL import ImageTk, Image


from Score import Score


class VisualScore(Score, tk.Frame):
    def __init__(self, master=None):
        Score.__init__(self)
        tk.Frame.__init__(self, master)
        self.pack(fill=tk.BOTH, expand=True)
        self.score_var = tk.StringVar(value=str(self.observer_score_points))

        self.score_label = tk.Label(self, height=1, textvariable=self.score_var, anchor="w", font=("Helvetica", 10))
        self.score_label.pack(fill=tk.BOTH, expand=True, padx=(20, 0))

    def image_chooser(self, photo):
        photo_normal = photo.resize((110, 40), Image.Resampling.LANCZOS)
        self.photo_normal_tk = ImageTk.PhotoImage(photo_normal)
        image_label = tk.Label(self, image=self.photo_normal_tk)
        image_label.pack(side=tk.RIGHT, padx=(0, 20))
        image_label.image = self.photo_normal_tk

    def update_score(self, new_score):
        self.score_var.set(str(new_score))
