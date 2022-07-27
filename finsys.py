
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
from tkinter.font import BOLD
from urllib.parse import parse_qs
from PIL import ImageTk, Image, ImageFile
from django.test import tag
from matplotlib.font_manager import json_dump
from numpy import choose, empty, place
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



# fbilldb = mysql.connector.connect(
#     host="localhost", user="root", password="", database="fbilling", port="3306"
# )
# fbcursor = fbilldb.cursor()

root=Tk()
root.geometry("1366x768")

root.title("Fin sYs")

plus = PhotoImage(file="images/plus.png")
backward = PhotoImage(file="images/back.png")

p1 = PhotoImage(file = 'images/favicon.png')
root.iconphoto(False, p1)

#--------------------------------------------------------------------------------------------Images

imgr1 =PIL.Image.open("images\logs.png")
exprefreshIcon=ImageTk.PhotoImage(imgr1)

mnu =PIL.Image.open("images\menu bar.PNG")
mnus=ImageTk.PhotoImage(mnu)


srh =PIL.Image.open("images\search.PNG")
srh_img=ImageTk.PhotoImage(srh)

logo =PIL.Image.open("images\logo-icon.png")
resized_image= logo.resize((50,50))
mai_logo= ImageTk.PhotoImage(resized_image)

#--------------------------------------------------------------------------------------------Create Sign In customer

