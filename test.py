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


#=============================================

#spinbox 2--------------------------
def cmt_calculateTotal2(event):
    try:
        if cmt_entry14.get() != 0:
            global tax_tot1,tax_tot2,tax_tot3,tax_tot4,b1tax_tot1,b1tax_tot2,b1tax_tot3,b1tax_tot4,b2tax_tot1,b2tax_tot2,b2tax_tot3,b2tax_tot4,b3tax_tot1,b3tax_tot2,b3tax_tot3,b3tax_tot4,b4tax_tot1,b4tax_tot2,b4tax_tot3,b4tax_tot4
            tax_tot1 = 0.0
            tax_tot2 = 0.0
            tax_tot3 = 0.0
            tax_tot4 = 0.0

            b1tax_tot1 = 0.0
            b1tax_tot2 = 0.0
            b1tax_tot3 = 0.0
            b1tax_tot4 = 0.0

            b2tax_tot1 = 0.0
            b2tax_tot2 = 0.0
            b2tax_tot3 = 0.0
            b2tax_tot4 = 0.0

            b3tax_tot1 = 0.0
            b3tax_tot2 = 0.0
            b3tax_tot3 = 0.0
            b3tax_tot4 = 0.0

            b4tax_tot1 = 0.0
            b4tax_tot2 = 0.0
            b4tax_tot3 = 0.0
            b4tax_tot4 = 0.0
            try:
                get_pro_sql = "SELECT * FROM app1_inventory WHERE name=%s AND cid_id=%s"
                get_pro_val = (cmt_entry11.get(),comp_data[0])
                fbcursor.execute(get_pro_sql,get_pro_val)
                get_pro_data = fbcursor.fetchone()

                get_pro_sql1 = "SELECT * FROM app1_noninventory WHERE name=%s AND cid_id=%s"
                get_pro_val1 = (cmt_entry11.get(),comp_data[0])
                fbcursor.execute(get_pro_sql1,get_pro_val1)
                get_pro_data1 = fbcursor.fetchone()

                get_pro_sql2 = "SELECT * FROM app1_service WHERE name=%s AND cid_id=%s"
                get_pro_val2 = (cmt_entry11.get(),comp_data[0])
                fbcursor.execute(get_pro_sql2,get_pro_val2)
                get_pro_data2 = fbcursor.fetchone()

                get_pro_sql3 = "SELECT * FROM app1_bundle WHERE name=%s AND cid_id=%s"
                get_pro_val3 = (cmt_entry11.get(),comp_data[0])
                fbcursor.execute(get_pro_sql3,get_pro_val3)
                get_pro_data3 = fbcursor.fetchone()
            except:
                pass

            if get_pro_data is not None:
                tot = int(get_pro_data[12]) * int(cmt_entry14.get())
                cmt_entry16.delete(0,END)
                cmt_entry16.insert(0,tot)
            elif get_pro_data1 is not None:
                tot = int(get_pro_data1[8]) * int(cmt_entry14.get())
                cmt_entry16.delete(0,END)
                cmt_entry16.insert(0,tot)
            elif get_pro_data2 is not None:
                pass
            else:
                view_bundleitems(b=2)

            cmt_entry8.delete(0,END)
            cmt_entry9.delete(0,END)
            cmt_entry10.delete(0,END)

            def split_gst(string):
                pattern1 = r'\(+'
                pattern2 = r'\%+'
                split1 = re.split(pattern1,string)
                split2 = re.split(pattern2,split1[1])
                return split2

            #product gst -----------------------------
            try:
                gst_value1 = split_gst(cmt_entry7.get())
            except:
                pass
            try:
                gst_value2 = split_gst(cmt_entry17.get())
            except:
                pass
            try:
                gst_value3 = split_gst(cmt_entry24.get())
            except:
                pass
            try:
                gst_value4 = split_gst(cmt_entry31.get())
            except:
                pass

            #bundle gst ------------------------------ 
            try:
                bgst_value1 = split_gst(bt1_entry7.get())
                bgst_value2 = split_gst(bt1_entry14.get())
                bgst_value3 = split_gst(bt1_entry21.get())
                bgst_value4 = split_gst(bt1_entry28.get())
            except:
                pass
            try:
                bgst_value5 = split_gst(bt2_entry7.get())
                bgst_value6 = split_gst(bt2_entry14.get())
                bgst_value7 = split_gst(bt2_entry21.get())
                bgst_value8 = split_gst(bt2_entry28.get())
            except:
                pass
            try:
                bgst_value9 = split_gst(bt3_entry7.get())
                bgst_value10 = split_gst(bt3_entry14.get())
                bgst_value11 = split_gst(bt3_entry21.get())
                bgst_value12 = split_gst(bt3_entry28.get())
            except:
                pass
            try:
                bgst_value13 = split_gst(bt4_entry7.get())
                bgst_value14 = split_gst(bt4_entry14.get())
                bgst_value15 = split_gst(bt4_entry21.get())
                bgst_value16 = split_gst(bt4_entry28.get())
            except:
                pass

            get_bun_sql = "SELECT name FROM app1_bundle WHERE cid_id=%s"
            get_bun_val = (comp_data[0],)
            fbcursor.execute(get_bun_sql,get_bun_val)
            get_bun_data = fbcursor.fetchall()
            
            b_list = []
            for g in get_bun_data:
                b_list.append(g[0])

#=====================================================================================
            #Bundle1--------------------------------------------
            try:
                if bt1_entry7.get() == "Choose" and bt1_entry14.get() == "Choose" and bt1_entry21.get() == "Choose" and bt1_entry28.get() == "Choose":
                    pass
                elif bt1_entry7.get() != "Choose" and bt1_entry14.get() == "Choose" and bt1_entry21.get() == "Choose" and bt1_entry28.get() == "Choose":
                    if bgst_value1 == "0" or bt1_entry7.get() == "Exempt GST(0%)" or bt1_entry7.get() == "Out of Scope(0%)":
                        b1tax_tot1 = 0
                    else:
                        b1tax_tot1 = (float(bt1_entry6.get()) * float(float((bgst_value1[0]))))/100
                    tax_total1 = b1tax_tot1
                elif bt1_entry7.get() != "Choose" and bt1_entry14.get() != "Choose" and bt1_entry21.get() == "Choose" and bt1_entry28.get() == "Choose":
                    if bgst_value1 == "0" or bt1_entry7.get() == "Exempt GST(0%)" or bt1_entry7.get() == "Out of Scope(0%)":
                        b1tax_tot1 = 0
                    else:
                        b1tax_tot1 = (float(bt1_entry6.get()) * float(float((bgst_value1[0]))))/100
                    
                    if bgst_value2 == "0" or bt1_entry14.get() == "Exempt GST(0%)" or bt1_entry14.get() == "Out of Scope(0%)":
                        b1tax_tot2 = 0
                    else:
                        b1tax_tot2 = (float(bt1_entry13.get()) * float(float((bgst_value2[0]))))/100
                    tax_total1 = b1tax_tot1 + b1tax_tot2
                elif bt1_entry7.get() != "Choose" and bt1_entry14.get() != "Choose" and bt1_entry21.get() != "Choose" and bt1_entry28.get() == "Choose":
                    if bgst_value1 == "0" or bt1_entry7.get() == "Exempt GST(0%)" or bt1_entry7.get() == "Out of Scope(0%)":
                        b1tax_tot1 = 0
                    else:
                        b1tax_tot1 = (float(bt1_entry6.get()) * float(float((bgst_value1[0]))))/100
                    
                    if bgst_value2 == "0" or bt1_entry14.get() == "Exempt GST(0%)" or bt1_entry14.get() == "Out of Scope(0%)":
                        b1tax_tot2 = 0
                    else:
                        b1tax_tot2 = (float(bt1_entry13.get()) * float(float((bgst_value2[0]))))/100

                    if bgst_value3 == "0" or bt1_entry21.get() == "Exempt GST(0%)" or bt1_entry21.get() == "Out of Scope(0%)":
                        b1tax_tot3 = 0
                    else:
                        b1tax_tot3 = (float(bt1_entry20.get()) * float(float((bgst_value3[0]))))/100
                    tax_total1 = b1tax_tot1 + b1tax_tot2 + b1tax_tot3
                elif bt1_entry7.get() != "Choose" and bt1_entry14.get() != "Choose" and bt1_entry21.get() != "Choose" and bt1_entry28.get() != "Choose":
                    if bgst_value1 == "0" or bt1_entry7.get() == "Exempt GST(0%)" or bt1_entry7.get() == "Out of Scope(0%)":
                        b1tax_tot1 = 0
                    else:
                        b1tax_tot1 = (float(bt1_entry6.get()) * float(float((bgst_value1[0]))))/100
                    
                    if bgst_value2 == "0" or bt1_entry14.get() == "Exempt GST(0%)" or bt1_entry14.get() == "Out of Scope(0%)":
                        b1tax_tot2 = 0
                    else:
                        b1tax_tot2 = (float(bt1_entry13.get()) * float(float((bgst_value2[0]))))/100

                    if bgst_value3 == "0" or bt1_entry21.get() == "Exempt GST(0%)" or bt1_entry21.get() == "Out of Scope(0%)":
                        b1tax_tot3 = 0
                    else:
                        b1tax_tot3 = (float(bt1_entry20.get()) * float(float((bgst_value3[0]))))/100

                    if bgst_value4 == "0" or bt1_entry28.get() == "Exempt GST(0%)" or bt1_entry28.get() == "Out of Scope(0%)":
                        b1tax_tot4 = 0
                    else:
                        b1tax_tot4 = (float(bt1_entry27.get()) * float(float((bgst_value4[0]))))/100
                    tax_total1 = b1tax_tot1 + b1tax_tot2 + b1tax_tot3 + b1tax_tot4
            except:
                pass

            #Bundle2--------------------------------------------
            try:
                if bt2_entry7.get() == "Choose" and bt2_entry14.get() == "Choose" and bt2_entry21.get() == "Choose" and bt2_entry28.get() == "Choose":
                    pass
                elif bt2_entry7.get() != "Choose" and bt2_entry14.get() == "Choose" and bt2_entry21.get() == "Choose" and bt2_entry28.get() == "Choose":
                    if bgst_value5 == "0" or bt2_entry7.get() == "Exempt GST(0%)" or bt2_entry7.get() == "Out of Scope(0%)":
                        b2tax_tot1 = 0
                    else:
                        b2tax_tot1 = (float(bt2_entry6.get()) * float(float((bgst_value5[0]))))/100
                    tax_total2 = b2tax_tot1
                elif bt2_entry7.get() != "Choose" and bt2_entry14.get() != "Choose" and bt2_entry21.get() == "Choose" and bt2_entry28.get() == "Choose":
                    if bgst_value5 == "0" or bt2_entry7.get() == "Exempt GST(0%)" or bt2_entry7.get() == "Out of Scope(0%)":
                        b2tax_tot1 = 0
                    else:
                        b2tax_tot1 = (float(bt2_entry6.get()) * float(float((bgst_value5[0]))))/100
                    
                    if bgst_value6 == "0" or bt2_entry14.get() == "Exempt GST(0%)" or bt2_entry14.get() == "Out of Scope(0%)":
                        b2tax_tot2 = 0
                    else:
                        b2tax_tot2 = (float(bt2_entry13.get()) * float(float((bgst_value6[0]))))/100
                    tax_total2 = b2tax_tot1 + b2tax_tot2
                elif bt2_entry7.get() != "Choose" and bt2_entry14.get() != "Choose" and bt2_entry21.get() != "Choose" and bt2_entry28.get() == "Choose":
                    if bgst_value5 == "0" or bt2_entry7.get() == "Exempt GST(0%)" or bt2_entry7.get() == "Out of Scope(0%)":
                        b2tax_tot1 = 0
                    else:
                        b2tax_tot1 = (float(bt2_entry6.get()) * float(float((bgst_value5[0]))))/100
                    
                    if bgst_value6 == "0" or bt2_entry14.get() == "Exempt GST(0%)" or bt2_entry14.get() == "Out of Scope(0%)":
                        b2tax_tot2 = 0
                    else:
                        b2tax_tot2 = (float(bt2_entry13.get()) * float(float((bgst_value6[0]))))/100

                    if bgst_value7 == "0" or bt2_entry21.get() == "Exempt GST(0%)" or bt2_entry21.get() == "Out of Scope(0%)":
                        b2tax_tot3 = 0
                    else:
                        b2tax_tot3 = (float(bt2_entry20.get()) * float(float((bgst_value7[0]))))/100
                    tax_total2 = b2tax_tot1 + b2tax_tot2 + b2tax_tot3
                elif bt2_entry7.get() != "Choose" and bt2_entry14.get() != "Choose" and bt2_entry21.get() != "Choose" and bt2_entry28.get() != "Choose":
                    if bgst_value5 == "0" or bt2_entry7.get() == "Exempt GST(0%)" or bt2_entry7.get() == "Out of Scope(0%)":
                        b2tax_tot1 = 0
                    else:
                        b2tax_tot1 = (float(bt2_entry6.get()) * float(float((bgst_value5[0]))))/100
                    
                    if bgst_value6 == "0" or bt2_entry14.get() == "Exempt GST(0%)" or bt2_entry14.get() == "Out of Scope(0%)":
                        b2tax_tot2 = 0
                    else:
                        b2tax_tot2 = (float(bt2_entry13.get()) * float(float((bgst_value6[0]))))/100

                    if bgst_value7 == "0" or bt2_entry21.get() == "Exempt GST(0%)" or bt2_entry21.get() == "Out of Scope(0%)":
                        b2tax_tot3 = 0
                    else:
                        b2tax_tot3 = (float(bt2_entry20.get()) * float(float((bgst_value7[0]))))/100

                    if bgst_value8 == "0" or bt2_entry28.get() == "Exempt GST(0%)" or bt2_entry28.get() == "Out of Scope(0%)":
                        b2tax_tot4 = 0
                    else:
                        b2tax_tot4 = (float(bt2_entry27.get()) * float(float((bgst_value8[0]))))/100
                    tax_total2 = b2tax_tot1 + b2tax_tot2 + b2tax_tot3 + b2tax_tot4
            except:
                pass

            #Bundle3--------------------------------------------
            try:
                if bt3_entry7.get() == "Choose" and bt3_entry14.get() == "Choose" and bt3_entry21.get() == "Choose" and bt3_entry28.get() == "Choose":
                    pass
                elif bt3_entry7.get() != "Choose" and bt3_entry14.get() == "Choose" and bt3_entry21.get() == "Choose" and bt3_entry28.get() == "Choose":
                    if bgst_value9 == "0" or bt3_entry7.get() == "Exempt GST(0%)" or bt3_entry7.get() == "Out of Scope(0%)":
                        b3tax_tot1 = 0
                    else:
                        b3tax_tot1 = (float(bt3_entry6.get()) * float(float((bgst_value9[0]))))/100
                    tax_total3 = b3tax_tot1
                elif bt3_entry7.get() != "Choose" and bt3_entry14.get() != "Choose" and bt3_entry21.get() == "Choose" and bt3_entry28.get() == "Choose":
                    if bgst_value9 == "0" or bt3_entry7.get() == "Exempt GST(0%)" or bt3_entry7.get() == "Out of Scope(0%)":
                        b3tax_tot1 = 0
                    else:
                        b3tax_tot1 = (float(bt3_entry6.get()) * float(float((bgst_value9[0]))))/100
                    
                    if bgst_value10 == "0" or bt3_entry14.get() == "Exempt GST(0%)" or bt3_entry14.get() == "Out of Scope(0%)":
                        b3tax_tot2 = 0
                    else:
                        b3tax_tot2 = (float(bt3_entry13.get()) * float(float((bgst_value10[0]))))/100
                    tax_total3 = b3tax_tot1 + b3tax_tot2
                elif bt3_entry7.get() != "Choose" and bt3_entry14.get() != "Choose" and bt3_entry21.get() != "Choose" and bt3_entry28.get() == "Choose":
                    if bgst_value9 == "0" or bt3_entry7.get() == "Exempt GST(0%)" or bt3_entry7.get() == "Out of Scope(0%)":
                        b3tax_tot1 = 0
                    else:
                        b3tax_tot1 = (float(bt3_entry6.get()) * float(float((bgst_value9[0]))))/100
                    
                    if bgst_value10 == "0" or bt3_entry14.get() == "Exempt GST(0%)" or bt3_entry14.get() == "Out of Scope(0%)":
                        b3tax_tot2 = 0
                    else:
                        b3tax_tot2 = (float(bt3_entry13.get()) * float(float((bgst_value10[0]))))/100

                    if bgst_value11 == "0" or bt3_entry21.get() == "Exempt GST(0%)" or bt3_entry21.get() == "Out of Scope(0%)":
                        b3tax_tot3 = 0
                    else:
                        b3tax_tot3 = (float(bt3_entry20.get()) * float(float((bgst_value11[0]))))/100
                    tax_total3 = b3tax_tot1 + b3tax_tot2 + b3tax_tot3
                elif bt3_entry7.get() != "Choose" and bt3_entry14.get() != "Choose" and bt3_entry21.get() != "Choose" and bt3_entry28.get() != "Choose":
                    if bgst_value9 == "0" or bt3_entry7.get() == "Exempt GST(0%)" or bt3_entry7.get() == "Out of Scope(0%)":
                        b3tax_tot1 = 0
                    else:
                        b3tax_tot1 = (float(bt3_entry6.get()) * float(float((bgst_value9[0]))))/100
                    
                    if bgst_value10 == "0" or bt3_entry14.get() == "Exempt GST(0%)" or bt3_entry14.get() == "Out of Scope(0%)":
                        b3tax_tot2 = 0
                    else:
                        b3tax_tot2 = (float(bt3_entry13.get()) * float(float((bgst_value10[0]))))/100

                    if bgst_value11 == "0" or bt3_entry21.get() == "Exempt GST(0%)" or bt3_entry21.get() == "Out of Scope(0%)":
                        b3tax_tot3 = 0
                    else:
                        b3tax_tot3 = (float(bt3_entry20.get()) * float(float((bgst_value11[0]))))/100

                    if bgst_value12 == "0" or bt3_entry28.get() == "Exempt GST(0%)" or bt3_entry28.get() == "Out of Scope(0%)":
                        b3tax_tot4 = 0
                    else:
                        b3tax_tot4 = (float(bt3_entry27.get()) * float(float((bgst_value12[0]))))/100
                    tax_total3 = b3tax_tot1 + b3tax_tot2 + b3tax_tot3 + b3tax_tot4
            except:
                pass

            #Bundle4--------------------------------------------
            try:
                if bt4_entry7.get() == "Choose" and bt4_entry14.get() == "Choose" and bt4_entry21.get() == "Choose" and bt4_entry28.get() == "Choose":
                    pass
                elif bt4_entry7.get() != "Choose" and bt4_entry14.get() == "Choose" and bt4_entry21.get() == "Choose" and bt4_entry28.get() == "Choose":
                    if bgst_value13 == "0" or bt4_entry7.get() == "Exempt GST(0%)" or bt4_entry7.get() == "Out of Scope(0%)":
                        b4tax_tot1 = 0
                    else:
                        b4tax_tot1 = (float(bt4_entry6.get()) * float(float((bgst_value13[0]))))/100
                    tax_total4 = b4tax_tot1
                elif bt4_entry7.get() != "Choose" and bt4_entry14.get() != "Choose" and bt4_entry21.get() == "Choose" and bt4_entry28.get() == "Choose":
                    if bgst_value13 == "0" or bt4_entry7.get() == "Exempt GST(0%)" or bt4_entry7.get() == "Out of Scope(0%)":
                        b4tax_tot1 = 0
                    else:
                        b4tax_tot1 = (float(bt4_entry6.get()) * float(float((bgst_value13[0]))))/100
                    
                    if bgst_value14 == "0" or bt4_entry14.get() == "Exempt GST(0%)" or bt4_entry14.get() == "Out of Scope(0%)":
                        b4tax_tot2 = 0
                    else:
                        b4tax_tot2 = (float(bt4_entry13.get()) * float(float((bgst_value14[0]))))/100
                    tax_total4 = b4tax_tot1 + b4tax_tot2
                elif bt4_entry7.get() != "Choose" and bt4_entry14.get() != "Choose" and bt4_entry21.get() != "Choose" and bt4_entry28.get() == "Choose":
                    if bgst_value13 == "0" or bt4_entry7.get() == "Exempt GST(0%)" or bt4_entry7.get() == "Out of Scope(0%)":
                        b4tax_tot1 = 0
                    else:
                        b4tax_tot1 = (float(bt4_entry6.get()) * float(float((bgst_value13[0]))))/100
                    
                    if bgst_value14 == "0" or bt4_entry14.get() == "Exempt GST(0%)" or bt4_entry14.get() == "Out of Scope(0%)":
                        b4tax_tot2 = 0
                    else:
                        b4tax_tot2 = (float(bt4_entry13.get()) * float(float((bgst_value14[0]))))/100

                    if bgst_value15 == "0" or bt4_entry21.get() == "Exempt GST(0%)" or bt4_entry21.get() == "Out of Scope(0%)":
                        b4tax_tot3 = 0
                    else:
                        b4tax_tot3 = (float(bt4_entry20.get()) * float(float((bgst_value15[0]))))/100
                    tax_total4 = b4tax_tot1 + b4tax_tot2 + b4tax_tot3
                elif bt4_entry7.get() != "Choose" and bt4_entry14.get() != "Choose" and bt4_entry21.get() != "Choose" and bt4_entry28.get() != "Choose":
                    if bgst_value13 == "0" or bt4_entry7.get() == "Exempt GST(0%)" or bt4_entry7.get() == "Out of Scope(0%)":
                        b4tax_tot1 = 0
                    else:
                        b4tax_tot1 = (float(bt4_entry6.get()) * float(float((bgst_value13[0]))))/100
                    
                    if bgst_value14 == "0" or bt4_entry14.get() == "Exempt GST(0%)" or bt4_entry14.get() == "Out of Scope(0%)":
                        b4tax_tot2 = 0
                    else:
                        b4tax_tot2 = (float(bt4_entry13.get()) * float(float((bgst_value14[0]))))/100

                    if bgst_value15 == "0" or bt4_entry21.get() == "Exempt GST(0%)" or bt4_entry21.get() == "Out of Scope(0%)":
                        b4tax_tot3 = 0
                    else:
                        b4tax_tot3 = (float(bt4_entry20.get()) * float(float((bgst_value15[0]))))/100

                    if bgst_value16 == "0" or bt4_entry28.get() == "Exempt GST(0%)" or bt4_entry28.get() == "Out of Scope(0%)":
                        b4tax_tot4 = 0
                    else:
                        b4tax_tot4 = (float(bt4_entry27.get()) * float(float((bgst_value16[0]))))/100
                    tax_total4 = b4tax_tot1 + b4tax_tot2 + b4tax_tot3 + b4tax_tot4
            except:
                pass

