import tkinter as tk
from PIL import ImageTk, Image


from Score import Score
from constants import CELL_SIZE

class VisualScore(Score, tk.Frame):
    def __init__(self, master=None):
        Score.__init__(self)
        tk.Frame.__init__(self, master)
        self.pack(fill=tk.BOTH, expand=True)
        self.score_var = tk.StringVar(value=str(self.observer_score_points))
        self.photo = Image.open("pictures/three_pacmans_first.png")
        self.photo_normal = self.photo.resize((100, 40), Image.Resampling.LANCZOS)
        self.photo_normal_tk = ImageTk.PhotoImage(self.photo_normal)
        self.score_label = tk.Label(self, height=2, textvariable=self.score_var, anchor="w", font=("Helvetica", 10))
        self.score_label.pack(fill=tk.BOTH, expand=True, padx=(20, 0), pady=(30, 0))
        self.image_label = tk.Label(self, image=self.photo_normal_tk)
        self.image_label.pack(side=tk.RIGHT, padx=(0, 20))

    def update_score(self, new_score):
        self.score_var.set(str(new_score))
