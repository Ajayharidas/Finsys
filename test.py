from tkinter import *
import finsys
from finsys import *

from calendar import c
from cgitb import enable, reset, text
from distutils import command
from itertools import count
from pydoc import describe
from secrets import choice
from sqlite3 import enable_callback_tracebacks
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from textwrap import wrap
from tkinter import font
import tkinter
from tkinter.font import BOLD
from unicodedata import name
from urllib.parse import parse_qs
from PIL import ImageTk, Image, ImageFile
from django.test import tag
from matplotlib.font_manager import json_dump
from numpy import choose, empty, pad, place
import pandas as pd
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename
import os
import webbrowser
from pip import main
from tkcalendar import Calendar
from tkcalendar import DateEntry
from datetime import date
from tkinter import filedialog
import subprocess
import mysql.connector
import io
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import shutil
import csv
import json
from tkPDFViewer import tkPDFViewer as pdf
from tkinter import Tk, Canvas
from matplotlib import cm

import customtkinter
import PIL.Image
from PIL import ImageGrab
from PIL import ImageTk, Image, ImageFile
import PIL.Image

# def redraw_line(event):
#     width = event.width
#     height = event.height
#     canvas = event.widget
#     # print(width)
#     # print(height)
#     # print(canvas)
#     canvas.coords("diagonal", 0, 0, width, 0)

# root=Tk()
# for x in range(10):
#     for y in range(10):
#         canvas=Canvas(root, width='15',height='15',highlightthickness=0,bg='red')                      
#         canvas.bind("<Configure>", redraw_line)
#         # coordinates are irrelevant; they will change as soon as
#         # the widget is mapped to the screen.
#         canvas.create_line(0,0,0,0, tags=("diagonal",))
#         canvas.grid(row=y,column=x,sticky='NESW')

# for x in range(10):
#     for y in range(10):
#         root.columnconfigure(x,weight=1)
#         root.rowconfigure(y,weight=1)


# root.mainloop()


# import tkinter as tk

# class App(tk.Frame):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.hourstr=tk.StringVar(self,'10')
#         self.hour = tk.Spinbox(self,from_=0,to=23,wrap=True,textvariable=self.hourstr,width=2,state="readonly")
#         self.minstr=tk.StringVar(self,'30')
#         self.minstr.trace("w",self.trace_var)
#         self.last_value = ""
#         self.min = tk.Spinbox(self,from_=0,to=59,wrap=True,textvariable=self.minstr,width=2,state="readonly")
#         self.hour.grid()
#         self.min.grid(row=0,column=1)

#     def trace_var(self,*args):
#         if self.last_value == "59" and self.minstr.get() == "0":
#             self.hourstr.set(int(self.hourstr.get())+1 if self.hourstr.get() !="23" else 0)
#         self.last_value = self.minstr.get()

# root = tk.Tk()
# App(root).pack()
# root.mainloop()


sr_Frame = Frame(tab3_1)
sr_Frame.grid(row=0,column=0,sticky='nsew')