def main_sign_in():
    try:
        main_frame_signup.destroy()
    except:
        pass
    try:
        main_frame_signin.destroy()
    except:
        pass
    Sys_top_frame=Frame(root, height=70,bg="#213b52")
    Sys_top_frame.pack(fill=X,)

    #---------------------------------------------------------------------------------------Top Menu
    tp_lb_nm=LabelFrame(Sys_top_frame,height=70,bg="#213b52",width=400)#-----------------------------Logo Name Frame
    tp_lb_nm.grid(row=1,column=1)

    label = Label(tp_lb_nm, image = mai_logo,height=70,bg="#213b52",border=0)
    label.grid(row=2,column=1)
    label = Label(tp_lb_nm, text="Fin sYs",bg="#213b52", fg="white",font=('Calibri 30 bold'),border=0)
    label.grid(row=2,column=2)
  
    mnu_btn = Button(tp_lb_nm, image=mnus, bg="white", fg="black",border=0)
    mnu_btn.grid(row=2,column=4,padx=50)

    tp_lb_srh=LabelFrame(Sys_top_frame,height=70,bg="#213b52",width=700)#-------------------------Serch area Frame
    tp_lb_srh.grid(row=1,column=2)
    def srh_fn(event):
        if srh_top.get()=="Search":
            srh_top.delete(0,END)
        else:
            pass

    srh_top = Entry(tp_lb_srh, width=50, font=('Calibri 16'))
    srh_top.insert(0,"Search")
    srh_top.bind("<Button-1>",srh_fn)
    srh_top.grid(row=2,column=1,padx=(70,0), pady=20)

    srh_btn = Button(tp_lb_srh, image=srh_img, bg="white", fg="black",border=0)
    srh_btn.grid(row=2,column=4,padx=(0,70))

    tp_lb_nm=LabelFrame(Sys_top_frame,height=70,bg="#213b52",width=100)#----------------Notification
    tp_lb_nm.grid(row=1,column=3)
    tp_lb_nm=LabelFrame(Sys_top_frame,height=70,bg="#213b52",width=200)#----------------profile area name
    tp_lb_nm.grid(row=1,column=4)

    Sys_top_frame2=Frame(root, height=10,bg="#213b52")
    Sys_top_frame2.pack(fill=X,)
    
    
  
    s = ttk.Style()
    s.theme_use('default')
    s.configure('TNotebook.Tab', background="#213b52",foreground="white", width=150,anchor="center", padding=5)
    s.map('TNotebook.Tab',background=[("selected","#2f516f")])
    def right_nav():
        
        tabControl.pack_forget()
        btn_nav.place_forget()
        tabControl2.pack(expand = 1, fill ="both")
        btn_nav2.place(x=0,y=0)
        try:
            btn_nav3.place_forget()
        except:
            pass
    def left_nav():
        
        tabControl2.pack_forget()
        btn_nav2.place_forget()
        tabControl.pack(expand = 1, fill ="both")
        global btn_nav3
        btn_nav3=Button(Sys_top_frame2,text=">>", command=right_nav, width=3, bg="#213b52",fg="white")
        btn_nav3.place(x=1325,y=0)

    tabControl = ttk.Notebook(Sys_top_frame2)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3=  ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)
    tab6=  ttk.Frame(tabControl)
    tab7 = ttk.Frame(tabControl)
    tab8 = ttk.Frame(tabControl)
    
    
    btn_nav=Button(Sys_top_frame2,text=">>", command=right_nav, width=3, bg="#213b52",fg="white")
    btn_nav.place(x=1325,y=0)
    tabControl.add(tab1,compound = LEFT, text ='Dashboard',)
    tabControl.add(tab2,compound = LEFT, text ='Bancking')
    tabControl.add(tab3,compound = LEFT, text ='Sales')
    tabControl.add(tab4,compound = LEFT, text ='Expenses')
    tabControl.add(tab5,compound = LEFT, text ='Payroll') 
    tabControl.add(tab6,compound = LEFT, text ='Report')
    tabControl.add(tab7,compound = LEFT, text ='Taxes')
    tabControl.add(tab8,compound = LEFT, text ='Accounting')
    
    tabControl.pack(expand = 1, fill ="both")


    
    tabControl2 = ttk.Notebook(Sys_top_frame2)
    tab9 =  ttk.Frame(tabControl2)
    tab10=  ttk.Frame(tabControl2)
    tab11 = ttk.Frame(tabControl2)
    tab12=  ttk.Frame(tabControl2)
    tab13 = ttk.Frame(tabControl2)
    tab14 = ttk.Frame(tabControl2)
    tab15 =  ttk.Frame(tabControl2)

    btn_nav2=Button(Sys_top_frame2,text="<<", command=left_nav, width=3, bg="#213b52",fg="white")
    
        
    tabControl2.add(tab9,compound = LEFT, text ='My Account')
    tabControl2.add(tab10,compound = LEFT, text ='Cash Management')
    tabControl2.add(tab11,compound = LEFT, text ='Production')
    tabControl2.add(tab12,compound = LEFT, text ='Quality Management')
    tabControl2.add(tab13,compound = LEFT, text ='Project Management')
    tabControl2.add(tab14,compound = LEFT, text ='Usage Decisions')
    tabControl2.add(tab15,compound = LEFT, text ='Account & Payable')

   

    Sys_mains_frame=Frame(tab1, height=750,bg="#213b52")
    Sys_mains_frame.pack(fill=X)

    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333Banking Section(Tab2)

    tab_bank = ttk.Notebook(tab2)
    tab2_1 =  ttk.Frame(tab_bank)
    tab2_2=  ttk.Frame(tab_bank)
    tab2_3 = ttk.Frame(tab_bank)

    tab_bank.add(tab2_1,compound = LEFT, text ='Online Banking')
    tab_bank.add(tab2_2,compound = LEFT, text ='Offline banking')
    tab_bank.add(tab2_3,compound = LEFT, text ='Bank Reconvilation')

 
    tab_bank.pack(expand = 1, fill ="both")

    #333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Sales Tab}
    tab_sales = ttk.Notebook(tab3)
    tab3_1 =  ttk.Frame(tab_sales)
    tab3_2=  ttk.Frame(tab_sales)
    tab3_3 = ttk.Frame(tab_sales)
    tab3_4=  ttk.Frame(tab_sales)

    
        
    tab_sales.add(tab3_1,compound = LEFT, text ='Sales Records')
    tab_sales.add(tab3_2,compound = LEFT, text ='Invoices')
    tab_sales.add(tab3_3,compound = LEFT, text ='Customers')
    tab_sales.add(tab3_4,compound = LEFT, text ='Product & Services')
 
    tab_sales.pack(expand = 1, fill ="both")

    tab3_1.grid_columnconfigure(0,weight=1)
    tab3_1.grid_rowconfigure(0,weight=1)

    # s = ttk.Style()
    # s.theme_use('clam')
    # s.configure('TCombobox',fieldbackground="#2f516f",background="#2f516f",foreground='white')


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

            dcanvas.coords("date",dwidth/2.71,dheight/1.435)

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
            y21 = dheight/0.45


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
            

            dcanvas.coords("label1",dwidth/2,dheight/8.24)
            dcanvas.coords("label2",dwidth/2,dheight/2.4)

            #payment-------------

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

            #sales receipt-----------

            dcanvas.coords("label21",dwidth/7.91,dheight/1.76)
            dcanvas.coords("label22",dwidth/2.47,dheight/1.76)
            dcanvas.coords("label23",dwidth/6.13,dheight/1.49)
            dcanvas.coords("label24",dwidth/2.27,dheight/1.49)
            dcanvas.coords("label25",dwidth/6.13,dheight/0.965)
            dcanvas.coords("label26",dwidth/6.13,dheight/0.875)
            dcanvas.coords("label27",dwidth/2.27,dheight/0.875)
            try:
                dcanvas.coords("label28",dwidth/1.395,dheight/0.875)
            except:
                pass
            dcanvas.coords("label29",dwidth/1.225,dheight/1.75)
            dcanvas.coords("label30",dwidth/1.2,dheight/1.63)
            dcanvas.coords("label31",dwidth/20,dheight/0.77)
            dcanvas.coords("label32",dwidth/20,dheight/0.733)
            dcanvas.coords("label33",dwidth/20,dheight/0.699)
            dcanvas.coords("label34",dwidth/20,dheight/0.666)
            dcanvas.coords("label35",dwidth/20,dheight/0.637)
            dcanvas.coords("label36",dwidth/7.91,dheight/0.77)
            dcanvas.coords("label37",dwidth/4.09,dheight/0.77)
            dcanvas.coords("label38",dwidth/2.57,dheight/0.77)
            dcanvas.coords("label39",dwidth/1.88,dheight/0.77)
            dcanvas.coords("label40",dwidth/1.51,dheight/0.77)
            dcanvas.coords("label41",dwidth/1.25,dheight/0.77)
            dcanvas.coords("label42",dwidth/1.09,dheight/0.77)
            dcanvas.coords("label43",dwidth/1.52,dheight/0.595)
            dcanvas.coords("label44",dwidth/1.52,dheight/0.566)
            dcanvas.coords("label45",dwidth/1.52,dheight/0.541)

            dcanvas.coords("entry13",dwidth/2.72,dheight/1.68)
            dcanvas.coords("entry14",dwidth/11,dheight/1.43)
            dcanvas.coords("entry15",dwidth/11,dheight/0.94)
            dcanvas.coords("entry16",dwidth/11,dheight/0.855)
            dcanvas.coords("entry17",dwidth/2.72,dheight/0.855)
            dcanvas.coords("entry18",dwidth/5.16,dheight/0.741)
            dcanvas.coords("entry19",dwidth/3.25,dheight/0.741)
            dcanvas.coords("entry20",dwidth/2.07,dheight/0.741)
            dcanvas.coords("entry21",dwidth/1.681,dheight/0.741)
            dcanvas.coords("entry22",dwidth/1.351,dheight/0.741)
            dcanvas.coords("entry23",dwidth/1.35,dheight/0.6)
            dcanvas.coords("entry24",dwidth/1.35,dheight/0.572)
            dcanvas.coords("entry25",dwidth/1.35,dheight/0.546)
            dcanvas.coords("entry26",dwidth/11,dheight/0.8225)

            dcanvas.coords("combo3",dwidth/11,dheight/1.68)
            try:
                dcanvas.coords("combo4",dwidth/1.55,dheight/0.855)
            except:
                pass
            dcanvas.coords("combo5",dwidth/7.909,dheight/0.733)
            dcanvas.coords("combo6",dwidth/1.091,dheight/0.733)

            dcanvas.coords("button5",dwidth/4,dheight/1.636)
            try:
                dcanvas.coords("button6",dwidth/1.245,dheight/0.844)
            except:
                pass
            dcanvas.coords("button7",dwidth/1.114,dheight/0.51)
            
            dcanvas.coords("line17",dwidth/31.6,dheight/0.79,dwidth/1.039,dheight/0.79)
            dcanvas.coords("line18",dwidth/31.6,dheight/0.75,dwidth/1.039,dheight/0.75)
            dcanvas.coords("line19",dwidth/31.6,dheight/0.715,dwidth/1.039,dheight/0.715)
            dcanvas.coords("line20",dwidth/31.6,dheight/0.683,dwidth/1.039,dheight/0.683)
            dcanvas.coords("line21",dwidth/31.6,dheight/0.653,dwidth/1.039,dheight/0.653)
            dcanvas.coords("line22",dwidth/31.6,dheight/0.625,dwidth/1.039,dheight/0.625)
            dcanvas.coords("line23",dwidth/31.6,dheight/0.79,dwidth/31.6,dheight/0.625)
            dcanvas.coords("line24",dwidth/1.039,dheight/0.79,dwidth/1.039,dheight/0.625)
            dcanvas.coords("line25",dwidth/15,dheight/0.79,dwidth/15,dheight/0.625)
            dcanvas.coords("line26",dwidth/5.3,dheight/0.79,dwidth/5.3,dheight/0.625)
            dcanvas.coords("line27",dwidth/3.3,dheight/0.79,dwidth/3.3,dheight/0.625)
            dcanvas.coords("line28",dwidth/2.1,dheight/0.79,dwidth/2.1,dheight/0.625)
            dcanvas.coords("line29",dwidth/1.7,dheight/0.79,dwidth/1.7,dheight/0.625)
            dcanvas.coords("line30",dwidth/1.365,dheight/0.79,dwidth/1.365,dheight/0.625)
            dcanvas.coords("line31",dwidth/1.15,dheight/0.79,dwidth/1.15,dheight/0.625)

            dcanvas.coords("line32",dwidth/1.7,dheight/0.61,dwidth/1.039,dheight/0.61)
            dcanvas.coords("line33",dwidth/1.7,dheight/0.58,dwidth/1.039,dheight/0.58)
            dcanvas.coords("line34",dwidth/1.7,dheight/0.553,dwidth/1.039,dheight/0.553)
            dcanvas.coords("line35",dwidth/1.7,dheight/0.529,dwidth/1.039,dheight/0.529)
            dcanvas.coords("line36",dwidth/1.7,dheight/0.61,dwidth/1.7,dheight/0.529)
            dcanvas.coords("line37",dwidth/1.365,dheight/0.61,dwidth/1.365,dheight/0.529)
            dcanvas.coords("line38",dwidth/1.039,dheight/0.61,dwidth/1.039,dheight/0.529)

        sr_Canvas_1 = Canvas(sr_Frame_1,bg='#2f516f',scrollregion=(0,0,700,1200))

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

            rp_custCombo = ttk.Combobox(sr_Canvas_1,width=28)
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

                cust_title = ttk.Combobox(sr_Canvas_2,width=33)
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_title,tags=("combo1"))

                cust_label4 = Label(sr_Canvas_2,width=20,height=1,text="First name",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label4,tags=('label4'))

                cust_fname = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_fname,tags=("entry2"))

                cust_label5 = Label(sr_Canvas_2,width=20,height=1,text="Last name",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label5,tags=('label5'))

                cust_lname = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_lname,tags=("entry3"))

                cust_label6 = Label(sr_Canvas_2,width=20,height=1,text="Company",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label6,tags=('label6'))

                cust_company = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_company,tags=("entry4"))

                cust_label7 = Label(sr_Canvas_2,width=20,height=1,text="Location",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label7,tags=('label7'))

                cust_location = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_location,tags=("entry5"))

                cust_label8 = Label(sr_Canvas_2,width=20,height=1,text="GST type",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label8,tags=('label8'))

                cust_gtype = ttk.Combobox(sr_Canvas_2,width=33)
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_gtype,tags=("combo2"))

                cust_label9 = Label(sr_Canvas_2,width=20,height=1,text="GSTIN",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label9,tags=('label9'))

                cust_gin = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_gin,tags=("entry6"))

                cust_label10 = Label(sr_Canvas_2,width=20,height=1,text="PAN NO",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label10,tags=('label10'))

                cust_pan = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pan,tags=("entry7"))

                cust_label11 = Label(sr_Canvas_2,width=20,height=1,text="Email",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label11,tags=('label11'))

                cust_email = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_email,tags=("entry8"))

                cust_label12 = Label(sr_Canvas_2,width=20,height=1,text="Website",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label12,tags=('label12'))

                cust_web = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_web,tags=("entry9"))

                cust_label13 = Label(sr_Canvas_2,width=20,height=1,text="Mobile",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label13,tags=('label13'))

                cust_mob = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_mob,tags=("entry10"))

                cust_label14 = Label(sr_Canvas_2,width=20,height=1,text="Billing Address",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label14,tags=('label14'))

                cust_label15 = Label(sr_Canvas_2,width=20,height=1,text="Street",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label15,tags=('label15'))

                cust_st1 = scrolledtext.ScrolledText(sr_Canvas_2,width=65,height=4,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_st1,tags=("entry11"))

                cust_label17 = Label(sr_Canvas_2,width=20,height=1,text="Shipping Address",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label17,tags=('label17'))

                cust_label16 = Label(sr_Canvas_2,width=20,height=1,text="Street",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label16,tags=('label16'))

                cust_st2 = scrolledtext.ScrolledText(sr_Canvas_2,width=65,height=4,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_st2,tags=("entry12"))

                cust_label18 = Label(sr_Canvas_2,width=20,height=1,text="City",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label18,tags=('label18'))

                cust_city = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_city,tags=("entry13"))

                cust_label19 = Label(sr_Canvas_2,width=20,height=1,text="State",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label19,tags=('label19'))

                cust_state = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_state,tags=("entry14"))

                cust_label20 = Label(sr_Canvas_2,width=20,height=1,text="City",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label20,tags=('label20'))

                cust_city1 = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_city1,tags=("entry15"))

                cust_label21 = Label(sr_Canvas_2,width=20,height=1,text="State",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label21,tags=('label21'))

                cust_state1 = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_state1,tags=("entry16"))
                #--
                cust_label22 = Label(sr_Canvas_2,width=20,height=1,text="Pin code",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label22,tags=('label22'))

                cust_pin = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pin,tags=("entry17"))

                cust_label23 = Label(sr_Canvas_2,width=20,height=1,text="Country",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label23,tags=('label23'))

                cust_country = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_country,tags=("entry18"))

                cust_label24 = Label(sr_Canvas_2,width=20,height=1,text="Pin code",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label24,tags=('label24'))

                cust_pin1 = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pin1,tags=("entry19"))

                cust_label25 = Label(sr_Canvas_2,width=20,height=1,text="Country",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label25,tags=('label25'))

                cust_country1 = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
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

                def rp_goBack1():
                    sr_Frame_2.grid_forget()
                    sr_Frame_1.grid(row=0,column=0,sticky='nsew')

                back_btn = Button(sr_Canvas_2,text='←  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:rp_goBack1())
                sr_Canvas_2.create_window(0,0,window=back_btn,tags=("button2"))

            rp_plus = Button(sr_Canvas_1,text='',bd=0,image=plus,activebackground='#1b3857',background='#1b3857',command=lambda:sr_addCustomer())
            sr_Canvas_1.create_window(0,0,window=rp_plus,tags=("button1"))

            rp_label3 = Label(sr_Canvas_1,width=10,height=1,text="Email",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_1.create_window(0,0,window=rp_label3,tags=('label4'))

            rp_email = Entry(sr_Canvas_1,width=35,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='nw',window=rp_email,tags=("entry1"))

            rp_label4 = Label(sr_Canvas_1,width=20,height=1,text="Find by invoice number",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
            sr_Canvas_1.create_window(0,0,window=rp_label4,tags=("label5"))

            rp_invnum = Entry(sr_Canvas_1,width=35,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='nw',window=rp_invnum,tags=("entry2"))

            rp_label6 = Label(sr_Canvas_1,width=20,height=1,text="Payment method",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
            sr_Canvas_1.create_window(0,0,window=rp_label6,tags=("label7"))

            def addnew_pmethod(event):
                if rp_pmethod.get() == "Add new":
                    rp_newmeth = Entry(sr_Canvas_1,width=35,background='#2f516f',foreground='white')
                    sr_Canvas_1.create_window(115,476,anchor='nw',window=rp_newmeth,tags=("entry7"))
                else:
                    pass

            rp_pmethod = ttk.Combobox(sr_Canvas_1,width=33,background='#2f516f')
            rp_pmethod['values'] = ['Add new',]
            rp_pmethod.current(0)
            rp_pmethod.bind("<<ComboboxSelected>>",addnew_pmethod)
            sr_Canvas_1.create_window(0,0,anchor='nw',window=rp_pmethod,tags=("entry3"))

            rp_label7 = Label(sr_Canvas_1,width=20,height=1,text="Deposit to",font=('arial 12'),background='#1b3857',fg="white",anchor="nw")
            sr_Canvas_1.create_window(0,0,window=rp_label7,tags=("label8"))

            rp_depositto = ttk.Combobox(sr_Canvas_1,width=28)
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
                    y21 = dheight/0.95


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
                    dcanvas.coords("label2",dwidth/4.58,dheight/2.44)
                    dcanvas.coords("label3",dwidth/1.59,dheight/2.44)
                    dcanvas.coords("label4",dwidth/4.58,dheight/1.99)
                    dcanvas.coords("label5",dwidth/1.59,dheight/1.99)
                    dcanvas.coords("label6",dwidth/1.55,dheight/1.67)
                    dcanvas.coords("label7",dwidth/1.59,dheight/1.43)

                    dcanvas.coords("entry1",dwidth/6.9,dheight/2.32)
                    dcanvas.coords("entry2",dwidth/1.8,dheight/2.32)
                    dcanvas.coords("entry3",dwidth/6.9,dheight/1.91)
                    dcanvas.coords("entry4",dwidth/1.8,dheight/1.91)
                    dcanvas.coords("entry5",dwidth/6.9,dheight/1.7)
                    dcanvas.coords("entry6",dwidth/1.8,dheight/1.6)
                    dcanvas.coords("entry7",dwidth/1.8,dheight/1.385)

                    dcanvas.coords("check1",dwidth/1.81,dheight/1.73)

                    dcanvas.coords("button1",dwidth/2,dheight/1.07)
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

                dep_acctype = ttk.Combobox(sr_Canvas_3,width=58,background='#2f516f',foreground='white')
                sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_acctype,tags=("entry1"))

                dep_label3 = Label(sr_Canvas_3,width=20,height=1,text="*Name",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
                sr_Canvas_3.create_window(0,0,window=dep_label3,tags=("label3"))

                dep_name = Entry(sr_Canvas_3,width=60,background='#2f516f',foreground='white')
                sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_name,tags=("entry2"))

                dep_label4 = Label(sr_Canvas_3,width=20,height=1,text="*Detail Type",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
                sr_Canvas_3.create_window(0,0,window=dep_label4,tags=("label4"))

                dep_dtype = ttk.Combobox(sr_Canvas_3,width=58,background='#2f516f',foreground='white')
                sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_dtype,tags=("entry3"))

                dep_label5 = Label(sr_Canvas_3,width=20,height=1,text="Description",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
                sr_Canvas_3.create_window(0,0,window=dep_label5,tags=("label5"))

                dep_desp = Entry(sr_Canvas_3,width=60,background='#2f516f',foreground='white')
                sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_desp,tags=("entry4"))

                dep_term = Text(sr_Canvas_3,width=45,height=8,background='#2f516f',foreground='white')
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

                dep_subacc = ttk.Combobox(sr_Canvas_3,width=58,background='#2f516f',foreground='white',state=DISABLED)
                sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_subacc,tags=("entry6"))

                dep_label7 = Label(sr_Canvas_3,width=20,height=1,text="Default Tax Code",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
                sr_Canvas_3.create_window(0,0,window=dep_label7,tags=("label7"))

                dep_dtaxcode = Entry(sr_Canvas_3,width=60,background='#2f516f',foreground='white')
                sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_dtaxcode,tags=("entry7"))

                dep_save = Button(sr_Canvas_3,text="Create",font=('arial 12 bold'),width=35,height=2,background="#198fed",activebackground="#198fed",foreground="white",activeforeground="white",bd=0)
                sr_Canvas_3.create_window(0,0,window=dep_save,tags=("button1"))

                def goBack2():
                    sr_Frame_3.grid_forget()
                    sr_Frame_1.grid(row=0,column=0,sticky='nsew')

                back_btn = Button(sr_Canvas_3,text='←  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:goBack2())
                sr_Canvas_3.create_window(0,0,window=back_btn,tags=("button2"))

            rp_plus1 = Button(sr_Canvas_1,text='',bd=0,image=plus,activebackground='#1b3857',background='#1b3857',command=lambda:add_depositTo())
            sr_Canvas_1.create_window(0,0,window=rp_plus1,tags=("button2"))

            rp_label8 = Label(sr_Canvas_1,width=20,height=1,text="Amount recieved",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
            sr_Canvas_1.create_window(0,0,window=rp_label8,tags=("label9"))

            rp_amntre = Entry(sr_Canvas_1,width=35,background='#2f516f',foreground='white')
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

            rp_amnttoapply = Entry(sr_Canvas_1,width=35,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(1130,825,anchor='c',window=rp_amnttoapply,tags=("entry5"))   

            rpt_label8 = Label(sr_Canvas_1,width=15,height=1,text="Amount to Credit", font=('arial 10 bold'),background='#1b3857',fg="white") 
            sr_Canvas_1.create_window(910, 875, anchor="c", window=rpt_label8,tags=("label19"))  

            rp_amnttocredit = Entry(sr_Canvas_1,width=35,background='#2f516f',foreground='white')
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

            rpt_descp = Entry(sr_Canvas_1,width=30,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='c',window=rpt_descp,tags=("entry8")) 

            rpt_due = Entry(sr_Canvas_1,width=19,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='c',window=rpt_due,tags=("entry9")) 

            rpt_original = Entry(sr_Canvas_1,width=48,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='c',window=rpt_original,tags=("entry10")) 

            rpt_obal = Entry(sr_Canvas_1,width=37,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='c',window=rpt_obal,tags=("entry11"))

            rpt_payment = Entry(sr_Canvas_1,width=30,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='c',window=rpt_payment,tags=("entry12")) 

            rp_label5 = Label(sr_Canvas_1,width=20,height=1,text="Payment date",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
            sr_Canvas_1.create_window(0,0,window=rp_label5,tags=("label6"))

            rp_pdate = DateEntry(sr_Canvas_1,width=33,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(115,398,anchor='nw',window=rp_pdate)
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

            cm_custCombo = ttk.Combobox(sr_Canvas_1,width=28)
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

                cust_title = ttk.Combobox(sr_Canvas_2,width=33)
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_title,tags=("combo1"))

                cust_label4 = Label(sr_Canvas_2,width=20,height=1,text="First name",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label4,tags=('label4'))

                cust_fname = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_fname,tags=("entry2"))

                cust_label5 = Label(sr_Canvas_2,width=20,height=1,text="Last name",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label5,tags=('label5'))

                cust_lname = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_lname,tags=("entry3"))

                cust_label6 = Label(sr_Canvas_2,width=20,height=1,text="Company",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label6,tags=('label6'))

                cust_company = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_company,tags=("entry4"))

                cust_label7 = Label(sr_Canvas_2,width=20,height=1,text="Location",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label7,tags=('label7'))

                cust_location = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_location,tags=("entry5"))

                cust_label8 = Label(sr_Canvas_2,width=20,height=1,text="GST type",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label8,tags=('label8'))

                cust_gtype = ttk.Combobox(sr_Canvas_2,width=33)
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_gtype,tags=("combo2"))

                cust_label9 = Label(sr_Canvas_2,width=20,height=1,text="GSTIN",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label9,tags=('label9'))

                cust_gin = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_gin,tags=("entry6"))

                cust_label10 = Label(sr_Canvas_2,width=20,height=1,text="PAN NO",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label10,tags=('label10'))

                cust_pan = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pan,tags=("entry7"))

                cust_label11 = Label(sr_Canvas_2,width=20,height=1,text="Email",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label11,tags=('label11'))

                cust_email = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_email,tags=("entry8"))

                cust_label12 = Label(sr_Canvas_2,width=20,height=1,text="Website",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label12,tags=('label12'))

                cust_web = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_web,tags=("entry9"))

                cust_label13 = Label(sr_Canvas_2,width=20,height=1,text="Mobile",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label13,tags=('label13'))

                cust_mob = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_mob,tags=("entry10"))

                cust_label14 = Label(sr_Canvas_2,width=20,height=1,text="Billing Address",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label14,tags=('label14'))

                cust_label15 = Label(sr_Canvas_2,width=20,height=1,text="Street",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label15,tags=('label15'))

                cust_st1 = scrolledtext.ScrolledText(sr_Canvas_2,width=65,height=4,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_st1,tags=("entry11"))

                cust_label17 = Label(sr_Canvas_2,width=20,height=1,text="Shipping Address",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label17,tags=('label17'))

                cust_label16 = Label(sr_Canvas_2,width=20,height=1,text="Street",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label16,tags=('label16'))

                cust_st2 = scrolledtext.ScrolledText(sr_Canvas_2,width=65,height=4,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_st2,tags=("entry12"))

                cust_label18 = Label(sr_Canvas_2,width=20,height=1,text="City",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label18,tags=('label18'))

                cust_city = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_city,tags=("entry13"))

                cust_label19 = Label(sr_Canvas_2,width=20,height=1,text="State",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label19,tags=('label19'))

                cust_state = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_state,tags=("entry14"))

                cust_label20 = Label(sr_Canvas_2,width=20,height=1,text="City",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label20,tags=('label20'))

                cust_city1 = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_city1,tags=("entry15"))

                cust_label21 = Label(sr_Canvas_2,width=20,height=1,text="State",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label21,tags=('label21'))

                cust_state1 = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_state1,tags=("entry16"))
                #--
                cust_label22 = Label(sr_Canvas_2,width=20,height=1,text="Pin code",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label22,tags=('label22'))

                cust_pin = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pin,tags=("entry17"))

                cust_label23 = Label(sr_Canvas_2,width=20,height=1,text="Country",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label23,tags=('label23'))

                cust_country = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_country,tags=("entry18"))

                cust_label24 = Label(sr_Canvas_2,width=20,height=1,text="Pin code",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label24,tags=('label24'))

                cust_pin1 = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pin1,tags=("entry19"))

                cust_label25 = Label(sr_Canvas_2,width=20,height=1,text="Country",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label25,tags=('label25'))

                cust_country1 = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
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

            cm_plus = Button(sr_Canvas_1,text='',bd=0,image=plus,activebackground='#1b3857',background='#1b3857',command=lambda:sr_addCustomer_1())
            sr_Canvas_1.create_window(0,0,window=cm_plus,tags=("button5"))

            cm_label4 = Label(sr_Canvas_1,width=10,height=1,text="Email",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_1.create_window(0,0,window=cm_label4,tags=('label22'))

            cm_email = Entry(sr_Canvas_1,width=35,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='nw',window=cm_email,tags=("entry13"))

            cm_label5 = Label(sr_Canvas_1,width=20,height=1,text="Billing Address",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_1.create_window(0,0,window=cm_label5,tags=('label23'))

            cm_baddress = scrolledtext.ScrolledText(sr_Canvas_1,width=24,height=10,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='nw',window=cm_baddress,tags=("entry14"))

            cm_label7 = Label(sr_Canvas_1,width=20,height=1,text="Place of Supply",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_1.create_window(0,0,window=cm_label7,tags=('label25'))

            cm_pofsupply = ttk.Combobox(sr_Canvas_1,width=33,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='nw',window=cm_pofsupply,tags=("entry15"))

            cm_label8 = Label(sr_Canvas_1,width=20,height=1,text="Payment Method",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_1.create_window(0,0,window=cm_label8,tags=('label26'))

            def addnew_pmethod_1(event):
                if cm_pmethod.get() == "Add new":
                    cm_newmeth = Entry(sr_Canvas_1,width=35,background='#2f516f',foreground='white')
                    sr_Canvas_1.create_window(115,690,anchor='nw',window=cm_newmeth,tags=("entry26"))
                else:
                    pass

            cm_pmethod = ttk.Combobox(sr_Canvas_1,width=33,background='#2f516f',foreground='white')
            cm_pmethod['values'] = ['Add new',]
            cm_pmethod.current(0)
            cm_pmethod.bind("<<ComboboxSelected>>",addnew_pmethod_1)
            sr_Canvas_1.create_window(0,0,anchor='nw',window=cm_pmethod,tags=("entry16"))

            cm_label9 = Label(sr_Canvas_1,width=20,height=1,text="Reference No:",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_1.create_window(0,0,window=cm_label9,tags=('label27'))

            cm_ref = Entry(sr_Canvas_1,width=35,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='nw',window=cm_ref,tags=("entry17"))

            cm_label10 = Label(sr_Canvas_1,width=20,height=1,text="Deposit to:",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_1.create_window(0,0,window=cm_label10,tags=('label28'))

            cm_depto = ttk.Combobox(sr_Canvas_1,width=28,background='#2f516f',foreground='white')
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
                    y21 = dheight/0.95


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
                    dcanvas.coords("label2",dwidth/4.58,dheight/2.44)
                    dcanvas.coords("label3",dwidth/1.59,dheight/2.44)
                    dcanvas.coords("label4",dwidth/4.58,dheight/1.99)
                    dcanvas.coords("label5",dwidth/1.59,dheight/1.99)
                    dcanvas.coords("label6",dwidth/1.55,dheight/1.67)
                    dcanvas.coords("label7",dwidth/1.59,dheight/1.43)

                    dcanvas.coords("entry1",dwidth/6.9,dheight/2.32)
                    dcanvas.coords("entry2",dwidth/1.8,dheight/2.32)
                    dcanvas.coords("entry3",dwidth/6.9,dheight/1.91)
                    dcanvas.coords("entry4",dwidth/1.8,dheight/1.91)
                    dcanvas.coords("entry5",dwidth/6.9,dheight/1.7)
                    dcanvas.coords("entry6",dwidth/1.8,dheight/1.6)
                    dcanvas.coords("entry7",dwidth/1.8,dheight/1.385)

                    dcanvas.coords("check1",dwidth/1.81,dheight/1.73)

                    dcanvas.coords("button1",dwidth/2,dheight/1.07)
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

                dep_acctype = ttk.Combobox(sr_Canvas_3,width=58,background='#2f516f',foreground='white')
                sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_acctype,tags=("entry1"))

                dep_label3 = Label(sr_Canvas_3,width=20,height=1,text="*Name",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
                sr_Canvas_3.create_window(0,0,window=dep_label3,tags=("label3"))

                dep_name = Entry(sr_Canvas_3,width=60,background='#2f516f',foreground='white')
                sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_name,tags=("entry2"))

                dep_label4 = Label(sr_Canvas_3,width=20,height=1,text="*Detail Type",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
                sr_Canvas_3.create_window(0,0,window=dep_label4,tags=("label4"))

                dep_dtype = ttk.Combobox(sr_Canvas_3,width=58,background='#2f516f',foreground='white')
                sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_dtype,tags=("entry3"))

                dep_label5 = Label(sr_Canvas_3,width=20,height=1,text="Description",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
                sr_Canvas_3.create_window(0,0,window=dep_label5,tags=("label5"))

                dep_desp = Entry(sr_Canvas_3,width=60,background='#2f516f',foreground='white')
                sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_desp,tags=("entry4"))

                dep_term = Text(sr_Canvas_3,width=45,height=8,background='#2f516f',foreground='white')
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

                dep_subacc = ttk.Combobox(sr_Canvas_3,width=58,background='#2f516f',foreground='white',state=DISABLED)
                sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_subacc,tags=("entry6"))

                dep_label7 = Label(sr_Canvas_3,width=20,height=1,text="Default Tax Code",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
                sr_Canvas_3.create_window(0,0,window=dep_label7,tags=("label7"))

                dep_dtaxcode = Entry(sr_Canvas_3,width=60,background='#2f516f',foreground='white')
                sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_dtaxcode,tags=("entry7"))

                dep_save = Button(sr_Canvas_3,text="Create",font=('arial 12 bold'),width=35,height=2,background="#198fed",activebackground="#198fed",foreground="white",activeforeground="white",bd=0)
                sr_Canvas_3.create_window(0,0,window=dep_save,tags=("button1"))

                def cm_goBack2():
                    sr_Frame_3.grid_forget()
                    sr_Frame_1.grid(row=0,column=0,sticky='nsew')

                back_btn = Button(sr_Canvas_3,text='←  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:cm_goBack2())
                sr_Canvas_3.create_window(0,0,window=back_btn,tags=("button2"))

            cm_plus1 = Button(sr_Canvas_1,text='',bd=0,image=plus,activebackground='#1b3857',background='#1b3857',command=lambda:add_depositTo_1())
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

            cm_label15 = Label(sr_Canvas_1,width=3,height=1,text="2",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
            sr_Canvas_1.create_window(0,0,window=cm_label15,tags=('label33'))

            cm_label16 = Label(sr_Canvas_1,width=3,height=1,text="3",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
            sr_Canvas_1.create_window(0,0,window=cm_label16,tags=('label34'))

            cm_label17 = Label(sr_Canvas_1,width=3,height=1,text="4",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
            sr_Canvas_1.create_window(0,0,window=cm_label17,tags=('label35'))

            cm_label18 = Label(sr_Canvas_1,width=15,height=1,text="Product / Service",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
            sr_Canvas_1.create_window(0,0,window=cm_label18,tags=('label36'))

            cm_label19 = Label(sr_Canvas_1,width=14,height=1,text="HSN",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
            sr_Canvas_1.create_window(0,0,window=cm_label19,tags=('label37'))

            cm_label20 = Label(sr_Canvas_1,width=18,height=1,text="Description",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
            sr_Canvas_1.create_window(0,0,window=cm_label20,tags=('label38'))

            cm_label21 = Label(sr_Canvas_1,width=10,height=1,text="Qty",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
            sr_Canvas_1.create_window(0,0,window=cm_label21,tags=('label39'))

            cm_label22 = Label(sr_Canvas_1,width=10,height=1,text="Price",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
            sr_Canvas_1.create_window(0,0,window=cm_label22,tags=('label40'))

            cm_label23 = Label(sr_Canvas_1,width=10,height=1,text="Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
            sr_Canvas_1.create_window(0,0,window=cm_label23,tags=('label41'))

            cm_label24 = Label(sr_Canvas_1,width=10,height=1,text="Tax (%)",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
            sr_Canvas_1.create_window(0,0,window=cm_label24,tags=('label42'))

            cmt_entry1 = ttk.Combobox(sr_Canvas_1,width=20,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='c',window=cmt_entry1,tags=("combo5"))

            cmt_entry2 = Entry(sr_Canvas_1,width=21,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='nw',window=cmt_entry2,tags=("entry18"))

            cmt_entry3 = Entry(sr_Canvas_1,width=33,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='nw',window=cmt_entry3,tags=("entry19"))

            cmt_entry4 = Entry(sr_Canvas_1,width=20,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='nw',window=cmt_entry4,tags=("entry20"))

            cmt_entry5 = Entry(sr_Canvas_1,width=27,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='nw',window=cmt_entry5,tags=("entry21"))

            cmt_entry6 = Entry(sr_Canvas_1,width=25,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='nw',window=cmt_entry6,tags=("entry22"))

            cmt_entry7 = ttk.Combobox(sr_Canvas_1,width=14,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='c',window=cmt_entry7,tags=("combo6"))

            cm_label25 = Label(sr_Canvas_1,width=10,height=1,text="Sub Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
            sr_Canvas_1.create_window(0,0,window=cm_label25,tags=('label43'))

            cm_label26 = Label(sr_Canvas_1,width=10,height=1,text="Tax Amount",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
            sr_Canvas_1.create_window(0,0,window=cm_label26,tags=('label44'))

            cm_label27 = Label(sr_Canvas_1,width=10,height=1,text="Grand Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
            sr_Canvas_1.create_window(0,0,window=cm_label27,tags=('label45'))

            cmt_entry8 = Entry(sr_Canvas_1,width=44,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='nw',window=cmt_entry8,tags=("entry23"))

            cmt_entry9 = Entry(sr_Canvas_1,width=44,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='nw',window=cmt_entry9,tags=("entry24"))

            cmt_entry10 = Entry(sr_Canvas_1,width=44,background='#2f516f',foreground='white')
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

            cm_srdate = DateEntry(sr_Canvas_1,width=33,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(465,395,anchor='nw',window=cm_srdate)
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

            cn_custCombo = ttk.Combobox(sr_Canvas_1,width=28)
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

                cust_title = ttk.Combobox(sr_Canvas_2,width=33)
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_title,tags=("combo1"))

                cust_label4 = Label(sr_Canvas_2,width=20,height=1,text="First name",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label4,tags=('label4'))

                cust_fname = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_fname,tags=("entry2"))

                cust_label5 = Label(sr_Canvas_2,width=20,height=1,text="Last name",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label5,tags=('label5'))

                cust_lname = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_lname,tags=("entry3"))

                cust_label6 = Label(sr_Canvas_2,width=20,height=1,text="Company",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label6,tags=('label6'))

                cust_company = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_company,tags=("entry4"))

                cust_label7 = Label(sr_Canvas_2,width=20,height=1,text="Location",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label7,tags=('label7'))

                cust_location = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_location,tags=("entry5"))

                cust_label8 = Label(sr_Canvas_2,width=20,height=1,text="GST type",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label8,tags=('label8'))

                cust_gtype = ttk.Combobox(sr_Canvas_2,width=33)
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_gtype,tags=("combo2"))

                cust_label9 = Label(sr_Canvas_2,width=20,height=1,text="GSTIN",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label9,tags=('label9'))

                cust_gin = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_gin,tags=("entry6"))

                cust_label10 = Label(sr_Canvas_2,width=20,height=1,text="PAN NO",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label10,tags=('label10'))

                cust_pan = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pan,tags=("entry7"))

                cust_label11 = Label(sr_Canvas_2,width=20,height=1,text="Email",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label11,tags=('label11'))

                cust_email = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_email,tags=("entry8"))

                cust_label12 = Label(sr_Canvas_2,width=20,height=1,text="Website",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label12,tags=('label12'))

                cust_web = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_web,tags=("entry9"))

                cust_label13 = Label(sr_Canvas_2,width=20,height=1,text="Mobile",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label13,tags=('label13'))

                cust_mob = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_mob,tags=("entry10"))

                cust_label14 = Label(sr_Canvas_2,width=20,height=1,text="Billing Address",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label14,tags=('label14'))

                cust_label15 = Label(sr_Canvas_2,width=20,height=1,text="Street",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label15,tags=('label15'))

                cust_st1 = scrolledtext.ScrolledText(sr_Canvas_2,width=65,height=4,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_st1,tags=("entry11"))

                cust_label17 = Label(sr_Canvas_2,width=20,height=1,text="Shipping Address",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label17,tags=('label17'))

                cust_label16 = Label(sr_Canvas_2,width=20,height=1,text="Street",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label16,tags=('label16'))

                cust_st2 = scrolledtext.ScrolledText(sr_Canvas_2,width=65,height=4,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_st2,tags=("entry12"))

                cust_label18 = Label(sr_Canvas_2,width=20,height=1,text="City",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label18,tags=('label18'))

                cust_city = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_city,tags=("entry13"))

                cust_label19 = Label(sr_Canvas_2,width=20,height=1,text="State",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label19,tags=('label19'))

                cust_state = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_state,tags=("entry14"))

                cust_label20 = Label(sr_Canvas_2,width=20,height=1,text="City",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label20,tags=('label20'))

                cust_city1 = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_city1,tags=("entry15"))

                cust_label21 = Label(sr_Canvas_2,width=20,height=1,text="State",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label21,tags=('label21'))

                cust_state1 = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_state1,tags=("entry16"))
                #--
                cust_label22 = Label(sr_Canvas_2,width=20,height=1,text="Pin code",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label22,tags=('label22'))

                cust_pin = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pin,tags=("entry17"))

                cust_label23 = Label(sr_Canvas_2,width=20,height=1,text="Country",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label23,tags=('label23'))

                cust_country = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_country,tags=("entry18"))

                cust_label24 = Label(sr_Canvas_2,width=20,height=1,text="Pin code",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label24,tags=('label24'))

                cust_pin1 = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
                sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pin1,tags=("entry19"))

                cust_label25 = Label(sr_Canvas_2,width=20,height=1,text="Country",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                sr_Canvas_2.create_window(0,0,window=cust_label25,tags=('label25'))

                cust_country1 = Entry(sr_Canvas_2,width=35,background='#2f516f',foreground='white')
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

            cn_plus = Button(sr_Canvas_1,text='',bd=0,image=plus,activebackground='#1b3857',background='#1b3857',command=lambda:sr_addCustomer_1())
            sr_Canvas_1.create_window(0,0,window=cn_plus,tags=("button5"))

            cn_label4 = Label(sr_Canvas_1,width=10,height=1,text="Email",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_1.create_window(0,0,window=cn_label4,tags=('label22'))

            cn_email = Entry(sr_Canvas_1,width=35,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='nw',window=cn_email,tags=("entry13"))

            cn_label5 = Label(sr_Canvas_1,width=20,height=1,text="Billing Address",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_1.create_window(0,0,window=cn_label5,tags=('label23'))

            cn_baddress = scrolledtext.ScrolledText(sr_Canvas_1,width=24,height=10,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='nw',window=cn_baddress,tags=("entry14"))

            cn_label7 = Label(sr_Canvas_1,width=20,height=1,text="Place of Supply",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_1.create_window(0,0,window=cn_label7,tags=('label25'))

            cn_pofsupply = ttk.Combobox(sr_Canvas_1,width=33,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='nw',window=cn_pofsupply,tags=("entry15"))

            cn_label8 = Label(sr_Canvas_1,width=20,height=1,text="Invoice Period",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_1.create_window(0,0,window=cn_label8,tags=('label26'))

            def addnew_pmethod_1(event):
                if cn_pmethod.get() == "Add new":
                    cn_newmeth = Entry(sr_Canvas_1,width=35,background='#2f516f',foreground='white')
                    sr_Canvas_1.create_window(115,690,anchor='nw',window=cn_newmeth,tags=("entry26"))
                else:
                    pass

            cn_pmethod = ttk.Combobox(sr_Canvas_1,width=33,background='#2f516f',foreground='white')
            cn_pmethod['values'] = ['Add new',]
            cn_pmethod.current(0)
            cn_pmethod.bind("<<ComboboxSelected>>",addnew_pmethod_1)
            sr_Canvas_1.create_window(0,0,anchor='nw',window=cn_pmethod,tags=("entry16"))

            cn_label9 = Label(sr_Canvas_1,width=20,height=1,text="Invoice No.",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_1.create_window(0,0,window=cn_label9,tags=('label27'))

            cn_ref = Entry(sr_Canvas_1,width=35,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='nw',window=cn_ref,tags=("entry17"))

            cn_label11 = Label(sr_Canvas_1,width=20,height=1,text="AMOUNT TO REFUND",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
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

            cn_label15 = Label(sr_Canvas_1,width=3,height=1,text="2",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
            sr_Canvas_1.create_window(0,0,window=cn_label15,tags=('label33'))

            cn_label16 = Label(sr_Canvas_1,width=3,height=1,text="3",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
            sr_Canvas_1.create_window(0,0,window=cn_label16,tags=('label34'))

            cn_label17 = Label(sr_Canvas_1,width=3,height=1,text="4",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
            sr_Canvas_1.create_window(0,0,window=cn_label17,tags=('label35'))

            cn_label18 = Label(sr_Canvas_1,width=15,height=1,text="Product / Service",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
            sr_Canvas_1.create_window(0,0,window=cn_label18,tags=('label36'))

            cn_label19 = Label(sr_Canvas_1,width=14,height=1,text="HSN",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
            sr_Canvas_1.create_window(0,0,window=cn_label19,tags=('label37'))

            cn_label20 = Label(sr_Canvas_1,width=18,height=1,text="Description",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
            sr_Canvas_1.create_window(0,0,window=cn_label20,tags=('label38'))

            cn_label21 = Label(sr_Canvas_1,width=10,height=1,text="Qty",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
            sr_Canvas_1.create_window(0,0,window=cn_label21,tags=('label39'))

            cn_label22 = Label(sr_Canvas_1,width=10,height=1,text="Price",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
            sr_Canvas_1.create_window(0,0,window=cn_label22,tags=('label40'))

            cn_label23 = Label(sr_Canvas_1,width=10,height=1,text="Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
            sr_Canvas_1.create_window(0,0,window=cn_label23,tags=('label41'))

            cn_label24 = Label(sr_Canvas_1,width=10,height=1,text="Tax (%)",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
            sr_Canvas_1.create_window(0,0,window=cn_label24,tags=('label42'))

            cnt_entry1 = ttk.Combobox(sr_Canvas_1,width=20,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='c',window=cnt_entry1,tags=("combo5"))

            cnt_entry2 = Entry(sr_Canvas_1,width=21,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='nw',window=cnt_entry2,tags=("entry18"))

            cnt_entry3 = Entry(sr_Canvas_1,width=33,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='nw',window=cnt_entry3,tags=("entry19"))

            cnt_entry4 = Entry(sr_Canvas_1,width=20,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='nw',window=cnt_entry4,tags=("entry20"))

            cnt_entry5 = Entry(sr_Canvas_1,width=27,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='nw',window=cnt_entry5,tags=("entry21"))

            cnt_entry6 = Entry(sr_Canvas_1,width=25,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='nw',window=cnt_entry6,tags=("entry22"))

            cnt_entry7 = ttk.Combobox(sr_Canvas_1,width=14,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='c',window=cnt_entry7,tags=("combo6"))

            cnt_label25 = Label(sr_Canvas_1,width=10,height=1,text="Sub Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
            sr_Canvas_1.create_window(0,0,window=cnt_label25,tags=('label43'))

            cnt_label26 = Label(sr_Canvas_1,width=10,height=1,text="Tax Amount",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
            sr_Canvas_1.create_window(0,0,window=cnt_label26,tags=('label44'))

            cnt_label27 = Label(sr_Canvas_1,width=10,height=1,text="Grand Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
            sr_Canvas_1.create_window(0,0,window=cnt_label27,tags=('label45'))

            cnt_entry8 = Entry(sr_Canvas_1,width=44,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='nw',window=cnt_entry8,tags=("entry23"))

            cnt_entry9 = Entry(sr_Canvas_1,width=44,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='nw',window=cnt_entry9,tags=("entry24"))

            cnt_entry10 = Entry(sr_Canvas_1,width=44,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(0,0,anchor='nw',window=cnt_entry10,tags=("entry25"))

            save_btn = Button(sr_Canvas_1,text='Save',width=20,height=2,font=('arial 10 bold'),background="#198fed",activebackground="#198fed",foreground="white",activeforeground="white",bd=0)
            sr_Canvas_1.create_window(0,0,window=save_btn,tags=("button7")) 

            def sr_goBack():
                sr_Frame_1.grid_forget()
                sr_Frame.grid(row=0,column=0,sticky='nsew')

            cn_back_btn = Button(sr_Canvas_1,text='←  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:sr_goBack())
            sr_Canvas_1.create_window(0,0,window=cn_back_btn,tags=("button3"))
            #--------------
            cn_label6 = Label(sr_Canvas_1,width=20,height=1,text="Credit Note Date:",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
            sr_Canvas_1.create_window(0,0,window=cn_label6,tags=('label24'))

            cn_srdate = DateEntry(sr_Canvas_1,width=33,background='#2f516f',foreground='white')
            sr_Canvas_1.create_window(465,395,anchor='nw',window=cn_srdate,tags=("date"))
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

    srt_actionCombo = ttk.Combobox(sr_Canvas,width=10)
    srt_actionCombo['values'] = ['Actions','Edit','Delete','View']
    srt_actionCombo.current(0)
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

    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Expenses Tab}
    tab_exp = ttk.Notebook(tab4)
    tab4_1 =  ttk.Frame(tab_exp)
    tab4_2=  ttk.Frame(tab_exp)
    tab_exp.add(tab4_1,compound = LEFT, text ='Expenses')
    tab_exp.add(tab4_2,compound = LEFT, text ='Supliers')
    tab_exp.pack(expand = 1, fill ="both")
    #33333333333333333333333333333333333333333333333333333333333333333333333333333333333{Pay Roll Tab}
    tab_payroll = ttk.Notebook(tab5)
    tab5_1 =  ttk.Frame(tab_payroll)
    tab5_2=  ttk.Frame(tab_payroll)
     
    tab_payroll.add(tab5_1,compound = LEFT, text ='Employee')
    tab_payroll.add(tab5_2,compound = LEFT, text ='Payslip')

    tab_payroll.pack(expand = 1, fill ="both")

    #333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Report Tab}

    tab_report = ttk.Notebook(tab6)
    tab6_1 =  ttk.Frame(tab_report)
    tab6_2=  ttk.Frame(tab_report)
    tab6_3 = ttk.Frame(tab_report)
    tab6_4=  ttk.Frame(tab_report)

    
        
    tab_report.add(tab6_1,compound = LEFT, text ='Profit & Loss')
    tab_report.add(tab6_2,compound = LEFT, text ='Balance Sheet')
    tab_report.add(tab6_3,compound = LEFT, text ='Accounts Receivables')
    tab_report.add(tab6_4,compound = LEFT, text ='Accounts Payables')
 
    tab_report.pack(expand = 1, fill ="both")

    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Taxes}

    tab_tax = ttk.Notebook(tab7)
    tab7_1 =  ttk.Frame(tab_tax)
    tab7_2=  ttk.Frame(tab_tax)

    tab_tax.add(tab7_1,compound = LEFT, text ='GST')
    tab_tax.add(tab7_2,compound = LEFT, text ='New')

    tab_tax.pack(expand = 1, fill ="both")

    #333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Accounting}
    tab_account = ttk.Notebook(tab8)
    tab8_1 =  ttk.Frame(tab_account)
    tab8_2=  ttk.Frame(tab_account)

    tab_account.add(tab8_1,compound = LEFT, text ='Chart Of Accounts')
    tab_account.add(tab8_2,compound = LEFT, text ='Reconcile')
   
 
    tab_account.pack(expand = 1, fill ="both")
    #33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Cash Management}
    tab_cash = ttk.Notebook(tab10)
    
    tab10_1 =  ttk.Frame(tab_cash)
    tab10_2=  ttk.Frame(tab_cash)
    tab10_3 = ttk.Frame(tab_cash)

    tab_cash.add(tab10_1,compound = LEFT, text ='Cash Position')
    tab_cash.add(tab10_2,compound = LEFT, text ='Cash Flow Analyzer')
    tab_cash.add(tab10_3,compound = LEFT, text ='Check Cash Flow')

    tab_cash.pack(expand = 1, fill ="both")
    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{My Account}
    Sys_mains_frame=Frame(tab9, height=750,bg="#2f516f")
    Sys_mains_frame.pack(fill=X)
#----------------------------------------------------------------------------------Sign in frame in signup section
def fun_sign_in():
    
    main_frame_signup.destroy()
    global main_frame_signin
    main_frame_signin=Frame(root, height=750)
    main_frame_signin.pack(fill=X,)

    sign_in=Label(main_frame_signin, text="Sign In",font=('Calibri 30 bold'), fg="black")
    sign_in.place(x=900, y=220)


    def sig_nm(event):
        if nm_ent.get()=="Username":
            nm_ent.delete(0,END)
        else:
            pass

    def sig_pass(event):
            if pass_ent.get()=="Password":
                pass_ent.delete(0,END)
            else:
                pass
    nm_ent = Entry(main_frame_signin, width=25, font=('Calibri 16'))
    nm_ent.insert(0,"Username")
    nm_ent.bind("<Button-1>",sig_nm)
    nm_ent.place(x=820,y=300)

    pass_ent = Entry(main_frame_signin, width=25, font=('Calibri 16'))
    pass_ent.insert(0,"Password")
    pass_ent.bind("<Button-1>",sig_pass)
    pass_ent.place(x=820,y=350)

    but_sign2 = customtkinter.CTkButton(master=main_frame_signin,command=lambda:main_sign_in(),text="Log In",bg="#213b52")
    but_sign2.place(relx=0.69, rely=0.58)

    #----------------------------------------------------------------------------------------left canvas
    lf_signup= Canvas(main_frame_signin,width=1500, height=1500)
    lf_signup.place(x=-700,y=0)

    lf_signup.create_oval(1400,1400,-800,-1700,fill="#213b52")

    label = Label(main_frame_signin, image = exprefreshIcon,bg="#213b52", width=500, justify=RIGHT)
    label.place(x=0,y=150)

    lft_lab=Label(main_frame_signin, text="New here ?",font=('Calibri 20 bold'), fg="white", bg="#213b52")
    lft_lab.place(x=250, y=40)
    lft_lab=Label(main_frame_signin, text="Join here to start a business with FinsYs!",font=('Calibri 16 bold'), fg="white", bg="#213b52")
    lft_lab.place(x=150, y=80)

    btn2 = Button(main_frame_signin, text = 'Sign Up', command=lambda:func_sign_up(), bg="white", fg="black",borderwidth = 3,height=1,width=10)
    btn2.place(x=275,y=130)


#-----------------------------------------------------------------------------------Sign Up Section
def func_sign_up():
    global main_frame_signup
    main_frame_signin.destroy()

    main_frame_signup=Frame(root, height=750)
    main_frame_signup.pack(fill=X,)

    lf_signup= Canvas(main_frame_signup,width=1500, height=1500)
    lf_signup.place(x=500,y=0)

    lf_signup.create_oval(1400,1400,150,-1700,fill="#213b52")

    #--------------------------------------------------------------------------------sign up section
    sign_in=Label(main_frame_signup, text="Sign Up",font=('Calibri 30 bold'), fg="black")
    sign_in.place(x=260, y=100)

    def nme(event):
        if fst_nm.get()=="Firstname":
            fst_nm.delete(0,END)
        else:
            pass

    def nme1(event):
        if lst_nm.get()=="Lastname":
            lst_nm.delete(0,END)
        else:
            pass
        
    def nme2(event):
        if sys_em.get()=="Email":
            sys_em.delete(0,END)
        else:
            pass
        
        
    def nme3(event):
        if sys_usr.get()=="Username":
            sys_usr.delete(0,END)
        else:
            pass
        
    def nme4(event):
        if sys_pass.get()=="Password":
            sys_pass.delete(0,END)
        else:
            pass
    
    def nme5(event):
        if sys_cf.get()=="Confirm Password":
            sys_cf.delete(0,END)
        else:
            pass
    
    

    fst_nm = Entry(main_frame_signup, width=25,text="Firstname", font=('Calibri 16'))
    fst_nm.insert(0,"Firstname")
    fst_nm.bind("<Button-1>",nme)
    fst_nm.place(x=200,y=200)

    lst_nm = Entry(main_frame_signup,  width=25, font=('Calibri 16'))
    lst_nm.insert(0,"Lastname")
    lst_nm.bind("<Button-1>",nme1)
    lst_nm.place(x=200,y=250)

    sys_em = Entry(main_frame_signup, width=25, font=('Calibri 16'))
    sys_em.insert(0,"Email")
    sys_em.bind("<Button-1>",nme2)
    sys_em.place(x=200,y=300)

    sys_usr = Entry(main_frame_signup, width=25, font=('Calibri 16'))
    sys_usr.insert(0,"Username")
    sys_usr.bind("<Button-1>",nme3)
    sys_usr.place(x=200,y=350)

    sys_pass = Entry(main_frame_signup, width=25, font=('Calibri 16'))
    sys_pass.insert(0,"Password")
    sys_pass.bind("<Button-1>",nme4)
    sys_pass.place(x=200,y=400)

    sys_cf = Entry(main_frame_signup, width=25, font=('Calibri 16'))
    sys_cf.insert(0,"Confirm Password")
    sys_cf.bind("<Button-1>",nme5)
    sys_cf.place(x=200,y=450)

    # sig_up =PIL.Image.open("images/register.png")
    # sign_up=ImageTk.PhotoImage(sig_up)

    # label = Label(main_frame_signup, image = sign_up,bg="#213b52", width=500, justify=RIGHT)
    # label.place(x=200,y=150)
    
    button_sign = customtkinter.CTkButton(master=main_frame_signup,text="Sign Up",bg="#213b52")
    button_sign.place(relx=0.2, rely=0.7) 

    lft_lab=Label(main_frame_signup, text="One of us ?",font=('Calibri 20 bold'), fg="white", bg="#213b52")
    lft_lab.place(x=900, y=40)
    lft_lab=Label(main_frame_signup, text="click here for work with FinsYs.",font=('Calibri 16 bold'), fg="white", bg="#213b52")
    lft_lab.place(x=820, y=80)

    btn_signup = Button(main_frame_signup, text='Sign In', command=fun_sign_in, bg="white", fg="black",borderwidth = 3,height=1,width=10)
    btn_signup.place(x=920,y=130)


main_frame_signin=Frame(root, height=750)
main_frame_signin.pack(fill=X,)

sign_in=Label(main_frame_signin, text="Sign In",font=('Calibri 30 bold'), fg="black")
sign_in.place(x=900, y=220)

def sig_nm(event):
        if nm_ent.get()=="Username":
            nm_ent.delete(0,END)
        else:
            pass

def sig_pass(event):
        if pass_ent.get()=="Password":
            pass_ent.delete(0,END)
        else:
            pass
nm_ent = Entry(main_frame_signin, width=25, font=('Calibri 16'))
nm_ent.insert(0,"Username")
nm_ent.bind("<Button-1>",sig_nm)
nm_ent.place(x=820,y=300)

pass_ent = Entry(main_frame_signin, width=25, font=('Calibri 16'))
pass_ent.insert(0,"Password")
pass_ent.bind("<Button-1>",sig_pass)
pass_ent.place(x=820,y=350)

button = customtkinter.CTkButton(master=main_frame_signin,command=main_sign_in,text="Log In",bg="#213b52")
button.place(relx=0.69, rely=0.58)

#----------------------------------------------------------------------------------------left canvas
lf_signup= Canvas(main_frame_signin,width=1500, height=1500)
lf_signup.place(x=-700,y=0)

lf_signup.create_oval(1400,1400,-800,-1700,fill="#213b52")

label = Label(main_frame_signin, image = exprefreshIcon,bg="#213b52", width=500, justify=RIGHT)
label.place(x=0,y=150)

lft_lab=Label(main_frame_signin, text="New here ?",font=('Calibri 20 bold'), fg="white", bg="#213b52")
lft_lab.place(x=250, y=40)
lft_lab=Label(main_frame_signin, text="Join here to start a business with FinsYs!",font=('Calibri 16 bold'), fg="white", bg="#213b52")
lft_lab.place(x=150, y=80)

btn2 = Button(main_frame_signin, text = 'Sign Up', command = func_sign_up, bg="white", fg="black",borderwidth = 3,height=1,width=10)
btn2.place(x=275,y=130)

root.mainloop()