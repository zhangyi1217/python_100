import tkinter
import tkinter.messagebox

def main():
    flag = True
    #修改标签上的文字
    def change_label_text():
        nonlocal flag
        color, msg = ('red', 'hello,world!')\
            if flag else ('blue', 'Goodbye,world!')
        label.config(text=msg,fg=color)