#=============================================================================================

            #All products ----------------------------------------------------------------------------------------
            if cmt_entry1.get() not in b_list and cmt_entry11.get() not in b_list and cmt_entry18.get() not in b_list and cmt_entry25.get() not in b_list:
                cmt_entry8.insert(0,float(cmt_entry6.get()) + float(cmt_entry16.get()) + float(cmt_entry23.get()) + float(cmt_entry30.get()))
                if cmt_entry7.get() == "Choose" and cmt_entry17.get() == "Choose" and cmt_entry24.get() == "Choose" and cmt_entry31.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() == "Choose" and cmt_entry24.get() == "Choose" and cmt_entry31.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    ptax_total = tax_tot1
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() != "Choose" and cmt_entry24.get() == "Choose" and cmt_entry31.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100
                    ptax_total = tax_tot1 + tax_tot2
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() != "Choose" and cmt_entry24.get() != "Choose" and cmt_entry31.get() == "Choose":
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
                    ptax_total = tax_tot1 + tax_tot2 + tax_tot3
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() != "Choose" and cmt_entry24.get() != "Choose" and cmt_entry31.get() != "Choose":
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
                    ptax_total = tax_tot1 + tax_tot2 + tax_tot3 + tax_tot4

                cmt_entry9.insert(0,ptax_total)

            #All bundles -----------------------------------------------------------------------------------
            elif cmt_entry1.get() in b_list and cmt_entry11.get() in b_list and cmt_entry18.get() in b_list and cmt_entry25.get() in b_list:
                b1_tot = float(bt1_entry6.get()) + float(bt1_entry13.get()) + float(bt1_entry20.get()) + float(bt1_entry27.get())
                b2_tot = float(bt2_entry6.get()) + float(bt2_entry13.get()) + float(bt2_entry20.get()) + float(bt2_entry27.get())
                b3_tot = float(bt3_entry6.get()) + float(bt3_entry13.get()) + float(bt3_entry20.get()) + float(bt3_entry27.get())
                b4_tot = float(bt4_entry6.get()) + float(bt4_entry13.get()) + float(bt4_entry20.get()) + float(bt4_entry27.get())
                cmt_entry8.insert(0,b1_tot + b2_tot + b3_tot + b4_tot)

                cmt_entry9.insert(0,tax_total1 + tax_total2 + tax_total3 + tax_total4)

            #First row bundle-----------------------------------------
            elif cmt_entry1.get() in b_list and cmt_entry11.get() not in b_list and cmt_entry18.get() not in b_list and cmt_entry25.get() not in b_list:
                b1_tot = float(bt1_entry6.get()) + float(bt1_entry13.get()) + float(bt1_entry20.get()) + float(bt1_entry27.get())
                cmt_entry8.insert(0,b1_tot + float(cmt_entry16.get()) + float(cmt_entry23.get()) + float(cmt_entry30.get()))

                #Rest products--------------------------------------
                if cmt_entry17.get() == "Choose" and cmt_entry24.get() == "Choose" and cmt_entry31.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry17.get() != "Choose" and cmt_entry24.get() == "Choose" and cmt_entry31.get() == "Choose":                                               
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100
                    ptax_total = tax_tot2
                elif cmt_entry17.get() != "Choose" and cmt_entry24.get() != "Choose" and cmt_entry31.get() == "Choose":                                              
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100

                    if gst_value3 == "0" or cmt_entry24.get() == "Exempt GST(0%)" or cmt_entry24.get() == "Out of Scope(0%)":
                        tax_tot3 = 0
                    else:
                        tax_tot3 = (float(cmt_entry23.get()) * float(float((gst_value3[0]))))/100
                    ptax_total = tax_tot2 + tax_tot3
                elif cmt_entry17.get() != "Choose" and cmt_entry24.get() != "Choose" and cmt_entry31.get() != "Choose":
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
                    ptax_total = tax_tot2 + tax_tot3 + tax_tot4
                cmt_entry9.insert(0,tax_total1 + ptax_total)

            #First and Second row Bundle -------------------------------------
            elif cmt_entry1.get() in b_list and cmt_entry11.get() in b_list and cmt_entry18.get() not in b_list and cmt_entry25.get() not in b_list:
                b1_tot = float(bt1_entry6.get()) + float(bt1_entry13.get()) + float(bt1_entry20.get()) + float(bt1_entry27.get())
                b2_tot = float(bt2_entry6.get()) + float(bt2_entry13.get()) + float(bt2_entry20.get()) + float(bt2_entry27.get())
                cmt_entry8.insert(0,b1_tot + b2_tot + float(cmt_entry23.get()) + float(cmt_entry30.get()))

                #Rest products--------------------------------------
                if cmt_entry24.get() == "Choose" and cmt_entry31.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry24.get() != "Choose" and cmt_entry31.get() == "Choose":
                    if gst_value3 == "0" or cmt_entry24.get() == "Exempt GST(0%)" or cmt_entry24.get() == "Out of Scope(0%)":
                        tax_tot3 = 0
                    else:
                        tax_tot3 = (float(cmt_entry23.get()) * float(float((gst_value3[0]))))/100
                    ptax_total = tax_tot3
                elif cmt_entry24.get() != "Choose" and cmt_entry31.get() != "Choose":
                    if gst_value3 == "0" or cmt_entry24.get() == "Exempt GST(0%)" or cmt_entry24.get() == "Out of Scope(0%)":
                        tax_tot3 = 0
                    else:
                        tax_tot3 = (float(cmt_entry23.get()) * float(float((gst_value3[0]))))/100

                    if gst_value4 == "0" or cmt_entry31.get() == "Exempt GST(0%)" or cmt_entry31.get() == "Out of Scope(0%)":
                        tax_tot4 = 0
                    else:
                        tax_tot4 = (float(cmt_entry30.get()) * float(float((gst_value4[0]))))/100
                    ptax_total = tax_tot3 + tax_tot4

                cmt_entry9.insert(0,tax_total1 + tax_total2 + ptax_total)

            #First,Second and Third row Bundle -------------------------------------
            elif cmt_entry1.get() in b_list and cmt_entry11.get() in b_list and cmt_entry18.get() in b_list and cmt_entry25.get() not in b_list:
                b1_tot = float(bt1_entry6.get()) + float(bt1_entry13.get()) + float(bt1_entry20.get()) + float(bt1_entry27.get())
                b2_tot = float(bt2_entry6.get()) + float(bt2_entry13.get()) + float(bt2_entry20.get()) + float(bt2_entry27.get())
                b3_tot = float(bt3_entry6.get()) + float(bt3_entry13.get()) + float(bt3_entry20.get()) + float(bt3_entry27.get())
                cmt_entry8.insert(0,b1_tot + b2_tot + b3_tot + float(cmt_entry30.get()))

                #Rest products--------------------------------------
                if cmt_entry31.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry31.get() != "Choose":
                    if gst_value4 == "0" or cmt_entry31.get() == "Exempt GST(0%)" or cmt_entry31.get() == "Out of Scope(0%)":
                        tax_tot4 = 0
                    else:
                        tax_tot4 = (float(cmt_entry30.get()) * float(float((gst_value4[0]))))/100
                    ptax_total = tax_tot4
                cmt_entry9.insert(0,tax_total1 + tax_total2 + tax_total3 + ptax_total)
            
            #Second row Bundle------------------------------------
            elif cmt_entry1.get() not in b_list and cmt_entry11.get() in b_list and cmt_entry18.get() not in b_list and cmt_entry25.get() not in b_list:
                b2_tot = float(bt2_entry6.get()) + float(bt2_entry13.get()) + float(bt2_entry20.get()) + float(bt2_entry27.get())
                cmt_entry8.insert(0,float(cmt_entry6.get()) + b2_tot + float(cmt_entry23.get()) + float(cmt_entry30.get()))

                if cmt_entry7.get() == "Choose" and cmt_entry24.get() == "Choose" and cmt_entry31.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry7.get() != "Choose" and cmt_entry24.get() == "Choose" and cmt_entry31.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    ptax_total = tax_tot1
                elif cmt_entry7.get() != "Choose" and cmt_entry24.get() != "Choose" and cmt_entry31.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100

                    if gst_value3 == "0" or cmt_entry24.get() == "Exempt GST(0%)" or cmt_entry24.get() == "Out of Scope(0%)":
                        tax_tot3 = 0
                    else:
                        tax_tot3 = (float(cmt_entry23.get()) * float(float((gst_value3[0]))))/100
                    ptax_total = tax_tot1 + tax_tot3
                elif cmt_entry7.get() != "Choose" and cmt_entry24.get() != "Choose" and cmt_entry31.get() != "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100

                    if gst_value3 == "0" or cmt_entry24.get() == "Exempt GST(0%)" or cmt_entry24.get() == "Out of Scope(0%)":
                        tax_tot3 = 0
                    else:
                        tax_tot3 = (float(cmt_entry23.get()) * float(float((gst_value3[0]))))/100

                    if gst_value4 == "0" or cmt_entry31.get() == "Exempt GST(0%)" or cmt_entry31.get() == "Out of Scope(0%)":
                        tax_tot4 = 0
                    else:
                        tax_tot4 = (float(cmt_entry30.get()) * float(float((gst_value4[0]))))/100
                    ptax_total = tax_tot1 + tax_tot3 + tax_tot4
                cmt_entry9.insert(0,tax_total2 + ptax_total)

            #Second,Third row Bundle------------------------------------
            elif cmt_entry1.get() not in b_list and cmt_entry11.get() in b_list and cmt_entry18.get() in b_list and cmt_entry25.get() not in b_list:
                b2_tot = float(bt2_entry6.get()) + float(bt2_entry13.get()) + float(bt2_entry20.get()) + float(bt2_entry27.get())
                b3_tot = float(bt3_entry6.get()) + float(bt3_entry13.get()) + float(bt3_entry20.get()) + float(bt3_entry27.get())
                cmt_entry8.insert(0,float(cmt_entry6.get()) + b2_tot + b3_tot + float(cmt_entry30.get()))

                if cmt_entry7.get() == "Choose" and cmt_entry31.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry7.get() != "Choose" and cmt_entry31.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    ptax_total = tax_tot1
                elif cmt_entry7.get() != "Choose" and cmt_entry31.get() != "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100

                    if gst_value4 == "0" or cmt_entry31.get() == "Exempt GST(0%)" or cmt_entry31.get() == "Out of Scope(0%)":
                        tax_tot4 = 0
                    else:
                        tax_tot4 = (float(cmt_entry30.get()) * float(float((gst_value4[0]))))/100
                    ptax_total = tax_tot1 + tax_tot4
                cmt_entry9.insert(0,tax_total2 + tax_total3 + ptax_total)

            #Second,Fourth row Bundle------------------------------------
            elif cmt_entry1.get() not in b_list and cmt_entry11.get() in b_list and cmt_entry18.get() not in b_list and cmt_entry25.get() in b_list:
                b2_tot = float(bt2_entry6.get()) + float(bt2_entry13.get()) + float(bt2_entry20.get()) + float(bt2_entry27.get())
                b4_tot = float(bt4_entry6.get()) + float(bt4_entry13.get()) + float(bt4_entry20.get()) + float(bt4_entry27.get())
                cmt_entry8.insert(0,float(cmt_entry6.get()) + b2_tot + float(cmt_entry23.get()) + b4_tot)

                if cmt_entry7.get() == "Choose" and cmt_entry24.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry7.get() != "Choose" and cmt_entry24.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    ptax_total = tax_tot1
                elif cmt_entry7.get() != "Choose" and cmt_entry24.get() != "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100

                    if gst_value3 == "0" or cmt_entry24.get() == "Exempt GST(0%)" or cmt_entry24.get() == "Out of Scope(0%)":
                        tax_tot3 = 0
                    else:
                        tax_tot3 = (float(cmt_entry23.get()) * float(float((gst_value3[0]))))/100
                    ptax_total = tax_tot1 + tax_tot3
                cmt_entry9.insert(0,tax_total2 + tax_total4 + ptax_total)

            #Second,Third and Fourth row Bundle------------------------------------
            elif cmt_entry1.get() not in b_list and cmt_entry11.get() in b_list and cmt_entry18.get() in b_list and cmt_entry25.get() in b_list:
                b2_tot = float(bt2_entry6.get()) + float(bt2_entry13.get()) + float(bt2_entry20.get()) + float(bt2_entry27.get())
                b3_tot = float(bt3_entry6.get()) + float(bt3_entry13.get()) + float(bt3_entry20.get()) + float(bt3_entry27.get())
                b4_tot = float(bt4_entry6.get()) + float(bt4_entry13.get()) + float(bt4_entry20.get()) + float(bt4_entry27.get())
                cmt_entry8.insert(0,float(cmt_entry6.get()) + b2_tot + b3_tot + b4_tot)

                if cmt_entry7.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry7.get() != "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    ptax_total = tax_tot1
                cmt_entry9.insert(0,tax_total2 + tax_total3 + tax_total4 + ptax_total)
            
            #Third row Bundle---------------------------------------------
            elif cmt_entry1.get() not in b_list and cmt_entry11.get() not in b_list and cmt_entry18.get() in b_list and cmt_entry25.get() not in b_list:
                b3_tot = float(bt3_entry6.get()) + float(bt3_entry13.get()) + float(bt3_entry20.get()) + float(bt3_entry27.get())
                cmt_entry8.insert(0,float(cmt_entry6.get()) + float(cmt_entry16.get()) + b3_tot + float(cmt_entry30.get()))

                if cmt_entry7.get() == "Choose" and cmt_entry17.get() == "Choose" and cmt_entry31.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() == "Choose" and cmt_entry31.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    ptax_total = tax_tot1
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() != "Choose" and cmt_entry31.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100
                    ptax_total = tax_tot1 + tax_tot2
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() != "Choose" and cmt_entry31.get() != "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100

                    if gst_value4 == "0" or cmt_entry31.get() == "Exempt GST(0%)" or cmt_entry31.get() == "Out of Scope(0%)":
                        tax_tot4 = 0
                    else:
                        tax_tot4 = (float(cmt_entry30.get()) * float(float((gst_value4[0]))))/100
                    ptax_total = tax_tot1 + tax_tot2 + tax_tot4
                
                cmt_entry9.insert(0,tax_total3 + ptax_total)

            #Third,first row Bundle---------------------------------------------
            elif cmt_entry1.get() in b_list and cmt_entry11.get() not in b_list and cmt_entry18.get() in b_list and cmt_entry25.get() not in b_list:
                b1_tot = float(bt1_entry6.get()) + float(bt1_entry13.get()) + float(bt1_entry20.get()) + float(bt1_entry27.get())
                b3_tot = float(bt3_entry6.get()) + float(bt3_entry13.get()) + float(bt3_entry20.get()) + float(bt3_entry27.get())
                cmt_entry8.insert(0,b1_tot + float(cmt_entry16.get()) + b3_tot + float(cmt_entry30.get()))

                if cmt_entry17.get() == "Choose" and cmt_entry31.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry17.get() != "Choose" and cmt_entry31.get() == "Choose":                                            
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100
                    ptax_total = tax_tot2
                elif cmt_entry17.get() != "Choose" and cmt_entry31.get() != "Choose":                                            
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100

                    if gst_value4 == "0" or cmt_entry31.get() == "Exempt GST(0%)" or cmt_entry31.get() == "Out of Scope(0%)":
                        tax_tot4 = 0
                    else:
                        tax_tot4 = (float(cmt_entry30.get()) * float(float((gst_value4[0]))))/100
                    ptax_total = tax_tot2 + tax_tot4
                
                cmt_entry9.insert(0,tax_total1 + tax_total3 + ptax_total)

            #Third,fourth row Bundle---------------------------------------------
            elif cmt_entry1.get() not in b_list and cmt_entry11.get() not in b_list and cmt_entry18.get() in b_list and cmt_entry25.get() in b_list:
                b3_tot = float(bt3_entry6.get()) + float(bt3_entry13.get()) + float(bt3_entry20.get()) + float(bt3_entry27.get())
                b4_tot = float(bt4_entry6.get()) + float(bt4_entry13.get()) + float(bt4_entry20.get()) + float(bt4_entry27.get())
                cmt_entry8.insert(0,float(cmt_entry6.get()) + float(cmt_entry16.get()) + b3_tot + b4_tot)

                if cmt_entry7.get() == "Choose" and cmt_entry17.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    ptax_total = tax_tot1
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() != "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100
                    ptax_total = tax_tot1 + tax_tot2
                
                cmt_entry9.insert(0,tax_total3 + tax_total4 + ptax_total)

            #Third,first and fourth row Bundle---------------------------------------------
            elif cmt_entry1.get() in b_list and cmt_entry11.get() not in b_list and cmt_entry18.get() in b_list and cmt_entry25.get() in b_list:
                b1_tot = float(bt1_entry6.get()) + float(bt1_entry13.get()) + float(bt1_entry20.get()) + float(bt1_entry27.get())
                b3_tot = float(bt3_entry6.get()) + float(bt3_entry13.get()) + float(bt3_entry20.get()) + float(bt3_entry27.get())
                b4_tot = float(bt4_entry6.get()) + float(bt4_entry13.get()) + float(bt4_entry20.get()) + float(bt4_entry27.get())
                cmt_entry8.insert(0,b1_tot + float(cmt_entry16.get()) + b3_tot + b4_tot)

                if cmt_entry17.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry17.get() != "Choose":                                            
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100
                    ptax_total = tax_tot2
                
                cmt_entry9.insert(0,tax_total1 + tax_total3 + tax_total4 + ptax_total)

            #Fourth row Bundle -----------------------------------------------------
            elif cmt_entry1.get() not in b_list and cmt_entry11.get() not in b_list and cmt_entry18.get() not in b_list and cmt_entry25.get() in b_list:
                b4_tot = float(bt4_entry6.get()) + float(bt4_entry13.get()) + float(bt4_entry20.get()) + float(bt4_entry27.get())
                cmt_entry8.insert(0,float(cmt_entry6.get()) + float(cmt_entry16.get()) + float(cmt_entry23.get()) + b4_tot)

                if cmt_entry7.get() == "Choose" and cmt_entry17.get() == "Choose" and cmt_entry24.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() == "Choose" and cmt_entry24.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    ptax_total = tax_tot1
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() != "Choose" and cmt_entry24.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100
                    ptax_total = tax_tot1 + tax_tot2
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() != "Choose" and cmt_entry24.get() != "Choose":
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
                    ptax_total = tax_tot1 + tax_tot2 + tax_tot3
                cmt_entry9.insert(0,tax_total4 + ptax_total)

            #Fourth,First row Bundle -----------------------------------------------------
            elif cmt_entry1.get() in b_list and cmt_entry11.get() not in b_list and cmt_entry18.get() not in b_list and cmt_entry25.get() in b_list:
                b4_tot = float(bt4_entry6.get()) + float(bt4_entry13.get()) + float(bt4_entry20.get()) + float(bt4_entry27.get())
                b1_tot = float(bt1_entry6.get()) + float(bt1_entry13.get()) + float(bt1_entry20.get()) + float(bt1_entry27.get())
                cmt_entry8.insert(0,b1_tot + float(cmt_entry16.get()) + float(cmt_entry23.get()) + b4_tot)

                if cmt_entry17.get() == "Choose" and cmt_entry24.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry17.get() != "Choose" and cmt_entry24.get() == "Choose":                                            
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100
                    ptax_total = tax_tot2
                elif cmt_entry17.get() != "Choose" and cmt_entry24.get() != "Choose":                                            
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100

                    if gst_value3 == "0" or cmt_entry24.get() == "Exempt GST(0%)" or cmt_entry24.get() == "Out of Scope(0%)":
                        tax_tot3 = 0
                    else:
                        tax_tot3 = (float(cmt_entry23.get()) * float(float((gst_value3[0]))))/100
                    ptax_total = tax_tot2 + tax_tot3
                cmt_entry9.insert(0,tax_total1 + tax_total4 + ptax_total)

            #Fourth,First and Second row Bundle -----------------------------------------------------
            elif cmt_entry1.get() in b_list and cmt_entry11.get() in b_list and cmt_entry18.get() not in b_list and cmt_entry25.get() in b_list:
                b4_tot = float(bt4_entry6.get()) + float(bt4_entry13.get()) + float(bt4_entry20.get()) + float(bt4_entry27.get())
                b1_tot = float(bt1_entry6.get()) + float(bt1_entry13.get()) + float(bt1_entry20.get()) + float(bt1_entry27.get())
                b2_tot = float(bt2_entry6.get()) + float(bt2_entry13.get()) + float(bt2_entry20.get()) + float(bt2_entry27.get())
                cmt_entry8.insert(0,b1_tot + b2_tot + float(cmt_entry23.get()) + b4_tot)

                if cmt_entry24.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry24.get() != "Choose":
                    if gst_value3 == "0" or cmt_entry24.get() == "Exempt GST(0%)" or cmt_entry24.get() == "Out of Scope(0%)":
                        tax_tot3 = 0
                    else:
                        tax_tot3 = (float(cmt_entry23.get()) * float(float((gst_value3[0]))))/100
                    ptax_total = tax_tot3
                cmt_entry9.insert(0,tax_total1 + tax_total2 + tax_total4 + ptax_total)
            cmt_entry10.insert(0,float(cmt_entry8.get()) + float(float(cmt_entry9.get())))
        else:
            pass
    except:
        pass

