import sys
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()


def say_hi():
    print("Hello")


# button = tk.Button(frame, text="Click Me", fg="red",
#                    command=say_hi)
button = tk.Button(frame,
                   text="Click Me",
                   fg="red",
                   command=lambda: print("Hello"))


button.pack(side=tk.LEFT)
root.mainloop
