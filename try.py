from tkinter import *

def redraw_line(event):
    width = event.width
    height = event.height
    canvas = event.widget
    # print(width)
    # print(height)
    # print(canvas)
    canvas.coords("diagonal", 0, 0, width, 0)

root=Tk()
for x in range(10):
    for y in range(10):
        canvas=Canvas(root, width='15',height='15',highlightthickness=0,bg='red')                      
        canvas.bind("<Configure>", redraw_line)
        # coordinates are irrelevant; they will change as soon as
        # the widget is mapped to the screen.
        canvas.create_line(0,0,0,0, tags=("diagonal",))
        canvas.grid(row=y,column=x,sticky='NESW')

for x in range(10):
    for y in range(10):
        root.columnconfigure(x,weight=1)
        root.rowconfigure(y,weight=1)


root.mainloop()