#spinbox 3--------------------------------

def cmt_calculateTotal3(event):
    try:
        if cmt_entry21.get() != 0:
            global tax_tot1,tax_tot2,tax_tot3,tax_tot4,b1tax_tot1,b1tax_tot2,b1tax_tot3,b1tax_tot4,b2tax_tot1,b2tax_tot2,b2tax_tot3,b2tax_tot4,b3tax_tot1,b3tax_tot2,b3tax_tot3,b3tax_tot4,b4tax_tot1,b4tax_tot2,b4tax_tot3,b4tax_tot4
            tax_tot1 = 0.0
            tax_tot2 = 0.0
            tax_tot3 = 0.0
            tax_tot4 = 0.0

            b1tax_tot1 = 0.0
            b1tax_tot2 = 0.0
            b1tax_tot3 = 0.0
            b1tax_tot4 = 0.0

            b2tax_tot1 = 0.0
            b2tax_tot2 = 0.0
            b2tax_tot3 = 0.0
            b2tax_tot4 = 0.0

            b3tax_tot1 = 0.0
            b3tax_tot2 = 0.0
            b3tax_tot3 = 0.0
            b3tax_tot4 = 0.0

            b4tax_tot1 = 0.0
            b4tax_tot2 = 0.0
            b4tax_tot3 = 0.0
            b4tax_tot4 = 0.0
            try:
                get_pro_sql = "SELECT * FROM app1_inventory WHERE name=%s AND cid_id=%s"
                get_pro_val = (cmt_entry18.get(),comp_data[0])
                fbcursor.execute(get_pro_sql,get_pro_val)
                get_pro_data = fbcursor.fetchone()

                get_pro_sql1 = "SELECT * FROM app1_noninventory WHERE name=%s AND cid_id=%s"
                get_pro_val1 = (cmt_entry18.get(),comp_data[0])
                fbcursor.execute(get_pro_sql1,get_pro_val1)
                get_pro_data1 = fbcursor.fetchone()

                get_pro_sql2 = "SELECT * FROM app1_service WHERE name=%s AND cid_id=%s"
                get_pro_val2 = (cmt_entry18.get(),comp_data[0])
                fbcursor.execute(get_pro_sql2,get_pro_val2)
                get_pro_data2 = fbcursor.fetchone()

                get_pro_sql3 = "SELECT * FROM app1_bundle WHERE name=%s AND cid_id=%s"
                get_pro_val3 = (cmt_entry18.get(),comp_data[0])
                fbcursor.execute(get_pro_sql3,get_pro_val3)
                get_pro_data3 = fbcursor.fetchone()
            except:
                pass

            if get_pro_data is not None:
                tot = int(get_pro_data[12]) * int(cmt_entry21.get())
                cmt_entry23.delete(0,END)
                cmt_entry23.insert(0,tot)
            elif get_pro_data1 is not None:
                tot = int(get_pro_data1[8]) * int(cmt_entry21.get())
                cmt_entry23.delete(0,END)
                cmt_entry23.insert(0,tot)
            elif get_pro_data2 is not None:
                pass
            else:
                view_bundleitems(b=3)

            cmt_entry8.delete(0,END)
            cmt_entry9.delete(0,END)
            cmt_entry10.delete(0,END)

            def split_gst(string):
                pattern1 = r'\(+'
                pattern2 = r'\%+'
                split1 = re.split(pattern1,string)
                split2 = re.split(pattern2,split1[1])
                return split2

            #product gst -----------------------------
            try:
                gst_value1 = split_gst(cmt_entry7.get())
            except:
                pass
            try:
                gst_value2 = split_gst(cmt_entry17.get())
            except:
                pass
            try:
                gst_value3 = split_gst(cmt_entry24.get())
            except:
                pass
            try:
                gst_value4 = split_gst(cmt_entry31.get())
            except:
                pass

            #bundle gst ------------------------------ 
            try:
                bgst_value1 = split_gst(bt1_entry7.get())
                bgst_value2 = split_gst(bt1_entry14.get())
                bgst_value3 = split_gst(bt1_entry21.get())
                bgst_value4 = split_gst(bt1_entry28.get())
            except:
                pass
            try:
                bgst_value5 = split_gst(bt2_entry7.get())
                bgst_value6 = split_gst(bt2_entry14.get())
                bgst_value7 = split_gst(bt2_entry21.get())
                bgst_value8 = split_gst(bt2_entry28.get())
            except:
                pass
            try:
                bgst_value9 = split_gst(bt3_entry7.get())
                bgst_value10 = split_gst(bt3_entry14.get())
                bgst_value11 = split_gst(bt3_entry21.get())
                bgst_value12 = split_gst(bt3_entry28.get())
            except:
                pass
            try:
                bgst_value13 = split_gst(bt4_entry7.get())
                bgst_value14 = split_gst(bt4_entry14.get())
                bgst_value15 = split_gst(bt4_entry21.get())
                bgst_value16 = split_gst(bt4_entry28.get())
            except:
                pass

            get_bun_sql = "SELECT name FROM app1_bundle WHERE cid_id=%s"
            get_bun_val = (comp_data[0],)
            fbcursor.execute(get_bun_sql,get_bun_val)
            get_bun_data = fbcursor.fetchall()
            
            b_list = []
            for g in get_bun_data:
                b_list.append(g[0])