def responsive_widgets(event):
    dwidth = event.width
    dheight = event.height
    dcanvas = event.widget
    dcanvas.coords("line1", dwidth/31.6, dheight/2.002, dwidth/1.039, dheight/2.002)
    dcanvas.coords("line17", dwidth/31.6, dheight/2.002, dwidth/31.6, dheight/1.274)
    dcanvas.coords("line2", dwidth/31.6, dheight/1.797, dwidth/1.039, dheight/1.797)
    dcanvas.coords("line3", dwidth/1.039, dheight/2.002, dwidth/1.039, dheight/1.274)
    dcanvas.coords("line4", dwidth/31.6, dheight/1.63, dwidth/1.039, dheight/1.63)
    dcanvas.coords("line5", dwidth/31.6, dheight/1.491, dwidth/1.039, dheight/1.491)
    dcanvas.coords("line6", dwidth/31.6, dheight/1.374, dwidth/1.039, dheight/1.374)
    dcanvas.coords("line7", dwidth/31.6, dheight/1.274, dwidth/1.039, dheight/1.274)
    dcanvas.coords("line8", dwidth/7.92, dheight/2.002, dwidth/7.92, dheight/1.274)
    dcanvas.coords("line9", dwidth/4.22, dheight/2.002, dwidth/4.22, dheight/1.274)
    dcanvas.coords("line10", dwidth/3.2, dheight/2.002, dwidth/3.2, dheight/1.274)
    dcanvas.coords("line11", dwidth/2.3, dheight/2.002, dwidth/2.3, dheight/1.274)
    dcanvas.coords("line12", dwidth/1.9, dheight/2.002, dwidth/1.9, dheight/1.274)
    dcanvas.coords("line13", dwidth/1.6, dheight/2.002, dwidth/1.6, dheight/1.274)
    dcanvas.coords("line14", dwidth/1.38, dheight/2.002, dwidth/1.38, dheight/1.274)
    dcanvas.coords("line15", dwidth/1.28, dheight/2.002, dwidth/1.28, dheight/1.274)
    dcanvas.coords("line16", dwidth/1.14, dheight/2.002, dwidth/1.14, dheight/1.274)

    r1 = 25
    x1 = dwidth/63
    x2 = dwidth/1.021
    y1 = dheight/14 
    y2 = dheight/3.505

    dcanvas.coords("poly1",x1 + r1,y1,
    x1 + r1,y1,
    x2 - r1,y1,
    x2 - r1,y1,     
    x2,y1,     
    #--------------------
    x2,y1 + r1,     
    x2,y1 + r1,     
    x2,y2 - r1,     
    x2,y2 - r1,     
    x2,y2,
    #--------------------
    x2 - r1,y2,     
    x2 - r1,y2,     
    x1 + r1,y2,
    x1 + r1,y2,
    x1,y2,
    #--------------------
    x1,y2 - r1,
    x1,y2 - r1,
    x1,y1 + r1,
    x1,y1 + r1,
    x1,y1,
    )

    dcanvas.coords("hline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
    
    r2 = 25
    x11 = dwidth/63
    x21 = dwidth/1.021
    y11 = dheight/2.8
    y21 = dheight/1.168


    dcanvas.coords("poly2",x11 + r2,y11,
    x11 + r2,y11,
    x21 - r2,y11,
    x21 - r2,y11,     
    x21,y11,     
    #--------------------
    x21,y11 + r2,     
    x21,y11 + r2,     
    x21,y21 - r2,     
    x21,y21 - r2,     
    x21,y21,
    #--------------------
    x21 - r2,y21,     
    x21 - r2,y21,     
    x11 + r2,y21,
    x11 + r2,y21,
    x11,y21,
    #--------------------
    x11,y21 - r2,
    x11,y21 - r2,
    x11,y11 + r2,
    x11,y11 + r2,
    x11,y11,
    )

    dcanvas.coords("label1",dwidth/2,dheight/8.24)
    dcanvas.coords("label2",dwidth/12.67,dheight/1.71)
    dcanvas.coords("label3",dwidth/5.5,dheight/1.71)
    dcanvas.coords("label4",dwidth/3.63,dheight/1.71)
    dcanvas.coords("label5",dwidth/2.67,dheight/1.71)
    dcanvas.coords("label6",dwidth/2.08,dheight/1.71)
    dcanvas.coords("label7",dwidth/1.735,dheight/1.71)
    dcanvas.coords("label8",dwidth/1.48,dheight/1.71)
    dcanvas.coords("label9",dwidth/1.327,dheight/1.71)
    dcanvas.coords("label10",dwidth/1.206,dheight/1.71)
    
    dcanvas.coords("label11",dwidth/12.67,dheight/1.894)
    dcanvas.coords("label12",dwidth/5.5,dheight/1.894)
    dcanvas.coords("label13",dwidth/3.63,dheight/1.894)
    dcanvas.coords("label14",dwidth/2.67,dheight/1.894)
    dcanvas.coords("label15",dwidth/2.08,dheight/1.894)
    dcanvas.coords("label16",dwidth/1.735,dheight/1.894)
    dcanvas.coords("label17",dwidth/1.48,dheight/1.894)
    dcanvas.coords("label18",dwidth/1.327,dheight/1.894)
    dcanvas.coords("label19",dwidth/1.206,dheight/1.894)
    dcanvas.coords("label20",dwidth/1.088,dheight/1.894)


    dcanvas.coords("combo1",dwidth/1.088,dheight/1.71)
    dcanvas.coords("combo2",dwidth/1.101,dheight/2.261)

sr_Canvas = Canvas(sr_Frame,bg='#2f516f',scrollregion=(0,0,700,1200))

sr_Frame.grid_rowconfigure(0,weight=1)
sr_Frame.grid_columnconfigure(0,weight=1)

sr_Scroll = Scrollbar(sr_Frame,orient=VERTICAL)
sr_Scroll.grid(row=0,column=1,sticky='ns')
sr_Scroll.config(command=sr_Canvas.yview)
sr_Canvas.bind("<Configure>", responsive_widgets)
sr_Canvas.config(yscrollcommand=sr_Scroll.set)
sr_Canvas.grid(row=0,column=0,sticky='nsew')


sr_Canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly1"))

sr_label = Label(sr_Canvas,width=15,height=1,text="SALES RECORDS",font=('arial 25'),background="#1b3857",fg="white")
sr_label_win = sr_Canvas.create_window(0,0,anchor="c",window=sr_label,tags=("label1"))
sr_Canvas.create_line(0,0,0,0,fill='gray',width=1,tags=("hline"))

sr_Canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly2"))

#Payment--------------------------
def sr_transCombo_options(event):
    sr_Frame.grid_forget()
    sr_Frame_1 = Frame(tab3_1,)
    sr_Frame_1.grid(row=0,column=0,sticky='nsew')

    def responsive_widgets1(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget
        
        r1 = 25
        x1 = dwidth/63
        x2 = dwidth/1.021
        y1 = dheight/14 
        y2 = dheight/3.505

        dcanvas.coords("poly1",x1 + r1,y1,
        x1 + r1,y1,
        x2 - r1,y1,
        x2 - r1,y1,     
        x2,y1,     
        #--------------------
        x2,y1 + r1,     
        x2,y1 + r1,     
        x2,y2 - r1,     
        x2,y2 - r1,     
        x2,y2,
        #--------------------
        x2 - r1,y2,     
        x2 - r1,y2,     
        x1 + r1,y2,
        x1 + r1,y2,
        x1,y2,
        #--------------------
        x1,y2 - r1,
        x1,y2 - r1,
        x1,y1 + r1,
        x1,y1 + r1,
        x1,y1,
        )

        dcanvas.coords("hline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
        
        r2 = 25
        x11 = dwidth/63
        x21 = dwidth/1.021
        y11 = dheight/2.8
        y21 = dheight/0.6


        dcanvas.coords("poly2",x11 + r2,y11,
        x11 + r2,y11,
        x21 - r2,y11,
        x21 - r2,y11,     
        x21,y11,     
        #--------------------
        x21,y11 + r2,     
        x21,y11 + r2,     
        x21,y21 - r2,     
        x21,y21 - r2,     
        x21,y21,
        #--------------------
        x21 - r2,y21,     
        x21 - r2,y21,     
        x11 + r2,y21,
        x11 + r2,y21,
        x11,y21,
        #--------------------
        x11,y21 - r2,
        x11,y21 - r2,
        x11,y11 + r2,
        x11,y11 + r2,
        x11,y11,
        )

        r2 = 25
        x11 = dwidth/63
        x21 = dwidth/1.021
        y11 = dheight/2.8
        y21 = dheight/0.37


        dcanvas.coords("poly3",x11 + r2,y11,
        x11 + r2,y11,
        x21 - r2,y11,
        x21 - r2,y11,     
        x21,y11,     
        #--------------------
        x21,y11 + r2,     
        x21,y11 + r2,     
        x21,y21 - r2,     
        x21,y21 - r2,     
        x21,y21,
        #--------------------
        x21 - r2,y21,     
        x21 - r2,y21,     
        x11 + r2,y21,
        x11 + r2,y21,
        x11,y21,
        #--------------------
        x11,y21 - r2,
        x11,y21 - r2,
        x11,y11 + r2,
        x11,y11 + r2,
        x11,y11,
        )

        r2 = 25
        x11 = dwidth/63
        x21 = dwidth/1.021
        y11 = dheight/2.8
        y21 = dheight/0.68


        dcanvas.coords("poly4",x11 + r2,y11,
        x11 + r2,y11,
        x21 - r2,y11,
        x21 - r2,y11,     
        x21,y11,     
        #--------------------
        x21,y11 + r2,     
        x21,y11 + r2,     
        x21,y21 - r2,     
        x21,y21 - r2,     
        x21,y21,
        #--------------------
        x21 - r2,y21,     
        x21 - r2,y21,     
        x11 + r2,y21,
        x11 + r2,y21,
        x11,y21,
        #--------------------
        x11,y21 - r2,
        x11,y21 - r2,
        x11,y11 + r2,
        x11,y11 + r2,
        x11,y11,
        )
        

        dcanvas.coords("label1",dwidth/2,dheight/8.24)
        dcanvas.coords("label2",dwidth/2,dheight/2.4)

        #payment-------------
        try:
            dcanvas.coords("label3",dwidth/7.91,dheight/1.76)
            dcanvas.coords("label4",dwidth/2.28,dheight/1.76)
            dcanvas.coords("label5",dwidth/1.23,dheight/1.76)
            dcanvas.coords("label6",dwidth/6.1,dheight/1.445)
            dcanvas.coords("label7",dwidth/6.1,dheight/1.235)
            dcanvas.coords("label8",dwidth/1.23,dheight/1.445)
            dcanvas.coords("label9",dwidth/1.23,dheight/1.235)
            dcanvas.coords("label10",dwidth/1.23,dheight/1.09)
            dcanvas.coords("label11",dwidth/1.23,dheight/1.04)
            dcanvas.coords("label12",dwidth/16.2,dheight/0.97)
            dcanvas.coords("label13",dwidth/5.9,dheight/0.97)
            dcanvas.coords("label14",dwidth/3.28,dheight/0.97)
            dcanvas.coords("label15",dwidth/2.1,dheight/0.97)
            dcanvas.coords("label16",dwidth/1.42,dheight/0.97)
            dcanvas.coords("label17",dwidth/1.14,dheight/0.97)
            dcanvas.coords("label18",dwidth/1.49,dheight/0.819)
            dcanvas.coords("label19",dwidth/1.49,dheight/0.759)
            dcanvas.coords("label20",dwidth/16.2,dheight/0.91)

            dcanvas.coords("entry1",dwidth/2.5,dheight/1.68)
            dcanvas.coords("entry2",dwidth/1.35,dheight/1.68)
            dcanvas.coords("entry3",dwidth/11,dheight/1.195)
            dcanvas.coords("entry4",dwidth/1.35,dheight/1.195)
            dcanvas.coords("entry5",dwidth/1.18,dheight/0.819)
            dcanvas.coords("entry6",dwidth/1.18,dheight/0.759)
            try:
                dcanvas.coords("entry7",dwidth/11,dheight/1.1)
            except:
                pass
            dcanvas.coords("entry8",dwidth/5.9,dheight/0.91)
            dcanvas.coords("entry9",dwidth/3.28,dheight/0.91)
            dcanvas.coords("entry10",dwidth/2.07,dheight/0.91)
            dcanvas.coords("entry11",dwidth/1.42,dheight/0.91)
            dcanvas.coords("entry12",dwidth/1.135,dheight/0.91)

            dcanvas.coords("combo1",dwidth/11,dheight/1.68)
            dcanvas.coords("combo2",dwidth/1.35,dheight/1.39)

            dcanvas.coords("button1",dwidth/3.89,dheight/1.6115)
            dcanvas.coords("button2",dwidth/1.103,dheight/1.3415)
            dcanvas.coords("button3",dwidth/27,dheight/3)
            dcanvas.coords("button4",dwidth/1.114,dheight/0.70)

            dcanvas.coords("line1",dwidth/31.6,dheight/1.002,dwidth/1.039,dheight/1.002)
            dcanvas.coords("line2",dwidth/31.6,dheight/0.94,dwidth/1.039,dheight/0.94)
            dcanvas.coords("line3",dwidth/31.6,dheight/1.002,dwidth/31.6,dheight/0.878)
            dcanvas.coords("line4",dwidth/1.039,dheight/1.002,dwidth/1.039,dheight/0.878)
            dcanvas.coords("line5",dwidth/11,dheight/1.002,dwidth/11,dheight/0.878)
            dcanvas.coords("line6",dwidth/4,dheight/1.002,dwidth/4,dheight/0.878)
            dcanvas.coords("line7",dwidth/2.8,dheight/1.002,dwidth/2.8,dheight/0.878)
            dcanvas.coords("line8",dwidth/1.65,dheight/1.002,dwidth/1.65,dheight/0.878)
            dcanvas.coords("line9",dwidth/1.25,dheight/1.002,dwidth/1.25,dheight/0.878)
            dcanvas.coords("line10",dwidth/1.65,dheight/0.85,dwidth/1.65,dheight/0.73)
            dcanvas.coords("line11",dwidth/1.039,dheight/0.85,dwidth/1.039,dheight/0.73)
            dcanvas.coords("line12",dwidth/1.65,dheight/0.85,dwidth/1.039,dheight/0.85)
            dcanvas.coords("line13",dwidth/1.65,dheight/0.73,dwidth/1.039,dheight/0.73)
            dcanvas.coords("line14",dwidth/1.65,dheight/0.785,dwidth/1.039,dheight/0.785)
            dcanvas.coords("line15",dwidth/1.36,dheight/0.85,dwidth/1.36,dheight/0.73)
            dcanvas.coords("line16",dwidth/31.6,dheight/0.878,dwidth/1.039,dheight/0.878)
        except:
            pass

        #sales receipt-----------
        try:
            dcanvas.coords("label21",dwidth/7.91,dheight/1.76)
            dcanvas.coords("label22",dwidth/2.47,dheight/1.76)
            dcanvas.coords("label23",dwidth/6.13,dheight/1.44)
            dcanvas.coords("label24",dwidth/2.27,dheight/1.45)
            dcanvas.coords("label25",dwidth/6.13,dheight/0.907)
            dcanvas.coords("label26",dwidth/6.13,dheight/0.81)
            dcanvas.coords("label27",dwidth/2.27,dheight/0.81)
            try:
                dcanvas.coords("label28",dwidth/1.395,dheight/0.81)
            except:
                pass
            dcanvas.coords("label29",dwidth/1.225,dheight/1.75)
            dcanvas.coords("label30",dwidth/1.2,dheight/1.63)
            dcanvas.coords("label31",dwidth/20,dheight/0.68)
            dcanvas.coords("label32",dwidth/20,dheight/0.64)
            dcanvas.coords("label33",dwidth/7.91,dheight/0.68)
            dcanvas.coords("label34",dwidth/4.09,dheight/0.68)
            dcanvas.coords("label35",dwidth/2.57,dheight/0.68)
            dcanvas.coords("label36",dwidth/1.88,dheight/0.68)
            dcanvas.coords("label37",dwidth/1.51,dheight/0.68)
            dcanvas.coords("label38",dwidth/1.25,dheight/0.68)
            dcanvas.coords("label39",dwidth/1.09,dheight/0.68)
            dcanvas.coords("label40",dwidth/1.52,dheight/0.507)
            dcanvas.coords("label41",dwidth/1.52,dheight/0.483)
            dcanvas.coords("label42",dwidth/1.52,dheight/0.462)
            dcanvas.coords("label43",dwidth/1.54,dheight/1.45)

            dcanvas.coords("label44",dwidth/20,dheight/1.135)
            dcanvas.coords("label45",dwidth/20,dheight/1.03)
            dcanvas.coords("label46",dwidth/7.4,dheight/1.135)
            dcanvas.coords("label47",dwidth/3.342,dheight/1.135)
            dcanvas.coords("label48",dwidth/2.19,dheight/1.135)
            dcanvas.coords("label49",dwidth/1.68,dheight/1.135)
            dcanvas.coords("label50",dwidth/1.328,dheight/1.135)
            dcanvas.coords("label51",dwidth/1.11,dheight/1.135)
            dcanvas.coords("label52",dwidth/1.41,dheight/0.83)
            dcanvas.coords("label53",dwidth/1.41,dheight/0.77)
            dcanvas.coords("label54",dwidth/1.41,dheight/0.715)

            dcanvas.coords("label55",dwidth/2.4,dheight/2.254)
            dcanvas.coords("label56",dwidth/1.49,dheight/2.254)
            dcanvas.coords("label57",dwidth/2.4,dheight/1.8)
            dcanvas.coords("label58",dwidth/2.4,dheight/1.5)
            dcanvas.coords("label59",dwidth/2.4,dheight/1.28)
            dcanvas.coords("label60",dwidth/1.598,dheight/1.28)
            dcanvas.coords("label61",dwidth/1.212,dheight/1.28)
            dcanvas.coords("label62",dwidth/2.4,dheight/1.105)
            dcanvas.coords("label63",dwidth/2.4,dheight/0.979)

            dcanvas.coords("entry13",dwidth/2.72,dheight/1.68)
            dcanvas.coords("entry14",dwidth/11,dheight/1.39)
            dcanvas.coords("entry15",dwidth/11,dheight/0.885)
            dcanvas.coords("entry16",dwidth/11,dheight/0.79)
            dcanvas.coords("entry17",dwidth/2.72,dheight/0.79)
            dcanvas.coords("entry18",dwidth/5.13,dheight/0.653)
            dcanvas.coords("entry19",dwidth/3.19,dheight/0.653)
            dcanvas.coords("entry20",dwidth/2.05,dheight/0.653)
            dcanvas.coords("entry21",dwidth/1.676,dheight/0.653)
            dcanvas.coords("entry22",dwidth/1.346,dheight/0.653)
            dcanvas.coords("entry23",dwidth/1.35,dheight/0.513)
            dcanvas.coords("entry24",dwidth/1.35,dheight/0.489)
            dcanvas.coords("entry25",dwidth/1.35,dheight/0.467)
            dcanvas.coords("entry26",dwidth/11,dheight/0.751)

            dcanvas.coords("entry27",dwidth/4.7,dheight/1.057)
            dcanvas.coords("entry28",dwidth/2.43,dheight/1.057)
            dcanvas.coords("entry29",dwidth/1.91,dheight/1.057)
            dcanvas.coords("entry30",dwidth/1.46,dheight/1.057)

            dcanvas.coords("entry31",dwidth/1.275,dheight/0.85)
            dcanvas.coords("entry32",dwidth/1.275,dheight/0.784)
            dcanvas.coords("entry33",dwidth/1.275,dheight/0.727)
            dcanvas.coords("entry34",dwidth/1.525,dheight/1.45)

            dcanvas.coords("entry35",dwidth/1.81,dheight/1.24)
            dcanvas.coords("entry36",dwidth/1.33,dheight/1.24)
            dcanvas.coords("entry37",dwidth/2.91,dheight/1.08)
            dcanvas.coords("entry38",dwidth/2.91,dheight/0.96)

            dcanvas.coords("combo3",dwidth/11,dheight/1.68)
            try:
                dcanvas.coords("combo4",dwidth/1.55,dheight/0.79)
            except:
                pass
            dcanvas.coords("combo5",dwidth/7.909,dheight/0.643)
            dcanvas.coords("combo6",dwidth/1.091,dheight/0.643)
            dcanvas.coords("combo7",dwidth/7.4,dheight/1.035)
            dcanvas.coords("combo8",dwidth/1.111,dheight/1.035)

            dcanvas.coords("combo9",dwidth/1.294,dheight/2.05)
            dcanvas.coords("combo10",dwidth/2.91,dheight/1.73)
            dcanvas.coords("combo11",dwidth/2.91,dheight/1.45)
            dcanvas.coords("combo12",dwidth/2.91,dheight/1.24)

            dcanvas.coords("button5",dwidth/3.89,dheight/1.61)
            try:
                dcanvas.coords("button6",dwidth/1.23,dheight/0.775)
            except:
                pass
            dcanvas.coords("button7",dwidth/1.114,dheight/0.431)
            dcanvas.coords("button8",dwidth/1.114,dheight/0.65)

            dcanvas.coords("button9",dwidth/1.09,dheight/2.04)
            dcanvas.coords("button10",dwidth/1.09,dheight/1.66)
            dcanvas.coords("button11",dwidth/1.57,dheight/0.79)
            
            dcanvas.coords("line17",dwidth/31.6,dheight/0.7,dwidth/1.039,dheight/0.7)
            dcanvas.coords("line18",dwidth/31.6,dheight/0.66,dwidth/1.039,dheight/0.66)
            dcanvas.coords("line19",dwidth/31.6,dheight/0.625,dwidth/1.039,dheight/0.625)
            dcanvas.coords("line20",dwidth/31.6,dheight/0.593,dwidth/1.039,dheight/0.593)
            dcanvas.coords("line21",dwidth/31.6,dheight/0.564,dwidth/1.039,dheight/0.564)
            dcanvas.coords("line22",dwidth/31.6,dheight/0.537,dwidth/1.039,dheight/0.537)
            dcanvas.coords("line23",dwidth/31.6,dheight/0.7,dwidth/31.6,dheight/0.537)
            dcanvas.coords("line24",dwidth/1.039,dheight/0.7,dwidth/1.039,dheight/0.537)
            dcanvas.coords("line25",dwidth/15,dheight/0.7,dwidth/15,dheight/0.537)
            dcanvas.coords("line26",dwidth/5.3,dheight/0.7,dwidth/5.3,dheight/0.537)
            dcanvas.coords("line27",dwidth/3.3,dheight/0.7,dwidth/3.3,dheight/0.537)
            dcanvas.coords("line28",dwidth/2.1,dheight/0.7,dwidth/2.1,dheight/0.537)
            dcanvas.coords("line29",dwidth/1.7,dheight/0.7,dwidth/1.7,dheight/0.537)
            dcanvas.coords("line30",dwidth/1.365,dheight/0.7,dwidth/1.365,dheight/0.537)
            dcanvas.coords("line31",dwidth/1.15,dheight/0.7,dwidth/1.15,dheight/0.537)

            dcanvas.coords("line32",dwidth/1.7,dheight/0.52,dwidth/1.039,dheight/0.52)
            dcanvas.coords("line33",dwidth/1.7,dheight/0.495,dwidth/1.039,dheight/0.495)
            dcanvas.coords("line34",dwidth/1.7,dheight/0.472,dwidth/1.039,dheight/0.472)
            dcanvas.coords("line35",dwidth/1.7,dheight/0.451,dwidth/1.039,dheight/0.451)
            dcanvas.coords("line36",dwidth/1.7,dheight/0.52,dwidth/1.7,dheight/0.451)
            dcanvas.coords("line37",dwidth/1.365,dheight/0.52,dwidth/1.365,dheight/0.451)
            dcanvas.coords("line38",dwidth/1.039,dheight/0.52,dwidth/1.039,dheight/0.451)

            dcanvas.coords("line39",dwidth/31.6,dheight/1.2,dwidth/1.039,dheight/1.2)
            dcanvas.coords("line40",dwidth/31.6,dheight/1.085,dwidth/1.039,dheight/1.085)
            dcanvas.coords("line41",dwidth/31.6,dheight/0.99,dwidth/1.039,dheight/0.99)
            dcanvas.coords("line42",dwidth/31.6,dheight/0.91,dwidth/1.039,dheight/0.91)
            dcanvas.coords("line43",dwidth/31.6,dheight/1.2,dwidth/31.6,dheight/0.91)
            dcanvas.coords("line44",dwidth/15,dheight/1.2,dwidth/15,dheight/0.91)
            dcanvas.coords("line45",dwidth/4.9,dheight/1.2,dwidth/4.9,dheight/0.91)
            dcanvas.coords("line46",dwidth/2.5,dheight/1.2,dwidth/2.5,dheight/0.91)
            dcanvas.coords("line47",dwidth/1.95,dheight/1.2,dwidth/1.95,dheight/0.91)
            dcanvas.coords("line48",dwidth/1.48,dheight/1.2,dwidth/1.48,dheight/0.91)
            dcanvas.coords("line49",dwidth/1.195,dheight/1.2,dwidth/1.195,dheight/0.91)
            dcanvas.coords("line50",dwidth/1.039,dheight/1.2,dwidth/1.039,dheight/0.91)

            dcanvas.coords("line51",dwidth/1.55,dheight/0.87,dwidth/1.039,dheight/0.87)
            dcanvas.coords("line52",dwidth/1.55,dheight/0.8,dwidth/1.039,dheight/0.8)
            dcanvas.coords("line53",dwidth/1.55,dheight/0.74,dwidth/1.039,dheight/0.74)
            dcanvas.coords("line54",dwidth/1.55,dheight/0.69,dwidth/1.039,dheight/0.69)
            dcanvas.coords("line55",dwidth/1.55,dheight/0.87,dwidth/1.55,dheight/0.69)
            dcanvas.coords("line56",dwidth/1.29,dheight/0.87,dwidth/1.29,dheight/0.69)
            dcanvas.coords("line57",dwidth/1.039,dheight/0.87,dwidth/1.039,dheight/0.69)
        except:
            pass

        try:
            dcanvas.coords("date",dwidth/2.71,dheight/1.392)
            dcanvas.coords("date1",dwidth/1.73,dheight/1.392)
            dcanvas.coords("date2",dwidth/11,dheight/1.392)
            dcanvas.coords("date3",dwidth/2.91,dheight/2.154)
            dcanvas.coords("date4",dwidth/11,dheight/1.39)
        except:
            pass

        dcanvas.coords("image1",dwidth/30,dheight/2.37)

    sr_Canvas_1 = Canvas(sr_Frame_1,bg='#2f516f',scrollregion=(0,0,700,1400))

    sr_Frame_1.grid_columnconfigure(0,weight=1)
    sr_Frame_1.grid_rowconfigure(0,weight=1)

    sr_Scroll_1 = Scrollbar(sr_Frame_1,orient=VERTICAL)
    sr_Scroll_1.grid(row=0,column=1,sticky='ns')
    sr_Scroll_1.config(command=sr_Canvas_1.yview)
    sr_Canvas_1.bind("<Configure>", responsive_widgets1)
    sr_Canvas_1.config(yscrollcommand=sr_Scroll_1.set)
    sr_Canvas_1.grid(row=0,column=0,sticky='nsew')


    if sr_transCombo.get() == 'Payment':
        sr_Canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly1"))
        rp_label = Label(sr_Canvas_1,width=18,height=1,text="RECIEVE PAYMENT",font=('arial 25'),background='#1b3857',fg="white")
        sr_Canvas_1.create_window(0,0,anchor="c",window=rp_label,tags=("label1"))
        sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("hline"))

        sr_Canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly2"))

        rp_label1 = Label(sr_Canvas_1,width=18,height=1,text="Fin sYs",font=('arial 25'),background='#1b3857',fg="white")
        sr_Canvas_1.create_window(0,0,anchor="c",window=rp_label1,tags=("label2"))

        rp_label2 = Label(sr_Canvas_1,width=10,height=1,text="Customer",font=('arial 12'),background='#1b3857',fg="white",anchor='w')
        sr_Canvas_1.create_window(0,0,window=rp_label2,tags=("label3"))

        rp_custCombo = ttk.Combobox(sr_Canvas_1,width=15,font=('arial 15'))
        sr_Canvas_1.create_window(0,0,anchor='nw',window=rp_custCombo,tags=("combo1"))

        global sr_addCustomer
        def sr_addCustomer():
            sr_Frame_1.grid_forget()
            sr_Frame_2 = Frame(tab3_1,)
            sr_Frame_2.grid(row=0,column=0,sticky='nsew')

            def responsive_widgets2(event):
                dwidth = event.width
                dheight = event.height
                dcanvas = event.widget
                
                r1 = 25
                x1 = dwidth/63
                x2 = dwidth/1.021
                y1 = dheight/14 
                y2 = dheight/3.505

                dcanvas.coords("poly1",x1 + r1,y1,
                x1 + r1,y1,
                x2 - r1,y1,
                x2 - r1,y1,     
                x2,y1,     
                #--------------------
                x2,y1 + r1,     
                x2,y1 + r1,     
                x2,y2 - r1,     
                x2,y2 - r1,     
                x2,y2,
                #--------------------
                x2 - r1,y2,     
                x2 - r1,y2,     
                x1 + r1,y2,
                x1 + r1,y2,
                x1,y2,
                #--------------------
                x1,y2 - r1,
                x1,y2 - r1,
                x1,y1 + r1,
                x1,y1 + r1,
                x1,y1,
                )

                dcanvas.coords("hline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
                
                r2 = 25
                x11 = dwidth/63
                x21 = dwidth/1.021
                y11 = dheight/2.8
                y21 = dheight/0.6


                dcanvas.coords("poly2",x11 + r2,y11,
                x11 + r2,y11,
                x21 - r2,y11,
                x21 - r2,y11,     
                x21,y11,     
                #--------------------
                x21,y11 + r2,     
                x21,y11 + r2,     
                x21,y21 - r2,     
                x21,y21 - r2,     
                x21,y21,
                #--------------------
                x21 - r2,y21,     
                x21 - r2,y21,     
                x11 + r2,y21,
                x11 + r2,y21,
                x11,y21,
                #--------------------
                x11,y21 - r2,
                x11,y21 - r2,
                x11,y11 + r2,
                x11,y11 + r2,
                x11,y11,
                )

                dcanvas.coords("label1",dwidth/2,dheight/8.24)
                dcanvas.coords("label2",dwidth/6,dheight/2.4)
                dcanvas.coords("label3",dwidth/8.2,dheight/2)
                dcanvas.coords("label4",dwidth/2.8,dheight/2)
                dcanvas.coords("label5",dwidth/1.7,dheight/2)
                dcanvas.coords("label6",dwidth/8.2,dheight/1.66)
                dcanvas.coords("label7",dwidth/2.8,dheight/1.66)
                dcanvas.coords("label8",dwidth/8.2,dheight/1.42)
                dcanvas.coords("label9",dwidth/2.8,dheight/1.42)
                dcanvas.coords("label10",dwidth/1.7,dheight/1.42)
                dcanvas.coords("label11",dwidth/8.2,dheight/1.24)
                dcanvas.coords("label12",dwidth/2.8,dheight/1.24)
                dcanvas.coords("label13",dwidth/1.7,dheight/1.24)
                dcanvas.coords("label14",dwidth/5.97,dheight/1.09)
                dcanvas.coords("label15",dwidth/8.2,dheight/0.98)
                dcanvas.coords("label16",dwidth/1.71,dheight/0.98)
                dcanvas.coords("label17",dwidth/1.58,dheight/1.09)
                dcanvas.coords("label18",dwidth/8.2,dheight/0.824)
                dcanvas.coords("label19",dwidth/2.62,dheight/0.824)
                dcanvas.coords("label20",dwidth/1.7,dheight/0.824)
                dcanvas.coords("label21",dwidth/1.185,dheight/0.824)
                dcanvas.coords("label22",dwidth/8.2,dheight/0.76)
                dcanvas.coords("label23",dwidth/2.62,dheight/0.76)
                dcanvas.coords("label24",dwidth/1.7,dheight/0.76)
                dcanvas.coords("label25",dwidth/1.185,dheight/0.76)
                dcanvas.coords("label26",dwidth/1.28,dheight/1.087)
                dcanvas.coords("label27",dwidth/6.3,dheight/0.709)

                dcanvas.coords("line1",dwidth/21,dheight/2.2,dwidth/1.055,dheight/2.2)

                dcanvas.coords("combo1",dwidth/20,dheight/1.9)
                dcanvas.coords("combo2",dwidth/20,dheight/1.37)

                dcanvas.coords("entry2",dwidth/3.52,dheight/1.9)
                dcanvas.coords("entry3",dwidth/1.94,dheight/1.9)
                dcanvas.coords("entry4",dwidth/20,dheight/1.6)
                dcanvas.coords("entry5",dwidth/3.52,dheight/1.6)
                dcanvas.coords("entry6",dwidth/3.52,dheight/1.38)
                dcanvas.coords("entry7",dwidth/1.94,dheight/1.38)
                dcanvas.coords("entry8",dwidth/20,dheight/1.21)
                dcanvas.coords("entry9",dwidth/3.52,dheight/1.21)
                dcanvas.coords("entry10",dwidth/1.94,dheight/1.21)
                dcanvas.coords("entry11",dwidth/20,dheight/0.96)
                dcanvas.coords("entry12",dwidth/1.95,dheight/0.96)
                dcanvas.coords("entry13",dwidth/20,dheight/0.81)
                dcanvas.coords("entry14",dwidth/3.23,dheight/0.81)
                dcanvas.coords("entry15",dwidth/1.94,dheight/0.81)
                dcanvas.coords("entry16",dwidth/1.296,dheight/0.81)
                dcanvas.coords("entry17",dwidth/20,dheight/0.749)
                dcanvas.coords("entry18",dwidth/3.23,dheight/0.749)
                dcanvas.coords("entry19",dwidth/1.94,dheight/0.749)
                dcanvas.coords("entry20",dwidth/1.296,dheight/0.749)

                dcanvas.coords("check1",dwidth/1.45,dheight/1.11)
                dcanvas.coords("check2",dwidth/20,dheight/0.72)

                dcanvas.coords("button1",dwidth/2,dheight/0.655)
                dcanvas.coords("button2",dwidth/27,dheight/3)

            sr_Canvas_2 = Canvas(sr_Frame_2,bg='#2f516f',scrollregion=(0,0,700,1200))

            sr_Frame_2.grid_columnconfigure(0,weight=1)
            sr_Frame_2.grid_rowconfigure(0,weight=1)

            sr_Scroll_2 = Scrollbar(sr_Frame_2,orient=VERTICAL)
            sr_Scroll_2.grid(row=0,column=1,sticky='ns')
            sr_Scroll_2.config(command=sr_Canvas_2.yview)
            sr_Canvas_2.bind("<Configure>", responsive_widgets2)
            sr_Canvas_2.config(yscrollcommand=sr_Scroll_2.set)
            sr_Canvas_2.grid(row=0,column=0,sticky='nsew')

            sr_Canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly1"))
            cust_label1 = Label(sr_Canvas_2,width=18,height=1,text="ADD CUSTOMER",font=('arial 25'),background='#1b3857',fg="white")
            sr_Canvas_2.create_window(0,0,anchor="c",window=cust_label1,tags=("label1"))
            sr_Canvas_2.create_line(0,0,0,0,fill='gray',width=1,tags=("hline"))

            sr_Canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly2"))

            cust_label2 = Label(sr_Canvas_2,width=20,height=1,text="Customer Information",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label2,tags=('label2'))

            sr_Canvas_2.create_line(0,0,0,0,fill='gray',width=1,tags=("line1"))

            cust_label3 = Label(sr_Canvas_2,width=20,height=1,text="Title",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label3,tags=('label3'))

            cust_title = ttk.Combobox(sr_Canvas_2,width=19,font=('arial 15'))
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_title,tags=("combo1"))

            cust_label4 = Label(sr_Canvas_2,width=20,height=1,text="First name",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label4,tags=('label4'))

            cust_fname = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_fname,tags=("entry2"))

            cust_label5 = Label(sr_Canvas_2,width=20,height=1,text="Last name",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label5,tags=('label5'))

            cust_lname = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_lname,tags=("entry3"))

            cust_label6 = Label(sr_Canvas_2,width=20,height=1,text="Company",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label6,tags=('label6'))

            cust_company = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_company,tags=("entry4"))

            cust_label7 = Label(sr_Canvas_2,width=20,height=1,text="Location",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label7,tags=('label7'))

            cust_location = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_location,tags=("entry5"))

            cust_label8 = Label(sr_Canvas_2,width=20,height=1,text="GST type",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label8,tags=('label8'))

            cust_gtype = ttk.Combobox(sr_Canvas_2,width=19,font=('arial 15'))
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_gtype,tags=("combo2"))

            cust_label9 = Label(sr_Canvas_2,width=20,height=1,text="GSTIN",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label9,tags=('label9'))

            cust_gin = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_gin,tags=("entry6"))

            cust_label10 = Label(sr_Canvas_2,width=20,height=1,text="PAN NO",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label10,tags=('label10'))

            cust_pan = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pan,tags=("entry7"))

            cust_label11 = Label(sr_Canvas_2,width=20,height=1,text="Email",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label11,tags=('label11'))

            cust_email = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_email,tags=("entry8"))

            cust_label12 = Label(sr_Canvas_2,width=20,height=1,text="Website",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label12,tags=('label12'))

            cust_web = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_web,tags=("entry9"))

            cust_label13 = Label(sr_Canvas_2,width=20,height=1,text="Mobile",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label13,tags=('label13'))

            cust_mob = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_mob,tags=("entry10"))

            cust_label14 = Label(sr_Canvas_2,width=20,height=1,text="Billing Address",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label14,tags=('label14'))

            cust_label15 = Label(sr_Canvas_2,width=20,height=1,text="Street",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label15,tags=('label15'))

            cust_st1 = scrolledtext.ScrolledText(sr_Canvas_2,width=66,height=4,background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_st1,tags=("entry11"))

            cust_label17 = Label(sr_Canvas_2,width=20,height=1,text="Shipping Address",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label17,tags=('label17'))

            cust_label16 = Label(sr_Canvas_2,width=20,height=1,text="Street",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label16,tags=('label16'))

            cust_st2 = scrolledtext.ScrolledText(sr_Canvas_2,width=66,height=4,background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_st2,tags=("entry12"))

            cust_label18 = Label(sr_Canvas_2,width=20,height=1,text="City",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label18,tags=('label18'))

            cust_city = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_city,tags=("entry13"))

            cust_label19 = Label(sr_Canvas_2,width=20,height=1,text="State",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label19,tags=('label19'))

            cust_state = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_state,tags=("entry14"))

            cust_label20 = Label(sr_Canvas_2,width=20,height=1,text="City",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label20,tags=('label20'))

            cust_city1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_city1,tags=("entry15"))

            cust_label21 = Label(sr_Canvas_2,width=20,height=1,text="State",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label21,tags=('label21'))

            cust_state1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_state1,tags=("entry16"))
            #--
            cust_label22 = Label(sr_Canvas_2,width=20,height=1,text="Pin code",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label22,tags=('label22'))

            cust_pin = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pin,tags=("entry17"))

            cust_label23 = Label(sr_Canvas_2,width=20,height=1,text="Country",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label23,tags=('label23'))

            cust_country = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_country,tags=("entry18"))

            cust_label24 = Label(sr_Canvas_2,width=20,height=1,text="Pin code",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label24,tags=('label24'))

            cust_pin1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pin1,tags=("entry19"))

            cust_label25 = Label(sr_Canvas_2,width=20,height=1,text="Country",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label25,tags=('label25'))

            cust_country1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_country1,tags=("entry20"))

            cust_sameb = Checkbutton(sr_Canvas_2,onvalue=1,offvalue=0,background='#1b3857',activebackground="#1b3857")
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_sameb,tags=("check1"))

            cust_label26 = Label(sr_Canvas_2,width=20,height=1,text="Same as billing address",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label26,tags=('label26'))

            cust_term = Checkbutton(sr_Canvas_2,onvalue=1,offvalue=0,background='#1b3857',activebackground="#1b3857")
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_term,tags=("check2"))

            cust_label27 = Label(sr_Canvas_2,width=25,height=1,text="Agree to terms and conditions",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label27,tags=('label27'))
            
            cust_save = Button(sr_Canvas_2,text="Submit Form",font=('arial 12 bold'),width=40,height=2,background="#198fed",activebackground="#198fed",foreground="white",activeforeground="white",bd=0)
            sr_Canvas_2.create_window(0,0,window=cust_save,tags=("button1"))

            def dc_goBack1():
                sr_Frame_2.grid_forget()
                sr_Frame_1.grid(row=0,column=0,sticky='nsew')

            back_btn = Button(sr_Canvas_2,text='←  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:dc_goBack1())
            sr_Canvas_2.create_window(0,0,window=back_btn,tags=("button2"))

        rp_plus = Button(sr_Canvas_1,text='+',font=('arial 10 bold'),foreground='white',activebackground='#1b3857',background='#1b3857',padx=7,command=lambda:sr_addCustomer())
        sr_Canvas_1.create_window(0,0,window=rp_plus,tags=("button1"))

        rp_label3 = Label(sr_Canvas_1,width=10,height=1,text="Email",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(0,0,window=rp_label3,tags=('label4'))

        rp_email = Entry(sr_Canvas_1,width=20,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=rp_email,tags=("entry1"))

        rp_label4 = Label(sr_Canvas_1,width=20,height=1,text="Find by invoice number",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
        sr_Canvas_1.create_window(0,0,window=rp_label4,tags=("label5"))

        rp_invnum = Entry(sr_Canvas_1,width=20,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=rp_invnum,tags=("entry2"))

        rp_label6 = Label(sr_Canvas_1,width=20,height=1,text="Payment method",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
        sr_Canvas_1.create_window(0,0,window=rp_label6,tags=("label7"))

        def addnew_pmethod(event):
            if rp_pmethod.get() == "Add new":
                sr_Canvas_1.itemconfig("entry7",state='normal')
            else:
                sr_Canvas_1.itemconfig("entry7",state='hidden')

        rp_pmethod = ttk.Combobox(sr_Canvas_1,font=('arial 15'),width=19,background='#2f516f')
        rp_pmethod['values'] = ['Add new','']
        rp_pmethod.current(0)
        rp_pmethod.bind("<<ComboboxSelected>>",addnew_pmethod)
        sr_Canvas_1.create_window(0,0,anchor='nw',window=rp_pmethod,tags=("entry3"))

        rp_newmeth = Entry(sr_Canvas_1,font=('arial 15'),width=20,background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',state=HIDDEN,window=rp_newmeth,tags=("entry7"))

        rp_label7 = Label(sr_Canvas_1,width=20,height=1,text="Deposit to",font=('arial 12'),background='#1b3857',fg="white",anchor="nw")
        sr_Canvas_1.create_window(0,0,window=rp_label7,tags=("label8"))

        rp_depositto = ttk.Combobox(sr_Canvas_1,font=('arial 15'),width=15)
        sr_Canvas_1.create_window(0,0,anchor='nw',window=rp_depositto,tags=("combo2"))

        def add_depositTo():
            sr_Frame_1.grid_forget()
            sr_Frame_3 = Frame(tab3_1,)
            sr_Frame_3.grid(row=0,column=0,sticky='nsew')

            def responsive_widgets3(event):
                dwidth = event.width
                dheight = event.height
                dcanvas = event.widget

                r1 = 25
                x1 = dwidth/63
                x2 = dwidth/1.021
                y1 = dheight/14 
                y2 = dheight/3.505

                dcanvas.coords("poly1",x1 + r1,y1,
                x1 + r1,y1,
                x2 - r1,y1,
                x2 - r1,y1,     
                x2,y1,     
                #--------------------
                x2,y1 + r1,     
                x2,y1 + r1,     
                x2,y2 - r1,     
                x2,y2 - r1,     
                x2,y2,
                #--------------------
                x2 - r1,y2,     
                x2 - r1,y2,     
                x1 + r1,y2,
                x1 + r1,y2,
                x1,y2,
                #--------------------
                x1,y2 - r1,
                x1,y2 - r1,
                x1,y1 + r1,
                x1,y1 + r1,
                x1,y1,
                )

                dcanvas.coords("hline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
                
                r2 = 25
                x11 = dwidth/63
                x21 = dwidth/1.021
                y11 = dheight/2.8
                y21 = dheight/0.9


                dcanvas.coords("poly2",x11 + r2,y11,
                x11 + r2,y11,
                x21 - r2,y11,
                x21 - r2,y11,     
                x21,y11,     
                #--------------------
                x21,y11 + r2,     
                x21,y11 + r2,     
                x21,y21 - r2,     
                x21,y21 - r2,     
                x21,y21,
                #--------------------
                x21 - r2,y21,     
                x21 - r2,y21,     
                x11 + r2,y21,
                x11 + r2,y21,
                x11,y21,
                #--------------------
                x11,y21 - r2,
                x11,y21 - r2,
                x11,y11 + r2,
                x11,y11 + r2,
                x11,y11,
                )

                dcanvas.coords("label1",dwidth/2,dheight/8.24)
                dcanvas.coords("label2",dwidth/8.2,dheight/2.44)
                dcanvas.coords("label3",dwidth/1.655,dheight/2.44)
                dcanvas.coords("label4",dwidth/8.2,dheight/1.89)
                dcanvas.coords("label5",dwidth/1.655,dheight/1.89)
                dcanvas.coords("label6",dwidth/1.605,dheight/1.522)
                dcanvas.coords("label7",dwidth/1.655,dheight/1.27)

                dcanvas.coords("entry1",dwidth/20,dheight/2.32)
                dcanvas.coords("entry2",dwidth/1.88,dheight/2.32)
                dcanvas.coords("entry3",dwidth/20,dheight/1.8)
                dcanvas.coords("entry4",dwidth/1.88,dheight/1.805)
                dcanvas.coords("entry5",dwidth/20,dheight/1.605)
                dcanvas.coords("entry6",dwidth/1.88,dheight/1.46)
                dcanvas.coords("entry7",dwidth/1.88,dheight/1.23)

                dcanvas.coords("check1",dwidth/1.89,dheight/1.57)

                dcanvas.coords("button1",dwidth/2,dheight/0.97)
                dcanvas.coords("button2",dwidth/27,dheight/3)

            sr_Canvas_3 = Canvas(sr_Frame_3,bg='#2f516f',scrollregion=(0,0,700,1200))

            sr_Frame_3.grid_columnconfigure(0,weight=1)
            sr_Frame_3.grid_rowconfigure(0,weight=1)

            sr_Scroll_2 = Scrollbar(sr_Frame_3,orient=VERTICAL)
            sr_Scroll_2.grid(row=0,column=1,sticky='ns')
            sr_Scroll_2.config(command=sr_Canvas_3.yview)
            sr_Canvas_3.bind("<Configure>", responsive_widgets3)
            sr_Canvas_3.config(yscrollcommand=sr_Scroll_2.set)
            sr_Canvas_3.grid(row=0,column=0,sticky='nsew')

            sr_Canvas_3.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly1"))
            dep_label1 = Label(sr_Canvas_3,width=18,height=1,text="ACCOUNT CREATE",font=('arial 25'),background='#1b3857',fg="white")
            sr_Canvas_3.create_window(0,0,anchor="c",window=dep_label1,tags=("label1"))
            sr_Canvas_3.create_line(0,0,0,0,fill='gray',width=1,tags=("hline"))

            sr_Canvas_3.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly2"))

            dep_label2 = Label(sr_Canvas_3,width=20,height=1,text="Account type",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
            sr_Canvas_3.create_window(0,0,window=dep_label2,tags=("label2"))

            dep_acctype = ttk.Combobox(sr_Canvas_3,width=46,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_acctype,tags=("entry1"))

            dep_label3 = Label(sr_Canvas_3,width=20,height=1,text="*Name",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
            sr_Canvas_3.create_window(0,0,window=dep_label3,tags=("label3"))

            dep_name = Entry(sr_Canvas_3,width=47,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_name,tags=("entry2"))

            dep_label4 = Label(sr_Canvas_3,width=20,height=1,text="*Detail Type",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
            sr_Canvas_3.create_window(0,0,window=dep_label4,tags=("label4"))

            dep_dtype = ttk.Combobox(sr_Canvas_3,width=46,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_dtype,tags=("entry3"))

            dep_label5 = Label(sr_Canvas_3,width=20,height=1,text="Description",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
            sr_Canvas_3.create_window(0,0,window=dep_label5,tags=("label5"))

            dep_desp = Entry(sr_Canvas_3,width=47,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_desp,tags=("entry4"))

            dep_term = Text(sr_Canvas_3,width=47,font=('arial 15'),height=7,background='#2f516f',foreground='white')
            term_txt = "Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills."
            dep_term.insert('1.0',term_txt)
            dep_term.config(state=DISABLED)
            sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_term,tags=("entry5"))

            def sr_subAccount():
                if subaccVar.get() == True:
                    dep_subacc["state"] = NORMAL
                else:
                    dep_subacc["state"] = DISABLED

            subaccVar = BooleanVar()
            dep_subcheck = Checkbutton(sr_Canvas_3,variable=subaccVar,onvalue=1,offvalue=0,background='#1b3857',activebackground="#1b3857",command=sr_subAccount)
            sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_subcheck,tags=("check1"))

            dep_label6 = Label(sr_Canvas_3,width=20,height=1,text="Is sub-account",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
            sr_Canvas_3.create_window(0,0,window=dep_label6,tags=("label6"))

            dep_subacc = ttk.Combobox(sr_Canvas_3,width=46,font=('arial 15'),background='#2f516f',foreground='white',state=DISABLED)
            sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_subacc,tags=("entry6"))

            dep_label7 = Label(sr_Canvas_3,width=20,height=1,text="Default Tax Code",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
            sr_Canvas_3.create_window(0,0,window=dep_label7,tags=("label7"))

            dep_dtaxcode = Entry(sr_Canvas_3,width=47,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_dtaxcode,tags=("entry7"))

            dep_save = Button(sr_Canvas_3,text="Create",font=('arial 12 bold'),width=35,height=2,background="#198fed",activebackground="#198fed",foreground="white",activeforeground="white",bd=0)
            sr_Canvas_3.create_window(0,0,window=dep_save,tags=("button1"))

            def goBack2():
                sr_Frame_3.grid_forget()
                sr_Frame_1.grid(row=0,column=0,sticky='nsew')

            back_btn = Button(sr_Canvas_3,text='←  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:goBack2())
            sr_Canvas_3.create_window(0,0,window=back_btn,tags=("button2"))

        rp_plus1 = Button(sr_Canvas_1,text='+',font=('arial 10 bold'),foreground='white',activebackground='#1b3857',background='#1b3857',padx=7,command=lambda:add_depositTo())
        sr_Canvas_1.create_window(0,0,window=rp_plus1,tags=("button2"))

        rp_label8 = Label(sr_Canvas_1,width=20,height=1,text="Amount recieved",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
        sr_Canvas_1.create_window(0,0,window=rp_label8,tags=("label9"))

        rp_amntre = Entry(sr_Canvas_1,font=('arial 15'),width=20,background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=rp_amntre,tags=("entry4"))

        rp_label9 = Label(sr_Canvas_1,width=20,height=1,text="AMOUNT RECIEVED",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
        sr_Canvas_1.create_window(0,0,window=rp_label9,tags=("label10"))

        rp_label10 = Label(sr_Canvas_1,width=20,height=1,text="0.00",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
        sr_Canvas_1.create_window(0,0,window=rp_label10,tags=("label11"))

        sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("line1"))
        sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("line2"))
        sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("line3"))
        sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("line4"))
        sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("line5"))
        sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("line6"))
        sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("line7"))
        sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("line8"))
        sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("line9"))
        sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("line16"))

        rpt_label1 = Label(sr_Canvas_1,width=5,height=1,text="#", font=('arial 10 bold'),background='#1b3857',fg="white") 
        sr_Canvas_1.create_window(0, 0, anchor="c", window=rpt_label1,tags=("label12"))

        rpt_label2 = Label(sr_Canvas_1,width=15,height=1,text="DESCRIPTION", font=('arial 10 bold'),background='#1b3857',fg="white") 
        sr_Canvas_1.create_window(0, 0, anchor="c", window=rpt_label2,tags=("label13"))

        rpt_label3 = Label(sr_Canvas_1,width=15,height=1,text="DUE DATE", font=('arial 10 bold'),background='#1b3857',fg="white") 
        sr_Canvas_1.create_window(0, 0, anchor="c", window=rpt_label3,tags=("label14"))

        rpt_label4 = Label(sr_Canvas_1,width=15,height=1,text="ORIGINAL AMOUNT", font=('arial 10 bold'),background='#1b3857',fg="white") 
        sr_Canvas_1.create_window(0, 0, anchor="c", window=rpt_label4,tags=("label15"))

        rpt_label5 = Label(sr_Canvas_1,width=15,height=1,text="OPEN BALANCE", font=('arial 10 bold'),background='#1b3857',fg="white") 
        sr_Canvas_1.create_window(0, 0, anchor="c", window=rpt_label5,tags=("label16"))

        rpt_label6 = Label(sr_Canvas_1,width=15,height=1,text="PAYMENT", font=('arial 10 bold'),background='#1b3857',fg="white") 
        sr_Canvas_1.create_window(0, 0, anchor="c", window=rpt_label6,tags=("label17"))

        sr_Canvas_1.create_line(820,800,1260,800,fill='gray',width=1,tags=("line10"))
        sr_Canvas_1.create_line(820,850,1260,850,fill='gray',width=1,tags=("line11"))
        sr_Canvas_1.create_line(820,900,1260,900,fill='gray',width=1,tags=("line12"))
        sr_Canvas_1.create_line(820,800,820,900,fill='gray',width=1,tags=("line13"))
        sr_Canvas_1.create_line(1000,800,1000,900,fill='gray',width=1,tags=("line14"))
        sr_Canvas_1.create_line(1260,800,1260,900,fill='gray',width=1,tags=("line15"))

        rpt_label7 = Label(sr_Canvas_1,width=15,height=1,text="Amount to Apply", font=('arial 10 bold'),background='#1b3857',fg="white") 
        sr_Canvas_1.create_window(910, 825, anchor="c", window=rpt_label7,tags=("label18"))  

        rp_amnttoapply = Entry(sr_Canvas_1,font=('arial 15'),width=24,background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(1130,825,anchor='c',window=rp_amnttoapply,tags=("entry5"))   

        rpt_label8 = Label(sr_Canvas_1,width=15,height=1,text="Amount to Credit", font=('arial 10 bold'),background='#1b3857',fg="white") 
        sr_Canvas_1.create_window(910, 875, anchor="c", window=rpt_label8,tags=("label19"))  

        rp_amnttocredit = Entry(sr_Canvas_1,font=('arial 15'),width=24,background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(1130,875,anchor='c',window=rp_amnttocredit,tags=("entry6"))   

        def sr_goBack():
            sr_Frame_1.grid_forget()
            sr_Frame.grid(row=0,column=0,sticky='nsew')

        back_btn = Button(sr_Canvas_1,text='←  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:sr_goBack())
        sr_Canvas_1.create_window(0,0,window=back_btn,tags=("button3")) 

        save_btn = Button(sr_Canvas_1,text='Save',width=20,height=2,font=('arial 10 bold'),background="#198fed",activebackground="#198fed",foreground="white",activeforeground="white",bd=0)
        sr_Canvas_1.create_window(0,0,window=save_btn,tags=("button4")) 

        rpt_label9 = Label(sr_Canvas_1,width=5,height=1,text="1",font=('arial 12'),background='#1b3857',fg="white",anchor="c")
        sr_Canvas_1.create_window(0,0,window=rpt_label9,tags=("label20"))

        rpt_descp = Entry(sr_Canvas_1,font=('arial 15'),width=16,background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='c',window=rpt_descp,tags=("entry8")) 

        rpt_due = Entry(sr_Canvas_1,font=('arial 15'),width=10,background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='c',window=rpt_due,tags=("entry9")) 

        rpt_original = Entry(sr_Canvas_1,font=('arial 15'),width=26,background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='c',window=rpt_original,tags=("entry10")) 

        rpt_obal = Entry(sr_Canvas_1,font=('arial 15'),width=20,background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='c',window=rpt_obal,tags=("entry11"))

        rpt_payment = Entry(sr_Canvas_1,font=('arial 15'),width=17,background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='c',window=rpt_payment,tags=("entry12")) 

        rp_label5 = Label(sr_Canvas_1,width=20,height=1,text="Payment date",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
        sr_Canvas_1.create_window(0,0,window=rp_label5,tags=("label6"))

        rp_pdate = DateEntry(sr_Canvas_1,font=('arial 15'),width=19,background='#2f516f',foreground='white')

        cwidth = root.winfo_screenwidth()

        if cwidth > 1280:
            sr_Canvas_1.create_window(122.27272727272727,442.44604316546764,anchor='nw',window=rp_pdate,tags=('date4'))
        elif cwidth <= 1024:
            sr_Canvas_1.create_window(91.54545454545455,456.1151079136691,anchor='nw',window=rp_pdate,tags=('date4'))
        else:
            sr_Canvas_1.create_window(114.81818181818181,407.9136690647482,anchor='nw',window=rp_pdate,tags=('date4'))

        
    elif sr_transCombo.get() == 'Sales Receipt':
        sr_Canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly1"))
        cm_label1 = Label(sr_Canvas_1,width=18,height=1,text="CASH MEMO",font=('arial 25'),background='#1b3857',fg="white")
        sr_Canvas_1.create_window(0,0,anchor="c",window=cm_label1,tags=("label1"))
        sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("hline"))

        sr_Canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly3"))

        cm_label2 = Label(sr_Canvas_1,width=18,height=1,text="Fin sYs",font=('arial 25'),background='#1b3857',fg="white")
        sr_Canvas_1.create_window(0,0,anchor="c",window=cm_label2,tags=("label2"))

        cm_label3 = Label(sr_Canvas_1,width=10,height=1,text="Customer",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
        sr_Canvas_1.create_window(0,0,window=cm_label3,tags=("label21"))

        cm_custCombo = ttk.Combobox(sr_Canvas_1,width=15,font=('arial 15'))
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cm_custCombo,tags=("combo3"))

        def sr_addCustomer_1():
            sr_Frame_1.grid_forget()
            sr_Frame_2 = Frame(tab3_1,)
            sr_Frame_2.grid(row=0,column=0,sticky='nsew')

            def responsive_widgets2(event):
                dwidth = event.width
                dheight = event.height
                dcanvas = event.widget
                
                r1 = 25
                x1 = dwidth/63
                x2 = dwidth/1.021
                y1 = dheight/14 
                y2 = dheight/3.505

                dcanvas.coords("poly1",x1 + r1,y1,
                x1 + r1,y1,
                x2 - r1,y1,
                x2 - r1,y1,     
                x2,y1,     
                #--------------------
                x2,y1 + r1,     
                x2,y1 + r1,     
                x2,y2 - r1,     
                x2,y2 - r1,     
                x2,y2,
                #--------------------
                x2 - r1,y2,     
                x2 - r1,y2,     
                x1 + r1,y2,
                x1 + r1,y2,
                x1,y2,
                #--------------------
                x1,y2 - r1,
                x1,y2 - r1,
                x1,y1 + r1,
                x1,y1 + r1,
                x1,y1,
                )

                dcanvas.coords("hline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
                
                r2 = 25
                x11 = dwidth/63
                x21 = dwidth/1.021
                y11 = dheight/2.8
                y21 = dheight/0.6


                dcanvas.coords("poly2",x11 + r2,y11,
                x11 + r2,y11,
                x21 - r2,y11,
                x21 - r2,y11,     
                x21,y11,     
                #--------------------
                x21,y11 + r2,     
                x21,y11 + r2,     
                x21,y21 - r2,     
                x21,y21 - r2,     
                x21,y21,
                #--------------------
                x21 - r2,y21,     
                x21 - r2,y21,     
                x11 + r2,y21,
                x11 + r2,y21,
                x11,y21,
                #--------------------
                x11,y21 - r2,
                x11,y21 - r2,
                x11,y11 + r2,
                x11,y11 + r2,
                x11,y11,
                )

                dcanvas.coords("label1",dwidth/2,dheight/8.24)
                dcanvas.coords("label2",dwidth/6,dheight/2.4)
                dcanvas.coords("label3",dwidth/8.2,dheight/2)
                dcanvas.coords("label4",dwidth/2.8,dheight/2)
                dcanvas.coords("label5",dwidth/1.7,dheight/2)
                dcanvas.coords("label6",dwidth/8.2,dheight/1.66)
                dcanvas.coords("label7",dwidth/2.8,dheight/1.66)
                dcanvas.coords("label8",dwidth/8.2,dheight/1.42)
                dcanvas.coords("label9",dwidth/2.8,dheight/1.42)
                dcanvas.coords("label10",dwidth/1.7,dheight/1.42)
                dcanvas.coords("label11",dwidth/8.2,dheight/1.24)
                dcanvas.coords("label12",dwidth/2.8,dheight/1.24)
                dcanvas.coords("label13",dwidth/1.7,dheight/1.24)
                dcanvas.coords("label14",dwidth/5.97,dheight/1.09)
                dcanvas.coords("label15",dwidth/8.2,dheight/0.98)
                dcanvas.coords("label16",dwidth/1.71,dheight/0.98)
                dcanvas.coords("label17",dwidth/1.58,dheight/1.09)
                dcanvas.coords("label18",dwidth/8.2,dheight/0.824)
                dcanvas.coords("label19",dwidth/2.62,dheight/0.824)
                dcanvas.coords("label20",dwidth/1.7,dheight/0.824)
                dcanvas.coords("label21",dwidth/1.185,dheight/0.824)
                dcanvas.coords("label22",dwidth/8.2,dheight/0.76)
                dcanvas.coords("label23",dwidth/2.62,dheight/0.76)
                dcanvas.coords("label24",dwidth/1.7,dheight/0.76)
                dcanvas.coords("label25",dwidth/1.185,dheight/0.76)
                dcanvas.coords("label26",dwidth/1.28,dheight/1.087)
                dcanvas.coords("label27",dwidth/6.3,dheight/0.709)

                dcanvas.coords("line1",dwidth/21,dheight/2.2,dwidth/1.055,dheight/2.2)

                dcanvas.coords("combo1",dwidth/20,dheight/1.9)
                dcanvas.coords("combo2",dwidth/20,dheight/1.37)

                dcanvas.coords("entry2",dwidth/3.52,dheight/1.9)
                dcanvas.coords("entry3",dwidth/1.94,dheight/1.9)
                dcanvas.coords("entry4",dwidth/20,dheight/1.6)
                dcanvas.coords("entry5",dwidth/3.52,dheight/1.6)
                dcanvas.coords("entry6",dwidth/3.52,dheight/1.38)
                dcanvas.coords("entry7",dwidth/1.94,dheight/1.38)
                dcanvas.coords("entry8",dwidth/20,dheight/1.21)
                dcanvas.coords("entry9",dwidth/3.52,dheight/1.21)
                dcanvas.coords("entry10",dwidth/1.94,dheight/1.21)
                dcanvas.coords("entry11",dwidth/20,dheight/0.96)
                dcanvas.coords("entry12",dwidth/1.95,dheight/0.96)
                dcanvas.coords("entry13",dwidth/20,dheight/0.81)
                dcanvas.coords("entry14",dwidth/3.23,dheight/0.81)
                dcanvas.coords("entry15",dwidth/1.94,dheight/0.81)
                dcanvas.coords("entry16",dwidth/1.296,dheight/0.81)
                dcanvas.coords("entry17",dwidth/20,dheight/0.749)
                dcanvas.coords("entry18",dwidth/3.23,dheight/0.749)
                dcanvas.coords("entry19",dwidth/1.94,dheight/0.749)
                dcanvas.coords("entry20",dwidth/1.296,dheight/0.749)

                dcanvas.coords("check1",dwidth/1.45,dheight/1.11)
                dcanvas.coords("check2",dwidth/20,dheight/0.72)

                dcanvas.coords("button1",dwidth/2,dheight/0.655)
                dcanvas.coords("button2",dwidth/27,dheight/3)

            sr_Canvas_2 = Canvas(sr_Frame_2,bg='#2f516f',scrollregion=(0,0,700,1200))

            sr_Frame_2.grid_columnconfigure(0,weight=1)
            sr_Frame_2.grid_rowconfigure(0,weight=1)

            sr_Scroll_2 = Scrollbar(sr_Frame_2,orient=VERTICAL)
            sr_Scroll_2.grid(row=0,column=1,sticky='ns')
            sr_Scroll_2.config(command=sr_Canvas_2.yview)
            sr_Canvas_2.bind("<Configure>", responsive_widgets2)
            sr_Canvas_2.config(yscrollcommand=sr_Scroll_2.set)
            sr_Canvas_2.grid(row=0,column=0,sticky='nsew')

            sr_Canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly1"))
            cust_label1 = Label(sr_Canvas_2,width=18,height=1,text="ADD CUSTOMER",font=('arial 25'),background='#1b3857',fg="white")
            sr_Canvas_2.create_window(0,0,anchor="c",window=cust_label1,tags=("label1"))
            sr_Canvas_2.create_line(0,0,0,0,fill='gray',width=1,tags=("hline"))

            sr_Canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly2"))

            cust_label2 = Label(sr_Canvas_2,width=20,height=1,text="Customer Information",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label2,tags=('label2'))

            sr_Canvas_2.create_line(0,0,0,0,fill='gray',width=1,tags=("line1"))

            cust_label3 = Label(sr_Canvas_2,width=20,height=1,text="Title",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label3,tags=('label3'))

            cust_title = ttk.Combobox(sr_Canvas_2,width=19,font=('arial 15'))
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_title,tags=("combo1"))

            cust_label4 = Label(sr_Canvas_2,width=20,height=1,text="First name",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label4,tags=('label4'))

            cust_fname = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_fname,tags=("entry2"))

            cust_label5 = Label(sr_Canvas_2,width=20,height=1,text="Last name",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label5,tags=('label5'))

            cust_lname = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_lname,tags=("entry3"))

            cust_label6 = Label(sr_Canvas_2,width=20,height=1,text="Company",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label6,tags=('label6'))

            cust_company = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_company,tags=("entry4"))

            cust_label7 = Label(sr_Canvas_2,width=20,height=1,text="Location",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label7,tags=('label7'))

            cust_location = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_location,tags=("entry5"))

            cust_label8 = Label(sr_Canvas_2,width=20,height=1,text="GST type",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label8,tags=('label8'))

            cust_gtype = ttk.Combobox(sr_Canvas_2,width=19,font=('arial 15'))
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_gtype,tags=("combo2"))

            cust_label9 = Label(sr_Canvas_2,width=20,height=1,text="GSTIN",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label9,tags=('label9'))

            cust_gin = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_gin,tags=("entry6"))

            cust_label10 = Label(sr_Canvas_2,width=20,height=1,text="PAN NO",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label10,tags=('label10'))

            cust_pan = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pan,tags=("entry7"))

            cust_label11 = Label(sr_Canvas_2,width=20,height=1,text="Email",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label11,tags=('label11'))

            cust_email = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_email,tags=("entry8"))

            cust_label12 = Label(sr_Canvas_2,width=20,height=1,text="Website",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label12,tags=('label12'))

            cust_web = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_web,tags=("entry9"))

            cust_label13 = Label(sr_Canvas_2,width=20,height=1,text="Mobile",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label13,tags=('label13'))

            cust_mob = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_mob,tags=("entry10"))

            cust_label14 = Label(sr_Canvas_2,width=20,height=1,text="Billing Address",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label14,tags=('label14'))

            cust_label15 = Label(sr_Canvas_2,width=20,height=1,text="Street",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label15,tags=('label15'))

            cust_st1 = scrolledtext.ScrolledText(sr_Canvas_2,width=66,height=4,background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_st1,tags=("entry11"))

            cust_label17 = Label(sr_Canvas_2,width=20,height=1,text="Shipping Address",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label17,tags=('label17'))

            cust_label16 = Label(sr_Canvas_2,width=20,height=1,text="Street",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label16,tags=('label16'))

            cust_st2 = scrolledtext.ScrolledText(sr_Canvas_2,width=66,height=4,background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_st2,tags=("entry12"))

            cust_label18 = Label(sr_Canvas_2,width=20,height=1,text="City",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label18,tags=('label18'))

            cust_city = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_city,tags=("entry13"))

            cust_label19 = Label(sr_Canvas_2,width=20,height=1,text="State",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label19,tags=('label19'))

            cust_state = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_state,tags=("entry14"))

            cust_label20 = Label(sr_Canvas_2,width=20,height=1,text="City",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label20,tags=('label20'))

            cust_city1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_city1,tags=("entry15"))

            cust_label21 = Label(sr_Canvas_2,width=20,height=1,text="State",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label21,tags=('label21'))

            cust_state1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_state1,tags=("entry16"))
            #--
            cust_label22 = Label(sr_Canvas_2,width=20,height=1,text="Pin code",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label22,tags=('label22'))

            cust_pin = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pin,tags=("entry17"))

            cust_label23 = Label(sr_Canvas_2,width=20,height=1,text="Country",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label23,tags=('label23'))

            cust_country = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_country,tags=("entry18"))

            cust_label24 = Label(sr_Canvas_2,width=20,height=1,text="Pin code",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label24,tags=('label24'))

            cust_pin1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pin1,tags=("entry19"))

            cust_label25 = Label(sr_Canvas_2,width=20,height=1,text="Country",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label25,tags=('label25'))

            cust_country1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_country1,tags=("entry20"))

            cust_sameb = Checkbutton(sr_Canvas_2,onvalue=1,offvalue=0,background='#1b3857',activebackground="#1b3857")
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_sameb,tags=("check1"))

            cust_label26 = Label(sr_Canvas_2,width=20,height=1,text="Same as billing address",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label26,tags=('label26'))

            cust_term = Checkbutton(sr_Canvas_2,onvalue=1,offvalue=0,background='#1b3857',activebackground="#1b3857")
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_term,tags=("check2"))

            cust_label27 = Label(sr_Canvas_2,width=25,height=1,text="Agree to terms and conditions",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label27,tags=('label27'))
            
            cust_save = Button(sr_Canvas_2,text="Save",font=('arial 12 bold'),width=40,height=2,background="#198fed",activebackground="#198fed",foreground="white",activeforeground="white",bd=0)
            sr_Canvas_2.create_window(0,0,window=cust_save,tags=("button1"))

            def cm_goBack1():
                sr_Frame_2.grid_forget()
                sr_Frame_1.grid(row=0,column=0,sticky='nsew')

            back_btn = Button(sr_Canvas_2,text='←  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:cm_goBack1())
            sr_Canvas_2.create_window(0,0,window=back_btn,tags=("button2"))

        cm_plus = Button(sr_Canvas_1,text='+',font=('arial 10 bold'),foreground='white',activebackground='#1b3857',background='#1b3857',padx=7,command=lambda:sr_addCustomer_1())
        sr_Canvas_1.create_window(0,0,window=cm_plus,tags=("button5"))

        cm_label4 = Label(sr_Canvas_1,width=10,height=1,text="Email",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(0,0,window=cm_label4,tags=('label22'))

        cm_email = Entry(sr_Canvas_1,width=20,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cm_email,tags=("entry13"))

        cm_label5 = Label(sr_Canvas_1,width=20,height=1,text="Billing Address",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(0,0,window=cm_label5,tags=('label23'))

        cm_baddress = Text(sr_Canvas_1,width=20,font=('arial 15'),height=7,background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cm_baddress,tags=("entry14"))

        cm_label7 = Label(sr_Canvas_1,width=20,height=1,text="Place of Supply",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(0,0,window=cm_label7,tags=('label25'))

        cm_pofsupply = ttk.Combobox(sr_Canvas_1,width=19,font=('arial 15'),background='#2f516f')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cm_pofsupply,tags=("entry15"))

        cm_label8 = Label(sr_Canvas_1,width=20,height=1,text="Payment Method",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(0,0,window=cm_label8,tags=('label26'))

        def addnew_pmethod_1(event):
            if cm_pmethod.get() == "Add new":
                sr_Canvas_1.itemconfig("entry26",state='normal')
            else:
                sr_Canvas_1.itemconfig("entry26",state='hidden')

        cm_pmethod = ttk.Combobox(sr_Canvas_1,width=19,font=('arial 15'),background='#2f516f')
        cm_pmethod['values'] = ['Add new','',]
        cm_pmethod.current(0)
        cm_pmethod.bind("<<ComboboxSelected>>",addnew_pmethod_1)
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cm_pmethod,tags=("entry16"))

        cm_newmeth = Entry(sr_Canvas_1,width=20,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(115,755,anchor='nw',state=HIDDEN,window=cm_newmeth,tags=("entry26"))

        cm_label9 = Label(sr_Canvas_1,width=20,height=1,text="Reference No:",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(0,0,window=cm_label9,tags=('label27'))

        cm_ref = Entry(sr_Canvas_1,width=20,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cm_ref,tags=("entry17"))

        cm_label10 = Label(sr_Canvas_1,width=20,height=1,text="Deposit to:",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(0,0,window=cm_label10,tags=('label28'))

        cm_depto = ttk.Combobox(sr_Canvas_1,width=15,font=('arial 15'),background='#2f516f')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cm_depto,tags=("combo4"))

        def add_depositTo_1():
            sr_Frame_1.grid_forget()
            sr_Frame_3 = Frame(tab3_1,)
            sr_Frame_3.grid(row=0,column=0,sticky='nsew')

            def responsive_widgets3(event):
                dwidth = event.width
                dheight = event.height
                dcanvas = event.widget

                r1 = 25
                x1 = dwidth/63
                x2 = dwidth/1.021
                y1 = dheight/14 
                y2 = dheight/3.505

                dcanvas.coords("poly1",x1 + r1,y1,
                x1 + r1,y1,
                x2 - r1,y1,
                x2 - r1,y1,     
                x2,y1,     
                #--------------------
                x2,y1 + r1,     
                x2,y1 + r1,     
                x2,y2 - r1,     
                x2,y2 - r1,     
                x2,y2,
                #--------------------
                x2 - r1,y2,     
                x2 - r1,y2,     
                x1 + r1,y2,
                x1 + r1,y2,
                x1,y2,
                #--------------------
                x1,y2 - r1,
                x1,y2 - r1,
                x1,y1 + r1,
                x1,y1 + r1,
                x1,y1,
                )

                dcanvas.coords("hline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
                
                r2 = 25
                x11 = dwidth/63
                x21 = dwidth/1.021
                y11 = dheight/2.8
                y21 = dheight/0.9


                dcanvas.coords("poly2",x11 + r2,y11,
                x11 + r2,y11,
                x21 - r2,y11,
                x21 - r2,y11,     
                x21,y11,     
                #--------------------
                x21,y11 + r2,     
                x21,y11 + r2,     
                x21,y21 - r2,     
                x21,y21 - r2,     
                x21,y21,
                #--------------------
                x21 - r2,y21,     
                x21 - r2,y21,     
                x11 + r2,y21,
                x11 + r2,y21,
                x11,y21,
                #--------------------
                x11,y21 - r2,
                x11,y21 - r2,
                x11,y11 + r2,
                x11,y11 + r2,
                x11,y11,
                )

                dcanvas.coords("label1",dwidth/2,dheight/8.24)
                dcanvas.coords("label2",dwidth/8.2,dheight/2.44)
                dcanvas.coords("label3",dwidth/1.655,dheight/2.44)
                dcanvas.coords("label4",dwidth/8.2,dheight/1.89)
                dcanvas.coords("label5",dwidth/1.655,dheight/1.89)
                dcanvas.coords("label6",dwidth/1.605,dheight/1.522)
                dcanvas.coords("label7",dwidth/1.655,dheight/1.27)

                dcanvas.coords("entry1",dwidth/20,dheight/2.32)
                dcanvas.coords("entry2",dwidth/1.88,dheight/2.32)
                dcanvas.coords("entry3",dwidth/20,dheight/1.8)
                dcanvas.coords("entry4",dwidth/1.88,dheight/1.805)
                dcanvas.coords("entry5",dwidth/20,dheight/1.605)
                dcanvas.coords("entry6",dwidth/1.88,dheight/1.46)
                dcanvas.coords("entry7",dwidth/1.88,dheight/1.23)

                dcanvas.coords("check1",dwidth/1.89,dheight/1.57)

                dcanvas.coords("button1",dwidth/2,dheight/0.97)
                dcanvas.coords("button2",dwidth/27,dheight/3)

            sr_Canvas_3 = Canvas(sr_Frame_3,bg='#2f516f',scrollregion=(0,0,700,1200))

            sr_Frame_3.grid_columnconfigure(0,weight=1)
            sr_Frame_3.grid_rowconfigure(0,weight=1)

            sr_Scroll_2 = Scrollbar(sr_Frame_3,orient=VERTICAL)
            sr_Scroll_2.grid(row=0,column=1,sticky='ns')
            sr_Scroll_2.config(command=sr_Canvas_3.yview)
            sr_Canvas_3.bind("<Configure>", responsive_widgets3)
            sr_Canvas_3.config(yscrollcommand=sr_Scroll_2.set)
            sr_Canvas_3.grid(row=0,column=0,sticky='nsew')

            sr_Canvas_3.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly1"))
            dep_label1 = Label(sr_Canvas_3,width=18,height=1,text="ACCOUNT CREATE",font=('arial 25'),background='#1b3857',fg="white")
            sr_Canvas_3.create_window(0,0,anchor="c",window=dep_label1,tags=("label1"))
            sr_Canvas_3.create_line(0,0,0,0,fill='gray',width=1,tags=("hline"))

            sr_Canvas_3.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly2"))

            dep_label2 = Label(sr_Canvas_3,width=20,height=1,text="Account type",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
            sr_Canvas_3.create_window(0,0,window=dep_label2,tags=("label2"))

            dep_acctype = ttk.Combobox(sr_Canvas_3,width=46,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_acctype,tags=("entry1"))

            dep_label3 = Label(sr_Canvas_3,width=20,height=1,text="*Name",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
            sr_Canvas_3.create_window(0,0,window=dep_label3,tags=("label3"))

            dep_name = Entry(sr_Canvas_3,width=47,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_name,tags=("entry2"))

            dep_label4 = Label(sr_Canvas_3,width=20,height=1,text="*Detail Type",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
            sr_Canvas_3.create_window(0,0,window=dep_label4,tags=("label4"))

            dep_dtype = ttk.Combobox(sr_Canvas_3,width=46,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_dtype,tags=("entry3"))

            dep_label5 = Label(sr_Canvas_3,width=20,height=1,text="Description",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
            sr_Canvas_3.create_window(0,0,window=dep_label5,tags=("label5"))

            dep_desp = Entry(sr_Canvas_3,width=47,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_desp,tags=("entry4"))

            dep_term = Text(sr_Canvas_3,width=47,font=('arial 15'),height=7,background='#2f516f',foreground='white')
            term_txt = "Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills."
            dep_term.insert('1.0',term_txt)
            dep_term.config(state=DISABLED)
            sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_term,tags=("entry5"))

            def sr_subAccount():
                if subaccVar.get() == True:
                    dep_subacc["state"] = NORMAL
                else:
                    dep_subacc["state"] = DISABLED

            subaccVar = BooleanVar()
            dep_subcheck = Checkbutton(sr_Canvas_3,variable=subaccVar,onvalue=1,offvalue=0,background='#1b3857',activebackground="#1b3857",command=sr_subAccount)
            sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_subcheck,tags=("check1"))

            dep_label6 = Label(sr_Canvas_3,width=20,height=1,text="Is sub-account",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
            sr_Canvas_3.create_window(0,0,window=dep_label6,tags=("label6"))

            dep_subacc = ttk.Combobox(sr_Canvas_3,width=46,font=('arial 15'),background='#2f516f',foreground='white',state=DISABLED)
            sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_subacc,tags=("entry6"))

            dep_label7 = Label(sr_Canvas_3,width=20,height=1,text="Default Tax Code",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
            sr_Canvas_3.create_window(0,0,window=dep_label7,tags=("label7"))

            dep_dtaxcode = Entry(sr_Canvas_3,width=47,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_dtaxcode,tags=("entry7"))

            dep_save = Button(sr_Canvas_3,text="Create",font=('arial 12 bold'),width=35,height=2,background="#198fed",activebackground="#198fed",foreground="white",activeforeground="white",bd=0)
            sr_Canvas_3.create_window(0,0,window=dep_save,tags=("button1"))

            def goBack2():
                sr_Frame_3.grid_forget()
                sr_Frame_1.grid(row=0,column=0,sticky='nsew')

            back_btn = Button(sr_Canvas_3,text='←  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:goBack2())
            sr_Canvas_3.create_window(0,0,window=back_btn,tags=("button2"))

        cm_plus1 = Button(sr_Canvas_1,text='+',font=('arial 10 bold'),foreground='white',activebackground='#1b3857',background='#1b3857',padx=7,command=lambda:add_depositTo_1())
        sr_Canvas_1.create_window(0,0,window=cm_plus1,tags=("button6"))

        cm_label11 = Label(sr_Canvas_1,width=20,height=1,text="AMOUNT",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(0,0,window=cm_label11,tags=('label29'))

        cm_label12 = Label(sr_Canvas_1,width=20,height=1,text="0.00",font=('arial 14'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(0,0,window=cm_label12,tags=('label30'))

        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line17"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line18"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line19"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line20"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line21"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line22"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line23"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line24"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line25"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line26"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line27"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line28"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line29"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line30"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line31"))

        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line32"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line33"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line34"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line35"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line36"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line37"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line38"))

        cm_label13 = Label(sr_Canvas_1,width=3,height=1,text="#",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=cm_label13,tags=('label31'))

        cm_label14 = Label(sr_Canvas_1,width=3,height=1,text="1",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=cm_label14,tags=('label32'))

        cm_label18 = Label(sr_Canvas_1,width=15,height=1,text="Product / Service",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=cm_label18,tags=('label33'))

        cm_label19 = Label(sr_Canvas_1,width=14,height=1,text="HSN",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=cm_label19,tags=('label34'))

        cm_label20 = Label(sr_Canvas_1,width=18,height=1,text="Description",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=cm_label20,tags=('label35'))

        cm_label21 = Label(sr_Canvas_1,width=10,height=1,text="Qty",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=cm_label21,tags=('label36'))

        cm_label22 = Label(sr_Canvas_1,width=10,height=1,text="Price",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=cm_label22,tags=('label37'))

        cm_label23 = Label(sr_Canvas_1,width=10,height=1,text="Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=cm_label23,tags=('label38'))

        cm_label24 = Label(sr_Canvas_1,width=10,height=1,text="Tax (%)",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=cm_label24,tags=('label39'))

        cmt_entry1 = ttk.Combobox(sr_Canvas_1,width=10,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='c',window=cmt_entry1,tags=("combo5"))

        cmt_entry2 = Entry(sr_Canvas_1,width=11,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cmt_entry2,tags=("entry18"))

        cmt_entry3 = Entry(sr_Canvas_1,width=17,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cmt_entry3,tags=("entry19"))

        cmt_entry4 = Entry(sr_Canvas_1,width=10,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cmt_entry4,tags=("entry20"))

        cmt_entry5 = Entry(sr_Canvas_1,width=14,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cmt_entry5,tags=("entry21"))

        cmt_entry6 = Entry(sr_Canvas_1,width=13,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cmt_entry6,tags=("entry22"))

        cmt_entry7 = ttk.Combobox(sr_Canvas_1,width=7,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='c',window=cmt_entry7,tags=("combo6"))

        cm_label25 = Label(sr_Canvas_1,width=10,height=1,text="Sub Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=cm_label25,tags=('label40'))

        cm_label26 = Label(sr_Canvas_1,width=10,height=1,text="Tax Amount",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=cm_label26,tags=('label41'))

        cm_label27 = Label(sr_Canvas_1,width=10,height=1,text="Grand Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=cm_label27,tags=('label42'))

        cmt_entry8 = Entry(sr_Canvas_1,width=24,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cmt_entry8,tags=("entry23"))

        cmt_entry9 = Entry(sr_Canvas_1,width=24,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cmt_entry9,tags=("entry24"))

        cmt_entry10 = Entry(sr_Canvas_1,width=24,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cmt_entry10,tags=("entry25"))

        save_btn = Button(sr_Canvas_1,text='Save',width=20,height=2,font=('arial 10 bold'),background="#198fed",activebackground="#198fed",foreground="white",activeforeground="white",bd=0)
        sr_Canvas_1.create_window(0,0,window=save_btn,tags=("button7")) 

        def sr_goBack():
            sr_Frame_1.grid_forget()
            sr_Frame.grid(row=0,column=0,sticky='nsew')

        back_btn = Button(sr_Canvas_1,text='←  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:sr_goBack())
        sr_Canvas_1.create_window(0,0,window=back_btn,tags=("button3"))
        #--------------
        cm_label6 = Label(sr_Canvas_1,width=20,height=1,text="Sales receipt date:",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(0,0,window=cm_label6,tags=('label24'))

        cwidth = root.winfo_screenwidth()

        cm_srdate = DateEntry(sr_Canvas_1,width=19,font=('arial 15'),background='#2f516f',foreground='white')
        if cwidth > 1280:
            sr_Canvas_1.create_window(495,442,anchor='nw',window=cm_srdate,tags=("date"))
        elif cwidth <= 1024:
            sr_Canvas_1.create_window(370,455,anchor='nw',window=cm_srdate,tags=("date"))
        else:
            sr_Canvas_1.create_window(465,407,anchor='nw',window=cm_srdate,tags=("date"))
    elif sr_transCombo.get() == 'Credit Note': 
        sr_Canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly1"))
        cn_label1 = Label(sr_Canvas_1,width=18,height=1,text="CREDIT NOTE",font=('arial 25'),background='#1b3857',fg="white")
        sr_Canvas_1.create_window(0,0,anchor="c",window=cn_label1,tags=("label1"))
        sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("hline"))

        sr_Canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly3"))   

        cn_label2 = Label(sr_Canvas_1,width=18,height=1,text="Fin sYs",font=('arial 25'),background='#1b3857',fg="white")
        sr_Canvas_1.create_window(0,0,anchor="c",window=cn_label2,tags=("label2"))

        cn_label3 = Label(sr_Canvas_1,width=10,height=1,text="Customer",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
        sr_Canvas_1.create_window(0,0,window=cn_label3,tags=("label21"))

        cn_custCombo = ttk.Combobox(sr_Canvas_1,width=15,font=('arial 15'))
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cn_custCombo,tags=("combo3"))

        def sr_addCustomer_1():
            sr_Frame_1.grid_forget()
            sr_Frame_2 = Frame(tab3_1,)
            sr_Frame_2.grid(row=0,column=0,sticky='nsew')

            def responsive_widgets2(event):
                dwidth = event.width
                dheight = event.height
                dcanvas = event.widget
                
                r1 = 25
                x1 = dwidth/63
                x2 = dwidth/1.021
                y1 = dheight/14 
                y2 = dheight/3.505

                dcanvas.coords("poly1",x1 + r1,y1,
                x1 + r1,y1,
                x2 - r1,y1,
                x2 - r1,y1,     
                x2,y1,     
                #--------------------
                x2,y1 + r1,     
                x2,y1 + r1,     
                x2,y2 - r1,     
                x2,y2 - r1,     
                x2,y2,
                #--------------------
                x2 - r1,y2,     
                x2 - r1,y2,     
                x1 + r1,y2,
                x1 + r1,y2,
                x1,y2,
                #--------------------
                x1,y2 - r1,
                x1,y2 - r1,
                x1,y1 + r1,
                x1,y1 + r1,
                x1,y1,
                )

                dcanvas.coords("hline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
                
                r2 = 25
                x11 = dwidth/63
                x21 = dwidth/1.021
                y11 = dheight/2.8
                y21 = dheight/0.6


                dcanvas.coords("poly2",x11 + r2,y11,
                x11 + r2,y11,
                x21 - r2,y11,
                x21 - r2,y11,     
                x21,y11,     
                #--------------------
                x21,y11 + r2,     
                x21,y11 + r2,     
                x21,y21 - r2,     
                x21,y21 - r2,     
                x21,y21,
                #--------------------
                x21 - r2,y21,     
                x21 - r2,y21,     
                x11 + r2,y21,
                x11 + r2,y21,
                x11,y21,
                #--------------------
                x11,y21 - r2,
                x11,y21 - r2,
                x11,y11 + r2,
                x11,y11 + r2,
                x11,y11,
                )

                dcanvas.coords("label1",dwidth/2,dheight/8.24)
                dcanvas.coords("label2",dwidth/6,dheight/2.4)
                dcanvas.coords("label3",dwidth/8.2,dheight/2)
                dcanvas.coords("label4",dwidth/2.8,dheight/2)
                dcanvas.coords("label5",dwidth/1.7,dheight/2)
                dcanvas.coords("label6",dwidth/8.2,dheight/1.66)
                dcanvas.coords("label7",dwidth/2.8,dheight/1.66)
                dcanvas.coords("label8",dwidth/8.2,dheight/1.42)
                dcanvas.coords("label9",dwidth/2.8,dheight/1.42)
                dcanvas.coords("label10",dwidth/1.7,dheight/1.42)
                dcanvas.coords("label11",dwidth/8.2,dheight/1.24)
                dcanvas.coords("label12",dwidth/2.8,dheight/1.24)
                dcanvas.coords("label13",dwidth/1.7,dheight/1.24)
                dcanvas.coords("label14",dwidth/5.97,dheight/1.09)
                dcanvas.coords("label15",dwidth/8.2,dheight/0.98)
                dcanvas.coords("label16",dwidth/1.71,dheight/0.98)
                dcanvas.coords("label17",dwidth/1.58,dheight/1.09)
                dcanvas.coords("label18",dwidth/8.2,dheight/0.824)
                dcanvas.coords("label19",dwidth/2.62,dheight/0.824)
                dcanvas.coords("label20",dwidth/1.7,dheight/0.824)
                dcanvas.coords("label21",dwidth/1.185,dheight/0.824)
                dcanvas.coords("label22",dwidth/8.2,dheight/0.76)
                dcanvas.coords("label23",dwidth/2.62,dheight/0.76)
                dcanvas.coords("label24",dwidth/1.7,dheight/0.76)
                dcanvas.coords("label25",dwidth/1.185,dheight/0.76)
                dcanvas.coords("label26",dwidth/1.28,dheight/1.087)
                dcanvas.coords("label27",dwidth/6.3,dheight/0.709)

                dcanvas.coords("line1",dwidth/21,dheight/2.2,dwidth/1.055,dheight/2.2)

                dcanvas.coords("combo1",dwidth/20,dheight/1.9)
                dcanvas.coords("combo2",dwidth/20,dheight/1.37)

                dcanvas.coords("entry2",dwidth/3.52,dheight/1.9)
                dcanvas.coords("entry3",dwidth/1.94,dheight/1.9)
                dcanvas.coords("entry4",dwidth/20,dheight/1.6)
                dcanvas.coords("entry5",dwidth/3.52,dheight/1.6)
                dcanvas.coords("entry6",dwidth/3.52,dheight/1.38)
                dcanvas.coords("entry7",dwidth/1.94,dheight/1.38)
                dcanvas.coords("entry8",dwidth/20,dheight/1.21)
                dcanvas.coords("entry9",dwidth/3.52,dheight/1.21)
                dcanvas.coords("entry10",dwidth/1.94,dheight/1.21)
                dcanvas.coords("entry11",dwidth/20,dheight/0.96)
                dcanvas.coords("entry12",dwidth/1.95,dheight/0.96)
                dcanvas.coords("entry13",dwidth/20,dheight/0.81)
                dcanvas.coords("entry14",dwidth/3.23,dheight/0.81)
                dcanvas.coords("entry15",dwidth/1.94,dheight/0.81)
                dcanvas.coords("entry16",dwidth/1.296,dheight/0.81)
                dcanvas.coords("entry17",dwidth/20,dheight/0.749)
                dcanvas.coords("entry18",dwidth/3.23,dheight/0.749)
                dcanvas.coords("entry19",dwidth/1.94,dheight/0.749)
                dcanvas.coords("entry20",dwidth/1.296,dheight/0.749)

                dcanvas.coords("check1",dwidth/1.45,dheight/1.11)
                dcanvas.coords("check2",dwidth/20,dheight/0.72)

                dcanvas.coords("button1",dwidth/2,dheight/0.655)
                dcanvas.coords("button2",dwidth/27,dheight/3)

            sr_Canvas_2 = Canvas(sr_Frame_2,bg='#2f516f',scrollregion=(0,0,700,1200))

            sr_Frame_2.grid_columnconfigure(0,weight=1)
            sr_Frame_2.grid_rowconfigure(0,weight=1)

            sr_Scroll_2 = Scrollbar(sr_Frame_2,orient=VERTICAL)
            sr_Scroll_2.grid(row=0,column=1,sticky='ns')
            sr_Scroll_2.config(command=sr_Canvas_2.yview)
            sr_Canvas_2.bind("<Configure>", responsive_widgets2)
            sr_Canvas_2.config(yscrollcommand=sr_Scroll_2.set)
            sr_Canvas_2.grid(row=0,column=0,sticky='nsew')

            sr_Canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly1"))
            cust_label1 = Label(sr_Canvas_2,width=18,height=1,text="ADD CUSTOMER",font=('arial 25'),background='#1b3857',fg="white")
            sr_Canvas_2.create_window(0,0,anchor="c",window=cust_label1,tags=("label1"))
            sr_Canvas_2.create_line(0,0,0,0,fill='gray',width=1,tags=("hline"))

            sr_Canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly2"))

            cust_label2 = Label(sr_Canvas_2,width=20,height=1,text="Customer Information",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label2,tags=('label2'))

            sr_Canvas_2.create_line(0,0,0,0,fill='gray',width=1,tags=("line1"))

            cust_label3 = Label(sr_Canvas_2,width=20,height=1,text="Title",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label3,tags=('label3'))

            cust_title = ttk.Combobox(sr_Canvas_2,width=19,font=('arial 15'))
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_title,tags=("combo1"))

            cust_label4 = Label(sr_Canvas_2,width=20,height=1,text="First name",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label4,tags=('label4'))

            cust_fname = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_fname,tags=("entry2"))

            cust_label5 = Label(sr_Canvas_2,width=20,height=1,text="Last name",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label5,tags=('label5'))

            cust_lname = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_lname,tags=("entry3"))

            cust_label6 = Label(sr_Canvas_2,width=20,height=1,text="Company",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label6,tags=('label6'))

            cust_company = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_company,tags=("entry4"))

            cust_label7 = Label(sr_Canvas_2,width=20,height=1,text="Location",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label7,tags=('label7'))

            cust_location = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_location,tags=("entry5"))

            cust_label8 = Label(sr_Canvas_2,width=20,height=1,text="GST type",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label8,tags=('label8'))

            cust_gtype = ttk.Combobox(sr_Canvas_2,width=19,font=('arial 15'))
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_gtype,tags=("combo2"))

            cust_label9 = Label(sr_Canvas_2,width=20,height=1,text="GSTIN",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label9,tags=('label9'))

            cust_gin = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_gin,tags=("entry6"))

            cust_label10 = Label(sr_Canvas_2,width=20,height=1,text="PAN NO",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label10,tags=('label10'))

            cust_pan = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pan,tags=("entry7"))

            cust_label11 = Label(sr_Canvas_2,width=20,height=1,text="Email",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label11,tags=('label11'))

            cust_email = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_email,tags=("entry8"))

            cust_label12 = Label(sr_Canvas_2,width=20,height=1,text="Website",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label12,tags=('label12'))

            cust_web = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_web,tags=("entry9"))

            cust_label13 = Label(sr_Canvas_2,width=20,height=1,text="Mobile",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label13,tags=('label13'))

            cust_mob = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_mob,tags=("entry10"))

            cust_label14 = Label(sr_Canvas_2,width=20,height=1,text="Billing Address",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label14,tags=('label14'))

            cust_label15 = Label(sr_Canvas_2,width=20,height=1,text="Street",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label15,tags=('label15'))

            cust_st1 = scrolledtext.ScrolledText(sr_Canvas_2,width=66,height=4,background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_st1,tags=("entry11"))

            cust_label17 = Label(sr_Canvas_2,width=20,height=1,text="Shipping Address",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label17,tags=('label17'))

            cust_label16 = Label(sr_Canvas_2,width=20,height=1,text="Street",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label16,tags=('label16'))

            cust_st2 = scrolledtext.ScrolledText(sr_Canvas_2,width=66,height=4,background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_st2,tags=("entry12"))

            cust_label18 = Label(sr_Canvas_2,width=20,height=1,text="City",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label18,tags=('label18'))

            cust_city = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_city,tags=("entry13"))

            cust_label19 = Label(sr_Canvas_2,width=20,height=1,text="State",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label19,tags=('label19'))

            cust_state = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_state,tags=("entry14"))

            cust_label20 = Label(sr_Canvas_2,width=20,height=1,text="City",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label20,tags=('label20'))

            cust_city1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_city1,tags=("entry15"))

            cust_label21 = Label(sr_Canvas_2,width=20,height=1,text="State",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label21,tags=('label21'))

            cust_state1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_state1,tags=("entry16"))
            #--
            cust_label22 = Label(sr_Canvas_2,width=20,height=1,text="Pin code",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label22,tags=('label22'))

            cust_pin = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pin,tags=("entry17"))

            cust_label23 = Label(sr_Canvas_2,width=20,height=1,text="Country",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label23,tags=('label23'))

            cust_country = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_country,tags=("entry18"))

            cust_label24 = Label(sr_Canvas_2,width=20,height=1,text="Pin code",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label24,tags=('label24'))

            cust_pin1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pin1,tags=("entry19"))

            cust_label25 = Label(sr_Canvas_2,width=20,height=1,text="Country",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label25,tags=('label25'))

            cust_country1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_country1,tags=("entry20"))

            cust_sameb = Checkbutton(sr_Canvas_2,onvalue=1,offvalue=0,background='#1b3857',activebackground="#1b3857")
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_sameb,tags=("check1"))

            cust_label26 = Label(sr_Canvas_2,width=20,height=1,text="Same as billing address",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label26,tags=('label26'))

            cust_term = Checkbutton(sr_Canvas_2,onvalue=1,offvalue=0,background='#1b3857',activebackground="#1b3857")
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_term,tags=("check2"))

            cust_label27 = Label(sr_Canvas_2,width=25,height=1,text="Agree to terms and conditions",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label27,tags=('label27'))
            
            cust_save = Button(sr_Canvas_2,text="Save",font=('arial 12 bold'),width=40,height=2,background="#198fed",activebackground="#198fed",foreground="white",activeforeground="white",bd=0)
            sr_Canvas_2.create_window(0,0,window=cust_save,tags=("button1"))

            def cn_goBack1():
                sr_Frame_2.grid_forget()
                sr_Frame_1.grid(row=0,column=0,sticky='nsew')

            back_btn = Button(sr_Canvas_2,text='←  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:cn_goBack1())
            sr_Canvas_2.create_window(0,0,window=back_btn,tags=("button2"))

        cn_plus = Button(sr_Canvas_1,text='+',font=('arial 10 bold'),foreground='white',activebackground='#1b3857',background='#1b3857',padx=7,command=lambda:sr_addCustomer_1())
        sr_Canvas_1.create_window(0,0,window=cn_plus,tags=("button5"))

        cn_label4 = Label(sr_Canvas_1,width=10,height=1,text="Email",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(0,0,window=cn_label4,tags=('label22'))

        cn_email = Entry(sr_Canvas_1,width=20,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cn_email,tags=("entry13"))

        cn_label5 = Label(sr_Canvas_1,width=20,height=1,text="Billing Address",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(0,0,window=cn_label5,tags=('label23'))

        cn_baddress = Text(sr_Canvas_1,width=20,font=('arial 15'),height=7,background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cn_baddress,tags=("entry14"))

        cn_label7 = Label(sr_Canvas_1,width=20,height=1,text="Place of Supply",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(0,0,window=cn_label7,tags=('label25'))

        cn_pofsupply = ttk.Combobox(sr_Canvas_1,width=19,font=('arial 15'),background='#2f516f')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cn_pofsupply,tags=("entry15"))

        cn_label8 = Label(sr_Canvas_1,width=20,height=1,text="Invoice Period",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(0,0,window=cn_label8,tags=('label26'))

        cn_pmethod = ttk.Combobox(sr_Canvas_1,width=19,font=('arial 15'),background='#2f516f')
        cn_pmethod['values'] = ['Add new',]
        cn_pmethod.current(0)
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cn_pmethod,tags=("entry16"))

        cn_label9 = Label(sr_Canvas_1,width=20,height=1,text="Invoice No.",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(0,0,window=cn_label9,tags=('label27'))

        cn_ref = Entry(sr_Canvas_1,width=20,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cn_ref,tags=("entry17"))

        cn_label11 = Label(sr_Canvas_1,width=20,height=1,text="AMOUNT",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(0,0,window=cn_label11,tags=('label29'))

        cn_label12 = Label(sr_Canvas_1,width=20,height=1,text="0.00",font=('arial 14'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(0,0,window=cn_label12,tags=('label30'))

        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line17"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line18"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line19"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line20"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line21"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line22"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line23"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line24"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line25"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line26"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line27"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line28"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line29"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line30"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line31"))

        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line32"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line33"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line34"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line35"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line36"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line37"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line38"))

        cn_label13 = Label(sr_Canvas_1,width=3,height=1,text="#",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=cn_label13,tags=('label31'))

        cn_label14 = Label(sr_Canvas_1,width=3,height=1,text="1",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=cn_label14,tags=('label32'))

        cn_label18 = Label(sr_Canvas_1,width=15,height=1,text="Product / Service",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=cn_label18,tags=('label33'))

        cn_label19 = Label(sr_Canvas_1,width=14,height=1,text="HSN",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=cn_label19,tags=('label34'))

        cn_label20 = Label(sr_Canvas_1,width=18,height=1,text="Description",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=cn_label20,tags=('label35'))

        cn_label21 = Label(sr_Canvas_1,width=10,height=1,text="Qty",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=cn_label21,tags=('label36'))

        cn_label22 = Label(sr_Canvas_1,width=10,height=1,text="Price",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=cn_label22,tags=('label37'))

        cn_label23 = Label(sr_Canvas_1,width=10,height=1,text="Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=cn_label23,tags=('label38'))

        cn_label24 = Label(sr_Canvas_1,width=10,height=1,text="Tax (%)",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=cn_label24,tags=('label39'))

        cnt_entry1 = ttk.Combobox(sr_Canvas_1,width=10,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='c',window=cnt_entry1,tags=("combo5"))

        cnt_entry2 = Entry(sr_Canvas_1,width=11,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cnt_entry2,tags=("entry18"))

        cnt_entry3 = Entry(sr_Canvas_1,width=17,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cnt_entry3,tags=("entry19"))

        cnt_entry4 = Entry(sr_Canvas_1,width=10,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cnt_entry4,tags=("entry20"))

        cnt_entry5 = Entry(sr_Canvas_1,width=14,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cnt_entry5,tags=("entry21"))

        cnt_entry6 = Entry(sr_Canvas_1,width=13,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cnt_entry6,tags=("entry22"))

        cnt_entry7 = ttk.Combobox(sr_Canvas_1,width=7,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='c',window=cnt_entry7,tags=("combo6"))

        cn_label25 = Label(sr_Canvas_1,width=10,height=1,text="Sub Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=cn_label25,tags=('label40'))

        cn_label26 = Label(sr_Canvas_1,width=10,height=1,text="Tax Amount",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=cn_label26,tags=('label41'))

        cn_label27 = Label(sr_Canvas_1,width=10,height=1,text="Grand Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=cn_label27,tags=('label42'))

        cnt_entry8 = Entry(sr_Canvas_1,width=24,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cnt_entry8,tags=("entry23"))

        cnt_entry9 = Entry(sr_Canvas_1,width=24,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cnt_entry9,tags=("entry24"))

        cnt_entry10 = Entry(sr_Canvas_1,width=24,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=cnt_entry10,tags=("entry25"))

        save_btn = Button(sr_Canvas_1,text='Save',width=20,height=2,font=('arial 10 bold'),background="#198fed",activebackground="#198fed",foreground="white",activeforeground="white",bd=0)
        sr_Canvas_1.create_window(0,0,window=save_btn,tags=("button7")) 

        def sr_goBack():
            sr_Frame_1.grid_forget()
            sr_Frame.grid(row=0,column=0,sticky='nsew')

        back_btn = Button(sr_Canvas_1,text='←  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:sr_goBack())
        sr_Canvas_1.create_window(0,0,window=back_btn,tags=("button3"))
        #--------------
        cn_label6 = Label(sr_Canvas_1,width=20,height=1,text="Credit Note Date",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(0,0,window=cn_label6,tags=('label24'))

        cwidth = root.winfo_screenwidth()

        cn_creditdate = DateEntry(sr_Canvas_1,width=19,font=('arial 15'),background='#2f516f',foreground='white')

        if cwidth > 1280:
            sr_Canvas_1.create_window(495,442,anchor='nw',window=cn_creditdate,tags=("date"))
        elif cwidth <= 1024:
            sr_Canvas_1.create_window(370,455,anchor='nw',window=cn_creditdate,tags=("date"))
        else:
            sr_Canvas_1.create_window(465,407,anchor='nw',window=cn_creditdate,tags=("date"))
    elif sr_transCombo.get() == "Estimate":
        sr_Canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly1"))
        es_label1 = Label(sr_Canvas_1,width=18,height=1,text="ESTIMATE",font=('arial 25'),background='#1b3857',fg="white")
        sr_Canvas_1.create_window(0,0,anchor="c",window=es_label1,tags=("label1"))
        sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("hline"))

        sr_Canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly3"))   

        es_label2 = Label(sr_Canvas_1,width=18,height=1,text="Fin sYs",font=('arial 25'),background='#1b3857',fg="white")
        sr_Canvas_1.create_window(0,0,anchor="c",window=es_label2,tags=("label2"))

        es_label3 = Label(sr_Canvas_1,width=10,height=1,text="Customer",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
        sr_Canvas_1.create_window(0,0,window=es_label3,tags=("label21"))

        es_custCombo = ttk.Combobox(sr_Canvas_1,width=15,font=('arial 15'))
        sr_Canvas_1.create_window(0,0,anchor='nw',window=es_custCombo,tags=("combo3"))

        def sr_addCustomer_1():
            sr_Frame_1.grid_forget()
            sr_Frame_2 = Frame(tab3_1,)
            sr_Frame_2.grid(row=0,column=0,sticky='nsew')

            def responsive_widgets2(event):
                dwidth = event.width
                dheight = event.height
                dcanvas = event.widget
                
                r1 = 25
                x1 = dwidth/63
                x2 = dwidth/1.021
                y1 = dheight/14 
                y2 = dheight/3.505

                dcanvas.coords("poly1",x1 + r1,y1,
                x1 + r1,y1,
                x2 - r1,y1,
                x2 - r1,y1,     
                x2,y1,     
                #--------------------
                x2,y1 + r1,     
                x2,y1 + r1,     
                x2,y2 - r1,     
                x2,y2 - r1,     
                x2,y2,
                #--------------------
                x2 - r1,y2,     
                x2 - r1,y2,     
                x1 + r1,y2,
                x1 + r1,y2,
                x1,y2,
                #--------------------
                x1,y2 - r1,
                x1,y2 - r1,
                x1,y1 + r1,
                x1,y1 + r1,
                x1,y1,
                )

                dcanvas.coords("hline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
                
                r2 = 25
                x11 = dwidth/63
                x21 = dwidth/1.021
                y11 = dheight/2.8
                y21 = dheight/0.6


                dcanvas.coords("poly2",x11 + r2,y11,
                x11 + r2,y11,
                x21 - r2,y11,
                x21 - r2,y11,     
                x21,y11,     
                #--------------------
                x21,y11 + r2,     
                x21,y11 + r2,     
                x21,y21 - r2,     
                x21,y21 - r2,     
                x21,y21,
                #--------------------
                x21 - r2,y21,     
                x21 - r2,y21,     
                x11 + r2,y21,
                x11 + r2,y21,
                x11,y21,
                #--------------------
                x11,y21 - r2,
                x11,y21 - r2,
                x11,y11 + r2,
                x11,y11 + r2,
                x11,y11,
                )

                dcanvas.coords("label1",dwidth/2,dheight/8.24)
                dcanvas.coords("label2",dwidth/6,dheight/2.4)
                dcanvas.coords("label3",dwidth/8.2,dheight/2)
                dcanvas.coords("label4",dwidth/2.8,dheight/2)
                dcanvas.coords("label5",dwidth/1.7,dheight/2)
                dcanvas.coords("label6",dwidth/8.2,dheight/1.66)
                dcanvas.coords("label7",dwidth/2.8,dheight/1.66)
                dcanvas.coords("label8",dwidth/8.2,dheight/1.42)
                dcanvas.coords("label9",dwidth/2.8,dheight/1.42)
                dcanvas.coords("label10",dwidth/1.7,dheight/1.42)
                dcanvas.coords("label11",dwidth/8.2,dheight/1.24)
                dcanvas.coords("label12",dwidth/2.8,dheight/1.24)
                dcanvas.coords("label13",dwidth/1.7,dheight/1.24)
                dcanvas.coords("label14",dwidth/5.97,dheight/1.09)
                dcanvas.coords("label15",dwidth/8.2,dheight/0.98)
                dcanvas.coords("label16",dwidth/1.71,dheight/0.98)
                dcanvas.coords("label17",dwidth/1.58,dheight/1.09)
                dcanvas.coords("label18",dwidth/8.2,dheight/0.824)
                dcanvas.coords("label19",dwidth/2.62,dheight/0.824)
                dcanvas.coords("label20",dwidth/1.7,dheight/0.824)
                dcanvas.coords("label21",dwidth/1.185,dheight/0.824)
                dcanvas.coords("label22",dwidth/8.2,dheight/0.76)
                dcanvas.coords("label23",dwidth/2.62,dheight/0.76)
                dcanvas.coords("label24",dwidth/1.7,dheight/0.76)
                dcanvas.coords("label25",dwidth/1.185,dheight/0.76)
                dcanvas.coords("label26",dwidth/1.28,dheight/1.087)
                dcanvas.coords("label27",dwidth/6.3,dheight/0.709)

                dcanvas.coords("line1",dwidth/21,dheight/2.2,dwidth/1.055,dheight/2.2)

                dcanvas.coords("combo1",dwidth/20,dheight/1.9)
                dcanvas.coords("combo2",dwidth/20,dheight/1.37)

                dcanvas.coords("entry2",dwidth/3.52,dheight/1.9)
                dcanvas.coords("entry3",dwidth/1.94,dheight/1.9)
                dcanvas.coords("entry4",dwidth/20,dheight/1.6)
                dcanvas.coords("entry5",dwidth/3.52,dheight/1.6)
                dcanvas.coords("entry6",dwidth/3.52,dheight/1.38)
                dcanvas.coords("entry7",dwidth/1.94,dheight/1.38)
                dcanvas.coords("entry8",dwidth/20,dheight/1.21)
                dcanvas.coords("entry9",dwidth/3.52,dheight/1.21)
                dcanvas.coords("entry10",dwidth/1.94,dheight/1.21)
                dcanvas.coords("entry11",dwidth/20,dheight/0.96)
                dcanvas.coords("entry12",dwidth/1.95,dheight/0.96)
                dcanvas.coords("entry13",dwidth/20,dheight/0.81)
                dcanvas.coords("entry14",dwidth/3.23,dheight/0.81)
                dcanvas.coords("entry15",dwidth/1.94,dheight/0.81)
                dcanvas.coords("entry16",dwidth/1.296,dheight/0.81)
                dcanvas.coords("entry17",dwidth/20,dheight/0.749)
                dcanvas.coords("entry18",dwidth/3.23,dheight/0.749)
                dcanvas.coords("entry19",dwidth/1.94,dheight/0.749)
                dcanvas.coords("entry20",dwidth/1.296,dheight/0.749)

                dcanvas.coords("check1",dwidth/1.45,dheight/1.11)
                dcanvas.coords("check2",dwidth/20,dheight/0.72)

                dcanvas.coords("button1",dwidth/2,dheight/0.655)
                dcanvas.coords("button2",dwidth/27,dheight/3)

            sr_Canvas_2 = Canvas(sr_Frame_2,bg='#2f516f',scrollregion=(0,0,700,1200))

            sr_Frame_2.grid_columnconfigure(0,weight=1)
            sr_Frame_2.grid_rowconfigure(0,weight=1)

            sr_Scroll_2 = Scrollbar(sr_Frame_2,orient=VERTICAL)
            sr_Scroll_2.grid(row=0,column=1,sticky='ns')
            sr_Scroll_2.config(command=sr_Canvas_2.yview)
            sr_Canvas_2.bind("<Configure>", responsive_widgets2)
            sr_Canvas_2.config(yscrollcommand=sr_Scroll_2.set)
            sr_Canvas_2.grid(row=0,column=0,sticky='nsew')

            sr_Canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly1"))
            cust_label1 = Label(sr_Canvas_2,width=18,height=1,text="ADD CUSTOMER",font=('arial 25'),background='#1b3857',fg="white")
            sr_Canvas_2.create_window(0,0,anchor="c",window=cust_label1,tags=("label1"))
            sr_Canvas_2.create_line(0,0,0,0,fill='gray',width=1,tags=("hline"))

            sr_Canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly2"))

            cust_label2 = Label(sr_Canvas_2,width=20,height=1,text="Customer Information",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label2,tags=('label2'))

            sr_Canvas_2.create_line(0,0,0,0,fill='gray',width=1,tags=("line1"))

            cust_label3 = Label(sr_Canvas_2,width=20,height=1,text="Title",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label3,tags=('label3'))

            cust_title = ttk.Combobox(sr_Canvas_2,width=19,font=('arial 15'))
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_title,tags=("combo1"))

            cust_label4 = Label(sr_Canvas_2,width=20,height=1,text="First name",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label4,tags=('label4'))

            cust_fname = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_fname,tags=("entry2"))

            cust_label5 = Label(sr_Canvas_2,width=20,height=1,text="Last name",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label5,tags=('label5'))

            cust_lname = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_lname,tags=("entry3"))

            cust_label6 = Label(sr_Canvas_2,width=20,height=1,text="Company",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label6,tags=('label6'))

            cust_company = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_company,tags=("entry4"))

            cust_label7 = Label(sr_Canvas_2,width=20,height=1,text="Location",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label7,tags=('label7'))

            cust_location = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_location,tags=("entry5"))

            cust_label8 = Label(sr_Canvas_2,width=20,height=1,text="GST type",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label8,tags=('label8'))

            cust_gtype = ttk.Combobox(sr_Canvas_2,width=19,font=('arial 15'))
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_gtype,tags=("combo2"))

            cust_label9 = Label(sr_Canvas_2,width=20,height=1,text="GSTIN",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label9,tags=('label9'))

            cust_gin = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_gin,tags=("entry6"))

            cust_label10 = Label(sr_Canvas_2,width=20,height=1,text="PAN NO",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label10,tags=('label10'))

            cust_pan = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pan,tags=("entry7"))

            cust_label11 = Label(sr_Canvas_2,width=20,height=1,text="Email",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label11,tags=('label11'))

            cust_email = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_email,tags=("entry8"))

            cust_label12 = Label(sr_Canvas_2,width=20,height=1,text="Website",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label12,tags=('label12'))

            cust_web = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_web,tags=("entry9"))

            cust_label13 = Label(sr_Canvas_2,width=20,height=1,text="Mobile",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label13,tags=('label13'))

            cust_mob = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_mob,tags=("entry10"))

            cust_label14 = Label(sr_Canvas_2,width=20,height=1,text="Billing Address",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label14,tags=('label14'))

            cust_label15 = Label(sr_Canvas_2,width=20,height=1,text="Street",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label15,tags=('label15'))

            cust_st1 = scrolledtext.ScrolledText(sr_Canvas_2,width=66,height=4,background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_st1,tags=("entry11"))

            cust_label17 = Label(sr_Canvas_2,width=20,height=1,text="Shipping Address",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label17,tags=('label17'))

            cust_label16 = Label(sr_Canvas_2,width=20,height=1,text="Street",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label16,tags=('label16'))

            cust_st2 = scrolledtext.ScrolledText(sr_Canvas_2,width=66,height=4,background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_st2,tags=("entry12"))

            cust_label18 = Label(sr_Canvas_2,width=20,height=1,text="City",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label18,tags=('label18'))

            cust_city = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_city,tags=("entry13"))

            cust_label19 = Label(sr_Canvas_2,width=20,height=1,text="State",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label19,tags=('label19'))

            cust_state = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_state,tags=("entry14"))

            cust_label20 = Label(sr_Canvas_2,width=20,height=1,text="City",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label20,tags=('label20'))

            cust_city1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_city1,tags=("entry15"))

            cust_label21 = Label(sr_Canvas_2,width=20,height=1,text="State",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label21,tags=('label21'))

            cust_state1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_state1,tags=("entry16"))
            #--
            cust_label22 = Label(sr_Canvas_2,width=20,height=1,text="Pin code",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label22,tags=('label22'))

            cust_pin = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pin,tags=("entry17"))

            cust_label23 = Label(sr_Canvas_2,width=20,height=1,text="Country",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label23,tags=('label23'))

            cust_country = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_country,tags=("entry18"))

            cust_label24 = Label(sr_Canvas_2,width=20,height=1,text="Pin code",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label24,tags=('label24'))

            cust_pin1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pin1,tags=("entry19"))

            cust_label25 = Label(sr_Canvas_2,width=20,height=1,text="Country",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label25,tags=('label25'))

            cust_country1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_country1,tags=("entry20"))

            cust_sameb = Checkbutton(sr_Canvas_2,onvalue=1,offvalue=0,background='#1b3857',activebackground="#1b3857")
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_sameb,tags=("check1"))

            cust_label26 = Label(sr_Canvas_2,width=20,height=1,text="Same as billing address",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label26,tags=('label26'))

            cust_term = Checkbutton(sr_Canvas_2,onvalue=1,offvalue=0,background='#1b3857',activebackground="#1b3857")
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_term,tags=("check2"))

            cust_label27 = Label(sr_Canvas_2,width=25,height=1,text="Agree to terms and conditions",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label27,tags=('label27'))
            
            cust_save = Button(sr_Canvas_2,text="Submit Form",font=('arial 12 bold'),width=40,height=2,background="#198fed",activebackground="#198fed",foreground="white",activeforeground="white",bd=0)
            sr_Canvas_2.create_window(0,0,window=cust_save,tags=("button1"))

            def es_goBack1():
                sr_Frame_2.grid_forget()
                sr_Frame_1.grid(row=0,column=0,sticky='nsew')

            back_btn = Button(sr_Canvas_2,text='←  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:es_goBack1())
            sr_Canvas_2.create_window(0,0,window=back_btn,tags=("button2"))

        es_plus = Button(sr_Canvas_1,text='+',font=('arial 10 bold'),foreground='white',activebackground='#1b3857',background='#1b3857',padx=7,command=lambda:sr_addCustomer_1())
        sr_Canvas_1.create_window(0,0,window=es_plus,tags=("button5"))

        es_label4 = Label(sr_Canvas_1,width=10,height=1,text="Email",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(0,0,window=es_label4,tags=('label22'))

        es_email = Entry(sr_Canvas_1,width=20,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=es_email,tags=("entry13"))

        es_label5 = Label(sr_Canvas_1,width=20,height=1,text="Billing Address",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(0,0,window=es_label5,tags=('label23'))

        es_baddress = Text(sr_Canvas_1,width=20,font=('arial 15'),height=7,background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=es_baddress,tags=("entry14"))

        es_label7 = Label(sr_Canvas_1,width=20,height=1,text="Place of Supply",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(0,0,window=es_label7,tags=('label25'))

        es_pofsupply = Entry(sr_Canvas_1,width=20,font=('arial 15'),background='#2f516f')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=es_pofsupply,tags=("entry15"))

        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line17"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line18"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line19"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line20"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line21"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line22"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line23"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line24"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line25"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line26"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line27"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line28"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line29"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line30"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line31"))

        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line32"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line33"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line34"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line35"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line36"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line37"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line38"))

        es_label13 = Label(sr_Canvas_1,width=3,height=1,text="#",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=es_label13,tags=('label31'))

        es_label14 = Label(sr_Canvas_1,width=3,height=1,text="1",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=es_label14,tags=('label32'))

        es_label18 = Label(sr_Canvas_1,width=15,height=1,text="Product / Service",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=es_label18,tags=('label33'))

        es_label19 = Label(sr_Canvas_1,width=14,height=1,text="HSN",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=es_label19,tags=('label34'))

        es_label20 = Label(sr_Canvas_1,width=18,height=1,text="Description",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=es_label20,tags=('label35'))

        es_label21 = Label(sr_Canvas_1,width=10,height=1,text="Qty",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=es_label21,tags=('label36'))

        es_label22 = Label(sr_Canvas_1,width=10,height=1,text="Price",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=es_label22,tags=('label37'))

        es_label23 = Label(sr_Canvas_1,width=10,height=1,text="Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=es_label23,tags=('label38'))

        es_label24 = Label(sr_Canvas_1,width=10,height=1,text="Tax (%)",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=es_label24,tags=('label39'))

        est_entry1 = ttk.Combobox(sr_Canvas_1,width=10,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='c',window=est_entry1,tags=("combo5"))

        est_entry2 = Entry(sr_Canvas_1,width=11,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry2,tags=("entry18"))

        est_entry3 = Entry(sr_Canvas_1,width=17,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry3,tags=("entry19"))

        est_entry4 = Entry(sr_Canvas_1,width=10,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry4,tags=("entry20"))

        est_entry5 = Entry(sr_Canvas_1,width=14,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry5,tags=("entry21"))

        est_entry6 = Entry(sr_Canvas_1,width=13,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry6,tags=("entry22"))

        est_entry7 = ttk.Combobox(sr_Canvas_1,width=7,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='c',window=est_entry7,tags=("combo6"))

        es_label25 = Label(sr_Canvas_1,width=10,height=1,text="Sub Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=es_label25,tags=('label40'))

        es_label26 = Label(sr_Canvas_1,width=10,height=1,text="Tax Amount",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=es_label26,tags=('label41'))

        es_label27 = Label(sr_Canvas_1,width=10,height=1,text="Estimate Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=es_label27,tags=('label42'))

        est_entry8 = Entry(sr_Canvas_1,width=24,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry8,tags=("entry23"))

        est_entry9 = Entry(sr_Canvas_1,width=24,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry9,tags=("entry24"))

        est_entry10 = Entry(sr_Canvas_1,width=24,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=est_entry10,tags=("entry25"))

        save_btn = Button(sr_Canvas_1,text='Save',width=20,height=2,font=('arial 10 bold'),background="#198fed",activebackground="#198fed",foreground="white",activeforeground="white",bd=0)
        sr_Canvas_1.create_window(0,0,window=save_btn,tags=("button7")) 

        def sr_goBack():
            sr_Frame_1.grid_forget()
            sr_Frame.grid(row=0,column=0,sticky='nsew')

        back_btn = Button(sr_Canvas_1,text='←  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:sr_goBack())
        sr_Canvas_1.create_window(0,0,window=back_btn,tags=("button3"))
        #--------------
        es_label6 = Label(sr_Canvas_1,width=20,height=1,text="Estimate Date",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(0,0,window=es_label6,tags=('label24'))

        es_label28 = Label(sr_Canvas_1,width=20,height=1,text="Expiration Date",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(0,0,window=es_label28,tags=('label43'))

        cwidth = root.winfo_screenwidth()

        es_creditdate = DateEntry(sr_Canvas_1,width=19,font=('arial 15'),background='#2f516f',foreground='white')

        es_expdate = DateEntry(sr_Canvas_1,width=19,font=('arial 15'),background='#2f516f',foreground='white') 

        if cwidth > 1280:
            sr_Canvas_1.create_window(495,442,anchor='nw',window=es_creditdate,tags=("date"))
            sr_Canvas_1.create_window(775,442,anchor='nw',window=es_expdate,tags=("date1"))
        elif cwidth <= 1024:
            sr_Canvas_1.create_window(370,455,anchor='nw',window=es_creditdate,tags=("date"))
            sr_Canvas_1.create_window(580,455,anchor='nw',window=es_expdate,tags=("date1"))
        else:
            sr_Canvas_1.create_window(465,407,anchor='nw',window=es_creditdate,tags=("date"))
            sr_Canvas_1.create_window(730,407,anchor='nw',window=es_expdate,tags=("date1"))
    elif sr_transCombo.get() == "Delayed Charge":
        sr_Canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly1"))
        dc_label1 = Label(sr_Canvas_1,width=18,height=1,text="DELAYED CHARGE",font=('arial 25'),background='#1b3857',fg="white")
        sr_Canvas_1.create_window(0,0,anchor="c",window=dc_label1,tags=("label1"))
        sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("hline"))

        sr_Canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly4"))   

        dc_label2 = Label(sr_Canvas_1,width=18,height=1,text="Fin sYs",font=('arial 25'),background='#1b3857',fg="white")
        sr_Canvas_1.create_window(0,0,anchor="c",window=dc_label2,tags=("label2"))

        dc_label3 = Label(sr_Canvas_1,width=10,height=1,text="Customer",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
        sr_Canvas_1.create_window(0,0,window=dc_label3,tags=("label21"))

        dc_custCombo = ttk.Combobox(sr_Canvas_1,width=15,font=('arial 15'))
        sr_Canvas_1.create_window(0,0,anchor='nw',window=dc_custCombo,tags=("combo3"))

        def sr_addCustomer_1():
            sr_Frame_1.grid_forget()
            sr_Frame_2 = Frame(tab3_1,)
            sr_Frame_2.grid(row=0,column=0,sticky='nsew')

            def responsive_widgets2(event):
                dwidth = event.width
                dheight = event.height
                dcanvas = event.widget
                
                r1 = 25
                x1 = dwidth/63
                x2 = dwidth/1.021
                y1 = dheight/14 
                y2 = dheight/3.505

                dcanvas.coords("poly1",x1 + r1,y1,
                x1 + r1,y1,
                x2 - r1,y1,
                x2 - r1,y1,     
                x2,y1,     
                #--------------------
                x2,y1 + r1,     
                x2,y1 + r1,     
                x2,y2 - r1,     
                x2,y2 - r1,     
                x2,y2,
                #--------------------
                x2 - r1,y2,     
                x2 - r1,y2,     
                x1 + r1,y2,
                x1 + r1,y2,
                x1,y2,
                #--------------------
                x1,y2 - r1,
                x1,y2 - r1,
                x1,y1 + r1,
                x1,y1 + r1,
                x1,y1,
                )

                dcanvas.coords("hline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
                
                r2 = 25
                x11 = dwidth/63
                x21 = dwidth/1.021
                y11 = dheight/2.8
                y21 = dheight/0.6


                dcanvas.coords("poly2",x11 + r2,y11,
                x11 + r2,y11,
                x21 - r2,y11,
                x21 - r2,y11,     
                x21,y11,     
                #--------------------
                x21,y11 + r2,     
                x21,y11 + r2,     
                x21,y21 - r2,     
                x21,y21 - r2,     
                x21,y21,
                #--------------------
                x21 - r2,y21,     
                x21 - r2,y21,     
                x11 + r2,y21,
                x11 + r2,y21,
                x11,y21,
                #--------------------
                x11,y21 - r2,
                x11,y21 - r2,
                x11,y11 + r2,
                x11,y11 + r2,
                x11,y11,
                )

                dcanvas.coords("label1",dwidth/2,dheight/8.24)
                dcanvas.coords("label2",dwidth/6,dheight/2.4)
                dcanvas.coords("label3",dwidth/8.2,dheight/2)
                dcanvas.coords("label4",dwidth/2.8,dheight/2)
                dcanvas.coords("label5",dwidth/1.7,dheight/2)
                dcanvas.coords("label6",dwidth/8.2,dheight/1.66)
                dcanvas.coords("label7",dwidth/2.8,dheight/1.66)
                dcanvas.coords("label8",dwidth/8.2,dheight/1.42)
                dcanvas.coords("label9",dwidth/2.8,dheight/1.42)
                dcanvas.coords("label10",dwidth/1.7,dheight/1.42)
                dcanvas.coords("label11",dwidth/8.2,dheight/1.24)
                dcanvas.coords("label12",dwidth/2.8,dheight/1.24)
                dcanvas.coords("label13",dwidth/1.7,dheight/1.24)
                dcanvas.coords("label14",dwidth/5.97,dheight/1.09)
                dcanvas.coords("label15",dwidth/8.2,dheight/0.98)
                dcanvas.coords("label16",dwidth/1.71,dheight/0.98)
                dcanvas.coords("label17",dwidth/1.58,dheight/1.09)
                dcanvas.coords("label18",dwidth/8.2,dheight/0.824)
                dcanvas.coords("label19",dwidth/2.62,dheight/0.824)
                dcanvas.coords("label20",dwidth/1.7,dheight/0.824)
                dcanvas.coords("label21",dwidth/1.185,dheight/0.824)
                dcanvas.coords("label22",dwidth/8.2,dheight/0.76)
                dcanvas.coords("label23",dwidth/2.62,dheight/0.76)
                dcanvas.coords("label24",dwidth/1.7,dheight/0.76)
                dcanvas.coords("label25",dwidth/1.185,dheight/0.76)
                dcanvas.coords("label26",dwidth/1.28,dheight/1.087)
                dcanvas.coords("label27",dwidth/6.3,dheight/0.709)

                dcanvas.coords("line1",dwidth/21,dheight/2.2,dwidth/1.055,dheight/2.2)

                dcanvas.coords("combo1",dwidth/20,dheight/1.9)
                dcanvas.coords("combo2",dwidth/20,dheight/1.37)

                dcanvas.coords("entry2",dwidth/3.52,dheight/1.9)
                dcanvas.coords("entry3",dwidth/1.94,dheight/1.9)
                dcanvas.coords("entry4",dwidth/20,dheight/1.6)
                dcanvas.coords("entry5",dwidth/3.52,dheight/1.6)
                dcanvas.coords("entry6",dwidth/3.52,dheight/1.38)
                dcanvas.coords("entry7",dwidth/1.94,dheight/1.38)
                dcanvas.coords("entry8",dwidth/20,dheight/1.21)
                dcanvas.coords("entry9",dwidth/3.52,dheight/1.21)
                dcanvas.coords("entry10",dwidth/1.94,dheight/1.21)
                dcanvas.coords("entry11",dwidth/20,dheight/0.96)
                dcanvas.coords("entry12",dwidth/1.95,dheight/0.96)
                dcanvas.coords("entry13",dwidth/20,dheight/0.81)
                dcanvas.coords("entry14",dwidth/3.23,dheight/0.81)
                dcanvas.coords("entry15",dwidth/1.94,dheight/0.81)
                dcanvas.coords("entry16",dwidth/1.296,dheight/0.81)
                dcanvas.coords("entry17",dwidth/20,dheight/0.749)
                dcanvas.coords("entry18",dwidth/3.23,dheight/0.749)
                dcanvas.coords("entry19",dwidth/1.94,dheight/0.749)
                dcanvas.coords("entry20",dwidth/1.296,dheight/0.749)

                dcanvas.coords("check1",dwidth/1.45,dheight/1.11)
                dcanvas.coords("check2",dwidth/20,dheight/0.72)

                dcanvas.coords("button1",dwidth/2,dheight/0.655)
                dcanvas.coords("button2",dwidth/27,dheight/3)

            sr_Canvas_2 = Canvas(sr_Frame_2,bg='#2f516f',scrollregion=(0,0,700,1200))

            sr_Frame_2.grid_columnconfigure(0,weight=1)
            sr_Frame_2.grid_rowconfigure(0,weight=1)

            sr_Scroll_2 = Scrollbar(sr_Frame_2,orient=VERTICAL)
            sr_Scroll_2.grid(row=0,column=1,sticky='ns')
            sr_Scroll_2.config(command=sr_Canvas_2.yview)
            sr_Canvas_2.bind("<Configure>", responsive_widgets2)
            sr_Canvas_2.config(yscrollcommand=sr_Scroll_2.set)
            sr_Canvas_2.grid(row=0,column=0,sticky='nsew')

            sr_Canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly1"))
            cust_label1 = Label(sr_Canvas_2,width=18,height=1,text="ADD CUSTOMER",font=('arial 25'),background='#1b3857',fg="white")
            sr_Canvas_2.create_window(0,0,anchor="c",window=cust_label1,tags=("label1"))
            sr_Canvas_2.create_line(0,0,0,0,fill='gray',width=1,tags=("hline"))

            sr_Canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly2"))

            cust_label2 = Label(sr_Canvas_2,width=20,height=1,text="Customer Information",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label2,tags=('label2'))

            sr_Canvas_2.create_line(0,0,0,0,fill='gray',width=1,tags=("line1"))

            cust_label3 = Label(sr_Canvas_2,width=20,height=1,text="Title",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label3,tags=('label3'))

            cust_title = ttk.Combobox(sr_Canvas_2,width=19,font=('arial 15'))
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_title,tags=("combo1"))

            cust_label4 = Label(sr_Canvas_2,width=20,height=1,text="First name",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label4,tags=('label4'))

            cust_fname = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_fname,tags=("entry2"))

            cust_label5 = Label(sr_Canvas_2,width=20,height=1,text="Last name",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label5,tags=('label5'))

            cust_lname = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_lname,tags=("entry3"))

            cust_label6 = Label(sr_Canvas_2,width=20,height=1,text="Company",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label6,tags=('label6'))

            cust_company = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_company,tags=("entry4"))

            cust_label7 = Label(sr_Canvas_2,width=20,height=1,text="Location",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label7,tags=('label7'))

            cust_location = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_location,tags=("entry5"))

            cust_label8 = Label(sr_Canvas_2,width=20,height=1,text="GST type",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label8,tags=('label8'))

            cust_gtype = ttk.Combobox(sr_Canvas_2,width=19,font=('arial 15'))
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_gtype,tags=("combo2"))

            cust_label9 = Label(sr_Canvas_2,width=20,height=1,text="GSTIN",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label9,tags=('label9'))

            cust_gin = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_gin,tags=("entry6"))

            cust_label10 = Label(sr_Canvas_2,width=20,height=1,text="PAN NO",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label10,tags=('label10'))

            cust_pan = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pan,tags=("entry7"))

            cust_label11 = Label(sr_Canvas_2,width=20,height=1,text="Email",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label11,tags=('label11'))

            cust_email = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_email,tags=("entry8"))

            cust_label12 = Label(sr_Canvas_2,width=20,height=1,text="Website",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label12,tags=('label12'))

            cust_web = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_web,tags=("entry9"))

            cust_label13 = Label(sr_Canvas_2,width=20,height=1,text="Mobile",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label13,tags=('label13'))

            cust_mob = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_mob,tags=("entry10"))

            cust_label14 = Label(sr_Canvas_2,width=20,height=1,text="Billing Address",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label14,tags=('label14'))

            cust_label15 = Label(sr_Canvas_2,width=20,height=1,text="Street",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label15,tags=('label15'))

            cust_st1 = scrolledtext.ScrolledText(sr_Canvas_2,width=66,height=4,background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_st1,tags=("entry11"))

            cust_label17 = Label(sr_Canvas_2,width=20,height=1,text="Shipping Address",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label17,tags=('label17'))

            cust_label16 = Label(sr_Canvas_2,width=20,height=1,text="Street",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label16,tags=('label16'))

            cust_st2 = scrolledtext.ScrolledText(sr_Canvas_2,width=66,height=4,background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_st2,tags=("entry12"))

            cust_label18 = Label(sr_Canvas_2,width=20,height=1,text="City",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label18,tags=('label18'))

            cust_city = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_city,tags=("entry13"))

            cust_label19 = Label(sr_Canvas_2,width=20,height=1,text="State",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label19,tags=('label19'))

            cust_state = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_state,tags=("entry14"))

            cust_label20 = Label(sr_Canvas_2,width=20,height=1,text="City",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label20,tags=('label20'))

            cust_city1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_city1,tags=("entry15"))

            cust_label21 = Label(sr_Canvas_2,width=20,height=1,text="State",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label21,tags=('label21'))

            cust_state1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_state1,tags=("entry16"))
            #--
            cust_label22 = Label(sr_Canvas_2,width=20,height=1,text="Pin code",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label22,tags=('label22'))

            cust_pin = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pin,tags=("entry17"))

            cust_label23 = Label(sr_Canvas_2,width=20,height=1,text="Country",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label23,tags=('label23'))

            cust_country = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_country,tags=("entry18"))

            cust_label24 = Label(sr_Canvas_2,width=20,height=1,text="Pin code",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label24,tags=('label24'))

            cust_pin1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pin1,tags=("entry19"))

            cust_label25 = Label(sr_Canvas_2,width=20,height=1,text="Country",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label25,tags=('label25'))

            cust_country1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_country1,tags=("entry20"))

            cust_sameb = Checkbutton(sr_Canvas_2,onvalue=1,offvalue=0,background='#1b3857',activebackground="#1b3857")
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_sameb,tags=("check1"))

            cust_label26 = Label(sr_Canvas_2,width=20,height=1,text="Same as billing address",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label26,tags=('label26'))

            cust_term = Checkbutton(sr_Canvas_2,onvalue=1,offvalue=0,background='#1b3857',activebackground="#1b3857")
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_term,tags=("check2"))

            cust_label27 = Label(sr_Canvas_2,width=25,height=1,text="Agree to terms and conditions",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label27,tags=('label27'))
            
            cust_save = Button(sr_Canvas_2,text="Submit Form",font=('arial 12 bold'),width=40,height=2,background="#198fed",activebackground="#198fed",foreground="white",activeforeground="white",bd=0)
            sr_Canvas_2.create_window(0,0,window=cust_save,tags=("button1"))

            def dc_goBack1():
                sr_Frame_2.grid_forget()
                sr_Frame_1.grid(row=0,column=0,sticky='nsew')

            back_btn = Button(sr_Canvas_2,text='←  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:dc_goBack1())
            sr_Canvas_2.create_window(0,0,window=back_btn,tags=("button2"))

        dc_plus = Button(sr_Canvas_1,text='+',font=('arial 10 bold'),foreground='white',activebackground='#1b3857',background='#1b3857',padx=7,command=lambda:sr_addCustomer_1())
        sr_Canvas_1.create_window(0,0,window=dc_plus,tags=("button5"))

        dc_label11 = Label(sr_Canvas_1,width=20,height=1,text="AMOUNT",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(0,0,window=dc_label11,tags=('label29'))

        dc_label12 = Label(sr_Canvas_1,width=20,height=1,text="0.00",font=('arial 14'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(0,0,window=dc_label12,tags=('label30'))

        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line39"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line40"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line41"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line42"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line43"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line44"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line45"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line46"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line47"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line48"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line49"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line50"))

        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line51"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line52"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line53"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line54"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line55"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line56"))
        sr_Canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line57"))

        dc_label13 = Label(sr_Canvas_1,width=3,height=1,text="#",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=dc_label13,tags=('label44'))

        dc_label14 = Label(sr_Canvas_1,width=3,height=1,text="1",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=dc_label14,tags=('label45'))

        dc_label18 = Label(sr_Canvas_1,width=15,height=1,text="Product / Service",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=dc_label18,tags=('label46'))

        dc_label20 = Label(sr_Canvas_1,width=18,height=1,text="Description",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=dc_label20,tags=('label47'))

        dc_label21 = Label(sr_Canvas_1,width=10,height=1,text="Qty",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=dc_label21,tags=('label48'))

        dc_label22 = Label(sr_Canvas_1,width=10,height=1,text="Rate",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=dc_label22,tags=('label49'))

        dc_label23 = Label(sr_Canvas_1,width=10,height=1,text="Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=dc_label23,tags=('label50'))

        dc_label24 = Label(sr_Canvas_1,width=10,height=1,text="Tax (%)",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=dc_label24,tags=('label51'))

        dct_entry1 = ttk.Combobox(sr_Canvas_1,width=12,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='c',window=dct_entry1,tags=("combo7"))

        dct_entry3 = Entry(sr_Canvas_1,width=20,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=dct_entry3,tags=("entry27"))

        dct_entry4 = Entry(sr_Canvas_1,width=10,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=dct_entry4,tags=("entry28"))

        dct_entry5 = Entry(sr_Canvas_1,width=16,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=dct_entry5,tags=("entry29"))

        dct_entry6 = Entry(sr_Canvas_1,width=16,font=('arial 15'),background='#2f516f',foreground='white',state=DISABLED)
        sr_Canvas_1.create_window(0,0,anchor='nw',window=dct_entry6,tags=("entry30"))

        dct_entry7 = ttk.Combobox(sr_Canvas_1,width=10,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='c',window=dct_entry7,tags=("combo8"))

        dc_label25 = Label(sr_Canvas_1,width=10,height=1,text="Sub Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=dc_label25,tags=('label52'))

        dc_label26 = Label(sr_Canvas_1,width=10,height=1,text="Tax Amount",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=dc_label26,tags=('label53'))

        dc_label27 = Label(sr_Canvas_1,width=10,height=1,text="Grand Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=dc_label27,tags=('label54'))

        dct_entry8 = Entry(sr_Canvas_1,width=19,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=dct_entry8,tags=("entry31"))

        dct_entry9 = Entry(sr_Canvas_1,width=19,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=dct_entry9,tags=("entry32"))

        dct_entry10 = Entry(sr_Canvas_1,width=19,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=dct_entry10,tags=("entry33"))

        save_btn = Button(sr_Canvas_1,text='Save',width=20,height=2,font=('arial 10 bold'),background="#198fed",activebackground="#198fed",foreground="white",activeforeground="white",bd=0)
        sr_Canvas_1.create_window(0,0,window=save_btn,tags=("button8")) 

        def sr_goBack():
            sr_Frame_1.grid_forget()
            sr_Frame.grid(row=0,column=0,sticky='nsew')

        back_btn = Button(sr_Canvas_1,text='←  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:sr_goBack())
        sr_Canvas_1.create_window(0,0,window=back_btn,tags=("button3"))

        dc_label7 = Label(sr_Canvas_1,width=20,height=1,text="Delayed charge date",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(0,0,window=dc_label7,tags=('label23'))

        dc_dcdate = DateEntry(sr_Canvas_1,width=19,font=('arial 15'),background='#2f516f')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=dc_dcdate,tags=("entry14"))

        cwidth = root.winfo_screenwidth()

        if cwidth > 1280:
            sr_Canvas_1.create_window(122,442,anchor='nw',window=dc_dcdate,tags=("date2"))
        elif cwidth <= 1024:
            sr_Canvas_1.create_window(92,455,anchor='nw',window=dc_dcdate,tags=("date2"))
        else:
            sr_Canvas_1.create_window(115,407,anchor='nw',window=dc_dcdate,tags=("date2"))
    elif sr_transCombo.get() == "Time Activity":
        sr_Canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly1"))
        ta_label1 = Label(sr_Canvas_1,width=18,height=1,text="TIME ACTIVITY",font=('arial 25'),background='#1b3857',fg="white")
        sr_Canvas_1.create_window(0,0,anchor="c",window=ta_label1,tags=("label1"))
        sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("hline"))

        sr_Canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly4"))   

        ta_image = Image.open(r'images/time.png')
        resize_img = ta_image.resize((360,560))
        time_img = ImageTk.PhotoImage(resize_img)
        img_label = Label(sr_Canvas_1,image=time_img,bg="#1b3857")
        img_label.image = time_img
        sr_Canvas_1.create_window(0,0,anchor='nw',window=img_label,tags=('image1'))

        ta_label3 = Label(sr_Canvas_1,width=10,height=1,text="Name",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_1.create_window(0,0,window=ta_label3,tags=('label56'))

        ta_supplier = ttk.Combobox(sr_Canvas_1,width=26,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='c',window=ta_supplier,tags=("combo9"))

        def sr_addSupplier():
            sr_Frame_1.grid_forget()
            sr_Frame_2 = Frame(tab3_1,background="#2f516f")
            sr_Frame_2.grid(row=0,column=0,sticky='nsew')

            def responsive_widgets3(event):
                dwidth = event.width
                dheight = event.height
                dcanvas = event.widget
                
                r1 = 25
                x1 = dwidth/63
                x2 = dwidth/1.021
                y1 = dheight/14 
                y2 = dheight/3.505

                dcanvas.coords("poly1",x1 + r1,y1,
                x1 + r1,y1,
                x2 - r1,y1,
                x2 - r1,y1,     
                x2,y1,     
                #--------------------
                x2,y1 + r1,     
                x2,y1 + r1,     
                x2,y2 - r1,     
                x2,y2 - r1,     
                x2,y2,
                #--------------------
                x2 - r1,y2,     
                x2 - r1,y2,     
                x1 + r1,y2,
                x1 + r1,y2,
                x1,y2,
                #--------------------
                x1,y2 - r1,
                x1,y2 - r1,
                x1,y1 + r1,
                x1,y1 + r1,
                x1,y1,
                )

                dcanvas.coords("hline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
                dcanvas.coords("hline1",dwidth/21,dheight/0.85,dwidth/1.055,dheight/0.85)
                dcanvas.coords("hline2",dwidth/21,dheight/0.555,dwidth/1.055,dheight/0.555)
                
                r2 = 25
                x11 = dwidth/63
                x21 = dwidth/1.021
                y11 = dheight/2.8
                y21 = dheight/0.44


                dcanvas.coords("poly2",x11 + r2,y11,
                x11 + r2,y11,
                x21 - r2,y11,
                x21 - r2,y11,     
                x21,y11,     
                #--------------------
                x21,y11 + r2,     
                x21,y11 + r2,     
                x21,y21 - r2,     
                x21,y21 - r2,     
                x21,y21,
                #--------------------
                x21 - r2,y21,     
                x21 - r2,y21,     
                x11 + r2,y21,
                x11 + r2,y21,
                x11,y21,
                #--------------------
                x11,y21 - r2,
                x11,y21 - r2,
                x11,y11 + r2,
                x11,y11 + r2,
                x11,y11,
                )

                dcanvas.coords("label1",dwidth/2,dheight/8.24)
                dcanvas.coords("label2",dwidth/6,dheight/2.4)
                dcanvas.coords("label3",dwidth/8.2,dheight/2)
                dcanvas.coords("label4",dwidth/2.32,dheight/2)
                dcanvas.coords("label5",dwidth/1.355,dheight/2)
                dcanvas.coords("label6",dwidth/8.2,dheight/1.61)
                dcanvas.coords("label7",dwidth/2.845,dheight/1.61)
                dcanvas.coords("label8",dwidth/1.725,dheight/1.61)
                dcanvas.coords("label9",dwidth/1.24,dheight/1.61)
                dcanvas.coords("label10",dwidth/8.2,dheight/1.358)
                dcanvas.coords("label11",dwidth/2.845,dheight/1.358)
                dcanvas.coords("label12",dwidth/1.725,dheight/1.358)
                dcanvas.coords("label13",dwidth/1.24,dheight/1.358)
                dcanvas.coords("label14",dwidth/8.12,dheight/1.163)
                dcanvas.coords("label15",dwidth/2.33,dheight/1.163)
                dcanvas.coords("label16",dwidth/1.356,dheight/1.163)
                dcanvas.coords("label17",dwidth/1.29,dheight/1.041)
                dcanvas.coords("label18",dwidth/8.2,dheight/0.97)
                dcanvas.coords("label19",dwidth/2.845,dheight/0.97)
                dcanvas.coords("label20",dwidth/1.725,dheight/0.97)
                dcanvas.coords("label21",dwidth/1.24,dheight/0.97)
                dcanvas.coords("label22",dwidth/6,dheight/0.8)
                dcanvas.coords("label23",dwidth/8.2,dheight/0.76)
                dcanvas.coords("label24",dwidth/8.2,dheight/0.656)
                dcanvas.coords("label25",dwidth/1.715,dheight/0.656)
                dcanvas.coords("label26",dwidth/8.2,dheight/0.605)
                dcanvas.coords("label27",dwidth/1.715,dheight/0.605)
                dcanvas.coords("label28",dwidth/8.2,dheight/0.538)
                dcanvas.coords("label29",dwidth/6.3,dheight/0.485)

                dcanvas.coords("line1",dwidth/21,dheight/2.2,dwidth/1.055,dheight/2.2)

                dcanvas.coords("combo1",dwidth/20,dheight/1.9)
                dcanvas.coords("combo2",dwidth/3.6,dheight/1.31)
                dcanvas.coords("combo3",dwidth/2.8,dheight/1.13)
                dcanvas.coords("combo4",dwidth/1.975,dheight/0.945)
                dcanvas.coords("combo5",dwidth/1.364,dheight/0.945)

                dcanvas.coords("entry1",dwidth/2.8,dheight/1.9)
                dcanvas.coords("entry2",dwidth/1.505,dheight/1.9)
                dcanvas.coords("entry3",dwidth/20,dheight/1.55)
                dcanvas.coords("entry4",dwidth/3.6,dheight/1.55)
                dcanvas.coords("entry5",dwidth/1.975,dheight/1.55)
                dcanvas.coords("entry6",dwidth/1.364,dheight/1.55)
                dcanvas.coords("entry7",dwidth/20,dheight/1.31)
                dcanvas.coords("entry8",dwidth/1.975,dheight/1.31)
                dcanvas.coords("entry9",dwidth/1.364,dheight/1.31)
                dcanvas.coords("entry10",dwidth/20,dheight/1.13)
                dcanvas.coords("entry11",dwidth/1.505,dheight/1.13)
                dcanvas.coords("entry12",dwidth/20,dheight/0.945)
                dcanvas.coords("entry13",dwidth/20,dheight/0.745)
                dcanvas.coords("entry14",dwidth/20,dheight/0.644)
                dcanvas.coords("entry15",dwidth/1.96,dheight/0.644)
                dcanvas.coords("entry16",dwidth/20,dheight/0.595)
                dcanvas.coords("entry17",dwidth/1.96,dheight/0.595)
                dcanvas.coords("entry18",dwidth/20,dheight/0.53)
                
                dcanvas.coords("date",dwidth/3.6,dheight/0.945)

                dcanvas.coords("button1",dwidth/27,dheight/3)
                dcanvas.coords("button2",dwidth/2,dheight/0.46)

                dcanvas.coords("check1",dwidth/17,dheight/0.485)

            sr_Canvas_2 = Canvas(sr_Frame_2,bg='#2f516f',scrollregion=(0,0,700,1300))

            sr_Frame_2.grid_columnconfigure(0,weight=1)
            sr_Frame_2.grid_rowconfigure(0,weight=1)

            sr_Scroll_2 = Scrollbar(sr_Frame_2,orient=VERTICAL)
            sr_Scroll_2.grid(row=0,column=1,sticky='ns')
            sr_Scroll_2.config(command=sr_Canvas_2.yview)
            sr_Canvas_2.bind("<Configure>", responsive_widgets3)
            sr_Canvas_2.config(yscrollcommand=sr_Scroll_2.set)
            sr_Canvas_2.grid(row=0,column=0,sticky='nsew')

            sr_Canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly1"))
            sup_label1 = Label(sr_Canvas_2,width=18,height=1,text="ADD SUPPLIER",font=('arial 25'),background='#1b3857',fg="white")
            sr_Canvas_2.create_window(0,0,anchor="c",window=sup_label1,tags=("label1"))
            sr_Canvas_2.create_line(0,0,0,0,fill='gray',width=1,tags=("hline"))

            sr_Canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly2"))

            sup_label2 = Label(sr_Canvas_2,width=20,height=1,text="Supplier Information",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=sup_label2,tags=('label2'))

            sr_Canvas_2.create_line(0,0,0,0,fill='gray',width=1,tags=("line1"))

            sup_label3 = Label(sr_Canvas_2,width=20,height=1,text="Title",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=sup_label3,tags=('label3'))

            sup_title = ttk.Combobox(sr_Canvas_2,width=31,font=('arial 15'))
            sr_Canvas_2.create_window(0,0,anchor='nw',window=sup_title,tags=("combo1"))

            sup_label4 = Label(sr_Canvas_2,width=20,height=1,text="First name",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=sup_label4,tags=('label4'))

            sup_fname = Entry(sr_Canvas_2,width=32,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=sup_fname,tags=("entry1"))

            sup_label5 = Label(sr_Canvas_2,width=20,height=1,text="Last name",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=sup_label5,tags=('label5'))

            sup_lname = Entry(sr_Canvas_2,width=32,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=sup_lname,tags=("entry2"))

            sup_label6 = Label(sr_Canvas_2,width=20,height=1,text="Company",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=sup_label6,tags=('label6'))

            sup_company = Entry(sr_Canvas_2,width=24,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=sup_company,tags=("entry3"))

            sup_label7 = Label(sr_Canvas_2,width=20,height=1,text="Email",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=sup_label7,tags=('label7'))

            sup_email = Entry(sr_Canvas_2,width=24,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=sup_email,tags=("entry4"))

            sup_label8 = Label(sr_Canvas_2,width=20,height=1,text="Mobile",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=sup_label8,tags=('label8'))

            sup_mobile = Entry(sr_Canvas_2,width=24,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=sup_mobile,tags=("entry5"))

            sup_label9 = Label(sr_Canvas_2,width=20,height=1,text="Website",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=sup_label9,tags=('label9'))

            sup_web = Entry(sr_Canvas_2,width=24,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=sup_web,tags=("entry6"))

            sup_label10 = Label(sr_Canvas_2,width=20,height=1,text="Billing Rate",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=sup_label10,tags=('label10'))

            sup_brate = Entry(sr_Canvas_2,width=24,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=sup_brate,tags=("entry7"))

            sup_label11 = Label(sr_Canvas_2,width=20,height=1,text="Terms",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=sup_label11,tags=('label11'))

            def add_newTerms(evet):
                if sup_terms.get() == 'ADD NEW TERMS':
                    sr_Canvas_2.itemconfig("label12",state='normal')
                    sr_Canvas_2.itemconfig("entry8",state='normal')
                else:
                    sr_Canvas_2.itemconfig("label12",state='hidden')
                    sr_Canvas_2.itemconfig("entry8",state='hidden')


            sup_terms = ttk.Combobox(sr_Canvas_2,width=23,font=('arial 15'),background='#2f516f',foreground='black')
            sup_terms['values'] = ['ADD NEW TERMS','Due on Receipt','NET15','NET30','NET60',]
            sup_terms.current(0)
            sup_terms.bind("<<ComboboxSelected>>",add_newTerms)
            sr_Canvas_2.create_window(0,0,anchor='nw',window=sup_terms,tags=("combo2"))

            sup_label12 = Label(sr_Canvas_2,width=20,height=1,text="ADD NEW TERMS",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=sup_label12,tags=('label12'))

            sup_addterms = Entry(sr_Canvas_2,width=24,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=sup_addterms,tags=("entry8"))

            sup_label13 = Label(sr_Canvas_2,width=20,height=1,text="Opening Balance",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=sup_label13,tags=('label13'))

            sup_obal = Entry(sr_Canvas_2,width=24,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=sup_obal,tags=("entry9"))

            sup_label14 = Label(sr_Canvas_2,width=20,height=1,text="Account No",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=sup_label14,tags=('label14'))

            sup_accno = Entry(sr_Canvas_2,width=32,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=sup_accno,tags=("entry10"))

            sup_label15 = Label(sr_Canvas_2,width=20,height=1,text="GST Type",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=sup_label15,tags=('label15'))

            def selectGSTtype(evet):
                if sup_gtype.get() == "GST Unregistered":
                    sr_Canvas_2.itemconfig("label16",state='hidden')
                    sr_Canvas_2.itemconfig("entry11",state='hidden')
                    sr_Canvas_2.itemconfig("label17",state='hidden')
                else:
                    sr_Canvas_2.itemconfig("label16",state='normal')
                    sr_Canvas_2.itemconfig("entry11",state='normal')
                    sr_Canvas_2.itemconfig("label17",state='normal')

            sup_gtype = ttk.Combobox(sr_Canvas_2,width=31,font=('arial 15'))
            sup_gtype['values'] = ['Choose...','GST Registered - Regular','GST Registered - Composition','GST Unregistered']
            sup_gtype.current(0)
            sup_gtype.bind("<<ComboboxSelected>>",selectGSTtype)
            sr_Canvas_2.create_window(0,0,anchor='nw',window=sup_gtype,tags=("combo3"))

            sup_label16 = Label(sr_Canvas_2,width=20,height=1,text="GSTIN",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=sup_label16,tags=('label16'))

            sup_gstin = Entry(sr_Canvas_2,width=32,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=sup_gstin,tags=("entry11"))

            sup_label17 = Label(sr_Canvas_2,width=30,height=1,text="What is a GST registration type?",font=('arial 11'),background='#1b3857',anchor="w",fg="#3dd5f3")
            sr_Canvas_2.create_window(0,0,window=sup_label17,tags=('label17'))

            sup_label18 = Label(sr_Canvas_2,width=20,height=1,text="Tax Registration No",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=sup_label18,tags=('label18'))

            sup_taxregno = Entry(sr_Canvas_2,width=24,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=sup_taxregno,tags=("entry12"))

            sup_label20 = Label(sr_Canvas_2,width=20,height=1,text="Default Expense Account",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=sup_label20,tags=('label20'))

            sup_dexpenseaccnt = ttk.Combobox(sr_Canvas_2,width=23,font=('arial 15'),background='#2f516f',foreground='black')
            sup_dexpenseaccnt['values'] = ['Choose Account','Advertising /Promotional','Bank Charges','Business Licenses and Permits','Charitable Contributions','Computer and Internet Expense','Continuing Education','Depreciation Expense','Dues and Subscriptions','Housekeeping Charges',
            'Insurance Expense','Insurance Expense-General Liability Insurance','Insurance Expense-Health Insurance','Insurance Expense-Life and disability Insurance','Insurance Expense-Professional Liability','Internet Expense','Meals and Entertainment','Office Supplies',
            'Postage and delivery','Printing and Reproduction','Professional Fees','Purchases','Rent Expense','Repair and Maintenance','Small Tools and Equipment','Swachh Bharat Cess Expense','Taxes-Property','Telephone Expense','Travel Expense','Uncategorised Expense','Utilities',
            'Ask My Accountant','CGST write-off','GST write-off','IGST write-off','Miscellaneous Expense','Political Contributions','Reconciliation Discrepancies','SGST write-off','Tax Write-off','Vehicle Expenses','Cost of sales','Equipment Rental for Jobs','Freight and shipping Costs',
            'Merchant Account Fees','Purchases - Hardware For Resale','Purchases - Software For Resale','SubContracted Services','Tools and Craft Supplies',]
            sup_dexpenseaccnt.current(0)
            sr_Canvas_2.create_window(0,0,anchor='nw',window=sup_dexpenseaccnt,tags=("combo4"))

            sup_label21 = Label(sr_Canvas_2,width=20,height=1,text="Apply TDS for Supplier",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=sup_label21,tags=('label21'))

            sup_tds = ttk.Combobox(sr_Canvas_2,width=23,font=('arial 15'))
            sup_tds['values'] = ['Choose...','Yes','No']
            sup_tds.current(0)
            sr_Canvas_2.create_window(0,0,anchor='nw',window=sup_tds,tags=("combo5"))

            sr_Canvas_2.create_line(0,0,0,0,fill='gray',width=1,tags=("hline1"))

            sup_label22 = Label(sr_Canvas_2,width=20,height=1,text="Address",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=sup_label22,tags=('label22'))

            sup_label23 = Label(sr_Canvas_2,width=20,height=1,text="Street",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=sup_label23,tags=('label23'))

            sup_street = Text(sr_Canvas_2,width=103,height=3,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=sup_street,tags=("entry13"))

            sup_label24 = Label(sr_Canvas_2,width=20,height=1,text="City",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=sup_label24,tags=('label24'))

            sup_city = Entry(sr_Canvas_2,width=50,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=sup_city,tags=("entry14"))

            sup_label25 = Label(sr_Canvas_2,width=20,height=1,text="State",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=sup_label25,tags=('label25'))

            sup_state = Entry(sr_Canvas_2,width=50,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=sup_state,tags=("entry15"))

            sup_label26 = Label(sr_Canvas_2,width=20,height=1,text="Pin Code",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=sup_label26,tags=('label26'))

            sup_pin = Entry(sr_Canvas_2,width=50,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=sup_pin,tags=("entry16"))

            sup_label27 = Label(sr_Canvas_2,width=20,height=1,text="Country",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=sup_label27,tags=('label27'))

            sup_country = ttk.Combobox(sr_Canvas_2,width=49,font=('arial 15'))
            sup_country['values'] = ['Choose...',]
            sup_country.current(0)
            sr_Canvas_2.create_window(0,0,anchor='nw',window=sup_country,tags=("entry17"))

            sr_Canvas_2.create_line(0,0,0,0,fill='gray',width=1,tags=("hline2"))

            sup_label28 = Label(sr_Canvas_2,width=20,height=1,text="Notes",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=sup_label28,tags=('label28'))

            sup_notes = Text(sr_Canvas_2,width=103,height=3,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=sup_notes,tags=("entry18"))

            sup_label29 = Label(sr_Canvas_2,width=25,height=1,text="Agree to terms and conditions",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=sup_label29,tags=('label29'))

            agreetoVar = BooleanVar()

            sup_agree = Checkbutton(sr_Canvas_2,background='#1b3857',activebackground='#1b3857',onvalue=1,offvalue=0,variable=agreetoVar)
            sr_Canvas_2.create_window(0,0,window=sup_agree,tags=("check1"))

            save_btn = Button(sr_Canvas_2,text="Submit Form",font=('arial 12 bold'),width=113,height=2,background="#198fed",activebackground="#198fed",foreground="white",activeforeground="white",bd=0)
            sr_Canvas_2.create_window(0,0,window=save_btn,tags=("button2"))

            def ta_goBack():
                sr_Frame_2.grid_forget()
                sr_Frame_1.grid(row=0,column=0,sticky='nsew')

            back_btn = Button(sr_Canvas_2,text='←  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:ta_goBack())
            sr_Canvas_2.create_window(0,0,window=back_btn,tags=("button1"))

            sup_label19 = Label(sr_Canvas_2,width=20,height=1,text="Effective Date",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=sup_label19,tags=('label19'))

            sup_effdate = DateEntry(sr_Canvas_2,width=23,font=('arial 15'),background='#2f516f',foreground='white')

            cwidth = root.winfo_screenwidth()

            if cwidth > 1280:
                sr_Canvas_2.create_window(373.6111111111111,650.7936507936508,anchor='nw',window=sup_effdate,tags=("date"))
            elif cwidth <= 1024:
                sr_Canvas_2.create_window(279.72222222222223,670.8994708994709,anchor='nw',window=sup_effdate,tags=("date"))
            else:
                sr_Canvas_2.create_window(350.8333333333333,600,anchor='nw',window=sup_effdate,tags=("date"))

        ta_plus1 = Button(sr_Canvas_1,text='+',font=('arial 10 bold'),foreground='white',activebackground='#1b3857',background='#1b3857',padx=7,command=lambda:sr_addSupplier())
        sr_Canvas_1.create_window(0,0,window=ta_plus1,tags=("button9"))

        ta_label4 = Label(sr_Canvas_1,width=20,height=1,text="Customer",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
        sr_Canvas_1.create_window(0,0,window=ta_label4,tags=("label57"))

        ta_custCombo = ttk.Combobox(sr_Canvas_1,width=62,font=('arial 15'))
        sr_Canvas_1.create_window(0,0,anchor='nw',window=ta_custCombo,tags=("combo10"))

        def sr_addCustomer_1():
            sr_Frame_1.grid_forget()
            sr_Frame_2 = Frame(tab3_1,)
            sr_Frame_2.grid(row=0,column=0,sticky='nsew')

            def responsive_widgets2(event):
                dwidth = event.width
                dheight = event.height
                dcanvas = event.widget
                
                r1 = 25
                x1 = dwidth/63
                x2 = dwidth/1.021
                y1 = dheight/14 
                y2 = dheight/3.505

                dcanvas.coords("poly1",x1 + r1,y1,
                x1 + r1,y1,
                x2 - r1,y1,
                x2 - r1,y1,     
                x2,y1,     
                #--------------------
                x2,y1 + r1,     
                x2,y1 + r1,     
                x2,y2 - r1,     
                x2,y2 - r1,     
                x2,y2,
                #--------------------
                x2 - r1,y2,     
                x2 - r1,y2,     
                x1 + r1,y2,
                x1 + r1,y2,
                x1,y2,
                #--------------------
                x1,y2 - r1,
                x1,y2 - r1,
                x1,y1 + r1,
                x1,y1 + r1,
                x1,y1,
                )

                dcanvas.coords("hline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
                
                r2 = 25
                x11 = dwidth/63
                x21 = dwidth/1.021
                y11 = dheight/2.8
                y21 = dheight/0.6


                dcanvas.coords("poly2",x11 + r2,y11,
                x11 + r2,y11,
                x21 - r2,y11,
                x21 - r2,y11,     
                x21,y11,     
                #--------------------
                x21,y11 + r2,     
                x21,y11 + r2,     
                x21,y21 - r2,     
                x21,y21 - r2,     
                x21,y21,
                #--------------------
                x21 - r2,y21,     
                x21 - r2,y21,     
                x11 + r2,y21,
                x11 + r2,y21,
                x11,y21,
                #--------------------
                x11,y21 - r2,
                x11,y21 - r2,
                x11,y11 + r2,
                x11,y11 + r2,
                x11,y11,
                )

                dcanvas.coords("label1",dwidth/2,dheight/8.24)
                dcanvas.coords("label2",dwidth/6,dheight/2.4)
                dcanvas.coords("label3",dwidth/8.2,dheight/2)
                dcanvas.coords("label4",dwidth/2.8,dheight/2)
                dcanvas.coords("label5",dwidth/1.7,dheight/2)
                dcanvas.coords("label6",dwidth/8.2,dheight/1.66)
                dcanvas.coords("label7",dwidth/2.8,dheight/1.66)
                dcanvas.coords("label8",dwidth/8.2,dheight/1.42)
                dcanvas.coords("label9",dwidth/2.8,dheight/1.42)
                dcanvas.coords("label10",dwidth/1.7,dheight/1.42)
                dcanvas.coords("label11",dwidth/8.2,dheight/1.24)
                dcanvas.coords("label12",dwidth/2.8,dheight/1.24)
                dcanvas.coords("label13",dwidth/1.7,dheight/1.24)
                dcanvas.coords("label14",dwidth/5.97,dheight/1.09)
                dcanvas.coords("label15",dwidth/8.2,dheight/0.98)
                dcanvas.coords("label16",dwidth/1.71,dheight/0.98)
                dcanvas.coords("label17",dwidth/1.58,dheight/1.09)
                dcanvas.coords("label18",dwidth/8.2,dheight/0.824)
                dcanvas.coords("label19",dwidth/2.62,dheight/0.824)
                dcanvas.coords("label20",dwidth/1.7,dheight/0.824)
                dcanvas.coords("label21",dwidth/1.185,dheight/0.824)
                dcanvas.coords("label22",dwidth/8.2,dheight/0.76)
                dcanvas.coords("label23",dwidth/2.62,dheight/0.76)
                dcanvas.coords("label24",dwidth/1.7,dheight/0.76)
                dcanvas.coords("label25",dwidth/1.185,dheight/0.76)
                dcanvas.coords("label26",dwidth/1.28,dheight/1.087)
                dcanvas.coords("label27",dwidth/6.3,dheight/0.709)

                dcanvas.coords("line1",dwidth/21,dheight/2.2,dwidth/1.055,dheight/2.2)

                dcanvas.coords("combo1",dwidth/20,dheight/1.9)
                dcanvas.coords("combo2",dwidth/20,dheight/1.37)

                dcanvas.coords("entry2",dwidth/3.52,dheight/1.9)
                dcanvas.coords("entry3",dwidth/1.94,dheight/1.9)
                dcanvas.coords("entry4",dwidth/20,dheight/1.6)
                dcanvas.coords("entry5",dwidth/3.52,dheight/1.6)
                dcanvas.coords("entry6",dwidth/3.52,dheight/1.38)
                dcanvas.coords("entry7",dwidth/1.94,dheight/1.38)
                dcanvas.coords("entry8",dwidth/20,dheight/1.21)
                dcanvas.coords("entry9",dwidth/3.52,dheight/1.21)
                dcanvas.coords("entry10",dwidth/1.94,dheight/1.21)
                dcanvas.coords("entry11",dwidth/20,dheight/0.96)
                dcanvas.coords("entry12",dwidth/1.95,dheight/0.96)
                dcanvas.coords("entry13",dwidth/20,dheight/0.81)
                dcanvas.coords("entry14",dwidth/3.23,dheight/0.81)
                dcanvas.coords("entry15",dwidth/1.94,dheight/0.81)
                dcanvas.coords("entry16",dwidth/1.296,dheight/0.81)
                dcanvas.coords("entry17",dwidth/20,dheight/0.749)
                dcanvas.coords("entry18",dwidth/3.23,dheight/0.749)
                dcanvas.coords("entry19",dwidth/1.94,dheight/0.749)
                dcanvas.coords("entry20",dwidth/1.296,dheight/0.749)

                dcanvas.coords("check1",dwidth/1.45,dheight/1.11)
                dcanvas.coords("check2",dwidth/20,dheight/0.72)

                dcanvas.coords("button1",dwidth/2,dheight/0.655)
                dcanvas.coords("button2",dwidth/27,dheight/3)

            sr_Canvas_2 = Canvas(sr_Frame_2,bg='#2f516f',scrollregion=(0,0,700,1200))

            sr_Frame_2.grid_columnconfigure(0,weight=1)
            sr_Frame_2.grid_rowconfigure(0,weight=1)

            sr_Scroll_2 = Scrollbar(sr_Frame_2,orient=VERTICAL)
            sr_Scroll_2.grid(row=0,column=1,sticky='ns')
            sr_Scroll_2.config(command=sr_Canvas_2.yview)
            sr_Canvas_2.bind("<Configure>", responsive_widgets2)
            sr_Canvas_2.config(yscrollcommand=sr_Scroll_2.set)
            sr_Canvas_2.grid(row=0,column=0,sticky='nsew')

            sr_Canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly1"))
            cust_label1 = Label(sr_Canvas_2,width=18,height=1,text="ADD CUSTOMER",font=('arial 25'),background='#1b3857',fg="white")
            sr_Canvas_2.create_window(0,0,anchor="c",window=cust_label1,tags=("label1"))
            sr_Canvas_2.create_line(0,0,0,0,fill='gray',width=1,tags=("hline"))

            sr_Canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly2"))

            cust_label2 = Label(sr_Canvas_2,width=20,height=1,text="Customer Information",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label2,tags=('label2'))

            sr_Canvas_2.create_line(0,0,0,0,fill='gray',width=1,tags=("line1"))

            cust_label3 = Label(sr_Canvas_2,width=20,height=1,text="Title",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label3,tags=('label3'))

            cust_title = ttk.Combobox(sr_Canvas_2,width=19,font=('arial 15'))
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_title,tags=("combo1"))

            cust_label4 = Label(sr_Canvas_2,width=20,height=1,text="First name",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label4,tags=('label4'))

            cust_fname = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_fname,tags=("entry2"))

            cust_label5 = Label(sr_Canvas_2,width=20,height=1,text="Last name",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label5,tags=('label5'))

            cust_lname = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_lname,tags=("entry3"))

            cust_label6 = Label(sr_Canvas_2,width=20,height=1,text="Company",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label6,tags=('label6'))

            cust_company = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_company,tags=("entry4"))

            cust_label7 = Label(sr_Canvas_2,width=20,height=1,text="Location",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label7,tags=('label7'))

            cust_location = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_location,tags=("entry5"))

            cust_label8 = Label(sr_Canvas_2,width=20,height=1,text="GST type",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label8,tags=('label8'))

            cust_gtype = ttk.Combobox(sr_Canvas_2,width=19,font=('arial 15'))
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_gtype,tags=("combo2"))

            cust_label9 = Label(sr_Canvas_2,width=20,height=1,text="GSTIN",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label9,tags=('label9'))

            cust_gin = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_gin,tags=("entry6"))

            cust_label10 = Label(sr_Canvas_2,width=20,height=1,text="PAN NO",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label10,tags=('label10'))

            cust_pan = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pan,tags=("entry7"))

            cust_label11 = Label(sr_Canvas_2,width=20,height=1,text="Email",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label11,tags=('label11'))

            cust_email = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_email,tags=("entry8"))

            cust_label12 = Label(sr_Canvas_2,width=20,height=1,text="Website",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label12,tags=('label12'))

            cust_web = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_web,tags=("entry9"))

            cust_label13 = Label(sr_Canvas_2,width=20,height=1,text="Mobile",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label13,tags=('label13'))

            cust_mob = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_mob,tags=("entry10"))

            cust_label14 = Label(sr_Canvas_2,width=20,height=1,text="Billing Address",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label14,tags=('label14'))

            cust_label15 = Label(sr_Canvas_2,width=20,height=1,text="Street",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label15,tags=('label15'))

            cust_st1 = scrolledtext.ScrolledText(sr_Canvas_2,width=66,height=4,background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_st1,tags=("entry11"))

            cust_label17 = Label(sr_Canvas_2,width=20,height=1,text="Shipping Address",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label17,tags=('label17'))

            cust_label16 = Label(sr_Canvas_2,width=20,height=1,text="Street",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label16,tags=('label16'))

            cust_st2 = scrolledtext.ScrolledText(sr_Canvas_2,width=66,height=4,background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_st2,tags=("entry12"))

            cust_label18 = Label(sr_Canvas_2,width=20,height=1,text="City",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label18,tags=('label18'))

            cust_city = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_city,tags=("entry13"))

            cust_label19 = Label(sr_Canvas_2,width=20,height=1,text="State",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label19,tags=('label19'))

            cust_state = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_state,tags=("entry14"))

            cust_label20 = Label(sr_Canvas_2,width=20,height=1,text="City",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label20,tags=('label20'))

            cust_city1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_city1,tags=("entry15"))

            cust_label21 = Label(sr_Canvas_2,width=20,height=1,text="State",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label21,tags=('label21'))

            cust_state1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_state1,tags=("entry16"))
            #--
            cust_label22 = Label(sr_Canvas_2,width=20,height=1,text="Pin code",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label22,tags=('label22'))

            cust_pin = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pin,tags=("entry17"))

            cust_label23 = Label(sr_Canvas_2,width=20,height=1,text="Country",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label23,tags=('label23'))

            cust_country = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_country,tags=("entry18"))

            cust_label24 = Label(sr_Canvas_2,width=20,height=1,text="Pin code",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label24,tags=('label24'))

            cust_pin1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pin1,tags=("entry19"))

            cust_label25 = Label(sr_Canvas_2,width=20,height=1,text="Country",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label25,tags=('label25'))

            cust_country1 = Entry(sr_Canvas_2,width=20,font=('arial 15'),background='#2f516f',foreground='white')
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_country1,tags=("entry20"))

            cust_sameb = Checkbutton(sr_Canvas_2,onvalue=1,offvalue=0,background='#1b3857',activebackground="#1b3857")
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_sameb,tags=("check1"))

            cust_label26 = Label(sr_Canvas_2,width=20,height=1,text="Same as billing address",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label26,tags=('label26'))

            cust_term = Checkbutton(sr_Canvas_2,onvalue=1,offvalue=0,background='#1b3857',activebackground="#1b3857")
            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_term,tags=("check2"))

            cust_label27 = Label(sr_Canvas_2,width=25,height=1,text="Agree to terms and conditions",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_2.create_window(0,0,window=cust_label27,tags=('label27'))
            
            cust_save = Button(sr_Canvas_2,text="Submit Form",font=('arial 12 bold'),width=40,height=2,background="#198fed",activebackground="#198fed",foreground="white",activeforeground="white",bd=0)
            sr_Canvas_2.create_window(0,0,window=cust_save,tags=("button1"))

            def dc_goBack1():
                sr_Frame_2.grid_forget()
                sr_Frame_1.grid(row=0,column=0,sticky='nsew')

            back_btn = Button(sr_Canvas_2,text='←  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:dc_goBack1())
            sr_Canvas_2.create_window(0,0,window=back_btn,tags=("button2"))

        ta_plus = Button(sr_Canvas_1,text='+',font=('arial 10 bold'),foreground='white',activebackground='#1b3857',background='#1b3857',padx=7,command=lambda:sr_addCustomer_1())
        sr_Canvas_1.create_window(0,0,window=ta_plus,tags=("button10"))

        ta_label5 = Label(sr_Canvas_1,width=20,height=1,text="billable(/hr)",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
        sr_Canvas_1.create_window(0,0,window=ta_label5,tags=("label58"))

        def ta_billable(event):
            if ta_billCombo.get() == 'Yes':
                sr_Canvas_1.itemconfig("entry34",state='normal')
            else:
                try:
                    sr_Canvas_1.itemconfig("entry34",state='hidden')
                except:
                    pass

        ta_billCombo = ttk.Combobox(sr_Canvas_1,width=30,font=('arial 15'))
        ta_billCombo['values'] = ['Yes','No',]
        ta_billCombo.current(1)
        ta_billCombo.bind("<<ComboboxSelected>>",ta_billable)
        sr_Canvas_1.create_window(0,0,anchor='nw',window=ta_billCombo,tags=("combo11"))

        ta_unknown = Entry(sr_Canvas_1,width=31,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=ta_unknown,state=HIDDEN,tags=("entry34"))

        ta_label6 = Label(sr_Canvas_1,width=20,height=1,text="Enter start and end time",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
        sr_Canvas_1.create_window(0,0,window=ta_label6,tags=("label59"))

        def ta_startend(event):
            if ta_startendCombo.get() == 'Yes':
                sr_Canvas_1.itemconfig("label60",state='normal')
                sr_Canvas_1.itemconfig("label61",state='normal')
                sr_Canvas_1.itemconfig("entry35",state='normal')
                sr_Canvas_1.itemconfig("entry36",state='normal')
            else:
                try:
                    sr_Canvas_1.itemconfig("label60",state='hidden')
                    sr_Canvas_1.itemconfig("label61",state='hidden')
                    sr_Canvas_1.itemconfig("entry35",state='hidden')
                    sr_Canvas_1.itemconfig("entry36",state='hidden')
                except:
                    pass

        ta_startendCombo = ttk.Combobox(sr_Canvas_1,width=20,font=('arial 15'))
        ta_startendCombo['values'] = ['Yes','No',]
        ta_startendCombo.current(1)
        ta_startendCombo.bind("<<ComboboxSelected>>",ta_startend)
        sr_Canvas_1.create_window(0,0,anchor='nw',window=ta_startendCombo,tags=("combo12"))

        ta_label7 = Label(sr_Canvas_1,width=20,height=1,text="Start date",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
        sr_Canvas_1.create_window(0,0,window=ta_label7,state=HIDDEN,tags=("label60"))

        ta_start = Entry(sr_Canvas_1,width=20,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=ta_start,state=HIDDEN,tags=("entry35"))

        ta_label8 = Label(sr_Canvas_1,width=20,height=1,text="End date",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
        sr_Canvas_1.create_window(0,0,window=ta_label8,state=HIDDEN,tags=("label61"))

        ta_end = Entry(sr_Canvas_1,width=20,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=ta_end,state=HIDDEN,tags=("entry36"))

        ta_label9 = Label(sr_Canvas_1,width=20,height=1,text="Time",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
        sr_Canvas_1.create_window(0,0,window=ta_label9,tags=("label62"))

        ta_time = Entry(sr_Canvas_1,width=67,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=ta_time,tags=("entry37"))

        ta_label10 = Label(sr_Canvas_1,width=20,height=1,text="Description",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
        sr_Canvas_1.create_window(0,0,window=ta_label10,tags=("label63"))

        ta_desc = Text(sr_Canvas_1,width=67,height=3,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(0,0,anchor='nw',window=ta_desc,tags=("entry38"))

        save_btn = Button(sr_Canvas_1,text="Submit Form",font=('arial 12 bold'),width=20,height=2,background="#198fed",activebackground="#198fed",foreground="white",activeforeground="white",bd=0)
        sr_Canvas_1.create_window(0,0,window=save_btn,tags=("button11"))

        def sr_goBack():
            sr_Frame_1.grid_forget()
            sr_Frame.grid(row=0,column=0,sticky='nsew')

        back_btn = Button(sr_Canvas_1,text='←  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:sr_goBack())
        sr_Canvas_1.create_window(0,0,window=back_btn,tags=("button3"))

        ta_label2 = Label(sr_Canvas_1,width=20,height=1,text="Date",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(0,0,window=ta_label2,tags=('label55'))

        ta_date = DateEntry(sr_Canvas_1,width=30,font=('arial 15'),background='#2f516f')

        cwidth = root.winfo_screenwidth()

        if cwidth > 1280:
            sr_Canvas_1.create_window(122,442,anchor='nw',window=ta_date,tags=("date3"))
        elif cwidth <= 1024:
            sr_Canvas_1.create_window(92,455,anchor='nw',window=ta_date,tags=("date3"))
        else:
            sr_Canvas_1.create_window(434,265,anchor='nw',window=ta_date,tags=("date3"))
    else:
        pass
    


sr_transCombo = ttk.Combobox(sr_Canvas,)
sr_transCombo['values'] = ['New Transactios','Invoice','Payment','Sales Receipt','Credit Note','Estimate','Delayed Charge','Time Activity']
sr_transCombo.current(0)
sr_transCombo.bind('<<ComboboxSelected>>',sr_transCombo_options)
sr_transCombo_win = sr_Canvas.create_window(0,0,window=sr_transCombo,tags=("combo2"))


sr_Canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line1"))
sr_Canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line17"))
sr_Canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line4"))
sr_Canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line5"))
sr_Canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line6"))
sr_Canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line7"))
sr_Canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line8"))
sr_Canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line9"))
sr_Canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line10"))
sr_Canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line11"))
sr_Canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line12"))
sr_Canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line13"))
sr_Canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line14"))
sr_Canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line15"))
sr_Canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line16"))
sr_Canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line3"))
sr_Canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line2"))

srt_dateLabel = Label(sr_Canvas,width=10,height=1,text="23-07-2022", font=('arial 10'),background="#1b3857",fg="white") 
sr_Canvas.create_window(0, 0, anchor="c", window=srt_dateLabel,tags=("label2"))

srt_typeLabel = Label(sr_Canvas,width=12,height=1,text="Payment", font=('arial 10'),background="#1b3857",fg="white") 
sr_Canvas.create_window(0, 0, anchor="c", window=srt_typeLabel,tags=("label3"))

srt_noLabel = Label(sr_Canvas,width=8,height=1,text="1010", font=('arial 10'),background="#1b3857",fg="white") 
sr_Canvas.create_window(0, 0, anchor="c", window=srt_noLabel,tags=("label4"))

srt_custLabel = Label(sr_Canvas,width=15,height=1,text="Nithin", font=('arial 10'),background="#1b3857",fg="white") 
sr_Canvas.create_window(0, 0, anchor="c", window=srt_custLabel,tags=("label5"))

srt_dueLabel = Label(sr_Canvas,width=10,height=1,text="30-07-2022", font=('arial 10'),background="#1b3857",fg="white") 
sr_Canvas.create_window(0, 0, anchor="c", window=srt_dueLabel,tags=("label6"))

srt_balLabel = Label(sr_Canvas,width=12,height=1,text="1000", font=('arial 10'),background="#1b3857",fg="white") 
sr_Canvas.create_window(0, 0, anchor="c", window=srt_balLabel,tags=("label7"))

srt_totbLabel = Label(sr_Canvas,width=12,height=1,text="1500", font=('arial 10'),background="#1b3857",fg="white") 
sr_Canvas.create_window(0, 0, anchor="c", window=srt_totbLabel,tags=("label8"))

srt_taxLabel = Label(sr_Canvas,width=7,height=1,text="100", font=('arial 10'),background="#1b3857",fg="white") 
sr_Canvas.create_window(0, 0, anchor="c", window=srt_taxLabel,tags=("label9"))

srt_totLabel = Label(sr_Canvas,width=12,height=1,text="1000", font=('arial 10'),background="#1b3857",fg="white") 
sr_Canvas.create_window(0, 0, anchor="c", window=srt_totLabel,tags=("label10"))
def sr_Actions(event):
    sr_Frame.grid_forget()
    sr_Frame_1 = Frame(tab3_1,)
    sr_Frame_1.grid(row=0,column=0,sticky='nsew')

    def responsive_widgets4(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget

        r1 = 25
        x1 = dwidth/63
        x2 = dwidth/1.021
        y1 = dheight/14 
        y2 = dheight/3.505

        dcanvas.coords("poly1",x1 + r1,y1,
        x1 + r1,y1,
        x2 - r1,y1,
        x2 - r1,y1,     
        x2,y1,     
        #--------------------
        x2,y1 + r1,     
        x2,y1 + r1,     
        x2,y2 - r1,     
        x2,y2 - r1,     
        x2,y2,
        #--------------------
        x2 - r1,y2,     
        x2 - r1,y2,     
        x1 + r1,y2,
        x1 + r1,y2,
        x1,y2,
        #--------------------
        x1,y2 - r1,
        x1,y2 - r1,
        x1,y1 + r1,
        x1,y1 + r1,
        x1,y1,
        )

        dcanvas.coords("hline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

        r2 = 25
        x11 = dwidth/63
        x21 = dwidth/1.021
        y11 = dheight/2.8
        y21 = dheight/0.37


        dcanvas.coords("poly2",x11 + r2,y11,
        x11 + r2,y11,
        x21 - r2,y11,
        x21 - r2,y11,     
        x21,y11,     
        #--------------------
        x21,y11 + r2,     
        x21,y11 + r2,     
        x21,y21 - r2,     
        x21,y21 - r2,     
        x21,y21,
        #--------------------
        x21 - r2,y21,     
        x21 - r2,y21,     
        x11 + r2,y21,
        x11 + r2,y21,
        x11,y21,
        #--------------------
        x11,y21 - r2,
        x11,y21 - r2,
        x11,y11 + r2,
        x11,y11 + r2,
        x11,y11,
        )
        

        dcanvas.coords("label1",dwidth/2,dheight/8.24)
        dcanvas.coords("label2",dwidth/2,dheight/2.4)

        #payment-------------
        try:
            dcanvas.coords("label3",dwidth/7.91,dheight/1.76)
            dcanvas.coords("label4",dwidth/2.28,dheight/1.76)
            dcanvas.coords("label5",dwidth/1.23,dheight/1.76)
            dcanvas.coords("label6",dwidth/6.1,dheight/1.49)
            dcanvas.coords("label7",dwidth/6.1,dheight/1.3)
            dcanvas.coords("label8",dwidth/1.23,dheight/1.49)
            dcanvas.coords("label9",dwidth/1.23,dheight/1.3)
            dcanvas.coords("label10",dwidth/1.23,dheight/1.14)
            dcanvas.coords("label11",dwidth/1.23,dheight/1.09)
            dcanvas.coords("label12",dwidth/16.2,dheight/0.97)
            dcanvas.coords("label13",dwidth/5.9,dheight/0.97)
            dcanvas.coords("label14",dwidth/3.28,dheight/0.97)
            dcanvas.coords("label15",dwidth/2.1,dheight/0.97)
            dcanvas.coords("label16",dwidth/1.42,dheight/0.97)
            dcanvas.coords("label17",dwidth/1.14,dheight/0.97)
            dcanvas.coords("label18",dwidth/1.49,dheight/0.819)
            dcanvas.coords("label19",dwidth/1.49,dheight/0.759)
            dcanvas.coords("label20",dwidth/16.2,dheight/0.91)

            dcanvas.coords("entry1",dwidth/2.5,dheight/1.68)
            dcanvas.coords("entry2",dwidth/1.35,dheight/1.68)
            dcanvas.coords("entry3",dwidth/11,dheight/1.26)
            dcanvas.coords("entry4",dwidth/1.35,dheight/1.26)
            dcanvas.coords("entry5",dwidth/1.18,dheight/0.819)
            dcanvas.coords("entry6",dwidth/1.18,dheight/0.759)
            try:
                dcanvas.coords("entry7",dwidth/11,dheight/1.19)
            except:
                pass
            dcanvas.coords("entry8",dwidth/5.9,dheight/0.91)
            dcanvas.coords("entry9",dwidth/3.28,dheight/0.91)
            dcanvas.coords("entry10",dwidth/2.07,dheight/0.91)
            dcanvas.coords("entry11",dwidth/1.42,dheight/0.91)
            dcanvas.coords("entry12",dwidth/1.135,dheight/0.91)

            dcanvas.coords("combo1",dwidth/11,dheight/1.68)
            dcanvas.coords("combo2",dwidth/1.35,dheight/1.43)

            dcanvas.coords("button1",dwidth/4,dheight/1.638)
            dcanvas.coords("button2",dwidth/1.11,dheight/1.399)
            dcanvas.coords("button3",dwidth/27,dheight/3)
            dcanvas.coords("button4",dwidth/1.114,dheight/0.70)

            dcanvas.coords("line1",dwidth/31.6,dheight/1.002,dwidth/1.039,dheight/1.002)
            dcanvas.coords("line2",dwidth/31.6,dheight/0.94,dwidth/1.039,dheight/0.94)
            dcanvas.coords("line3",dwidth/31.6,dheight/1.002,dwidth/31.6,dheight/0.878)
            dcanvas.coords("line4",dwidth/1.039,dheight/1.002,dwidth/1.039,dheight/0.878)
            dcanvas.coords("line5",dwidth/11,dheight/1.002,dwidth/11,dheight/0.878)
            dcanvas.coords("line6",dwidth/4,dheight/1.002,dwidth/4,dheight/0.878)
            dcanvas.coords("line7",dwidth/2.8,dheight/1.002,dwidth/2.8,dheight/0.878)
            dcanvas.coords("line8",dwidth/1.65,dheight/1.002,dwidth/1.65,dheight/0.878)
            dcanvas.coords("line9",dwidth/1.25,dheight/1.002,dwidth/1.25,dheight/0.878)
            dcanvas.coords("line10",dwidth/1.65,dheight/0.85,dwidth/1.65,dheight/0.73)
            dcanvas.coords("line11",dwidth/1.039,dheight/0.85,dwidth/1.039,dheight/0.73)
            dcanvas.coords("line12",dwidth/1.65,dheight/0.85,dwidth/1.039,dheight/0.85)
            dcanvas.coords("line13",dwidth/1.65,dheight/0.73,dwidth/1.039,dheight/0.73)
            dcanvas.coords("line14",dwidth/1.65,dheight/0.785,dwidth/1.039,dheight/0.785)
            dcanvas.coords("line15",dwidth/1.36,dheight/0.85,dwidth/1.36,dheight/0.73)
            dcanvas.coords("line16",dwidth/31.6,dheight/0.878,dwidth/1.039,dheight/0.878)
        except:
            pass

        #sales receipt-----------
        try:
            dcanvas.coords("label21",dwidth/7.91,dheight/1.76)
            dcanvas.coords("label22",dwidth/2.47,dheight/1.76)
            dcanvas.coords("label23",dwidth/6.13,dheight/1.44)
            dcanvas.coords("label24",dwidth/2.27,dheight/1.45)
            dcanvas.coords("label25",dwidth/6.13,dheight/0.907)
            dcanvas.coords("label26",dwidth/6.13,dheight/0.81)
            dcanvas.coords("label27",dwidth/2.27,dheight/0.81)
            try:
                dcanvas.coords("label28",dwidth/1.395,dheight/0.81)
            except:
                pass
            dcanvas.coords("label29",dwidth/1.225,dheight/1.75)
            dcanvas.coords("label30",dwidth/1.2,dheight/1.63)
            dcanvas.coords("label31",dwidth/20,dheight/0.68)
            dcanvas.coords("label32",dwidth/20,dheight/0.64)
            dcanvas.coords("label33",dwidth/7.91,dheight/0.68)
            dcanvas.coords("label34",dwidth/4.09,dheight/0.68)
            dcanvas.coords("label35",dwidth/2.57,dheight/0.68)
            dcanvas.coords("label36",dwidth/1.88,dheight/0.68)
            dcanvas.coords("label37",dwidth/1.51,dheight/0.68)
            dcanvas.coords("label38",dwidth/1.25,dheight/0.68)
            dcanvas.coords("label39",dwidth/1.09,dheight/0.68)
            dcanvas.coords("label40",dwidth/1.52,dheight/0.507)
            dcanvas.coords("label41",dwidth/1.52,dheight/0.483)
            dcanvas.coords("label42",dwidth/1.52,dheight/0.462)
            dcanvas.coords("label43",dwidth/1.54,dheight/1.45)
            dcanvas.coords("label44",dwidth/1.225,dheight/1.45)

            dcanvas.coords("entry13",dwidth/2.72,dheight/1.68)
            dcanvas.coords("entry14",dwidth/11,dheight/1.39)
            dcanvas.coords("entry15",dwidth/11,dheight/0.885)
            dcanvas.coords("entry16",dwidth/11,dheight/0.79)
            dcanvas.coords("entry17",dwidth/2.72,dheight/0.79)
            dcanvas.coords("entry18",dwidth/5.13,dheight/0.653)
            dcanvas.coords("entry19",dwidth/3.19,dheight/0.653)
            dcanvas.coords("entry20",dwidth/2.05,dheight/0.653)
            dcanvas.coords("entry21",dwidth/1.676,dheight/0.653)
            dcanvas.coords("entry22",dwidth/1.346,dheight/0.653)
            dcanvas.coords("entry23",dwidth/1.35,dheight/0.513)
            dcanvas.coords("entry24",dwidth/1.35,dheight/0.489)
            dcanvas.coords("entry25",dwidth/1.35,dheight/0.467)
            dcanvas.coords("entry26",dwidth/11,dheight/0.751)
            dcanvas.coords("entry27",dwidth/1.345,dheight/1.392)

            dcanvas.coords("combo3",dwidth/11,dheight/1.68)
            try:
                dcanvas.coords("combo4",dwidth/1.55,dheight/0.79)
            except:
                pass
            dcanvas.coords("combo5",dwidth/7.909,dheight/0.643)
            dcanvas.coords("combo6",dwidth/1.091,dheight/0.643)

            dcanvas.coords("button5",dwidth/3.89,dheight/1.61)
            try:
                dcanvas.coords("button6",dwidth/1.23,dheight/0.775)
            except:
                pass
            dcanvas.coords("button7",dwidth/1.114,dheight/0.431)
            
            dcanvas.coords("line17",dwidth/31.6,dheight/0.7,dwidth/1.039,dheight/0.7)
            dcanvas.coords("line18",dwidth/31.6,dheight/0.66,dwidth/1.039,dheight/0.66)
            dcanvas.coords("line19",dwidth/31.6,dheight/0.625,dwidth/1.039,dheight/0.625)
            dcanvas.coords("line20",dwidth/31.6,dheight/0.593,dwidth/1.039,dheight/0.593)
            dcanvas.coords("line21",dwidth/31.6,dheight/0.564,dwidth/1.039,dheight/0.564)
            dcanvas.coords("line22",dwidth/31.6,dheight/0.537,dwidth/1.039,dheight/0.537)
            dcanvas.coords("line23",dwidth/31.6,dheight/0.7,dwidth/31.6,dheight/0.537)
            dcanvas.coords("line24",dwidth/1.039,dheight/0.7,dwidth/1.039,dheight/0.537)
            dcanvas.coords("line25",dwidth/15,dheight/0.7,dwidth/15,dheight/0.537)
            dcanvas.coords("line26",dwidth/5.3,dheight/0.7,dwidth/5.3,dheight/0.537)
            dcanvas.coords("line27",dwidth/3.3,dheight/0.7,dwidth/3.3,dheight/0.537)
            dcanvas.coords("line28",dwidth/2.1,dheight/0.7,dwidth/2.1,dheight/0.537)
            dcanvas.coords("line29",dwidth/1.7,dheight/0.7,dwidth/1.7,dheight/0.537)
            dcanvas.coords("line30",dwidth/1.365,dheight/0.7,dwidth/1.365,dheight/0.537)
            dcanvas.coords("line31",dwidth/1.15,dheight/0.7,dwidth/1.15,dheight/0.537)

            dcanvas.coords("line32",dwidth/1.7,dheight/0.52,dwidth/1.039,dheight/0.52)
            dcanvas.coords("line33",dwidth/1.7,dheight/0.495,dwidth/1.039,dheight/0.495)
            dcanvas.coords("line34",dwidth/1.7,dheight/0.472,dwidth/1.039,dheight/0.472)
            dcanvas.coords("line35",dwidth/1.7,dheight/0.451,dwidth/1.039,dheight/0.451)
            dcanvas.coords("line36",dwidth/1.7,dheight/0.52,dwidth/1.7,dheight/0.451)
            dcanvas.coords("line37",dwidth/1.365,dheight/0.52,dwidth/1.365,dheight/0.451)
            dcanvas.coords("line38",dwidth/1.039,dheight/0.52,dwidth/1.039,dheight/0.451)
        except:
            pass

        try:
            dcanvas.coords("date",dwidth/2.71,dheight/1.392)
            dcanvas.coords("date1",dwidth/1.73,dheight/1.392)
        except:
            pass

    sr_Canvas_4 = Canvas(sr_Frame_1,bg='#2f516f',scrollregion=(0,0,700,1400))

    sr_Frame_1.grid_columnconfigure(0,weight=1)
    sr_Frame_1.grid_rowconfigure(0,weight=1)

    sr_Scroll_1 = Scrollbar(sr_Frame_1,orient=VERTICAL)
    sr_Scroll_1.grid(row=0,column=1,sticky='ns')
    sr_Scroll_1.config(command=sr_Canvas_4.yview)
    sr_Canvas_4.bind("<Configure>", responsive_widgets4)
    sr_Canvas_4.config(yscrollcommand=sr_Scroll_1.set)
    sr_Canvas_4.grid(row=0,column=0,sticky='nsew')

    if srt_actionCombo.get() == 'Edit':
        sr_Canvas_4.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly1"))
        cm_label1 = Label(sr_Canvas_4,width=18,height=1,text="CASH MEMO NO.",font=('arial 25'),background='#1b3857',fg="white")
        sr_Canvas_4.create_window(0,0,anchor="c",window=cm_label1,tags=("label1"))
        sr_Canvas_4.create_line(0,0,0,0,fill='gray',width=1,tags=("hline"))

        sr_Canvas_4.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly2"))

        cm_label2 = Label(sr_Canvas_4,width=18,height=1,text="Fin sYs",font=('arial 25'),background='#1b3857',fg="white")
        sr_Canvas_4.create_window(0,0,anchor="c",window=cm_label2,tags=("label2"))

        cm_label3 = Label(sr_Canvas_4,width=10,height=1,text="Customer",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
        sr_Canvas_4.create_window(0,0,window=cm_label3,tags=("label21"))

        cm_custCombo = ttk.Combobox(sr_Canvas_4,width=19,font=('arial 15'))
        sr_Canvas_4.create_window(0,0,anchor='nw',window=cm_custCombo,tags=("combo3"))

        cm_label4 = Label(sr_Canvas_4,width=10,height=1,text="Email",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_4.create_window(0,0,window=cm_label4,tags=('label22'))

        cm_email = Entry(sr_Canvas_4,width=20,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_4.create_window(0,0,anchor='nw',window=cm_email,tags=("entry13"))

        cm_label5 = Label(sr_Canvas_4,width=20,height=1,text="Billing Address",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_4.create_window(0,0,window=cm_label5,tags=('label23'))

        cm_baddress = Text(sr_Canvas_4,width=20,font=('arial 15'),height=7,background='#2f516f',foreground='white')
        sr_Canvas_4.create_window(0,0,anchor='nw',window=cm_baddress,tags=("entry14"))

        cm_label7 = Label(sr_Canvas_4,width=20,height=1,text="Place of Supply",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_4.create_window(0,0,window=cm_label7,tags=('label25'))

        cm_pofsupply = ttk.Combobox(sr_Canvas_4,width=19,font=('arial 15'),background='#2f516f')
        sr_Canvas_4.create_window(0,0,anchor='nw',window=cm_pofsupply,tags=("entry15"))

        cm_label8 = Label(sr_Canvas_4,width=20,height=1,text="Payment Method",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_4.create_window(0,0,window=cm_label8,tags=('label26'))

        def addnew_pmethod_1(event):
            if cm_pmethod.get() == "Add new":
                cm_newmeth = Entry(sr_Canvas_4,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                sr_Canvas_4.create_window(115,755,anchor='nw',window=cm_newmeth,tags=("entry26"))
            else:
                pass

        cm_pmethod = ttk.Combobox(sr_Canvas_4,width=19,font=('arial 15'),background='#2f516f')
        cm_pmethod['values'] = ['Add new',]
        cm_pmethod.current(0)
        cm_pmethod.bind("<<ComboboxSelected>>",addnew_pmethod_1)
        sr_Canvas_4.create_window(0,0,anchor='nw',window=cm_pmethod,tags=("entry16"))

        cm_label9 = Label(sr_Canvas_4,width=20,height=1,text="Reference No:",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_4.create_window(0,0,window=cm_label9,tags=('label27'))

        cm_ref = Entry(sr_Canvas_4,width=20,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_4.create_window(0,0,anchor='nw',window=cm_ref,tags=("entry17"))

        cm_label10 = Label(sr_Canvas_4,width=20,height=1,text="Deposit to:",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_4.create_window(0,0,window=cm_label10,tags=('label28'))

        cm_depto = ttk.Combobox(sr_Canvas_4,width=19,font=('arial 15'),background='#2f516f')
        sr_Canvas_4.create_window(0,0,anchor='nw',window=cm_depto,tags=("combo4"))

        cm_label11 = Label(sr_Canvas_4,width=20,height=1,text="AMOUNT",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_4.create_window(0,0,window=cm_label11,tags=('label29'))

        cm_label12 = Label(sr_Canvas_4,width=20,height=1,text="0.00",font=('arial 14'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_4.create_window(0,0,window=cm_label12,tags=('label30'))

        sr_Canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line17"))
        sr_Canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line18"))
        sr_Canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line19"))
        sr_Canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line20"))
        sr_Canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line21"))
        sr_Canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line22"))
        sr_Canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line23"))
        sr_Canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line24"))
        sr_Canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line25"))
        sr_Canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line26"))
        sr_Canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line27"))
        sr_Canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line28"))
        sr_Canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line29"))
        sr_Canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line30"))
        sr_Canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line31"))

        sr_Canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line32"))
        sr_Canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line33"))
        sr_Canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line34"))
        sr_Canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line35"))
        sr_Canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line36"))
        sr_Canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line37"))
        sr_Canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("line38"))

        cm_label13 = Label(sr_Canvas_4,width=3,height=1,text="#",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_4.create_window(0,0,window=cm_label13,tags=('label31'))

        cm_label14 = Label(sr_Canvas_4,width=3,height=1,text="1",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_4.create_window(0,0,window=cm_label14,tags=('label32'))

        cm_label18 = Label(sr_Canvas_4,width=15,height=1,text="Product / Service",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_4.create_window(0,0,window=cm_label18,tags=('label33'))

        cm_label19 = Label(sr_Canvas_4,width=14,height=1,text="HSN",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_4.create_window(0,0,window=cm_label19,tags=('label34'))

        cm_label20 = Label(sr_Canvas_4,width=18,height=1,text="Description",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_4.create_window(0,0,window=cm_label20,tags=('label35'))

        cm_label21 = Label(sr_Canvas_4,width=10,height=1,text="Qty",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_4.create_window(0,0,window=cm_label21,tags=('label36'))

        cm_label22 = Label(sr_Canvas_4,width=10,height=1,text="Price",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_4.create_window(0,0,window=cm_label22,tags=('label37'))

        cm_label23 = Label(sr_Canvas_4,width=10,height=1,text="Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_4.create_window(0,0,window=cm_label23,tags=('label38'))

        cm_label24 = Label(sr_Canvas_4,width=10,height=1,text="Tax (%)",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_4.create_window(0,0,window=cm_label24,tags=('label39'))

        cmt_entry1 = ttk.Combobox(sr_Canvas_4,width=10,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_4.create_window(0,0,anchor='c',window=cmt_entry1,tags=("combo5"))

        cmt_entry2 = Entry(sr_Canvas_4,width=11,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_4.create_window(0,0,anchor='nw',window=cmt_entry2,tags=("entry18"))

        cmt_entry3 = Entry(sr_Canvas_4,width=17,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_4.create_window(0,0,anchor='nw',window=cmt_entry3,tags=("entry19"))

        cmt_entry4 = Entry(sr_Canvas_4,width=10,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_4.create_window(0,0,anchor='nw',window=cmt_entry4,tags=("entry20"))

        cmt_entry5 = Entry(sr_Canvas_4,width=14,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_4.create_window(0,0,anchor='nw',window=cmt_entry5,tags=("entry21"))

        cmt_entry6 = Entry(sr_Canvas_4,width=13,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_4.create_window(0,0,anchor='nw',window=cmt_entry6,tags=("entry22"))

        cmt_entry7 = ttk.Combobox(sr_Canvas_4,width=7,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_4.create_window(0,0,anchor='c',window=cmt_entry7,tags=("combo6"))

        cm_label25 = Label(sr_Canvas_4,width=10,height=1,text="Sub Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_4.create_window(0,0,window=cm_label25,tags=('label40'))

        cm_label26 = Label(sr_Canvas_4,width=10,height=1,text="Tax Amount",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_4.create_window(0,0,window=cm_label26,tags=('label41'))

        cm_label27 = Label(sr_Canvas_4,width=10,height=1,text="Grand Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
        sr_Canvas_4.create_window(0,0,window=cm_label27,tags=('label42'))

        cmt_entry8 = Entry(sr_Canvas_4,width=24,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_4.create_window(0,0,anchor='nw',window=cmt_entry8,tags=("entry23"))

        cmt_entry9 = Entry(sr_Canvas_4,width=24,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_4.create_window(0,0,anchor='nw',window=cmt_entry9,tags=("entry24"))

        cmt_entry10 = Entry(sr_Canvas_4,width=24,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_4.create_window(0,0,anchor='nw',window=cmt_entry10,tags=("entry25"))

        save_btn = Button(sr_Canvas_4,text='Save',width=20,height=2,font=('arial 10 bold'),background="#198fed",activebackground="#198fed",foreground="white",activeforeground="white",bd=0)
        sr_Canvas_4.create_window(0,0,window=save_btn,tags=("button7")) 

        cm_label7 = Label(sr_Canvas_4,width=20,height=1,text="Sales receipt No:",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_4.create_window(0,0,window=cm_label7,tags=('label44'))

        cmt_entry11 = Entry(sr_Canvas_4,width=20,font=('arial 15'),background='#2f516f',foreground='white')
        sr_Canvas_4.create_window(0,0,anchor='nw',window=cmt_entry11,tags=("entry27"))

        def sr_goBack():
            sr_Frame_1.grid_forget()
            sr_Frame.grid(row=0,column=0,sticky='nsew')

        back_btn = Button(sr_Canvas_4,text='←  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:sr_goBack())
        sr_Canvas_4.create_window(0,0,window=back_btn,tags=("button3"))
        #--------------
        cm_label6 = Label(sr_Canvas_4,width=20,height=1,text="Sales receipt date:",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_4.create_window(0,0,window=cm_label6,tags=('label24'))

        cwidth = root.winfo_screenwidth()

        cm_srdate = DateEntry(sr_Canvas_4,width=19,font=('arial 15'),background='#2f516f',foreground='white')
        if cwidth > 1280:
            sr_Canvas_4.create_window(495,442,anchor='nw',window=cm_srdate,tags=("date"))
        elif cwidth <= 1024:
            sr_Canvas_4.create_window(370,455,anchor='nw',window=cm_srdate,tags=("date"))
        else:
            sr_Canvas_4.create_window(465,407,anchor='nw',window=cm_srdate,tags=("date"))

srt_actionCombo = ttk.Combobox(sr_Canvas,width=10)
srt_actionCombo['values'] = ['Actions','Edit','Delete','View']
srt_actionCombo.current(0)
srt_actionCombo.bind("<<ComboboxSelected>>",sr_Actions)
sr_Canvas.create_window(0,0,window=srt_actionCombo,tags=("combo1"))

srt_label1 = Label(sr_Canvas,width=10,height=1,text="DATE", font=('arial 10 bold'),background="#1b3857",fg="white") 
srt_winlabel1 = sr_Canvas.create_window(0, 0, anchor="c", window=srt_label1,tags=("label11"))
srt_label2 = Label(sr_Canvas,width=11,height=1,text="TYPE", font=('arial 10 bold'),background="#1b3857",fg="white") 
srt_winlabel2 = sr_Canvas.create_window(0, 0, anchor="c", window=srt_label2,tags=("label12"))
srt_label3 = Label(sr_Canvas,width=8,height=1,text="NO.", font=('arial 10 bold'),background="#1b3857",fg="white") 
srt_winlabel3 = sr_Canvas.create_window(0, 0, anchor="c", window=srt_label3,tags=("label13"))
srt_label4 = Label(sr_Canvas,width=11,height=1,text="CUSTOMER", font=('arial 10 bold'),background="#1b3857",fg="white") 
srt_winlabel4 = sr_Canvas.create_window(0, 0, anchor="c", window=srt_label4,tags=("label14"))
srt_label5 = Label(sr_Canvas,width=11,height=1,text="DUE DATE", font=('arial 10 bold'),background="#1b3857",fg="white") 
srt_winlabel5 = sr_Canvas.create_window(0, 0, anchor="c", window=srt_label5,tags=("label15"))
srt_label6 = Label(sr_Canvas,width=11,height=1,text="BALANCE", font=('arial 10 bold'),background="#1b3857",fg="white") 
srt_winlabel6 = sr_Canvas.create_window(0, 0, anchor="c", window=srt_label6,tags=("label16"))
srt_label7 = Label(sr_Canvas,width=12,height=1,text="TOTAL BEFORE", font=('arial 10 bold'),background="#1b3857",fg="white") 
srt_winlabel7 = sr_Canvas.create_window(0, 0, anchor="c", window=srt_label7,tags=("label17"))
srt_label8 = Label(sr_Canvas,width=7,height=1,text="TAX", font=('arial 10 bold'),background="#1b3857",fg="white") 
srt_winlabel8 = sr_Canvas.create_window(0, 0, anchor="c", window=srt_label8,tags=("label18"))
srt_label9 = Label(sr_Canvas,width=11,height=1,text="TOTAL", font=('arial 10 bold'),background="#1b3857",fg="white") 
srt_winlabel9 = sr_Canvas.create_window(0, 0, anchor="c", window=srt_label9,tags=("label19"))
srt_label10 = Label(sr_Canvas,width=10,height=1,text="ACTION", font=('arial 10 bold'),background="#1b3857",fg="white") 
srt_winlabel10 = sr_Canvas.create_window(0, 0, anchor="c", window=srt_label10,tags=("label20"))