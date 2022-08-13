from tkinter import *

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

root=Tk()

root.geometry("1920x1080+0+0")

finsysdb = mysql.connector.connect(
    host="localhost", user="root", password="", database="newfinsys", port="3306"
)
fbcursor = finsysdb.cursor(buffered=True)

t1_style = ttk.Style()
t1_style.theme_use('default')
t1_style.configure('Treeview.Heading',background='yellow')


t1 = ttk.Treeview(root,height=10,columns=('0','1','2'),show='headings')
t1.column('0',width=50)
t1.column('1',width=250)
t1.column('2',width=250)
t1.heading('0',text='#')
t1.heading('1',text='name')
t1.heading('2',text='tax')
t1.pack()


root.mainloop()