#=====================================================================================
            #Bundle1--------------------------------------------
            try:
                if bt1_entry7.get() == "Choose" and bt1_entry14.get() == "Choose" and bt1_entry21.get() == "Choose" and bt1_entry28.get() == "Choose":
                    pass
                elif bt1_entry7.get() != "Choose" and bt1_entry14.get() == "Choose" and bt1_entry21.get() == "Choose" and bt1_entry28.get() == "Choose":
                    if bgst_value1 == "0" or bt1_entry7.get() == "Exempt GST(0%)" or bt1_entry7.get() == "Out of Scope(0%)":
                        b1tax_tot1 = 0
                    else:
                        b1tax_tot1 = (float(bt1_entry6.get()) * float(float((bgst_value1[0]))))/100
                    tax_total1 = b1tax_tot1
                elif bt1_entry7.get() != "Choose" and bt1_entry14.get() != "Choose" and bt1_entry21.get() == "Choose" and bt1_entry28.get() == "Choose":
                    if bgst_value1 == "0" or bt1_entry7.get() == "Exempt GST(0%)" or bt1_entry7.get() == "Out of Scope(0%)":
                        b1tax_tot1 = 0
                    else:
                        b1tax_tot1 = (float(bt1_entry6.get()) * float(float((bgst_value1[0]))))/100
                    
                    if bgst_value2 == "0" or bt1_entry14.get() == "Exempt GST(0%)" or bt1_entry14.get() == "Out of Scope(0%)":
                        b1tax_tot2 = 0
                    else:
                        b1tax_tot2 = (float(bt1_entry13.get()) * float(float((bgst_value2[0]))))/100
                    tax_total1 = b1tax_tot1 + b1tax_tot2
                elif bt1_entry7.get() != "Choose" and bt1_entry14.get() != "Choose" and bt1_entry21.get() != "Choose" and bt1_entry28.get() == "Choose":
                    if bgst_value1 == "0" or bt1_entry7.get() == "Exempt GST(0%)" or bt1_entry7.get() == "Out of Scope(0%)":
                        b1tax_tot1 = 0
                    else:
                        b1tax_tot1 = (float(bt1_entry6.get()) * float(float((bgst_value1[0]))))/100
                    
                    if bgst_value2 == "0" or bt1_entry14.get() == "Exempt GST(0%)" or bt1_entry14.get() == "Out of Scope(0%)":
                        b1tax_tot2 = 0
                    else:
                        b1tax_tot2 = (float(bt1_entry13.get()) * float(float((bgst_value2[0]))))/100

                    if bgst_value3 == "0" or bt1_entry21.get() == "Exempt GST(0%)" or bt1_entry21.get() == "Out of Scope(0%)":
                        b1tax_tot3 = 0
                    else:
                        b1tax_tot3 = (float(bt1_entry20.get()) * float(float((bgst_value3[0]))))/100
                    tax_total1 = b1tax_tot1 + b1tax_tot2 + b1tax_tot3
                elif bt1_entry7.get() != "Choose" and bt1_entry14.get() != "Choose" and bt1_entry21.get() != "Choose" and bt1_entry28.get() != "Choose":
                    if bgst_value1 == "0" or bt1_entry7.get() == "Exempt GST(0%)" or bt1_entry7.get() == "Out of Scope(0%)":
                        b1tax_tot1 = 0
                    else:
                        b1tax_tot1 = (float(bt1_entry6.get()) * float(float((bgst_value1[0]))))/100
                    
                    if bgst_value2 == "0" or bt1_entry14.get() == "Exempt GST(0%)" or bt1_entry14.get() == "Out of Scope(0%)":
                        b1tax_tot2 = 0
                    else:
                        b1tax_tot2 = (float(bt1_entry13.get()) * float(float((bgst_value2[0]))))/100

                    if bgst_value3 == "0" or bt1_entry21.get() == "Exempt GST(0%)" or bt1_entry21.get() == "Out of Scope(0%)":
                        b1tax_tot3 = 0
                    else:
                        b1tax_tot3 = (float(bt1_entry20.get()) * float(float((bgst_value3[0]))))/100

                    if bgst_value4 == "0" or bt1_entry28.get() == "Exempt GST(0%)" or bt1_entry28.get() == "Out of Scope(0%)":
                        b1tax_tot4 = 0
                    else:
                        b1tax_tot4 = (float(bt1_entry27.get()) * float(float((bgst_value4[0]))))/100
                    tax_total1 = b1tax_tot1 + b1tax_tot2 + b1tax_tot3 + b1tax_tot4
            except:
                pass

            #Bundle2--------------------------------------------
            try:
                if bt2_entry7.get() == "Choose" and bt2_entry14.get() == "Choose" and bt2_entry21.get() == "Choose" and bt2_entry28.get() == "Choose":
                    pass
                elif bt2_entry7.get() != "Choose" and bt2_entry14.get() == "Choose" and bt2_entry21.get() == "Choose" and bt2_entry28.get() == "Choose":
                    if bgst_value5 == "0" or bt2_entry7.get() == "Exempt GST(0%)" or bt2_entry7.get() == "Out of Scope(0%)":
                        b2tax_tot1 = 0
                    else:
                        b2tax_tot1 = (float(bt2_entry6.get()) * float(float((bgst_value5[0]))))/100
                    tax_total2 = b2tax_tot1
                elif bt2_entry7.get() != "Choose" and bt2_entry14.get() != "Choose" and bt2_entry21.get() == "Choose" and bt2_entry28.get() == "Choose":
                    if bgst_value5 == "0" or bt2_entry7.get() == "Exempt GST(0%)" or bt2_entry7.get() == "Out of Scope(0%)":
                        b2tax_tot1 = 0
                    else:
                        b2tax_tot1 = (float(bt2_entry6.get()) * float(float((bgst_value5[0]))))/100
                    
                    if bgst_value6 == "0" or bt2_entry14.get() == "Exempt GST(0%)" or bt2_entry14.get() == "Out of Scope(0%)":
                        b2tax_tot2 = 0
                    else:
                        b2tax_tot2 = (float(bt2_entry13.get()) * float(float((bgst_value6[0]))))/100
                    tax_total2 = b2tax_tot1 + b2tax_tot2
                elif bt2_entry7.get() != "Choose" and bt2_entry14.get() != "Choose" and bt2_entry21.get() != "Choose" and bt2_entry28.get() == "Choose":
                    if bgst_value5 == "0" or bt2_entry7.get() == "Exempt GST(0%)" or bt2_entry7.get() == "Out of Scope(0%)":
                        b2tax_tot1 = 0
                    else:
                        b2tax_tot1 = (float(bt2_entry6.get()) * float(float((bgst_value5[0]))))/100
                    
                    if bgst_value6 == "0" or bt2_entry14.get() == "Exempt GST(0%)" or bt2_entry14.get() == "Out of Scope(0%)":
                        b2tax_tot2 = 0
                    else:
                        b2tax_tot2 = (float(bt2_entry13.get()) * float(float((bgst_value6[0]))))/100

                    if bgst_value7 == "0" or bt2_entry21.get() == "Exempt GST(0%)" or bt2_entry21.get() == "Out of Scope(0%)":
                        b2tax_tot3 = 0
                    else:
                        b2tax_tot3 = (float(bt2_entry20.get()) * float(float((bgst_value7[0]))))/100
                    tax_total2 = b2tax_tot1 + b2tax_tot2 + b2tax_tot3
                elif bt2_entry7.get() != "Choose" and bt2_entry14.get() != "Choose" and bt2_entry21.get() != "Choose" and bt2_entry28.get() != "Choose":
                    if bgst_value5 == "0" or bt2_entry7.get() == "Exempt GST(0%)" or bt2_entry7.get() == "Out of Scope(0%)":
                        b2tax_tot1 = 0
                    else:
                        b2tax_tot1 = (float(bt2_entry6.get()) * float(float((bgst_value5[0]))))/100
                    
                    if bgst_value6 == "0" or bt2_entry14.get() == "Exempt GST(0%)" or bt2_entry14.get() == "Out of Scope(0%)":
                        b2tax_tot2 = 0
                    else:
                        b2tax_tot2 = (float(bt2_entry13.get()) * float(float((bgst_value6[0]))))/100

                    if bgst_value7 == "0" or bt2_entry21.get() == "Exempt GST(0%)" or bt2_entry21.get() == "Out of Scope(0%)":
                        b2tax_tot3 = 0
                    else:
                        b2tax_tot3 = (float(bt2_entry20.get()) * float(float((bgst_value7[0]))))/100

                    if bgst_value8 == "0" or bt2_entry28.get() == "Exempt GST(0%)" or bt2_entry28.get() == "Out of Scope(0%)":
                        b2tax_tot4 = 0
                    else:
                        b2tax_tot4 = (float(bt2_entry27.get()) * float(float((bgst_value8[0]))))/100
                    tax_total2 = b2tax_tot1 + b2tax_tot2 + b2tax_tot3 + b2tax_tot4
            except:
                pass

            #Bundle3--------------------------------------------
            try:
                if bt3_entry7.get() == "Choose" and bt3_entry14.get() == "Choose" and bt3_entry21.get() == "Choose" and bt3_entry28.get() == "Choose":
                    pass
                elif bt3_entry7.get() != "Choose" and bt3_entry14.get() == "Choose" and bt3_entry21.get() == "Choose" and bt3_entry28.get() == "Choose":
                    if bgst_value9 == "0" or bt3_entry7.get() == "Exempt GST(0%)" or bt3_entry7.get() == "Out of Scope(0%)":
                        b3tax_tot1 = 0
                    else:
                        b3tax_tot1 = (float(bt3_entry6.get()) * float(float((bgst_value9[0]))))/100
                    tax_total3 = b3tax_tot1
                elif bt3_entry7.get() != "Choose" and bt3_entry14.get() != "Choose" and bt3_entry21.get() == "Choose" and bt3_entry28.get() == "Choose":
                    if bgst_value9 == "0" or bt3_entry7.get() == "Exempt GST(0%)" or bt3_entry7.get() == "Out of Scope(0%)":
                        b3tax_tot1 = 0
                    else:
                        b3tax_tot1 = (float(bt3_entry6.get()) * float(float((bgst_value9[0]))))/100
                    
                    if bgst_value10 == "0" or bt3_entry14.get() == "Exempt GST(0%)" or bt3_entry14.get() == "Out of Scope(0%)":
                        b3tax_tot2 = 0
                    else:
                        b3tax_tot2 = (float(bt3_entry13.get()) * float(float((bgst_value10[0]))))/100
                    tax_total3 = b3tax_tot1 + b3tax_tot2
                elif bt3_entry7.get() != "Choose" and bt3_entry14.get() != "Choose" and bt3_entry21.get() != "Choose" and bt3_entry28.get() == "Choose":
                    if bgst_value9 == "0" or bt3_entry7.get() == "Exempt GST(0%)" or bt3_entry7.get() == "Out of Scope(0%)":
                        b3tax_tot1 = 0
                    else:
                        b3tax_tot1 = (float(bt3_entry6.get()) * float(float((bgst_value9[0]))))/100
                    
                    if bgst_value10 == "0" or bt3_entry14.get() == "Exempt GST(0%)" or bt3_entry14.get() == "Out of Scope(0%)":
                        b3tax_tot2 = 0
                    else:
                        b3tax_tot2 = (float(bt3_entry13.get()) * float(float((bgst_value10[0]))))/100

                    if bgst_value11 == "0" or bt3_entry21.get() == "Exempt GST(0%)" or bt3_entry21.get() == "Out of Scope(0%)":
                        b3tax_tot3 = 0
                    else:
                        b3tax_tot3 = (float(bt3_entry20.get()) * float(float((bgst_value11[0]))))/100
                    tax_total3 = b3tax_tot1 + b3tax_tot2 + b3tax_tot3
                elif bt3_entry7.get() != "Choose" and bt3_entry14.get() != "Choose" and bt3_entry21.get() != "Choose" and bt3_entry28.get() != "Choose":
                    if bgst_value9 == "0" or bt3_entry7.get() == "Exempt GST(0%)" or bt3_entry7.get() == "Out of Scope(0%)":
                        b3tax_tot1 = 0
                    else:
                        b3tax_tot1 = (float(bt3_entry6.get()) * float(float((bgst_value9[0]))))/100
                    
                    if bgst_value10 == "0" or bt3_entry14.get() == "Exempt GST(0%)" or bt3_entry14.get() == "Out of Scope(0%)":
                        b3tax_tot2 = 0
                    else:
                        b3tax_tot2 = (float(bt3_entry13.get()) * float(float((bgst_value10[0]))))/100

                    if bgst_value11 == "0" or bt3_entry21.get() == "Exempt GST(0%)" or bt3_entry21.get() == "Out of Scope(0%)":
                        b3tax_tot3 = 0
                    else:
                        b3tax_tot3 = (float(bt3_entry20.get()) * float(float((bgst_value11[0]))))/100

                    if bgst_value12 == "0" or bt3_entry28.get() == "Exempt GST(0%)" or bt3_entry28.get() == "Out of Scope(0%)":
                        b3tax_tot4 = 0
                    else:
                        b3tax_tot4 = (float(bt3_entry27.get()) * float(float((bgst_value12[0]))))/100
                    tax_total3 = b3tax_tot1 + b3tax_tot2 + b3tax_tot3 + b3tax_tot4
            except:
                pass

            #Bundle4--------------------------------------------
            try:
                if bt4_entry7.get() == "Choose" and bt4_entry14.get() == "Choose" and bt4_entry21.get() == "Choose" and bt4_entry28.get() == "Choose":
                    pass
                elif bt4_entry7.get() != "Choose" and bt4_entry14.get() == "Choose" and bt4_entry21.get() == "Choose" and bt4_entry28.get() == "Choose":
                    if bgst_value13 == "0" or bt4_entry7.get() == "Exempt GST(0%)" or bt4_entry7.get() == "Out of Scope(0%)":
                        b4tax_tot1 = 0
                    else:
                        b4tax_tot1 = (float(bt4_entry6.get()) * float(float((bgst_value13[0]))))/100
                    tax_total4 = b4tax_tot1
                elif bt4_entry7.get() != "Choose" and bt4_entry14.get() != "Choose" and bt4_entry21.get() == "Choose" and bt4_entry28.get() == "Choose":
                    if bgst_value13 == "0" or bt4_entry7.get() == "Exempt GST(0%)" or bt4_entry7.get() == "Out of Scope(0%)":
                        b4tax_tot1 = 0
                    else:
                        b4tax_tot1 = (float(bt4_entry6.get()) * float(float((bgst_value13[0]))))/100
                    
                    if bgst_value14 == "0" or bt4_entry14.get() == "Exempt GST(0%)" or bt4_entry14.get() == "Out of Scope(0%)":
                        b4tax_tot2 = 0
                    else:
                        b4tax_tot2 = (float(bt4_entry13.get()) * float(float((bgst_value14[0]))))/100
                    tax_total4 = b4tax_tot1 + b4tax_tot2
                elif bt4_entry7.get() != "Choose" and bt4_entry14.get() != "Choose" and bt4_entry21.get() != "Choose" and bt4_entry28.get() == "Choose":
                    if bgst_value13 == "0" or bt4_entry7.get() == "Exempt GST(0%)" or bt4_entry7.get() == "Out of Scope(0%)":
                        b4tax_tot1 = 0
                    else:
                        b4tax_tot1 = (float(bt4_entry6.get()) * float(float((bgst_value13[0]))))/100
                    
                    if bgst_value14 == "0" or bt4_entry14.get() == "Exempt GST(0%)" or bt4_entry14.get() == "Out of Scope(0%)":
                        b4tax_tot2 = 0
                    else:
                        b4tax_tot2 = (float(bt4_entry13.get()) * float(float((bgst_value14[0]))))/100

                    if bgst_value15 == "0" or bt4_entry21.get() == "Exempt GST(0%)" or bt4_entry21.get() == "Out of Scope(0%)":
                        b4tax_tot3 = 0
                    else:
                        b4tax_tot3 = (float(bt4_entry20.get()) * float(float((bgst_value15[0]))))/100
                    tax_total4 = b4tax_tot1 + b4tax_tot2 + b4tax_tot3
                elif bt4_entry7.get() != "Choose" and bt4_entry14.get() != "Choose" and bt4_entry21.get() != "Choose" and bt4_entry28.get() != "Choose":
                    if bgst_value13 == "0" or bt4_entry7.get() == "Exempt GST(0%)" or bt4_entry7.get() == "Out of Scope(0%)":
                        b4tax_tot1 = 0
                    else:
                        b4tax_tot1 = (float(bt4_entry6.get()) * float(float((bgst_value13[0]))))/100
                    
                    if bgst_value14 == "0" or bt4_entry14.get() == "Exempt GST(0%)" or bt4_entry14.get() == "Out of Scope(0%)":
                        b4tax_tot2 = 0
                    else:
                        b4tax_tot2 = (float(bt4_entry13.get()) * float(float((bgst_value14[0]))))/100

                    if bgst_value15 == "0" or bt4_entry21.get() == "Exempt GST(0%)" or bt4_entry21.get() == "Out of Scope(0%)":
                        b4tax_tot3 = 0
                    else:
                        b4tax_tot3 = (float(bt4_entry20.get()) * float(float((bgst_value15[0]))))/100

                    if bgst_value16 == "0" or bt4_entry28.get() == "Exempt GST(0%)" or bt4_entry28.get() == "Out of Scope(0%)":
                        b4tax_tot4 = 0
                    else:
                        b4tax_tot4 = (float(bt4_entry27.get()) * float(float((bgst_value16[0]))))/100
                    tax_total4 = b4tax_tot1 + b4tax_tot2 + b4tax_tot3 + b4tax_tot4
            except:
                pass

