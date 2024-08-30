import customtkinter as ctk
import random
import time
from PIL import Image
from models.sound import Sound

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.widgets()
        self.title("You are an idiot!!")
        self.current_image = "white"
        self.movingfunction()
        Sound()

    def widgets(self):
        self.image = ctk.CTkImage(light_image=Image.open(r"views\image\white.jpg"), size=(320, 180))
        self.image_label = ctk.CTkLabel(self, image=self.image, text="")
        self.image_label.grid()

    def update_image(self):
        if self.current_image == "white":
            new_image = ctk.CTkImage(light_image=Image.open(r"views\image\black.jpg"), size=(320, 180))
            self.current_image = "black"
        else:
            new_image = ctk.CTkImage(light_image=Image.open(r"views\image\white.jpg"), size=(320, 180))
            self.current_image = "white"
        
        self.image_label.configure(image=new_image)
        self.image_label.image = new_image  # 参照を保持するために必要
        self.update()

    def movingfunction(self, start_x=0, start_y=0):
        self.random_grid()
        self.geometry("+%d+%d" % (start_x, start_y))
        
        if start_x > self.window_x:
            x_range = range(start_x, self.window_x, -1)
        else:
            x_range = range(start_x, self.window_x)
        
        if start_y > self.window_y:
            y_range = range(start_y, self.window_y, -1)
        else:
            y_range = range(start_y, self.window_y)
        
        x, y = start_x, start_y  # 初期値を設定
        for x, y in zip(x_range, y_range):
            self.geometry("+%d+%d" % (x, y))
            time.sleep(0.0001)
            self.update()
            if x % 100 == 0:
                self.update_image()
        self.after(1, lambda: self.movingfunction(start_x=x, start_y=y))

    def random_grid(self):
        self.window_x = random.randint(1, 1900)
        self.window_y = random.randint(1, 1000)
