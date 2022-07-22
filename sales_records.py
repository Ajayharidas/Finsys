from tkinter import *
import tkinter as tk
from tkinter import ttk
from turtle import width,color



root = Tk()
root.title('Finsys - Sales Records')
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" %(width,height))
s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook.Tab',background="#999999",width=20,padding=10)


# class HoverButton(tk.Button):
#     def __init__(self, master, **kw):
#         tk.Button.__init__(self,master=master,**kw)
#         self.defaultBackground = self["background"]
#         self.bind("<Enter>", self.on_enter)
#         self.bind("<Leave>", self.on_leave)

#     def on_enter(self, e):
#         self['background'] = self['activebackground']

#     def on_leave(self, e):
#         self['background'] = self.defaultBackground


sr_Frame = Frame(root,width=1325,height=800)
sr_Frame.pack(expand=True,fill=BOTH)
sr_Frame.place(x=2,y=0)
sr_Canvas = Canvas(sr_Frame,bg='#2f516f',width=1325,height=800,scrollregion=(0,0,700,1200))

sr_Scroll = Scrollbar(sr_Frame,orient=VERTICAL)
sr_Scroll.pack(side=RIGHT,fill=Y)
sr_Scroll.config(command=sr_Canvas.yview)
sr_Canvas.config(width=1325,height=720)

sr_Canvas.config(yscrollcommand=sr_Scroll.set)
sr_Canvas.pack(expand=True,side=LEFT,fill=BOTH)

def header_rectangle(x1,y1,x2,y2,radius=25,**kwargs):
    points = [x1+radius,y1,
    x1+radius,y1,
    x2-radius,y1,
    x2-radius,y1,
    x2,y1,
    x2,y1+radius,
    x2,y1+radius,
    x2,y2-radius,
    x2,y2-radius,
    x2,y2,
    x2-radius,y2,
    x2-radius,y2,
    x1+radius,y2,
    x1+radius,y2,
    x1,y2,
    x1,y2-radius,
    x1,y2-radius,
    x1,y1+radius,
    x1,y1+radius,
    x1,y1]
    return sr_Canvas.create_polygon(points,**kwargs,smooth=True)



sr_rectangle1 = header_rectangle(20,50,1300,200,radius=20,fill="#1b3857")
sr_label = Label(sr_Canvas,width=15,height=1,text="SALES RECORDS",font=('arial 25'),background="#1b3857",fg="white")
sr_label_win = sr_Canvas.create_window(550,85,anchor="nw",window=sr_label)
sr_Canvas.create_line(60,150,1260,150,fill='gray',width=1)

sr_rectangle2 = header_rectangle(20,250,1300,600,radius=20,fill="#1b3857")

sr_Canvas.create_line(40, 350, 1280, 350, fill='gray',width=1)
sr_Canvas.create_line(40, 350, 40, 400, fill='gray',width=1)
sr_Canvas.create_line(160, 350, 160, 400, fill='gray',width=1)
sr_Canvas.create_line(310, 350, 310, 400, fill='gray',width=1)
sr_Canvas.create_line(430, 350, 430, 400, fill='gray',width=1)
sr_Canvas.create_line(590, 350, 590, 400, fill='gray',width=1)
sr_Canvas.create_line(710, 350, 710, 400, fill='gray',width=1)
sr_Canvas.create_line(840, 350, 840, 400, fill='gray',width=1)
sr_Canvas.create_line(970, 350, 970, 400, fill='gray',width=1)
sr_Canvas.create_line(1060, 350, 1060, 400, fill='gray',width=1)
sr_Canvas.create_line(1190, 350, 1190, 400, fill='gray',width=1)
sr_Canvas.create_line(1280, 350, 1280, 400, fill='gray',width=1)
sr_Canvas.create_line(40, 400, 1280, 400, fill='gray',width=1)

srt_label1 = Label(sr_Canvas,width=10,height=1,text="DATE", font=('arial 10'),background="#1b3857",fg="white") 
srt_winlabel1 = sr_Canvas.create_window(100, 365, anchor="c", window=srt_label1)
srt_label2 = Label(sr_Canvas,width=11,height=1,text="TYPE", font=('arial 10'),background="#1b3857",fg="white") 
srt_winlabel2 = sr_Canvas.create_window(235, 365, anchor="c", window=srt_label2)
srt_label3 = Label(sr_Canvas,width=11,height=1,text="NO.", font=('arial 10'),background="#1b3857",fg="white") 
srt_winlabel3 = sr_Canvas.create_window(370, 365, anchor="c", window=srt_label3)
srt_label4 = Label(sr_Canvas,width=11,height=1,text="CUSTOMER", font=('arial 10'),background="#1b3857",fg="white") 
srt_winlabel4 = sr_Canvas.create_window(510, 365, anchor="c", window=srt_label4)
srt_label5 = Label(sr_Canvas,width=11,height=1,text="DUE DATE", font=('arial 10'),background="#1b3857",fg="white") 
srt_winlabel5 = sr_Canvas.create_window(650, 365, anchor="c", window=srt_label5)
srt_label6 = Label(sr_Canvas,width=11,height=1,text="BALANCE", font=('arial 10'),background="#1b3857",fg="white") 
srt_winlabel6 = sr_Canvas.create_window(775, 365, anchor="c", window=srt_label6)
srt_label7 = Label(sr_Canvas,width=12,height=1,text="TOTAL BEFORE", font=('arial 10'),background="#1b3857",fg="white") 
srt_winlabel7 = sr_Canvas.create_window(905, 365, anchor="c", window=srt_label7)
srt_label8 = Label(sr_Canvas,width=10,height=1,text="TAX", font=('arial 10'),background="#1b3857",fg="white") 
srt_winlabel8 = sr_Canvas.create_window(1015, 365, anchor="c", window=srt_label8)
srt_label9 = Label(sr_Canvas,width=11,height=1,text="TOTAL", font=('arial 10'),background="#1b3857",fg="white") 
srt_winlabel9 = sr_Canvas.create_window(1125, 365, anchor="c", window=srt_label9)
srt_label10 = Label(sr_Canvas,width=10,height=1,text="ACTION", font=('arial 10'),background="#1b3857",fg="white") 
srt_winlabel10 = sr_Canvas.create_window(1235, 365, anchor="c", window=srt_label10)


# def open_child():
#     frame2 = tk.Frame(root,width=1325,height=800,background='yellow')
#     frame2.pack(expand=True,fill=BOTH)
#     frame2.pack()
#     sr_Frame.pack_forget()

#     def close_child():
#         frame2.destroy()
#         sr_Frame.pack()
#     child_button = HoverButton(frame2,activebackground='gold',text="Close child",height=1,width=10,border=1,compound=TOP,command=lambda:close_child()).pack()

# my_label = tk.Label(sr_Frame,text="hi").pack()
# my_entry = tk.Entry(sr_Frame,).pack()
# my_button = HoverButton(sr_Frame,activebackground='gold',text="Click Me",wraplength=80,height=1,width=10,border=1, compound=TOP,command=lambda:open_child()).pack()

root.mainloop()