#=============================================================================================

            #All products ----------------------------------------------------------------------------------------
            if cmt_entry1.get() not in b_list and cmt_entry11.get() not in b_list and cmt_entry18.get() not in b_list and cmt_entry25.get() not in b_list:
                cmt_entry8.insert(0,float(cmt_entry6.get()) + float(cmt_entry16.get()) + float(cmt_entry23.get()) + float(cmt_entry30.get()))
                if cmt_entry7.get() == "Choose" and cmt_entry17.get() == "Choose" and cmt_entry24.get() == "Choose" and cmt_entry31.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() == "Choose" and cmt_entry24.get() == "Choose" and cmt_entry31.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    ptax_total = tax_tot1
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() != "Choose" and cmt_entry24.get() == "Choose" and cmt_entry31.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100
                    ptax_total = tax_tot1 + tax_tot2
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() != "Choose" and cmt_entry24.get() != "Choose" and cmt_entry31.get() == "Choose":
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
                    ptax_total = tax_tot1 + tax_tot2 + tax_tot3
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() != "Choose" and cmt_entry24.get() != "Choose" and cmt_entry31.get() != "Choose":
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
                    ptax_total = tax_tot1 + tax_tot2 + tax_tot3 + tax_tot4

                cmt_entry9.insert(0,ptax_total)

            #All bundles -----------------------------------------------------------------------------------
            elif cmt_entry1.get() in b_list and cmt_entry11.get() in b_list and cmt_entry18.get() in b_list and cmt_entry25.get() in b_list:
                b1_tot = float(bt1_entry6.get()) + float(bt1_entry13.get()) + float(bt1_entry20.get()) + float(bt1_entry27.get())
                b2_tot = float(bt2_entry6.get()) + float(bt2_entry13.get()) + float(bt2_entry20.get()) + float(bt2_entry27.get())
                b3_tot = float(bt3_entry6.get()) + float(bt3_entry13.get()) + float(bt3_entry20.get()) + float(bt3_entry27.get())
                b4_tot = float(bt4_entry6.get()) + float(bt4_entry13.get()) + float(bt4_entry20.get()) + float(bt4_entry27.get())
                cmt_entry8.insert(0,b1_tot + b2_tot + b3_tot + b4_tot)

                cmt_entry9.insert(0,tax_total1 + tax_total2 + tax_total3 + tax_total4)

            #First row bundle-----------------------------------------
            elif cmt_entry1.get() in b_list and cmt_entry11.get() not in b_list and cmt_entry18.get() not in b_list and cmt_entry25.get() not in b_list:
                b1_tot = float(bt1_entry6.get()) + float(bt1_entry13.get()) + float(bt1_entry20.get()) + float(bt1_entry27.get())
                cmt_entry8.insert(0,b1_tot + float(cmt_entry16.get()) + float(cmt_entry23.get()) + float(cmt_entry30.get()))

                #Rest products--------------------------------------
                if cmt_entry17.get() == "Choose" and cmt_entry24.get() == "Choose" and cmt_entry31.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry17.get() != "Choose" and cmt_entry24.get() == "Choose" and cmt_entry31.get() == "Choose":                                               
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100
                    ptax_total = tax_tot2
                elif cmt_entry17.get() != "Choose" and cmt_entry24.get() != "Choose" and cmt_entry31.get() == "Choose":                                              
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100

                    if gst_value3 == "0" or cmt_entry24.get() == "Exempt GST(0%)" or cmt_entry24.get() == "Out of Scope(0%)":
                        tax_tot3 = 0
                    else:
                        tax_tot3 = (float(cmt_entry23.get()) * float(float((gst_value3[0]))))/100
                    ptax_total = tax_tot2 + tax_tot3
                elif cmt_entry17.get() != "Choose" and cmt_entry24.get() != "Choose" and cmt_entry31.get() != "Choose":
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
                    ptax_total = tax_tot2 + tax_tot3 + tax_tot4
                cmt_entry9.insert(0,tax_total1 + ptax_total)

            #First and Second row Bundle -------------------------------------
            elif cmt_entry1.get() in b_list and cmt_entry11.get() in b_list and cmt_entry18.get() not in b_list and cmt_entry25.get() not in b_list:
                b1_tot = float(bt1_entry6.get()) + float(bt1_entry13.get()) + float(bt1_entry20.get()) + float(bt1_entry27.get())
                b2_tot = float(bt2_entry6.get()) + float(bt2_entry13.get()) + float(bt2_entry20.get()) + float(bt2_entry27.get())
                cmt_entry8.insert(0,b1_tot + b2_tot + float(cmt_entry23.get()) + float(cmt_entry30.get()))

                #Rest products--------------------------------------
                if cmt_entry24.get() == "Choose" and cmt_entry31.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry24.get() != "Choose" and cmt_entry31.get() == "Choose":
                    if gst_value3 == "0" or cmt_entry24.get() == "Exempt GST(0%)" or cmt_entry24.get() == "Out of Scope(0%)":
                        tax_tot3 = 0
                    else:
                        tax_tot3 = (float(cmt_entry23.get()) * float(float((gst_value3[0]))))/100
                    ptax_total = tax_tot3
                elif cmt_entry24.get() != "Choose" and cmt_entry31.get() != "Choose":
                    if gst_value3 == "0" or cmt_entry24.get() == "Exempt GST(0%)" or cmt_entry24.get() == "Out of Scope(0%)":
                        tax_tot3 = 0
                    else:
                        tax_tot3 = (float(cmt_entry23.get()) * float(float((gst_value3[0]))))/100

                    if gst_value4 == "0" or cmt_entry31.get() == "Exempt GST(0%)" or cmt_entry31.get() == "Out of Scope(0%)":
                        tax_tot4 = 0
                    else:
                        tax_tot4 = (float(cmt_entry30.get()) * float(float((gst_value4[0]))))/100
                    ptax_total = tax_tot3 + tax_tot4

                cmt_entry9.insert(0,tax_total1 + tax_total2 + ptax_total)

            #First,Second and Third row Bundle -------------------------------------
            elif cmt_entry1.get() in b_list and cmt_entry11.get() in b_list and cmt_entry18.get() in b_list and cmt_entry25.get() not in b_list:
                b1_tot = float(bt1_entry6.get()) + float(bt1_entry13.get()) + float(bt1_entry20.get()) + float(bt1_entry27.get())
                b2_tot = float(bt2_entry6.get()) + float(bt2_entry13.get()) + float(bt2_entry20.get()) + float(bt2_entry27.get())
                b3_tot = float(bt3_entry6.get()) + float(bt3_entry13.get()) + float(bt3_entry20.get()) + float(bt3_entry27.get())
                cmt_entry8.insert(0,b1_tot + b2_tot + b3_tot + float(cmt_entry30.get()))

                #Rest products--------------------------------------
                if cmt_entry31.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry31.get() != "Choose":
                    if gst_value4 == "0" or cmt_entry31.get() == "Exempt GST(0%)" or cmt_entry31.get() == "Out of Scope(0%)":
                        tax_tot4 = 0
                    else:
                        tax_tot4 = (float(cmt_entry30.get()) * float(float((gst_value4[0]))))/100
                    ptax_total = tax_tot4
                cmt_entry9.insert(0,tax_total1 + tax_total2 + tax_total3 + ptax_total)
            
            #Second row Bundle------------------------------------
            elif cmt_entry1.get() not in b_list and cmt_entry11.get() in b_list and cmt_entry18.get() not in b_list and cmt_entry25.get() not in b_list:
                b2_tot = float(bt2_entry6.get()) + float(bt2_entry13.get()) + float(bt2_entry20.get()) + float(bt2_entry27.get())
                cmt_entry8.insert(0,float(cmt_entry6.get()) + b2_tot + float(cmt_entry23.get()) + float(cmt_entry30.get()))

                if cmt_entry7.get() == "Choose" and cmt_entry24.get() == "Choose" and cmt_entry31.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry7.get() != "Choose" and cmt_entry24.get() == "Choose" and cmt_entry31.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    ptax_total = tax_tot1
                elif cmt_entry7.get() != "Choose" and cmt_entry24.get() != "Choose" and cmt_entry31.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100

                    if gst_value3 == "0" or cmt_entry24.get() == "Exempt GST(0%)" or cmt_entry24.get() == "Out of Scope(0%)":
                        tax_tot3 = 0
                    else:
                        tax_tot3 = (float(cmt_entry23.get()) * float(float((gst_value3[0]))))/100
                    ptax_total = tax_tot1 + tax_tot3
                elif cmt_entry7.get() != "Choose" and cmt_entry24.get() != "Choose" and cmt_entry31.get() != "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100

                    if gst_value3 == "0" or cmt_entry24.get() == "Exempt GST(0%)" or cmt_entry24.get() == "Out of Scope(0%)":
                        tax_tot3 = 0
                    else:
                        tax_tot3 = (float(cmt_entry23.get()) * float(float((gst_value3[0]))))/100

                    if gst_value4 == "0" or cmt_entry31.get() == "Exempt GST(0%)" or cmt_entry31.get() == "Out of Scope(0%)":
                        tax_tot4 = 0
                    else:
                        tax_tot4 = (float(cmt_entry30.get()) * float(float((gst_value4[0]))))/100
                    ptax_total = tax_tot1 + tax_tot3 + tax_tot4
                cmt_entry9.insert(0,tax_total2 + ptax_total)

            #Second,Third row Bundle------------------------------------
            elif cmt_entry1.get() not in b_list and cmt_entry11.get() in b_list and cmt_entry18.get() in b_list and cmt_entry25.get() not in b_list:
                b2_tot = float(bt2_entry6.get()) + float(bt2_entry13.get()) + float(bt2_entry20.get()) + float(bt2_entry27.get())
                b3_tot = float(bt3_entry6.get()) + float(bt3_entry13.get()) + float(bt3_entry20.get()) + float(bt3_entry27.get())
                cmt_entry8.insert(0,float(cmt_entry6.get()) + b2_tot + b3_tot + float(cmt_entry30.get()))

                if cmt_entry7.get() == "Choose" and cmt_entry31.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry7.get() != "Choose" and cmt_entry31.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    ptax_total = tax_tot1
                elif cmt_entry7.get() != "Choose" and cmt_entry31.get() != "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100

                    if gst_value4 == "0" or cmt_entry31.get() == "Exempt GST(0%)" or cmt_entry31.get() == "Out of Scope(0%)":
                        tax_tot4 = 0
                    else:
                        tax_tot4 = (float(cmt_entry30.get()) * float(float((gst_value4[0]))))/100
                    ptax_total = tax_tot1 + tax_tot4
                cmt_entry9.insert(0,tax_total2 + tax_total3 + ptax_total)

            #Second,Fourth row Bundle------------------------------------
            elif cmt_entry1.get() not in b_list and cmt_entry11.get() in b_list and cmt_entry18.get() not in b_list and cmt_entry25.get() in b_list:
                b2_tot = float(bt2_entry6.get()) + float(bt2_entry13.get()) + float(bt2_entry20.get()) + float(bt2_entry27.get())
                b4_tot = float(bt4_entry6.get()) + float(bt4_entry13.get()) + float(bt4_entry20.get()) + float(bt4_entry27.get())
                cmt_entry8.insert(0,float(cmt_entry6.get()) + b2_tot + float(cmt_entry23.get()) + b4_tot)

                if cmt_entry7.get() == "Choose" and cmt_entry24.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry7.get() != "Choose" and cmt_entry24.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    ptax_total = tax_tot1
                elif cmt_entry7.get() != "Choose" and cmt_entry24.get() != "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100

                    if gst_value3 == "0" or cmt_entry24.get() == "Exempt GST(0%)" or cmt_entry24.get() == "Out of Scope(0%)":
                        tax_tot3 = 0
                    else:
                        tax_tot3 = (float(cmt_entry23.get()) * float(float((gst_value3[0]))))/100
                    ptax_total = tax_tot1 + tax_tot3
                cmt_entry9.insert(0,tax_total2 + tax_total4 + ptax_total)

            #Second,Third and Fourth row Bundle------------------------------------
            elif cmt_entry1.get() not in b_list and cmt_entry11.get() in b_list and cmt_entry18.get() in b_list and cmt_entry25.get() in b_list:
                b2_tot = float(bt2_entry6.get()) + float(bt2_entry13.get()) + float(bt2_entry20.get()) + float(bt2_entry27.get())
                b3_tot = float(bt3_entry6.get()) + float(bt3_entry13.get()) + float(bt3_entry20.get()) + float(bt3_entry27.get())
                b4_tot = float(bt4_entry6.get()) + float(bt4_entry13.get()) + float(bt4_entry20.get()) + float(bt4_entry27.get())
                cmt_entry8.insert(0,float(cmt_entry6.get()) + b2_tot + b3_tot + b4_tot)

                if cmt_entry7.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry7.get() != "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    ptax_total = tax_tot1
                cmt_entry9.insert(0,tax_total2 + tax_total3 + tax_total4 + ptax_total)
            
            #Third row Bundle---------------------------------------------
            elif cmt_entry1.get() not in b_list and cmt_entry11.get() not in b_list and cmt_entry18.get() in b_list and cmt_entry25.get() not in b_list:
                b3_tot = float(bt3_entry6.get()) + float(bt3_entry13.get()) + float(bt3_entry20.get()) + float(bt3_entry27.get())
                cmt_entry8.insert(0,float(cmt_entry6.get()) + float(cmt_entry16.get()) + b3_tot + float(cmt_entry30.get()))

                if cmt_entry7.get() == "Choose" and cmt_entry17.get() == "Choose" and cmt_entry31.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() == "Choose" and cmt_entry31.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    ptax_total = tax_tot1
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() != "Choose" and cmt_entry31.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100
                    ptax_total = tax_tot1 + tax_tot2
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() != "Choose" and cmt_entry31.get() != "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100

                    if gst_value4 == "0" or cmt_entry31.get() == "Exempt GST(0%)" or cmt_entry31.get() == "Out of Scope(0%)":
                        tax_tot4 = 0
                    else:
                        tax_tot4 = (float(cmt_entry30.get()) * float(float((gst_value4[0]))))/100
                    ptax_total = tax_tot1 + tax_tot2 + tax_tot4
                
                cmt_entry9.insert(0,tax_total3 + ptax_total)

            #Third,first row Bundle---------------------------------------------
            elif cmt_entry1.get() in b_list and cmt_entry11.get() not in b_list and cmt_entry18.get() in b_list and cmt_entry25.get() not in b_list:
                b1_tot = float(bt1_entry6.get()) + float(bt1_entry13.get()) + float(bt1_entry20.get()) + float(bt1_entry27.get())
                b3_tot = float(bt3_entry6.get()) + float(bt3_entry13.get()) + float(bt3_entry20.get()) + float(bt3_entry27.get())
                cmt_entry8.insert(0,b1_tot + float(cmt_entry16.get()) + b3_tot + float(cmt_entry30.get()))

                if cmt_entry17.get() == "Choose" and cmt_entry31.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry17.get() != "Choose" and cmt_entry31.get() == "Choose":                                            
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100
                    ptax_total = tax_tot2
                elif cmt_entry17.get() != "Choose" and cmt_entry31.get() != "Choose":                                            
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100

                    if gst_value4 == "0" or cmt_entry31.get() == "Exempt GST(0%)" or cmt_entry31.get() == "Out of Scope(0%)":
                        tax_tot4 = 0
                    else:
                        tax_tot4 = (float(cmt_entry30.get()) * float(float((gst_value4[0]))))/100
                    ptax_total = tax_tot2 + tax_tot4
                
                cmt_entry9.insert(0,tax_total1 + tax_total3 + ptax_total)

            #Third,fourth row Bundle---------------------------------------------
            elif cmt_entry1.get() not in b_list and cmt_entry11.get() not in b_list and cmt_entry18.get() in b_list and cmt_entry25.get() in b_list:
                b3_tot = float(bt3_entry6.get()) + float(bt3_entry13.get()) + float(bt3_entry20.get()) + float(bt3_entry27.get())
                b4_tot = float(bt4_entry6.get()) + float(bt4_entry13.get()) + float(bt4_entry20.get()) + float(bt4_entry27.get())
                cmt_entry8.insert(0,float(cmt_entry6.get()) + float(cmt_entry16.get()) + b3_tot + b4_tot)

                if cmt_entry7.get() == "Choose" and cmt_entry17.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    ptax_total = tax_tot1
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() != "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100
                    ptax_total = tax_tot1 + tax_tot2
                
                cmt_entry9.insert(0,tax_total3 + tax_total4 + ptax_total)

            #Third,first and fourth row Bundle---------------------------------------------
            elif cmt_entry1.get() in b_list and cmt_entry11.get() not in b_list and cmt_entry18.get() in b_list and cmt_entry25.get() in b_list:
                b1_tot = float(bt1_entry6.get()) + float(bt1_entry13.get()) + float(bt1_entry20.get()) + float(bt1_entry27.get())
                b3_tot = float(bt3_entry6.get()) + float(bt3_entry13.get()) + float(bt3_entry20.get()) + float(bt3_entry27.get())
                b4_tot = float(bt4_entry6.get()) + float(bt4_entry13.get()) + float(bt4_entry20.get()) + float(bt4_entry27.get())
                cmt_entry8.insert(0,b1_tot + float(cmt_entry16.get()) + b3_tot + b4_tot)

                if cmt_entry17.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry17.get() != "Choose":                                            
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100
                    ptax_total = tax_tot2
                
                cmt_entry9.insert(0,tax_total1 + tax_total3 + tax_total4 + ptax_total)

            #Fourth row Bundle -----------------------------------------------------
            elif cmt_entry1.get() not in b_list and cmt_entry11.get() not in b_list and cmt_entry18.get() not in b_list and cmt_entry25.get() in b_list:
                b4_tot = float(bt4_entry6.get()) + float(bt4_entry13.get()) + float(bt4_entry20.get()) + float(bt4_entry27.get())
                cmt_entry8.insert(0,float(cmt_entry6.get()) + float(cmt_entry16.get()) + float(cmt_entry23.get()) + b4_tot)

                if cmt_entry7.get() == "Choose" and cmt_entry17.get() == "Choose" and cmt_entry24.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() == "Choose" and cmt_entry24.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    ptax_total = tax_tot1
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() != "Choose" and cmt_entry24.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100
                    ptax_total = tax_tot1 + tax_tot2
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() != "Choose" and cmt_entry24.get() != "Choose":
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
                    ptax_total = tax_tot1 + tax_tot2 + tax_tot3
                cmt_entry9.insert(0,tax_total4 + ptax_total)

            #Fourth,First row Bundle -----------------------------------------------------
            elif cmt_entry1.get() in b_list and cmt_entry11.get() not in b_list and cmt_entry18.get() not in b_list and cmt_entry25.get() in b_list:
                b4_tot = float(bt4_entry6.get()) + float(bt4_entry13.get()) + float(bt4_entry20.get()) + float(bt4_entry27.get())
                b1_tot = float(bt1_entry6.get()) + float(bt1_entry13.get()) + float(bt1_entry20.get()) + float(bt1_entry27.get())
                cmt_entry8.insert(0,b1_tot + float(cmt_entry16.get()) + float(cmt_entry23.get()) + b4_tot)

                if cmt_entry17.get() == "Choose" and cmt_entry24.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry17.get() != "Choose" and cmt_entry24.get() == "Choose":                                            
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100
                    ptax_total = tax_tot2
                elif cmt_entry17.get() != "Choose" and cmt_entry24.get() != "Choose":                                            
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100

                    if gst_value3 == "0" or cmt_entry24.get() == "Exempt GST(0%)" or cmt_entry24.get() == "Out of Scope(0%)":
                        tax_tot3 = 0
                    else:
                        tax_tot3 = (float(cmt_entry23.get()) * float(float((gst_value3[0]))))/100
                    ptax_total = tax_tot2 + tax_tot3
                cmt_entry9.insert(0,tax_total1 + tax_total4 + ptax_total)

            #Fourth,First and Second row Bundle -----------------------------------------------------
            elif cmt_entry1.get() in b_list and cmt_entry11.get() in b_list and cmt_entry18.get() not in b_list and cmt_entry25.get() in b_list:
                b4_tot = float(bt4_entry6.get()) + float(bt4_entry13.get()) + float(bt4_entry20.get()) + float(bt4_entry27.get())
                b1_tot = float(bt1_entry6.get()) + float(bt1_entry13.get()) + float(bt1_entry20.get()) + float(bt1_entry27.get())
                b2_tot = float(bt2_entry6.get()) + float(bt2_entry13.get()) + float(bt2_entry20.get()) + float(bt2_entry27.get())
                cmt_entry8.insert(0,b1_tot + b2_tot + float(cmt_entry23.get()) + b4_tot)

                if cmt_entry24.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry24.get() != "Choose":
                    if gst_value3 == "0" or cmt_entry24.get() == "Exempt GST(0%)" or cmt_entry24.get() == "Out of Scope(0%)":
                        tax_tot3 = 0
                    else:
                        tax_tot3 = (float(cmt_entry23.get()) * float(float((gst_value3[0]))))/100
                    ptax_total = tax_tot3
                cmt_entry9.insert(0,tax_total1 + tax_total2 + tax_total4 + ptax_total)
            cmt_entry10.insert(0,float(cmt_entry8.get()) + float(float(cmt_entry9.get())))
        else:
            pass
    except:
        pass

