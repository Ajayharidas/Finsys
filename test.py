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

# root=Tk()

# root.geometry("1920x1080+0+0")

# finsysdb = mysql.connector.connect(
#     host="localhost", user="root", password="", database="newfinsys", port="3306"
# )
# fbcursor = finsysdb.cursor(buffered=True)

# t1_style = ttk.Style()
# t1_style.theme_use('default')
# t1_style.configure('Treeview.Heading',background='yellow')


# t1 = ttk.Treeview(root,height=10,columns=('0','1','2'),show='headings')
# t1.column('0',width=50)
# t1.column('1',width=250)
# t1.column('2',width=250)
# t1.heading('0',text='#')
# t1.heading('1',text='name')
# t1.heading('2',text='tax')
# t1.pack()


# root.mainloop()

def calculateWithout_bundle():
    cmt_entry8.insert(0,float(cmt_entry6.get()) + float(cmt_entry16.get()) + float(cmt_entry23.get()) + float(cmt_entry30.get()))
    if cmt_entry7.get() == "Choose" and cmt_entry17.get() == "Choose" and cmt_entry24.get() == "Choose" and cmt_entry30.get() == "Choose":
        pass
    elif cmt_entry7.get() != "Choose" and cmt_entry17.get() == "Choose" and cmt_entry24.get() == "Choose" and cmt_entry31.get() == "Choose":
        gst_value1 = split_gst(cmt_entry7.get())
        if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
            tax_tot1 = 0
        else:
            tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
        cmt_entry9.insert(0,tax_tot1)
    elif cmt_entry7.get() != "Choose" and cmt_entry17.get() != "Choose" and cmt_entry24.get() == "Choose" and cmt_entry31.get() == "Choose":
        gst_value1 = split_gst(cmt_entry7.get())
        gst_value2 = split_gst(cmt_entry17.get())
        if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
            tax_tot1 = 0
        else:
            tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
        
        if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
            tax_tot2 = 0
        else:
            tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100
        cmt_entry9.insert(0,tax_tot1 + tax_tot2)
    elif cmt_entry7.get() != "Choose" and cmt_entry17.get() != "Choose" and cmt_entry24.get() != "Choose" and cmt_entry31.get() == "Choose":
        gst_value1 = split_gst(cmt_entry7.get())
        gst_value2 = split_gst(cmt_entry17.get())
        gst_value3 = split_gst(cmt_entry24.get())
        if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
            tax_tot1 = 0
        else:
            tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
        
        if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
            tax_tot2 = 0
        else:
            tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100

        if gst_value3 == "0" or cmt_entry24.get() == "Exempt GST(0%)" or cmt_entry24.get() == "Out of Scope(0%)":
            tax_tot3 = 0
        else:
            tax_tot3 = (float(cmt_entry23.get()) * float(float((gst_value3[0]))))/100
        cmt_entry9.insert(0,tax_tot1 + tax_tot2 + tax_tot3)
    elif cmt_entry7.get() != "Choose" and cmt_entry17.get() != "Choose" and cmt_entry24.get() != "Choose" and cmt_entry31.get() != "Choose":
        gst_value1 = split_gst(cmt_entry7.get())
        gst_value2 = split_gst(cmt_entry17.get())
        gst_value3 = split_gst(cmt_entry24.get())
        gst_value4 = split_gst(cmt_entry31.get())
        if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
            tax_tot1 = 0
        else:
            tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
        
        if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
            tax_tot2 = 0
        else:
            tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100

        if gst_value3 == "0" or cmt_entry24.get() == "Exempt GST(0%)" or cmt_entry24.get() == "Out of Scope(0%)":
            tax_tot3 = 0
        else:
            tax_tot3 = (float(cmt_entry23.get()) * float(float((gst_value3[0]))))/100

        if gst_value4 == "0" or cmt_entry31.get() == "Exempt GST(0%)" or cmt_entry31.get() == "Out of Scope(0%)":
            tax_tot4 = 0
        else:
            tax_tot4 = (float(cmt_entry30.get()) * float(float((gst_value4[0]))))/100
        cmt_entry9.insert(0,tax_tot1 + tax_tot2 + tax_tot3 + tax_tot4)
    cmt_entry10.insert(0,float(cmt_entry8.get()) + float(float(cmt_entry9.get())))

def calculateWith_bundle():
    # if not get_pro_data3:
    #     tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
    # else:
    if bt1_entry7.get() == "Choose" and bt1_entry14.get() == "Choose" and bt1_entry21.get() == "Choose" and bt1_entry28.get() == "Choose":
        pass
    elif bt1_entry7.get() != "Choose" and bt1_entry14.get() == "Choose" and bt1_entry21.get() == "Choose" and bt1_entry28.get() == "Choose":
        bgst_value1 = split_gst(bt1_entry7.get())
        if bgst_value1 == "0" or bt1_entry7.get() == "Exempt GST(0%)" or bt1_entry7.get() == "Out of Scope(0%)":
            btax_tot1 = 0
        else:
            btax_tot1 = (float(bt1_entry6.get()) * float(float(bgst_value1[0])))/100
        cmt_entry9.insert(0,btax_tot1)
    elif bt1_entry7.get() != "Choose" and bt1_entry14.get() != "Choose" and bt1_entry21.get() != "Choose" and bt1_entry28.get() != "Choose":
        bgst_value1 = split_gst(bt1_entry7.get())
        bgst_value2 = split_gst(bt1_entry14.get())
        bgst_value3 = split_gst(bt1_entry21.get())
        bgst_value4 = split_gst(bt1_entry28.get())
        tax_tot1 = (float(bt1_entry6.get()) * float(float(bgst_value1[0]))) + (float(bt1_entry13.get()) * float(float(bgst_value2[0]))) + (float(bt1_entry20.get()) * float(float(bgst_value3[0]))) + (float(bt1_entry27.get()) * float(float(bgst_value4[0])))
        print(tax_tot1)
        # cmt_entry9.insert(0,tax_tot1 + tax_tot2 + tax_tot3 + tax_tot4)
    cmt_entry10.insert(0,float(cmt_entry8.get()) + float(float(cmt_entry9.get())))

if not get_pro_data3:
    calculateWithout_bundle()
else:
    calculateWith_bundle()


