
# import tkinter as tk
from tkinter import ttk

class CustomCombobox(ttk.Combobox):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.postcommand=self.set_grab_current

    def set_grab_current(self):
        self.parent.tk.eval('tk::MakeGrab {}' .format(self.toplevel))
        # self.bind("<FocusIn>", self.on_focus_in)
        # self.bind("<FocusOut>", self.on_focus_out)

    def on_focus_in(self, event):
        self.parent.configure(background=Colors.ACTIVE_BACKGROUND)

    def on_focus_out(self, event):
        self.parent.configure(background='SystemButtonFace')



class Colors:
    BACKGROUND = "#2C3333"
    ACTIVE_BACKGROUND = "#2E4F4F"
    ACTIVE_FOREGROUND = "#0E8388"
    FOREGROUND = "#CBE4D0"
    
    BG_SHADE_1 = "#1b2222"
    BG_SHADE_2 = "#1b2232"
    BG_SHADE_3 = "#475151"
    
    FG_SHADE_1 = "#1cb9c8"
    FG_SHADE_2 = "#ffffff"
    FG_SHADE_3 = "#22c95a"
    
    LIGHT_BG = "#354040"
    LIGHT_FG = "#D2E7E0"
    
    SUCCESS = "#7CB342"
    ERROR = "#E53935"
    REMINDER = "#FB8C00"


class DarkFuturisticTheme:
        background_color = "#181818"
        text_color = "#ffffff"
        button_color = "#1cb9c8"
        button_hover_color = "#40c3d3"
        button_active_color = "#19959e"
        entry_background_color = "#232323"
        entry_text_color = "#ffffff"
        label_color = "#ffffff"
        highlight_color = "#1cb9c8"
        success_color = "#22c95a"
        warning_color = "#ffa500"
        error_color = "#ff4d4d"
        light_blue = "#1cb9c8"
        light_green = "#22c95a"
        dark_color = "#181818" 