#spinbox 4 --------------------------------------------

def cmt_calculateTotal4(event):
    try:
        if cmt_entry14.get() != 0:
            global tax_tot1,tax_tot2,tax_tot3,tax_tot4,b1tax_tot1,b1tax_tot2,b1tax_tot3,b1tax_tot4,b2tax_tot1,b2tax_tot2,b2tax_tot3,b2tax_tot4,b3tax_tot1,b3tax_tot2,b3tax_tot3,b3tax_tot4,b4tax_tot1,b4tax_tot2,b4tax_tot3,b4tax_tot4
            tax_tot1 = 0.0
            tax_tot2 = 0.0
            tax_tot3 = 0.0
            tax_tot4 = 0.0

            b1tax_tot1 = 0.0
            b1tax_tot2 = 0.0
            b1tax_tot3 = 0.0
            b1tax_tot4 = 0.0

            b2tax_tot1 = 0.0
            b2tax_tot2 = 0.0
            b2tax_tot3 = 0.0
            b2tax_tot4 = 0.0

            b3tax_tot1 = 0.0
            b3tax_tot2 = 0.0
            b3tax_tot3 = 0.0
            b3tax_tot4 = 0.0

            b4tax_tot1 = 0.0
            b4tax_tot2 = 0.0
            b4tax_tot3 = 0.0
            b4tax_tot4 = 0.0
            try:
                get_pro_sql = "SELECT * FROM app1_inventory WHERE name=%s AND cid_id=%s"
                get_pro_val = (cmt_entry25.get(),comp_data[0])
                fbcursor.execute(get_pro_sql,get_pro_val)
                get_pro_data = fbcursor.fetchone()

                get_pro_sql1 = "SELECT * FROM app1_noninventory WHERE name=%s AND cid_id=%s"
                get_pro_val1 = (cmt_entry25.get(),comp_data[0])
                fbcursor.execute(get_pro_sql1,get_pro_val1)
                get_pro_data1 = fbcursor.fetchone()

                get_pro_sql2 = "SELECT * FROM app1_service WHERE name=%s AND cid_id=%s"
                get_pro_val2 = (cmt_entry25.get(),comp_data[0])
                fbcursor.execute(get_pro_sql2,get_pro_val2)
                get_pro_data2 = fbcursor.fetchone()

                get_pro_sql3 = "SELECT * FROM app1_bundle WHERE name=%s AND cid_id=%s"
                get_pro_val3 = (cmt_entry25.get(),comp_data[0])
                fbcursor.execute(get_pro_sql3,get_pro_val3)
                get_pro_data3 = fbcursor.fetchone()
            except:
                pass

            if get_pro_data is not None:
                tot = int(get_pro_data[12]) * int(cmt_entry28.get())
                cmt_entry30.delete(0,END)
                cmt_entry30.insert(0,tot)
            elif get_pro_data1 is not None:
                tot = int(get_pro_data1[8]) * int(cmt_entry28.get())
                cmt_entry30.delete(0,END)
                cmt_entry30.insert(0,tot)
            elif get_pro_data2 is not None:
                pass
            else:
                view_bundleitems(b=4)

            cmt_entry8.delete(0,END)
            cmt_entry9.delete(0,END)
            cmt_entry10.delete(0,END)

            def split_gst(string):
                pattern1 = r'\(+'
                pattern2 = r'\%+'
                split1 = re.split(pattern1,string)
                split2 = re.split(pattern2,split1[1])
                return split2

            #product gst -----------------------------
            try:
                gst_value1 = split_gst(cmt_entry7.get())
            except:
                pass
            try:
                gst_value2 = split_gst(cmt_entry17.get())
            except:
                pass
            try:
                gst_value3 = split_gst(cmt_entry24.get())
            except:
                pass
            try:
                gst_value4 = split_gst(cmt_entry31.get())
            except:
                pass

            #bundle gst ------------------------------ 
            try:
                bgst_value1 = split_gst(bt1_entry7.get())
                bgst_value2 = split_gst(bt1_entry14.get())
                bgst_value3 = split_gst(bt1_entry21.get())
                bgst_value4 = split_gst(bt1_entry28.get())
            except:
                pass
            try:
                bgst_value5 = split_gst(bt2_entry7.get())
                bgst_value6 = split_gst(bt2_entry14.get())
                bgst_value7 = split_gst(bt2_entry21.get())
                bgst_value8 = split_gst(bt2_entry28.get())
            except:
                pass
            try:
                bgst_value9 = split_gst(bt3_entry7.get())
                bgst_value10 = split_gst(bt3_entry14.get())
                bgst_value11 = split_gst(bt3_entry21.get())
                bgst_value12 = split_gst(bt3_entry28.get())
            except:
                pass
            try:
                bgst_value13 = split_gst(bt4_entry7.get())
                bgst_value14 = split_gst(bt4_entry14.get())
                bgst_value15 = split_gst(bt4_entry21.get())
                bgst_value16 = split_gst(bt4_entry28.get())
            except:
                pass

            get_bun_sql = "SELECT name FROM app1_bundle WHERE cid_id=%s"
            get_bun_val = (comp_data[0],)
            fbcursor.execute(get_bun_sql,get_bun_val)
            get_bun_data = fbcursor.fetchall()
            
            b_list = []
            for g in get_bun_data:
                b_list.append(g[0])

#=====================================================================================
            #Bundle1--------------------------------------------
            try:
                if bt1_entry7.get() == "Choose" and bt1_entry14.get() == "Choose" and bt1_entry21.get() == "Choose" and bt1_entry28.get() == "Choose":
                    pass
                elif bt1_entry7.get() != "Choose" and bt1_entry14.get() == "Choose" and bt1_entry21.get() == "Choose" and bt1_entry28.get() == "Choose":
                    if bgst_value1 == "0" or bt1_entry7.get() == "Exempt GST(0%)" or bt1_entry7.get() == "Out of Scope(0%)":
                        b1tax_tot1 = 0
                    else:
                        b1tax_tot1 = (float(bt1_entry6.get()) * float(float((bgst_value1[0]))))/100
                    tax_total1 = b1tax_tot1
                elif bt1_entry7.get() != "Choose" and bt1_entry14.get() != "Choose" and bt1_entry21.get() == "Choose" and bt1_entry28.get() == "Choose":
                    if bgst_value1 == "0" or bt1_entry7.get() == "Exempt GST(0%)" or bt1_entry7.get() == "Out of Scope(0%)":
                        b1tax_tot1 = 0
                    else:
                        b1tax_tot1 = (float(bt1_entry6.get()) * float(float((bgst_value1[0]))))/100
                    
                    if bgst_value2 == "0" or bt1_entry14.get() == "Exempt GST(0%)" or bt1_entry14.get() == "Out of Scope(0%)":
                        b1tax_tot2 = 0
                    else:
                        b1tax_tot2 = (float(bt1_entry13.get()) * float(float((bgst_value2[0]))))/100
                    tax_total1 = b1tax_tot1 + b1tax_tot2
                elif bt1_entry7.get() != "Choose" and bt1_entry14.get() != "Choose" and bt1_entry21.get() != "Choose" and bt1_entry28.get() == "Choose":
                    if bgst_value1 == "0" or bt1_entry7.get() == "Exempt GST(0%)" or bt1_entry7.get() == "Out of Scope(0%)":
                        b1tax_tot1 = 0
                    else:
                        b1tax_tot1 = (float(bt1_entry6.get()) * float(float((bgst_value1[0]))))/100
                    
                    if bgst_value2 == "0" or bt1_entry14.get() == "Exempt GST(0%)" or bt1_entry14.get() == "Out of Scope(0%)":
                        b1tax_tot2 = 0
                    else:
                        b1tax_tot2 = (float(bt1_entry13.get()) * float(float((bgst_value2[0]))))/100

                    if bgst_value3 == "0" or bt1_entry21.get() == "Exempt GST(0%)" or bt1_entry21.get() == "Out of Scope(0%)":
                        b1tax_tot3 = 0
                    else:
                        b1tax_tot3 = (float(bt1_entry20.get()) * float(float((bgst_value3[0]))))/100
                    tax_total1 = b1tax_tot1 + b1tax_tot2 + b1tax_tot3
                elif bt1_entry7.get() != "Choose" and bt1_entry14.get() != "Choose" and bt1_entry21.get() != "Choose" and bt1_entry28.get() != "Choose":
                    if bgst_value1 == "0" or bt1_entry7.get() == "Exempt GST(0%)" or bt1_entry7.get() == "Out of Scope(0%)":
                        b1tax_tot1 = 0
                    else:
                        b1tax_tot1 = (float(bt1_entry6.get()) * float(float((bgst_value1[0]))))/100
                    
                    if bgst_value2 == "0" or bt1_entry14.get() == "Exempt GST(0%)" or bt1_entry14.get() == "Out of Scope(0%)":
                        b1tax_tot2 = 0
                    else:
                        b1tax_tot2 = (float(bt1_entry13.get()) * float(float((bgst_value2[0]))))/100

                    if bgst_value3 == "0" or bt1_entry21.get() == "Exempt GST(0%)" or bt1_entry21.get() == "Out of Scope(0%)":
                        b1tax_tot3 = 0
                    else:
                        b1tax_tot3 = (float(bt1_entry20.get()) * float(float((bgst_value3[0]))))/100

                    if bgst_value4 == "0" or bt1_entry28.get() == "Exempt GST(0%)" or bt1_entry28.get() == "Out of Scope(0%)":
                        b1tax_tot4 = 0
                    else:
                        b1tax_tot4 = (float(bt1_entry27.get()) * float(float((bgst_value4[0]))))/100
                    tax_total1 = b1tax_tot1 + b1tax_tot2 + b1tax_tot3 + b1tax_tot4
            except:
                pass

            #Bundle2--------------------------------------------
            try:
                if bt2_entry7.get() == "Choose" and bt2_entry14.get() == "Choose" and bt2_entry21.get() == "Choose" and bt2_entry28.get() == "Choose":
                    pass
                elif bt2_entry7.get() != "Choose" and bt2_entry14.get() == "Choose" and bt2_entry21.get() == "Choose" and bt2_entry28.get() == "Choose":
                    if bgst_value5 == "0" or bt2_entry7.get() == "Exempt GST(0%)" or bt2_entry7.get() == "Out of Scope(0%)":
                        b2tax_tot1 = 0
                    else:
                        b2tax_tot1 = (float(bt2_entry6.get()) * float(float((bgst_value5[0]))))/100
                    tax_total2 = b2tax_tot1
                elif bt2_entry7.get() != "Choose" and bt2_entry14.get() != "Choose" and bt2_entry21.get() == "Choose" and bt2_entry28.get() == "Choose":
                    if bgst_value5 == "0" or bt2_entry7.get() == "Exempt GST(0%)" or bt2_entry7.get() == "Out of Scope(0%)":
                        b2tax_tot1 = 0
                    else:
                        b2tax_tot1 = (float(bt2_entry6.get()) * float(float((bgst_value5[0]))))/100
                    
                    if bgst_value6 == "0" or bt2_entry14.get() == "Exempt GST(0%)" or bt2_entry14.get() == "Out of Scope(0%)":
                        b2tax_tot2 = 0
                    else:
                        b2tax_tot2 = (float(bt2_entry13.get()) * float(float((bgst_value6[0]))))/100
                    tax_total2 = b2tax_tot1 + b2tax_tot2
                elif bt2_entry7.get() != "Choose" and bt2_entry14.get() != "Choose" and bt2_entry21.get() != "Choose" and bt2_entry28.get() == "Choose":
                    if bgst_value5 == "0" or bt2_entry7.get() == "Exempt GST(0%)" or bt2_entry7.get() == "Out of Scope(0%)":
                        b2tax_tot1 = 0
                    else:
                        b2tax_tot1 = (float(bt2_entry6.get()) * float(float((bgst_value5[0]))))/100
                    
                    if bgst_value6 == "0" or bt2_entry14.get() == "Exempt GST(0%)" or bt2_entry14.get() == "Out of Scope(0%)":
                        b2tax_tot2 = 0
                    else:
                        b2tax_tot2 = (float(bt2_entry13.get()) * float(float((bgst_value6[0]))))/100

                    if bgst_value7 == "0" or bt2_entry21.get() == "Exempt GST(0%)" or bt2_entry21.get() == "Out of Scope(0%)":
                        b2tax_tot3 = 0
                    else:
                        b2tax_tot3 = (float(bt2_entry20.get()) * float(float((bgst_value7[0]))))/100
                    tax_total2 = b2tax_tot1 + b2tax_tot2 + b2tax_tot3
                elif bt2_entry7.get() != "Choose" and bt2_entry14.get() != "Choose" and bt2_entry21.get() != "Choose" and bt2_entry28.get() != "Choose":
                    if bgst_value5 == "0" or bt2_entry7.get() == "Exempt GST(0%)" or bt2_entry7.get() == "Out of Scope(0%)":
                        b2tax_tot1 = 0
                    else:
                        b2tax_tot1 = (float(bt2_entry6.get()) * float(float((bgst_value5[0]))))/100
                    
                    if bgst_value6 == "0" or bt2_entry14.get() == "Exempt GST(0%)" or bt2_entry14.get() == "Out of Scope(0%)":
                        b2tax_tot2 = 0
                    else:
                        b2tax_tot2 = (float(bt2_entry13.get()) * float(float((bgst_value6[0]))))/100

                    if bgst_value7 == "0" or bt2_entry21.get() == "Exempt GST(0%)" or bt2_entry21.get() == "Out of Scope(0%)":
                        b2tax_tot3 = 0
                    else:
                        b2tax_tot3 = (float(bt2_entry20.get()) * float(float((bgst_value7[0]))))/100

                    if bgst_value8 == "0" or bt2_entry28.get() == "Exempt GST(0%)" or bt2_entry28.get() == "Out of Scope(0%)":
                        b2tax_tot4 = 0
                    else:
                        b2tax_tot4 = (float(bt2_entry27.get()) * float(float((bgst_value8[0]))))/100
                    tax_total2 = b2tax_tot1 + b2tax_tot2 + b2tax_tot3 + b2tax_tot4
            except:
                pass

            #Bundle3--------------------------------------------
            try:
                if bt3_entry7.get() == "Choose" and bt3_entry14.get() == "Choose" and bt3_entry21.get() == "Choose" and bt3_entry28.get() == "Choose":
                    pass
                elif bt3_entry7.get() != "Choose" and bt3_entry14.get() == "Choose" and bt3_entry21.get() == "Choose" and bt3_entry28.get() == "Choose":
                    if bgst_value9 == "0" or bt3_entry7.get() == "Exempt GST(0%)" or bt3_entry7.get() == "Out of Scope(0%)":
                        b3tax_tot1 = 0
                    else:
                        b3tax_tot1 = (float(bt3_entry6.get()) * float(float((bgst_value9[0]))))/100
                    tax_total3 = b3tax_tot1
                elif bt3_entry7.get() != "Choose" and bt3_entry14.get() != "Choose" and bt3_entry21.get() == "Choose" and bt3_entry28.get() == "Choose":
                    if bgst_value9 == "0" or bt3_entry7.get() == "Exempt GST(0%)" or bt3_entry7.get() == "Out of Scope(0%)":
                        b3tax_tot1 = 0
                    else:
                        b3tax_tot1 = (float(bt3_entry6.get()) * float(float((bgst_value9[0]))))/100
                    
                    if bgst_value10 == "0" or bt3_entry14.get() == "Exempt GST(0%)" or bt3_entry14.get() == "Out of Scope(0%)":
                        b3tax_tot2 = 0
                    else:
                        b3tax_tot2 = (float(bt3_entry13.get()) * float(float((bgst_value10[0]))))/100
                    tax_total3 = b3tax_tot1 + b3tax_tot2
                elif bt3_entry7.get() != "Choose" and bt3_entry14.get() != "Choose" and bt3_entry21.get() != "Choose" and bt3_entry28.get() == "Choose":
                    if bgst_value9 == "0" or bt3_entry7.get() == "Exempt GST(0%)" or bt3_entry7.get() == "Out of Scope(0%)":
                        b3tax_tot1 = 0
                    else:
                        b3tax_tot1 = (float(bt3_entry6.get()) * float(float((bgst_value9[0]))))/100
                    
                    if bgst_value10 == "0" or bt3_entry14.get() == "Exempt GST(0%)" or bt3_entry14.get() == "Out of Scope(0%)":
                        b3tax_tot2 = 0
                    else:
                        b3tax_tot2 = (float(bt3_entry13.get()) * float(float((bgst_value10[0]))))/100

                    if bgst_value11 == "0" or bt3_entry21.get() == "Exempt GST(0%)" or bt3_entry21.get() == "Out of Scope(0%)":
                        b3tax_tot3 = 0
                    else:
                        b3tax_tot3 = (float(bt3_entry20.get()) * float(float((bgst_value11[0]))))/100
                    tax_total3 = b3tax_tot1 + b3tax_tot2 + b3tax_tot3
                elif bt3_entry7.get() != "Choose" and bt3_entry14.get() != "Choose" and bt3_entry21.get() != "Choose" and bt3_entry28.get() != "Choose":
                    if bgst_value9 == "0" or bt3_entry7.get() == "Exempt GST(0%)" or bt3_entry7.get() == "Out of Scope(0%)":
                        b3tax_tot1 = 0
                    else:
                        b3tax_tot1 = (float(bt3_entry6.get()) * float(float((bgst_value9[0]))))/100
                    
                    if bgst_value10 == "0" or bt3_entry14.get() == "Exempt GST(0%)" or bt3_entry14.get() == "Out of Scope(0%)":
                        b3tax_tot2 = 0
                    else:
                        b3tax_tot2 = (float(bt3_entry13.get()) * float(float((bgst_value10[0]))))/100

                    if bgst_value11 == "0" or bt3_entry21.get() == "Exempt GST(0%)" or bt3_entry21.get() == "Out of Scope(0%)":
                        b3tax_tot3 = 0
                    else:
                        b3tax_tot3 = (float(bt3_entry20.get()) * float(float((bgst_value11[0]))))/100

                    if bgst_value12 == "0" or bt3_entry28.get() == "Exempt GST(0%)" or bt3_entry28.get() == "Out of Scope(0%)":
                        b3tax_tot4 = 0
                    else:
                        b3tax_tot4 = (float(bt3_entry27.get()) * float(float((bgst_value12[0]))))/100
                    tax_total3 = b3tax_tot1 + b3tax_tot2 + b3tax_tot3 + b3tax_tot4
            except:
                pass

            #Bundle4--------------------------------------------
            try:
                if bt4_entry7.get() == "Choose" and bt4_entry14.get() == "Choose" and bt4_entry21.get() == "Choose" and bt4_entry28.get() == "Choose":
                    pass
                elif bt4_entry7.get() != "Choose" and bt4_entry14.get() == "Choose" and bt4_entry21.get() == "Choose" and bt4_entry28.get() == "Choose":
                    if bgst_value13 == "0" or bt4_entry7.get() == "Exempt GST(0%)" or bt4_entry7.get() == "Out of Scope(0%)":
                        b4tax_tot1 = 0
                    else:
                        b4tax_tot1 = (float(bt4_entry6.get()) * float(float((bgst_value13[0]))))/100
                    tax_total4 = b4tax_tot1
                elif bt4_entry7.get() != "Choose" and bt4_entry14.get() != "Choose" and bt4_entry21.get() == "Choose" and bt4_entry28.get() == "Choose":
                    if bgst_value13 == "0" or bt4_entry7.get() == "Exempt GST(0%)" or bt4_entry7.get() == "Out of Scope(0%)":
                        b4tax_tot1 = 0
                    else:
                        b4tax_tot1 = (float(bt4_entry6.get()) * float(float((bgst_value13[0]))))/100
                    
                    if bgst_value14 == "0" or bt4_entry14.get() == "Exempt GST(0%)" or bt4_entry14.get() == "Out of Scope(0%)":
                        b4tax_tot2 = 0
                    else:
                        b4tax_tot2 = (float(bt4_entry13.get()) * float(float((bgst_value14[0]))))/100
                    tax_total4 = b4tax_tot1 + b4tax_tot2
                elif bt4_entry7.get() != "Choose" and bt4_entry14.get() != "Choose" and bt4_entry21.get() != "Choose" and bt4_entry28.get() == "Choose":
                    if bgst_value13 == "0" or bt4_entry7.get() == "Exempt GST(0%)" or bt4_entry7.get() == "Out of Scope(0%)":
                        b4tax_tot1 = 0
                    else:
                        b4tax_tot1 = (float(bt4_entry6.get()) * float(float((bgst_value13[0]))))/100
                    
                    if bgst_value14 == "0" or bt4_entry14.get() == "Exempt GST(0%)" or bt4_entry14.get() == "Out of Scope(0%)":
                        b4tax_tot2 = 0
                    else:
                        b4tax_tot2 = (float(bt4_entry13.get()) * float(float((bgst_value14[0]))))/100

                    if bgst_value15 == "0" or bt4_entry21.get() == "Exempt GST(0%)" or bt4_entry21.get() == "Out of Scope(0%)":
                        b4tax_tot3 = 0
                    else:
                        b4tax_tot3 = (float(bt4_entry20.get()) * float(float((bgst_value15[0]))))/100
                    tax_total4 = b4tax_tot1 + b4tax_tot2 + b4tax_tot3
                elif bt4_entry7.get() != "Choose" and bt4_entry14.get() != "Choose" and bt4_entry21.get() != "Choose" and bt4_entry28.get() != "Choose":
                    if bgst_value13 == "0" or bt4_entry7.get() == "Exempt GST(0%)" or bt4_entry7.get() == "Out of Scope(0%)":
                        b4tax_tot1 = 0
                    else:
                        b4tax_tot1 = (float(bt4_entry6.get()) * float(float((bgst_value13[0]))))/100
                    
                    if bgst_value14 == "0" or bt4_entry14.get() == "Exempt GST(0%)" or bt4_entry14.get() == "Out of Scope(0%)":
                        b4tax_tot2 = 0
                    else:
                        b4tax_tot2 = (float(bt4_entry13.get()) * float(float((bgst_value14[0]))))/100

                    if bgst_value15 == "0" or bt4_entry21.get() == "Exempt GST(0%)" or bt4_entry21.get() == "Out of Scope(0%)":
                        b4tax_tot3 = 0
                    else:
                        b4tax_tot3 = (float(bt4_entry20.get()) * float(float((bgst_value15[0]))))/100

                    if bgst_value16 == "0" or bt4_entry28.get() == "Exempt GST(0%)" or bt4_entry28.get() == "Out of Scope(0%)":
                        b4tax_tot4 = 0
                    else:
                        b4tax_tot4 = (float(bt4_entry27.get()) * float(float((bgst_value16[0]))))/100
                    tax_total4 = b4tax_tot1 + b4tax_tot2 + b4tax_tot3 + b4tax_tot4
            except:
                pass

#=============================================================================================

            #All products ----------------------------------------------------------------------------------------
            if cmt_entry1.get() not in b_list and cmt_entry11.get() not in b_list and cmt_entry18.get() not in b_list and cmt_entry25.get() not in b_list:
                cmt_entry8.insert(0,float(cmt_entry6.get()) + float(cmt_entry16.get()) + float(cmt_entry23.get()) + float(cmt_entry30.get()))
                if cmt_entry7.get() == "Choose" and cmt_entry17.get() == "Choose" and cmt_entry24.get() == "Choose" and cmt_entry31.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() == "Choose" and cmt_entry24.get() == "Choose" and cmt_entry31.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    ptax_total = tax_tot1
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() != "Choose" and cmt_entry24.get() == "Choose" and cmt_entry31.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100
                    ptax_total = tax_tot1 + tax_tot2
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() != "Choose" and cmt_entry24.get() != "Choose" and cmt_entry31.get() == "Choose":
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
                    ptax_total = tax_tot1 + tax_tot2 + tax_tot3
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() != "Choose" and cmt_entry24.get() != "Choose" and cmt_entry31.get() != "Choose":
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
                    ptax_total = tax_tot1 + tax_tot2 + tax_tot3 + tax_tot4

                cmt_entry9.insert(0,ptax_total)

            #All bundles -----------------------------------------------------------------------------------
            elif cmt_entry1.get() in b_list and cmt_entry11.get() in b_list and cmt_entry18.get() in b_list and cmt_entry25.get() in b_list:
                b1_tot = float(bt1_entry6.get()) + float(bt1_entry13.get()) + float(bt1_entry20.get()) + float(bt1_entry27.get())
                b2_tot = float(bt2_entry6.get()) + float(bt2_entry13.get()) + float(bt2_entry20.get()) + float(bt2_entry27.get())
                b3_tot = float(bt3_entry6.get()) + float(bt3_entry13.get()) + float(bt3_entry20.get()) + float(bt3_entry27.get())
                b4_tot = float(bt4_entry6.get()) + float(bt4_entry13.get()) + float(bt4_entry20.get()) + float(bt4_entry27.get())
                cmt_entry8.insert(0,b1_tot + b2_tot + b3_tot + b4_tot)

                cmt_entry9.insert(0,tax_total1 + tax_total2 + tax_total3 + tax_total4)

            #First row bundle-----------------------------------------
            elif cmt_entry1.get() in b_list and cmt_entry11.get() not in b_list and cmt_entry18.get() not in b_list and cmt_entry25.get() not in b_list:
                b1_tot = float(bt1_entry6.get()) + float(bt1_entry13.get()) + float(bt1_entry20.get()) + float(bt1_entry27.get())
                cmt_entry8.insert(0,b1_tot + float(cmt_entry16.get()) + float(cmt_entry23.get()) + float(cmt_entry30.get()))

                #Rest products--------------------------------------
                if cmt_entry17.get() == "Choose" and cmt_entry24.get() == "Choose" and cmt_entry31.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry17.get() != "Choose" and cmt_entry24.get() == "Choose" and cmt_entry31.get() == "Choose":                                               
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100
                    ptax_total = tax_tot2
                elif cmt_entry17.get() != "Choose" and cmt_entry24.get() != "Choose" and cmt_entry31.get() == "Choose":                                              
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100

                    if gst_value3 == "0" or cmt_entry24.get() == "Exempt GST(0%)" or cmt_entry24.get() == "Out of Scope(0%)":
                        tax_tot3 = 0
                    else:
                        tax_tot3 = (float(cmt_entry23.get()) * float(float((gst_value3[0]))))/100
                    ptax_total = tax_tot2 + tax_tot3
                elif cmt_entry17.get() != "Choose" and cmt_entry24.get() != "Choose" and cmt_entry31.get() != "Choose":
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
                    ptax_total = tax_tot2 + tax_tot3 + tax_tot4
                cmt_entry9.insert(0,tax_total1 + ptax_total)

            #First and Second row Bundle -------------------------------------
            elif cmt_entry1.get() in b_list and cmt_entry11.get() in b_list and cmt_entry18.get() not in b_list and cmt_entry25.get() not in b_list:
                b1_tot = float(bt1_entry6.get()) + float(bt1_entry13.get()) + float(bt1_entry20.get()) + float(bt1_entry27.get())
                b2_tot = float(bt2_entry6.get()) + float(bt2_entry13.get()) + float(bt2_entry20.get()) + float(bt2_entry27.get())
                cmt_entry8.insert(0,b1_tot + b2_tot + float(cmt_entry23.get()) + float(cmt_entry30.get()))

                #Rest products--------------------------------------
                if cmt_entry24.get() == "Choose" and cmt_entry31.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry24.get() != "Choose" and cmt_entry31.get() == "Choose":
                    if gst_value3 == "0" or cmt_entry24.get() == "Exempt GST(0%)" or cmt_entry24.get() == "Out of Scope(0%)":
                        tax_tot3 = 0
                    else:
                        tax_tot3 = (float(cmt_entry23.get()) * float(float((gst_value3[0]))))/100
                    ptax_total = tax_tot3
                elif cmt_entry24.get() != "Choose" and cmt_entry31.get() != "Choose":
                    if gst_value3 == "0" or cmt_entry24.get() == "Exempt GST(0%)" or cmt_entry24.get() == "Out of Scope(0%)":
                        tax_tot3 = 0
                    else:
                        tax_tot3 = (float(cmt_entry23.get()) * float(float((gst_value3[0]))))/100

                    if gst_value4 == "0" or cmt_entry31.get() == "Exempt GST(0%)" or cmt_entry31.get() == "Out of Scope(0%)":
                        tax_tot4 = 0
                    else:
                        tax_tot4 = (float(cmt_entry30.get()) * float(float((gst_value4[0]))))/100
                    ptax_total = tax_tot3 + tax_tot4

                cmt_entry9.insert(0,tax_total1 + tax_total2 + ptax_total)

            #First,Second and Third row Bundle -------------------------------------
            elif cmt_entry1.get() in b_list and cmt_entry11.get() in b_list and cmt_entry18.get() in b_list and cmt_entry25.get() not in b_list:
                b1_tot = float(bt1_entry6.get()) + float(bt1_entry13.get()) + float(bt1_entry20.get()) + float(bt1_entry27.get())
                b2_tot = float(bt2_entry6.get()) + float(bt2_entry13.get()) + float(bt2_entry20.get()) + float(bt2_entry27.get())
                b3_tot = float(bt3_entry6.get()) + float(bt3_entry13.get()) + float(bt3_entry20.get()) + float(bt3_entry27.get())
                cmt_entry8.insert(0,b1_tot + b2_tot + b3_tot + float(cmt_entry30.get()))

                #Rest products--------------------------------------
                if cmt_entry31.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry31.get() != "Choose":
                    if gst_value4 == "0" or cmt_entry31.get() == "Exempt GST(0%)" or cmt_entry31.get() == "Out of Scope(0%)":
                        tax_tot4 = 0
                    else:
                        tax_tot4 = (float(cmt_entry30.get()) * float(float((gst_value4[0]))))/100
                    ptax_total = tax_tot4
                cmt_entry9.insert(0,tax_total1 + tax_total2 + tax_total3 + ptax_total)
            
            #Second row Bundle------------------------------------
            elif cmt_entry1.get() not in b_list and cmt_entry11.get() in b_list and cmt_entry18.get() not in b_list and cmt_entry25.get() not in b_list:
                b2_tot = float(bt2_entry6.get()) + float(bt2_entry13.get()) + float(bt2_entry20.get()) + float(bt2_entry27.get())
                cmt_entry8.insert(0,float(cmt_entry6.get()) + b2_tot + float(cmt_entry23.get()) + float(cmt_entry30.get()))

                if cmt_entry7.get() == "Choose" and cmt_entry24.get() == "Choose" and cmt_entry31.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry7.get() != "Choose" and cmt_entry24.get() == "Choose" and cmt_entry31.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    ptax_total = tax_tot1
                elif cmt_entry7.get() != "Choose" and cmt_entry24.get() != "Choose" and cmt_entry31.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100

                    if gst_value3 == "0" or cmt_entry24.get() == "Exempt GST(0%)" or cmt_entry24.get() == "Out of Scope(0%)":
                        tax_tot3 = 0
                    else:
                        tax_tot3 = (float(cmt_entry23.get()) * float(float((gst_value3[0]))))/100
                    ptax_total = tax_tot1 + tax_tot3
                elif cmt_entry7.get() != "Choose" and cmt_entry24.get() != "Choose" and cmt_entry31.get() != "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100

                    if gst_value3 == "0" or cmt_entry24.get() == "Exempt GST(0%)" or cmt_entry24.get() == "Out of Scope(0%)":
                        tax_tot3 = 0
                    else:
                        tax_tot3 = (float(cmt_entry23.get()) * float(float((gst_value3[0]))))/100

                    if gst_value4 == "0" or cmt_entry31.get() == "Exempt GST(0%)" or cmt_entry31.get() == "Out of Scope(0%)":
                        tax_tot4 = 0
                    else:
                        tax_tot4 = (float(cmt_entry30.get()) * float(float((gst_value4[0]))))/100
                    ptax_total = tax_tot1 + tax_tot3 + tax_tot4
                cmt_entry9.insert(0,tax_total2 + ptax_total)

            #Second,Third row Bundle------------------------------------
            elif cmt_entry1.get() not in b_list and cmt_entry11.get() in b_list and cmt_entry18.get() in b_list and cmt_entry25.get() not in b_list:
                b2_tot = float(bt2_entry6.get()) + float(bt2_entry13.get()) + float(bt2_entry20.get()) + float(bt2_entry27.get())
                b3_tot = float(bt3_entry6.get()) + float(bt3_entry13.get()) + float(bt3_entry20.get()) + float(bt3_entry27.get())
                cmt_entry8.insert(0,float(cmt_entry6.get()) + b2_tot + b3_tot + float(cmt_entry30.get()))

                if cmt_entry7.get() == "Choose" and cmt_entry31.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry7.get() != "Choose" and cmt_entry31.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    ptax_total = tax_tot1
                elif cmt_entry7.get() != "Choose" and cmt_entry31.get() != "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100

                    if gst_value4 == "0" or cmt_entry31.get() == "Exempt GST(0%)" or cmt_entry31.get() == "Out of Scope(0%)":
                        tax_tot4 = 0
                    else:
                        tax_tot4 = (float(cmt_entry30.get()) * float(float((gst_value4[0]))))/100
                    ptax_total = tax_tot1 + tax_tot4
                cmt_entry9.insert(0,tax_total2 + tax_total3 + ptax_total)

            #Second,Fourth row Bundle------------------------------------
            elif cmt_entry1.get() not in b_list and cmt_entry11.get() in b_list and cmt_entry18.get() not in b_list and cmt_entry25.get() in b_list:
                b2_tot = float(bt2_entry6.get()) + float(bt2_entry13.get()) + float(bt2_entry20.get()) + float(bt2_entry27.get())
                b4_tot = float(bt4_entry6.get()) + float(bt4_entry13.get()) + float(bt4_entry20.get()) + float(bt4_entry27.get())
                cmt_entry8.insert(0,float(cmt_entry6.get()) + b2_tot + float(cmt_entry23.get()) + b4_tot)

                if cmt_entry7.get() == "Choose" and cmt_entry24.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry7.get() != "Choose" and cmt_entry24.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    ptax_total = tax_tot1
                elif cmt_entry7.get() != "Choose" and cmt_entry24.get() != "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100

                    if gst_value3 == "0" or cmt_entry24.get() == "Exempt GST(0%)" or cmt_entry24.get() == "Out of Scope(0%)":
                        tax_tot3 = 0
                    else:
                        tax_tot3 = (float(cmt_entry23.get()) * float(float((gst_value3[0]))))/100
                    ptax_total = tax_tot1 + tax_tot3
                cmt_entry9.insert(0,tax_total2 + tax_total4 + ptax_total)

            #Second,Third and Fourth row Bundle------------------------------------
            elif cmt_entry1.get() not in b_list and cmt_entry11.get() in b_list and cmt_entry18.get() in b_list and cmt_entry25.get() in b_list:
                b2_tot = float(bt2_entry6.get()) + float(bt2_entry13.get()) + float(bt2_entry20.get()) + float(bt2_entry27.get())
                b3_tot = float(bt3_entry6.get()) + float(bt3_entry13.get()) + float(bt3_entry20.get()) + float(bt3_entry27.get())
                b4_tot = float(bt4_entry6.get()) + float(bt4_entry13.get()) + float(bt4_entry20.get()) + float(bt4_entry27.get())
                cmt_entry8.insert(0,float(cmt_entry6.get()) + b2_tot + b3_tot + b4_tot)

                if cmt_entry7.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry7.get() != "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    ptax_total = tax_tot1
                cmt_entry9.insert(0,tax_total2 + tax_total3 + tax_total4 + ptax_total)
            
            #Third row Bundle---------------------------------------------
            elif cmt_entry1.get() not in b_list and cmt_entry11.get() not in b_list and cmt_entry18.get() in b_list and cmt_entry25.get() not in b_list:
                b3_tot = float(bt3_entry6.get()) + float(bt3_entry13.get()) + float(bt3_entry20.get()) + float(bt3_entry27.get())
                cmt_entry8.insert(0,float(cmt_entry6.get()) + float(cmt_entry16.get()) + b3_tot + float(cmt_entry30.get()))

                if cmt_entry7.get() == "Choose" and cmt_entry17.get() == "Choose" and cmt_entry31.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() == "Choose" and cmt_entry31.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    ptax_total = tax_tot1
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() != "Choose" and cmt_entry31.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100
                    ptax_total = tax_tot1 + tax_tot2
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() != "Choose" and cmt_entry31.get() != "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100

                    if gst_value4 == "0" or cmt_entry31.get() == "Exempt GST(0%)" or cmt_entry31.get() == "Out of Scope(0%)":
                        tax_tot4 = 0
                    else:
                        tax_tot4 = (float(cmt_entry30.get()) * float(float((gst_value4[0]))))/100
                    ptax_total = tax_tot1 + tax_tot2 + tax_tot4
                
                cmt_entry9.insert(0,tax_total3 + ptax_total)

            #Third,first row Bundle---------------------------------------------
            elif cmt_entry1.get() in b_list and cmt_entry11.get() not in b_list and cmt_entry18.get() in b_list and cmt_entry25.get() not in b_list:
                b1_tot = float(bt1_entry6.get()) + float(bt1_entry13.get()) + float(bt1_entry20.get()) + float(bt1_entry27.get())
                b3_tot = float(bt3_entry6.get()) + float(bt3_entry13.get()) + float(bt3_entry20.get()) + float(bt3_entry27.get())
                cmt_entry8.insert(0,b1_tot + float(cmt_entry16.get()) + b3_tot + float(cmt_entry30.get()))

                if cmt_entry17.get() == "Choose" and cmt_entry31.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry17.get() != "Choose" and cmt_entry31.get() == "Choose":                                            
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100
                    ptax_total = tax_tot2
                elif cmt_entry17.get() != "Choose" and cmt_entry31.get() != "Choose":                                            
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100

                    if gst_value4 == "0" or cmt_entry31.get() == "Exempt GST(0%)" or cmt_entry31.get() == "Out of Scope(0%)":
                        tax_tot4 = 0
                    else:
                        tax_tot4 = (float(cmt_entry30.get()) * float(float((gst_value4[0]))))/100
                    ptax_total = tax_tot2 + tax_tot4
                
                cmt_entry9.insert(0,tax_total1 + tax_total3 + ptax_total)

            #Third,fourth row Bundle---------------------------------------------
            elif cmt_entry1.get() not in b_list and cmt_entry11.get() not in b_list and cmt_entry18.get() in b_list and cmt_entry25.get() in b_list:
                b3_tot = float(bt3_entry6.get()) + float(bt3_entry13.get()) + float(bt3_entry20.get()) + float(bt3_entry27.get())
                b4_tot = float(bt4_entry6.get()) + float(bt4_entry13.get()) + float(bt4_entry20.get()) + float(bt4_entry27.get())
                cmt_entry8.insert(0,float(cmt_entry6.get()) + float(cmt_entry16.get()) + b3_tot + b4_tot)

                if cmt_entry7.get() == "Choose" and cmt_entry17.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    ptax_total = tax_tot1
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() != "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100
                    ptax_total = tax_tot1 + tax_tot2
                
                cmt_entry9.insert(0,tax_total3 + tax_total4 + ptax_total)

            #Third,first and fourth row Bundle---------------------------------------------
            elif cmt_entry1.get() in b_list and cmt_entry11.get() not in b_list and cmt_entry18.get() in b_list and cmt_entry25.get() in b_list:
                b1_tot = float(bt1_entry6.get()) + float(bt1_entry13.get()) + float(bt1_entry20.get()) + float(bt1_entry27.get())
                b3_tot = float(bt3_entry6.get()) + float(bt3_entry13.get()) + float(bt3_entry20.get()) + float(bt3_entry27.get())
                b4_tot = float(bt4_entry6.get()) + float(bt4_entry13.get()) + float(bt4_entry20.get()) + float(bt4_entry27.get())
                cmt_entry8.insert(0,b1_tot + float(cmt_entry16.get()) + b3_tot + b4_tot)

                if cmt_entry17.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry17.get() != "Choose":                                            
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100
                    ptax_total = tax_tot2
                
                cmt_entry9.insert(0,tax_total1 + tax_total3 + tax_total4 + ptax_total)

            #Fourth row Bundle -----------------------------------------------------
            elif cmt_entry1.get() not in b_list and cmt_entry11.get() not in b_list and cmt_entry18.get() not in b_list and cmt_entry25.get() in b_list:
                b4_tot = float(bt4_entry6.get()) + float(bt4_entry13.get()) + float(bt4_entry20.get()) + float(bt4_entry27.get())
                cmt_entry8.insert(0,float(cmt_entry6.get()) + float(cmt_entry16.get()) + float(cmt_entry23.get()) + b4_tot)

                if cmt_entry7.get() == "Choose" and cmt_entry17.get() == "Choose" and cmt_entry24.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() == "Choose" and cmt_entry24.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    ptax_total = tax_tot1
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() != "Choose" and cmt_entry24.get() == "Choose":
                    if gst_value1 == "0" or cmt_entry7.get() == "Exempt GST(0%)" or cmt_entry7.get() == "Out of Scope(0%)":
                        tax_tot1 = 0
                    else:
                        tax_tot1 = (float(cmt_entry6.get()) * float(float((gst_value1[0]))))/100
                    
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100
                    ptax_total = tax_tot1 + tax_tot2
                elif cmt_entry7.get() != "Choose" and cmt_entry17.get() != "Choose" and cmt_entry24.get() != "Choose":
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
                    ptax_total = tax_tot1 + tax_tot2 + tax_tot3
                cmt_entry9.insert(0,tax_total4 + ptax_total)

            #Fourth,First row Bundle -----------------------------------------------------
            elif cmt_entry1.get() in b_list and cmt_entry11.get() not in b_list and cmt_entry18.get() not in b_list and cmt_entry25.get() in b_list:
                b4_tot = float(bt4_entry6.get()) + float(bt4_entry13.get()) + float(bt4_entry20.get()) + float(bt4_entry27.get())
                b1_tot = float(bt1_entry6.get()) + float(bt1_entry13.get()) + float(bt1_entry20.get()) + float(bt1_entry27.get())
                cmt_entry8.insert(0,b1_tot + float(cmt_entry16.get()) + float(cmt_entry23.get()) + b4_tot)

                if cmt_entry17.get() == "Choose" and cmt_entry24.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry17.get() != "Choose" and cmt_entry24.get() == "Choose":                                            
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100
                    ptax_total = tax_tot2
                elif cmt_entry17.get() != "Choose" and cmt_entry24.get() != "Choose":                                            
                    if gst_value2 == "0" or cmt_entry17.get() == "Exempt GST(0%)" or cmt_entry17.get() == "Out of Scope(0%)":
                        tax_tot2 = 0
                    else:
                        tax_tot2 = (float(cmt_entry16.get()) * float(float((gst_value2[0]))))/100

                    if gst_value3 == "0" or cmt_entry24.get() == "Exempt GST(0%)" or cmt_entry24.get() == "Out of Scope(0%)":
                        tax_tot3 = 0
                    else:
                        tax_tot3 = (float(cmt_entry23.get()) * float(float((gst_value3[0]))))/100
                    ptax_total = tax_tot2 + tax_tot3
                cmt_entry9.insert(0,tax_total1 + tax_total4 + ptax_total)

            #Fourth,First and Second row Bundle -----------------------------------------------------
            elif cmt_entry1.get() in b_list and cmt_entry11.get() in b_list and cmt_entry18.get() not in b_list and cmt_entry25.get() in b_list:
                b4_tot = float(bt4_entry6.get()) + float(bt4_entry13.get()) + float(bt4_entry20.get()) + float(bt4_entry27.get())
                b1_tot = float(bt1_entry6.get()) + float(bt1_entry13.get()) + float(bt1_entry20.get()) + float(bt1_entry27.get())
                b2_tot = float(bt2_entry6.get()) + float(bt2_entry13.get()) + float(bt2_entry20.get()) + float(bt2_entry27.get())
                cmt_entry8.insert(0,b1_tot + b2_tot + float(cmt_entry23.get()) + b4_tot)

                if cmt_entry24.get() == "Choose":
                    ptax_total = 0
                elif cmt_entry24.get() != "Choose":
                    if gst_value3 == "0" or cmt_entry24.get() == "Exempt GST(0%)" or cmt_entry24.get() == "Out of Scope(0%)":
                        tax_tot3 = 0
                    else:
                        tax_tot3 = (float(cmt_entry23.get()) * float(float((gst_value3[0]))))/100
                    ptax_total = tax_tot3
                cmt_entry9.insert(0,tax_total1 + tax_total2 + tax_total4 + ptax_total)
            cmt_entry10.insert(0,float(cmt_entry8.get()) + float(float(cmt_entry9.get())))
        else:
            pass
    except:
        pass

