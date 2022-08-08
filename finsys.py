
import matplotlib.pyplot as plt
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

import customtkinter
import PIL.Image
from PIL import ImageGrab
from PIL import ImageTk, Image, ImageFile
import PIL.Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import re
from datetime import date,datetime, timedelta

finsysdb = mysql.connector.connect(
    host="localhost", user="root", password="", database="newfinsys", port="3306"
)
fbcursor = finsysdb.cursor(buffered=True)

root=Tk()
root.geometry("1366x768+0+0")

root.title("Fin sYs")

p1 = PhotoImage(file = 'images/favicon.png')
root.iconphoto(False, p1)

#-------------------------------------------------------------------------------------------------------------------------Images
# banking = PhotoImage(file="images/banking.PNG")
# sales = PhotoImage(file="images/sheet.PNG")
# expenses = PhotoImage(file="images/expense.PNG")
# payroll = PhotoImage(file="images/payroll.PNG")
# report = PhotoImage(file="images/reports.PNG")
# taxes = PhotoImage(file="images/taxes.PNG")
# accounts = PhotoImage(file="images/accounting.PNG")

pro_pic =PIL.Image.open("profilepic\propic.jpg")
# resized_pro_pic= pro_pic.resize((170,170))
prof_pics=ImageTk.PhotoImage(pro_pic)

imgr1 =PIL.Image.open("images\logs.png")
exprefreshIcon=ImageTk.PhotoImage(imgr1)

notic =PIL.Image.open("images/bell.png")
noti=ImageTk.PhotoImage(notic)

mnu =PIL.Image.open("images\menu bar.PNG")
mnus=ImageTk.PhotoImage(mnu)


srh =PIL.Image.open("images\search.PNG")
srh_img=ImageTk.PhotoImage(srh)

stn =PIL.Image.open("images/brightness-solid-24.png")
stn_img=ImageTk.PhotoImage(stn)

logo =PIL.Image.open("images\logo-icon.png")
resized_image= logo.resize((50,50))
mai_logo= ImageTk.PhotoImage(resized_image)

sig_up =PIL.Image.open("images/register.png")
resized_sign_up= sig_up.resize((500,400))
sign_up=ImageTk.PhotoImage(resized_sign_up)


#------------------------------------------------------------------------------------------------------------Login Button Function

def main_sign_in():
    usr_nm=nm_ent.get()
    usr_pass=pass_ent.get()
    if usr_nm=="" or usr_pass=="" or usr_nm=="Username" or usr_pass=="Password":
        messagebox.showerror("Login Failed","Enter username and password")
    else:
        sql_log_sql='select * from auth_user where username=%s'
        sql_log_val = (usr_nm,)
        fbcursor.execute(sql_log_sql,sql_log_val)
        check_login=fbcursor.fetchone()

        if check_login is None:
            messagebox.showerror("Login Failed","Create an account")
        else:
            if check_login[4]==usr_nm and check_login[1]==usr_pass:
                try:
                    main_frame_signup.pack_forget()
                except:
                    pass
                try:
                    main_frame_signin.pack_forget()
                except:
                    pass
                Sys_top_frame=Frame(root, height=70,bg="#213b52")
                Sys_top_frame.pack(fill=X,)

                #---------------------------------------------------------------------------------------Top Menu
                tp_lb_nm=LabelFrame(Sys_top_frame,bg="#213b52")#-----------------------------Logo Name Frame
                tp_lb_nm.grid(row=1,column=1,sticky='nsew')
                tp_lb_nm.grid_rowconfigure(0,weight=1)
                tp_lb_nm.grid_columnconfigure(0,weight=1)

                label = Label(tp_lb_nm, image = mai_logo,height=70,bg="#213b52",border=0)
                label.grid(row=2,column=1,sticky='nsew')
                label = Label(tp_lb_nm, text="Fin sYs",bg="#213b52", fg="white",font=('Calibri 30 bold'),border=0)
                label.grid(row=2,column=2,sticky='nsew')
            
                mnu_btn = Button(tp_lb_nm, image=mnus, bg="white", fg="black",border=0)
                mnu_btn.grid(row=2,column=4,padx=50)

                

                tp_lb_srh=LabelFrame(Sys_top_frame,bg="#213b52")#-------------------------Serch area Frame
                tp_lb_srh.grid(row=1,column=2,sticky='nsew')
                tp_lb_srh.grid_rowconfigure(0,weight=1)
                tp_lb_srh.grid_columnconfigure(0,weight=1)

                def srh_fn(event):
                    if srh_top.get()=="Search":
                        srh_top.delete(0,END)
                    else:
                        pass

                srh_top = Entry(tp_lb_srh, width=50, font=('Calibri 16'))
                srh_top.insert(0,"Search")
                srh_top.bind("<Button-1>",srh_fn)
                srh_top.grid(row=2,column=1,padx=(30,0), pady=20,sticky='nsew')

                srh_btn = Button(tp_lb_srh, image=srh_img, bg="#213b52", fg="black",border=0)
                srh_btn.grid(row=2,column=4,padx=(0,30))

                #------------------------------------------------------settings 
                def close_lst_2():
                        lst_prf2.place_forget()
                        set_btn4 = Button(tp_lb_srh, image=stn_img,command=settings, bg="#213b52", fg="black",border=0)
                        set_btn4.grid(row=2,column=5,padx=(0,30))
                        
                def settings():
                    

                    # create a list box
                    stng = ("Accounts And Settings","Customize From Style","Chart Of Accounts")

                    stngs = StringVar(value=stng)
                    global lst_prf2
                    lst_prf2 = Listbox(root,listvariable=stngs,height=3 ,selectmode='extended',bg="black",fg="white")

                    lst_prf2.place(relx=0.70, rely=0.10)
                    lst_prf2.bind('<<ListboxSelect>>', )
                    set_btn.grid_forget()
                    set_btn2 = Button(tp_lb_srh, image=stn_img,command=close_lst_2, bg="#213b52", fg="black",border=0)
                    set_btn2.grid(row=2,column=5,padx=(0,30))

                set_btn = Button(tp_lb_srh, image=stn_img,command=settings, bg="#213b52", fg="black",border=0)
                set_btn.grid(row=2,column=5,padx=(0,30))

                tp_lb_nm=LabelFrame(Sys_top_frame,bg="#213b52")#-----------------------------Notification
                tp_lb_nm.grid(row=1,column=3,sticky='nsew')
                tp_lb_nm.grid_rowconfigure(0,weight=1)
                tp_lb_nm.grid_columnconfigure(0,weight=1)
                srh_btn = Button(tp_lb_nm, image=noti, bg="#213b52", fg="black",border=0)
                srh_btn.grid(row=0,column=0,padx=35)
                
                tp_lb_npr=LabelFrame(Sys_top_frame,bg="#213b52")#---------------------------profile area name
                tp_lb_npr.grid(row=1,column=4,sticky='nsew')
                tp_lb_npr.grid_rowconfigure(0,weight=1)
                tp_lb_npr.grid_columnconfigure(0,weight=1)

                label = Label(tp_lb_npr, text="Errors",bg="#213b52", fg="white", anchor="center",width=10,font=('Calibri 16 bold'),border=0)
                label.grid(row=1,column=1,sticky='nsew')
                label = Label(tp_lb_npr, text="Online",bg="#213b52", fg="white",width=15,font=('Calibri 12 bold'),border=0)
                label.grid(row=2,column=1,sticky='nsew')

                pro =PIL.Image.open("images/user.png")
                resized_pro= pro.resize((20,20))
                pro_pic= ImageTk.PhotoImage(resized_pro)
                
                def lst_frt():
                    lst_prf.place_forget()
                    srh_btn3 = Button(tp_lb_npr, bg="White", fg="black",height=2,width=5,border=0,command=profile)
                    srh_btn3.grid(row=2,column=2,padx=15)
                def lst_prf_slt(event):
                    def edit_profile():
                        def responsive_widgets_edit(event):
                            dwidth = event.width
                            dheight = event.height
                            dcanvas = event.widget
                            


                            r1 = 25
                            x1 = dwidth/63
                            x2 = dwidth/1.021
                            y1 = dheight/13
                            y2 = dheight/.53

                            dcanvas.coords("bg_polygen_pr",x1 + r1,y1,
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

                            
                            # dcanvas.coords("bg_polygen_pr",dwidth/16,dheight/.6,dwidth/1.07,dheight/9)
                            dcanvas.coords("my_pro",dwidth/2.3,dheight/12.5)
                            dcanvas.coords("pr_img",dwidth/2.3,dheight/5)
                            

                            dcanvas.coords("pr_hr_l",dwidth/16,dheight/6.5,dwidth/1.07,dheight/6.5)
                            dcanvas.coords("pr_hd",dwidth/20,dheight/2.2)
                            dcanvas.coords("pr_1_nm",dwidth/17.075,dheight/1.9)
                            dcanvas.coords("fr_name_ent",dwidth/17.075,dheight/1.75)
                            dcanvas.coords("pr_em_lb",dwidth/17.075,dheight/1.56)
                            dcanvas.coords("em_ent",dwidth/17.075,dheight/1.47)
                            dcanvas.coords("pr_crpass_lb",dwidth/17.075,dheight/1.33)
                            dcanvas.coords("pr_crpass_ent",dwidth/17.075,dheight/1.26)
                            dcanvas.coords("pr_re_pass_lb",dwidth/17.075,dheight/1.16)
                            dcanvas.coords("pr_re_pass_ent",dwidth/17.075,dheight/1.1)
                            dcanvas.coords("last_nm_lb",dwidth/1.92,dheight/1.9)
                            dcanvas.coords("lst_nm_ent",dwidth/1.92,dheight/1.75)
                            dcanvas.coords("usr_nm_lb",dwidth/1.92,dheight/1.56)
                            dcanvas.coords("usr_nm_ent",dwidth/1.92,dheight/1.47)
                            dcanvas.coords("pr_new_pass_lb",dwidth/1.92,dheight/1.33)
                            dcanvas.coords("pr_new_pass_ent",dwidth/1.92,dheight/1.26)

                            
                            #-------------------------------------------------------------------------company section
                            dcanvas.coords("cmp_hd",dwidth/20,dheight/1)
                            dcanvas.coords("cmp_nm_lb",dwidth/17.075,dheight/0.93)
                            dcanvas.coords("cmp_nm_ent",dwidth/17.075,dheight/0.89)
                            dcanvas.coords("cmp_cty_lb",dwidth/17.075,dheight/0.84)
                            dcanvas.coords("cmp_cty_ent",dwidth/17.075,dheight/0.81)
                            dcanvas.coords("cmp_pin_lb",dwidth/17.075,dheight/0.77)
                            dcanvas.coords("cmp_pin_ent",dwidth/17.075,dheight/.745)
                            dcanvas.coords("cmp_ph_lb",dwidth/17.075,dheight/.712)
                            dcanvas.coords("cmp_ph_ent",dwidth/17.075,dheight/.69)
                            dcanvas.coords("cmp_indest_lb",dwidth/17.075,dheight/.66)
                            dcanvas.coords("cmp_indest_ent",dwidth/17.075,dheight/.64)
                            dcanvas.coords("cmp_file_lb",dwidth/17.075,dheight/.615)
                            dcanvas.coords("cmp_file_ent",dwidth/17.075,dheight/.6)
                            

                            #--------------------------------------------------------------------------company right

                            dcanvas.coords("cmp_addr_lb",dwidth/1.92,dheight/0.93)
                            dcanvas.coords("cmp_addr_ent",dwidth/1.92,dheight/0.89)
                            dcanvas.coords("cmp_st_lb",dwidth/1.92,dheight/0.84)
                            dcanvas.coords("cmp_st_ent",dwidth/1.92,dheight/0.81)
                            dcanvas.coords("cmp_em_lb",dwidth/1.92,dheight/0.77)
                            dcanvas.coords("cmp_em_ent",dwidth/1.92,dheight/.745)
                            dcanvas.coords("cmp_lg_nm",dwidth/1.92,dheight/.712)
                            dcanvas.coords("cmp_lg_ent",dwidth/1.92,dheight/.69)
                            dcanvas.coords("cmp_typ_lb",dwidth/1.92,dheight/.66)
                            dcanvas.coords("cmp_typ_ent",dwidth/1.92,dheight/.64)
                            dcanvas.coords("btn_edit",dwidth/2.4,dheight/.57)
                        sql_pro="select * from auth_user where username=%s"
                        sql_pro_val=(nm_ent.get(),)
                        fbcursor.execute(sql_pro,sql_pro_val,)
                        edi_dtl=fbcursor.fetchone()

                        def update_profile():
                            first_name=fr_name_ent.get()
                            pro_email=em_ent.get()
                            last_name=lst_nm_ent.get()
                            pro_username=usr_nm_ent.get()
                            pro_new_pass=pr_new_pass_ent.get()
                            if pro_new_pass==pr_re_pass_ent.get() and pr_re_pass_ent.get()==pro_new_pass:
                                if pr_crpass_ent.get()==edi_dtl[1]:
                                    prof_edit="update auth_user set first_name=%s,last_name=%s,email=%s,username=%s,password=%s where id=%s" #adding values into db
                                    prof_edit_val=(first_name,last_name,pro_email,pro_username,pro_new_pass,edi_dtl[0])
                                    fbcursor.execute(prof_edit,prof_edit_val)
                                    finsysdb.commit()

                                    #compnay
                                    cmp_name=cmp_nm_ent.get()
                                    cmp_cty=cmp_cty_ent.get()
                                    cmp_pin=cmp_pin_ent.get()
                                    cmp_phn=cmp_ph_ent.get()
                                    cmp_ind=cmp_indest_ent.get()
                                    cmp_addr=cmp_addr_ent.get()
                                    cmp_st=cmp_st_ent.get()
                                    cmp_em=cmp_em_ent.get()
                                    cmp_bname=cmp_lg_ent.get()
                                    cmp_typ=cmp_typ_ent.get()
                                    logo=cmp_file_ent.get()

                                    cmp_edit="update app1_company set cname=%s,caddress=%s,city=%s,state=%s,pincode=%s,cemail=%s,phone=%s,cimg=%s,bname=%s,industry=%s,ctype=%s where id_id =%s" #adding values into db
                                    cmp_edit_val=(cmp_name,cmp_addr,cmp_cty,cmp_st,cmp_pin,cmp_em,cmp_phn,logo,cmp_bname,cmp_ind,cmp_typ,edi_dtl[0])
                                    fbcursor.execute(cmp_edit,cmp_edit_val)
                                    finsysdb.commit()
                                    messagebox.showerror("Sucess","Updation Success")
                                else:
                                    messagebox.showerror("Updation Failed","Please check your current password")
                            else:

                                messagebox.showerror("Updation Failed","password and conform password does not match")
                        
                        sql_pro_cmp="select * from app1_company where id_id=%s"
                        sql_pro_cmp_val=(pro_dtl[0],)
                        fbcursor.execute(sql_pro_cmp,sql_pro_cmp_val,)
                        edi_cmp_dtl=fbcursor.fetchone()

                        Sys_mains_frame_pr.place_forget()
                        global Sys_mains_frame_pr_ed
                        Sys_mains_frame_pr_ed=Frame(tab1, height=750)
                        Sys_mains_frame_pr_ed.grid(row=0,column=0,sticky='nsew')
                        Sys_mains_frame_pr_ed.grid_rowconfigure(0,weight=1)
                        Sys_mains_frame_pr_ed.grid_columnconfigure(0,weight=1)

                        pr_canvas_ed=Canvas(Sys_mains_frame_pr_ed,height=766,width=1340,scrollregion=(0,0,766,1650),bg="#2f516f",border=0)
                        pr_canvas_ed.bind('<Configure>', responsive_widgets_edit)
                        
                        pr_myscrollbar_ed=Scrollbar(Sys_mains_frame_pr_ed,orient="vertical",command=pr_canvas_ed.yview)
                        pr_canvas_ed.configure(yscrollcommand=pr_myscrollbar_ed.set)

                        pr_myscrollbar_ed.pack(side="right",fill="y")
                        pr_canvas_ed.pack(fill=X)

                        rth2 = pr_canvas_ed.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_pr"),smooth=True,)


                        grd1c=Label(pr_canvas_ed, text="MY PROFILE",bg="#213b52", fg="White", anchor="center",font=('Calibri 24 bold'))
                        win_inv1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=grd1c,tags=("my_pro"))

                        pr_img=Label(pr_canvas_ed,  image = prof_pics,bg="#213b52",width=170,height=170,  anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_img,tags=("pr_img"))

                        pr_canvas_ed.create_line(0,0, 0, 0,fill="gray",tags=("pr_hr_l") )
                        #----------------------------------------------------------------------------------------Personal info
                        pr_hd=Label(pr_canvas_ed, text="Personal Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
                        win_pr = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_hd,tags=("pr_hd"))

                        fir_name=Label(pr_canvas_ed, text="First Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=fir_name,tags=("pr_1_nm"))

                        fr_name_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        fr_name_ent.delete(0,END)
                        fr_name_ent.insert(0,edi_dtl[5])
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=fr_name_ent,tags=("fr_name_ent"))

                        pr_em_lb=Label(pr_canvas_ed, text="E-Mail",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_em_lb,tags=("pr_em_lb"))

                        em_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        em_ent.delete(0,END)
                        em_ent.insert(0,edi_dtl[7])
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=em_ent,tag=("em_ent"))

                        pr_crpass_lb=Label(pr_canvas_ed, text="Enter your Current Password",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_crpass_lb,tag=("pr_crpass_lb"))

                        pr_crpass_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_crpass_ent,tag=("pr_crpass_ent"))

                        pr_re_pass_lb=Label(pr_canvas_ed, text="Re-type new Password",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_re_pass_lb,tag=("pr_re_pass_lb"))

                        pr_re_pass_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_re_pass_ent,tag=("pr_re_pass_ent"))


                        last_nm_lb=Label(pr_canvas_ed, text="Last Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=last_nm_lb,tag=("last_nm_lb"))

                        lst_nm_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        lst_nm_ent.delete(0,END)
                        lst_nm_ent.insert(0,edi_dtl[6])
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=lst_nm_ent,tag=("lst_nm_ent"))

                        usr_nm_lb=Label(pr_canvas_ed, text="Username",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=usr_nm_lb, tag=("usr_nm_lb"))

                        usr_nm_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        usr_nm_ent.delete(0,END)
                        usr_nm_ent.insert(0,edi_dtl[4])
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=usr_nm_ent,tag=("usr_nm_ent"))

                        pr_new_pass_lb=Label(pr_canvas_ed, text="Enter New Password",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_new_pass_lb,tag=("pr_new_pass_lb"))

                        pr_new_pass_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_new_pass_ent,tag=("pr_new_pass_ent"))


                        # #------------------------------------------------------------------------------------------------COMPANY SECTION
                        cmp_hd=Label(pr_canvas_ed, text="Company Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
                        win_pr = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_hd,tag=("cmp_hd"))

                        cmp_nm_lb=Label(pr_canvas_ed, text="Company Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_nm_lb,tag=("cmp_nm_lb"))

                        cmp_nm_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        cmp_nm_ent.delete(0,END)
                        cmp_nm_ent.insert(0,edi_cmp_dtl[1])
                        
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_nm_ent,tag=("cmp_nm_ent"))

                        cmp_cty_lb=Label(pr_canvas_ed, text="City",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_cty_lb,tag=("cmp_cty_lb"))

                        cmp_cty_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        cmp_cty_ent.delete(0,END)
                        cmp_cty_ent.insert(0,edi_cmp_dtl[3])
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_cty_ent,tag=("cmp_cty_ent"))

                        cmp_pin_lb=Label(pr_canvas_ed, text="Pincode",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_pin_lb,tag=("cmp_pin_lb"))

                        cmp_pin_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        cmp_pin_ent.delete(0,END)
                        cmp_pin_ent.insert(0,edi_cmp_dtl[5])
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_pin_ent,tag=("cmp_pin_ent"))

                        cmp_ph_lb=Label(pr_canvas_ed, text="Phone Number",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_ph_lb,tag=("cmp_ph_lb"))

                        cmp_ph_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        cmp_ph_ent.delete(0,END)
                        cmp_ph_ent.insert(0,edi_cmp_dtl[7])
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_ph_ent,tag=("cmp_ph_ent"))

                        cmp_indest_lb=Label(pr_canvas_ed, text="Your Industry",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_indest_lb,tag=("cmp_indest_lb"))

                        cmp_indest_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        cmp_indest_ent.delete(0,END)
                        cmp_indest_ent.insert(0,edi_cmp_dtl[10])
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_indest_ent,tag=("cmp_indest_ent"))

                        # #----------------------------------------------------------------------------------------------------RIGHT SIDE
                        cmp_addr_lb=Label(pr_canvas_ed, text="Company Address",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_addr_lb,tag=("cmp_addr_lb"))

                        cmp_addr_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        cmp_addr_ent.delete(0,END)
                        cmp_addr_ent.insert(0,edi_cmp_dtl[2])
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_addr_ent,tag=("cmp_addr_ent"))

                        cmp_st_lb=Label(pr_canvas_ed, text="State",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_st_lb,tag=("cmp_st_lb"))

                        cmp_st_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        cmp_st_ent.delete(0,END)
                        cmp_st_ent.insert(0,edi_cmp_dtl[4])
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_st_ent,tag=("cmp_st_ent"))

                        cmp_em_lb=Label(pr_canvas_ed, text="Email",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_em_lb,tag=("cmp_em_lb"))

                        cmp_em_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        cmp_em_ent.delete(0,END)
                        cmp_em_ent.insert(0,edi_cmp_dtl[6])
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_em_ent,tag=("cmp_em_ent"))

                        cmp_lg_nm=Label(pr_canvas_ed, text="Legal Business Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_lg_nm,tag=("cmp_lg_nm"))

                        cmp_lg_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        cmp_lg_ent.delete(0,END)
                        cmp_lg_ent.insert(0,edi_cmp_dtl[9])
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_lg_ent,tag=("cmp_lg_ent"))

                        cmp_typ_lb=Label(pr_canvas_ed, text="Company Type",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_typ_lb,tag=("cmp_typ_lb"))

                        cmp_typ_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        cmp_typ_ent.delete(0,END)
                        cmp_typ_ent.insert(0,edi_cmp_dtl[11])
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_typ_ent,tag=("cmp_typ_ent"))

                        cmp_file_lb=Label(pr_canvas_ed, text="File",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_file_lb,tag=("cmp_file_lb"))
                        def fil_ents(event):
                    
                            cmp_logo = askopenfilename(filetypes=(("png file ",'.png'),('PDF', '*.pdf',),("jpg file", ".jpg"),  ("All files", "*.*"),))
                            logo_crp=cmp_logo.split('/',-1)
                            
                            im1 = Image.open(r""+cmp_logo) 
                            im1 = im1.save("profilepic/propic.jpg")

                            cmp_file_ent.delete(0,END)
                            cmp_file_ent.insert(0,logo_crp[-1])

                        cmp_file_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        cmp_file_ent.delete(0,END)
                        cmp_file_ent.insert(0,edi_cmp_dtl[8])
                        cmp_file_ent.bind("<Button-1>",fil_ents)
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_file_ent,tag=("cmp_file_ent"))


                        btn_edit = Button(pr_canvas_ed, text='Update Profile', command=update_profile, bg="#213b52", fg="White",borderwidth = 3,height=2,width=30)
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=btn_edit,tag=("btn_edit"))

                    
                    selected_indices = lst_prf.curselection()
                    selected_langs = ",".join([lst_prf.get(i) for i in selected_indices])
                    lst_prf.place_forget()

                    def pr_responsive_widgets(event):
                            
                            dwidth = event.width
                            dheight = event.height
                            dcanvas = event.widget
                        
                            
                            r1 = 25
                            x1 = dwidth/63
                            x2 = dwidth/1.021
                            y1 = dheight/13
                            y2 = dheight/.6

                            dcanvas.coords("bg_polygen_pr",x1 + r1,y1,
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
            
                            dcanvas.coords("my_pro",dwidth/2.3,dheight/13)
                            dcanvas.coords("pr_img",dwidth/2.3,dheight/5)

                            dcanvas.coords("pr_hr_l",dwidth/16,dheight/6.5,dwidth/1.07,dheight/6.5)
                            dcanvas.coords("pr_hd",dwidth/20,dheight/2.2)
                            dcanvas.coords("pr_1_nm",dwidth/17.075,dheight/1.9)
                            dcanvas.coords("fr_name_ent",dwidth/17.075,dheight/1.75)
                            
                            dcanvas.coords("pr_em_lb",dwidth/17.075,dheight/1.56)
                            dcanvas.coords("em_ent",dwidth/17.075,dheight/1.47)
                            dcanvas.coords("last_nm_lb",dwidth/1.92,dheight/1.9)
                            dcanvas.coords("lst_nm_ent",dwidth/1.92,dheight/1.75)
                            dcanvas.coords("usr_nm_lb",dwidth/1.92,dheight/1.56)
                            dcanvas.coords("usr_nm_ent",dwidth/1.92,dheight/1.47)

                            #-------------------------------------------------------------------------company section
                            dcanvas.coords("cmp_hd",dwidth/20,dheight/1.32)
                            dcanvas.coords("cmp_nm_lb",dwidth/17.075,dheight/1.22)
                            dcanvas.coords("cmp_nm_ent",dwidth/17.075,dheight/1.16)
                            dcanvas.coords("cmp_cty_lb",dwidth/17.075,dheight/1.07)
                            dcanvas.coords("cmp_cty_ent",dwidth/17.075,dheight/1.02)
                            dcanvas.coords("cmp_pin_lb",dwidth/17.075,dheight/.95)
                            dcanvas.coords("cmp_pin_ent",dwidth/17.075,dheight/.91)
                            dcanvas.coords("cmp_ph_lb",dwidth/17.075,dheight/.86)
                            dcanvas.coords("cmp_ph_ent",dwidth/17.075,dheight/.83)
                            dcanvas.coords("cmp_indest_lb",dwidth/17.075,dheight/.78)
                            dcanvas.coords("cmp_indest_ent",dwidth/17.075,dheight/.755)

                            #--------------------------------------------------------------------------company right

                            dcanvas.coords("cmp_addr_lb",dwidth/1.92,dheight/1.22)
                            dcanvas.coords("cmp_addr_ent",dwidth/1.92,dheight/1.16)
                            dcanvas.coords("cmp_st_lb",dwidth/1.92,dheight/1.07)
                            dcanvas.coords("cmp_st_ent",dwidth/1.92,dheight/1.02)
                            dcanvas.coords("cmp_em_lb",dwidth/1.92,dheight/.95)
                            dcanvas.coords("cmp_em_ent",dwidth/1.92,dheight/.91)
                            dcanvas.coords("cmp_lg_nm",dwidth/1.92,dheight/.86)
                            dcanvas.coords("cmp_lg_ent",dwidth/1.92,dheight/.83)
                            dcanvas.coords("cmp_typ_lb",dwidth/1.92,dheight/.78)
                            dcanvas.coords("cmp_typ_ent",dwidth/1.92,dheight/.755)
                            dcanvas.coords("btn_edit",dwidth/2.4,dheight/.71)

                    if selected_langs=="Profile":
                        # canvas.pack_forget()
                        # myscrollbar.pack_forget()
                        # Sys_mains_frame.pack_forget()
                        
                        sql_pro="select * from auth_user where username=%s"
                        sql_pro_val=(nm_ent.get(),)
                        fbcursor.execute(sql_pro,sql_pro_val,)
                        pro_dtl=fbcursor.fetchone()

                        sql_pro_cmp="select * from app1_company where id_id=%s"
                        sql_pro_cmp_val=(pro_dtl[0],)
                        fbcursor.execute(sql_pro_cmp,sql_pro_cmp_val,)
                        pro_cmp_dtl=fbcursor.fetchone()
                        

                        Sys_mains_frame_pr=Frame(tab1, height=750,bg="#2f516f",)
                        Sys_mains_frame_pr.grid(row=0,column=0,sticky='nsew')
                        Sys_mains_frame_pr.grid_rowconfigure(0,weight=1)
                        Sys_mains_frame_pr.grid_columnconfigure(0,weight=1)

                        pr_canvas=Canvas(Sys_mains_frame_pr,height=700,width=1340,scrollregion=(0,0,700,1300),bg="#2f516f",border=0)
                        pr_canvas.bind("<Configure>", pr_responsive_widgets)
                        
                        pr_myscrollbar=Scrollbar(Sys_mains_frame_pr,orient="vertical",command=pr_canvas.yview)
                        pr_canvas.configure(yscrollcommand=pr_myscrollbar.set)

                        pr_myscrollbar.pack(side="right",fill="y")
                        pr_canvas.pack(fill=X)

                        rth2 = pr_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",smooth=True,tags=("bg_polygen_pr"))

                        grd1c=Label(pr_canvas, text="MY PROFILE",bg="#213b52", fg="White", anchor="center",font=('Calibri 24 bold'))
                        win_inv1 = pr_canvas.create_window(0, 0, anchor="nw", window=grd1c,tags=("my_pro"))

                        pr_canvas.create_line(0,0, 0, 0,fill="gray",tags=("pr_hr_l") )
                        #----------------------------------------------------------------------------------------Personal info

        
                        pr_img=Label(pr_canvas, image = prof_pics,bg="#213b52",width=170,height=170, anchor="center",)
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=pr_img,tags=("pr_img"))

                        pr_hd=Label(pr_canvas, text="Personal Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
                        win_pr = pr_canvas.create_window(0, 0, anchor="nw", window=pr_hd,tags=("pr_hd"))

                        fir_name=Label(pr_canvas, text="First Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=fir_name,tags=("pr_1_nm"))

                        fr_name_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        fr_name_ent.delete(0,END)
                        fr_name_ent.insert(0,pro_dtl[5])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=fr_name_ent,tags=("fr_name_ent"))

                        pr_em_lb=Label(pr_canvas, text="E-Mail",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=pr_em_lb,tags=("pr_em_lb"))

                        em_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        em_ent.delete(0,END)
                        em_ent.insert(0,pro_dtl[7])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=em_ent,tag=("em_ent"))

                        last_nm_lb=Label(pr_canvas, text="Last Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=last_nm_lb,tag=("last_nm_lb"))

                        lst_nm_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        lst_nm_ent.delete(0,END)
                        lst_nm_ent.insert(0,pro_dtl[6])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=lst_nm_ent,tag=("lst_nm_ent"))

                        usr_nm_lb=Label(pr_canvas, text="Username",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=usr_nm_lb, tag=("usr_nm_lb"))

                        usr_nm_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        usr_nm_ent.delete(0,END)
                        usr_nm_ent.insert(0,pro_dtl[4])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=usr_nm_ent,tag=("usr_nm_ent"))

                        #------------------------------------------------------------------------------------------------COMPANY SECTION
                        cmp_hd=Label(pr_canvas, text="Company Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
                        win_pr = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_hd,tag=("cmp_hd"))

                        cmp_nm_lb=Label(pr_canvas, text="Company Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_nm_lb,tag=("cmp_nm_lb"))

                        cmp_nm_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        cmp_nm_ent.delete(0,END)
                        cmp_nm_ent.insert(0,pro_cmp_dtl[2])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_nm_ent,tag=("cmp_nm_ent"))

                        cmp_cty_lb=Label(pr_canvas, text="City",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_cty_lb,tag=("cmp_cty_lb"))

                        cmp_cty_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        cmp_cty_ent.delete(0,END)
                        cmp_cty_ent.insert(0,pro_cmp_dtl[3])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_cty_ent,tag=("cmp_cty_ent"))

                        cmp_pin_lb=Label(pr_canvas, text="Pincode",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_pin_lb,tag=("cmp_pin_lb"))

                        cmp_pin_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        cmp_pin_ent.delete(0,END)
                        cmp_pin_ent.insert(0,pro_cmp_dtl[5])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_pin_ent,tag=("cmp_pin_ent"))

                        cmp_ph_lb=Label(pr_canvas, text="Phone Number",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_ph_lb,tag=("cmp_ph_lb"))

                        cmp_ph_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        cmp_ph_ent.delete(0,END)
                        cmp_ph_ent.insert(0,pro_cmp_dtl[7])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_ph_ent,tag=("cmp_ph_ent"))

                        cmp_indest_lb=Label(pr_canvas, text="Your Industry",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_indest_lb,tag=("cmp_indest_lb"))

                        cmp_indest_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        cmp_indest_ent.delete(0,END)
                        cmp_indest_ent.insert(0,pro_cmp_dtl[10])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_indest_ent,tag=("cmp_indest_ent"))

                        #----------------------------------------------------------------------------------------------------RIGHT SIDE
                        cmp_addr_lb=Label(pr_canvas, text="Company Address",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_addr_lb,tag=("cmp_addr_lb"))

                        cmp_addr_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        cmp_addr_ent.delete(0,END)
                        cmp_addr_ent.insert(0,pro_cmp_dtl[2])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_addr_ent,tag=("cmp_addr_ent"))

                        cmp_st_lb=Label(pr_canvas, text="State",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_st_lb,tag=("cmp_st_lb"))

                        cmp_st_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        cmp_st_ent.delete(0,END)
                        cmp_st_ent.insert(0,pro_cmp_dtl[4])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_st_ent,tag=("cmp_st_ent"))

                        cmp_em_lb=Label(pr_canvas, text="Email",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_em_lb,tag=("cmp_em_lb"))

                        cmp_em_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        cmp_em_ent.delete(0,END)
                        cmp_em_ent.insert(0,pro_cmp_dtl[6])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_em_ent,tag=("cmp_em_ent"))

                        cmp_lg_nm=Label(pr_canvas, text="Legal Business Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_lg_nm,tag=("cmp_lg_nm"))

                        cmp_lg_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        cmp_lg_ent.delete(0,END)
                        cmp_lg_ent.insert(0,pro_cmp_dtl[9])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_lg_ent,tag=("cmp_lg_ent"))

                        cmp_typ_lb=Label(pr_canvas, text="Company Type",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_typ_lb,tag=("cmp_typ_lb"))

                        cmp_typ_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        cmp_typ_ent.delete(0,END)
                        cmp_typ_ent.insert(0,pro_cmp_dtl[11])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_typ_ent,tag=("cmp_typ_ent"))


                        btn_edit = Button(pr_canvas, text='Edit Profile', command=edit_profile, bg="#213b52", fg="White",borderwidth = 3,height=2,width=30)
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=btn_edit,tag=("btn_edit"))
                    
                    elif selected_langs=="Log Out":
                        
                        Sys_top_frame2.pack_forget()
                        Sys_top_frame.pack_forget()
                        main_frame_signin.pack(fill=X,)
                    elif selected_langs== "Dashboard":
                        try:
                            Sys_mains_frame_pr_ed.place_forget()
                        except:
                            pass
                        try:
                            
                            Sys_mains_frame_pr.place_forget()
                        except:
                            pass

                    else:
                        pass

                def profile():
                    # create a list box
                    langs = ("Dashboard","Profile","Log Out")

                    langs_var = StringVar(value=langs)
                    global lst_prf
                    lst_prf = Listbox(root,listvariable=langs_var,height=3 ,selectmode='extended',bg="black",fg="white")

                    lst_prf.place(relx=0.90, rely=0.10)
                    lst_prf.bind('<<ListboxSelect>>', lst_prf_slt)
                    srh_btn.grid_forget()
                    srh_btn2 = Button(tp_lb_npr, bg="White", fg="black",height=2,width=5,border=0,command=lst_frt)
                    srh_btn2.grid(row=2,column=2,padx=15)
            
                srh_btn = Button(tp_lb_npr, bg="White", fg="black",height=2,width=5,border=0,command=profile)
                srh_btn.grid(row=2,column=2,padx=15)

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
                    btn_nav2.place(relx=0, rely=0)
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
                    btn_nav3.place(relx=0.97, rely=0)

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
                btn_nav.place(relx=0.97, rely=0)
                tabControl.add(tab1,compound = LEFT, text ='Dashboard',)
                tabControl.add(tab2,compound = LEFT, text ='Banking')
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

            
                #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Dash Board}
                tab1.grid_columnconfigure(0,weight=1)
                tab1.grid_rowconfigure(0,weight=1)
                
                Sys_mains_frame=Frame(tab1,bg="#2f516f",)
                Sys_mains_frame.grid(row=0,column=0,sticky='nsew')
                
                def responsive_wid(event):
                    dwidth = event.width
                    dheight = event.height
                    dcanvas = event.widget
                
                    r1 = 25
                    x1 = dwidth/63
                    x2 = dwidth/1.021
                    y1 = dheight/13
                    y2 = dheight/6

                    dcanvas.coords("bg_polygen_dash",x1 + r1,y1,
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

                    r1 = 25
                    x1 = dwidth/63
                    x2 = dwidth/3.1
                    y1 = dheight/5
                    y2 = dheight/1.1

                    dcanvas.coords("bg_polygen_dash1",x1 + r1,y1,
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

                    r1 = 25
                    x1 = dwidth/2.95
                    x2 = dwidth/1.529
                    y1 = dheight/5
                    y2 = dheight/1.1

                    dcanvas.coords("bg_polygen_dash2",x1 + r1,y1,
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

                    r1 = 25
                    x1 = dwidth/1.49
                    x2 = dwidth/1.021
                    y1 = dheight/5
                    y2 = dheight/1.1

                    dcanvas.coords("bg_polygen_dash3",x1 + r1,y1,
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

                    r1 = 25
                    x1 = dwidth/63
                    x2 = dwidth/3.1
                    y1 = dheight/1.06
                    y2 = dheight/.59
                    
                    #-----------------------------------------second row
                    dcanvas.coords("bg_polygen_dash4",x1 + r1,y1,
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

                    r1 = 25
                    x1 = dwidth/2.95
                    x2 = dwidth/1.529
                    y1 = dheight/1.06
                    y2 = dheight/.59

                    dcanvas.coords("bg_polygen_dash5",x1 + r1,y1,
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

                    r1 = 25
                    x1 = dwidth/1.49
                    x2 = dwidth/1.021
                    y1 = dheight/1.06
                    y2 = dheight/.59

                    dcanvas.coords("bg_polygen_dash6",x1 + r1,y1,
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

                    dcanvas.coords("head_lb",dwidth/2,dheight/8.4)
                    dcanvas.coords("prf_lb",dwidth/53,dheight/4.7)
                    
                    dcanvas.coords("prf_hr",dwidth/53,dheight/3.7,dwidth/3.15,dheight/3.7)
                    dcanvas.coords("net_prf",dwidth/53,dheight/3.2)
                    dcanvas.coords("graph",dwidth/53,dheight/2.2)
                    #--------------------------------------------------------------second
                    dcanvas.coords("exp_hd_lb",dwidth/2.9,dheight/4.7)
                    dcanvas.coords("exp_hr",dwidth/2.9,dheight/3.7,dwidth/1.54,dheight/3.7)
                    dcanvas.coords("graph_2",dwidth/2.9,dheight/2.2)
                    
                    #-----------------------------------------------------------third
                    dcanvas.coords("bnk_lb",dwidth/1.48,dheight/4.7)
                    dcanvas.coords("bank_hr",dwidth/1.48,dheight/3.7,dwidth/1.03,dheight/3.7)
                    #--------------------------------------------------------------forth
                    dcanvas.coords("incom_lb",dwidth/53,dheight/1.04)
                    
                    dcanvas.coords("incom_hr",dwidth/53,dheight/0.99,dwidth/3.15,dheight/0.99)

                
                    dcanvas.coords("graph_4",dwidth/53,dheight/0.85)
            
                    #-------------------------------------------------------------fifth
                    dcanvas.coords("inv_lb",dwidth/2.9,dheight/1.04)
                    dcanvas.coords("invs_hr",dwidth/2.9,dheight/0.99,dwidth/1.54,dheight/0.99)
                    dcanvas.coords("inv_lb2",dwidth/2.9,dheight/0.95)
                    dcanvas.coords("inv_lb3",dwidth/2.9,dheight/0.90)
                    dcanvas.coords("graph_5",dwidth/2.9,dheight/0.85)
                    #-------------------------------------------------------------sixth
                    dcanvas.coords("sales_lb",dwidth/1.48,dheight/1.04)
                    dcanvas.coords("sales_hr",dwidth/1.48,dheight/0.99,dwidth/1.03,dheight/0.99)
                    
                    


                    dcanvas.coords("grapg_6",dwidth/1.48,dheight/0.85)
                        
                Sys_mains_frame.grid_rowconfigure(0,weight=1)
                Sys_mains_frame.grid_columnconfigure(0,weight=1)

                canvas = Canvas(Sys_mains_frame,height=700,bg='#2f516f',scrollregion=(0,0,700,1200))
                sr_Scroll = Scrollbar(Sys_mains_frame,orient=VERTICAL)
                sr_Scroll.grid(row=0,column=1,sticky='ns')
                sr_Scroll.config(command=canvas.yview)
                canvas.bind("<Configure>", responsive_wid)
                canvas.config(yscrollcommand=sr_Scroll.set)
                canvas.grid(row=0,column=0,sticky='nsew')
                

                cmp_name=Label(canvas, text="Clown",bg="#213b52", fg="White", anchor="center",font=('Calibri 24 bold'))
            
                win_inv1 = canvas.create_window(0, 0, anchor="center", window=cmp_name,tag=("head_lb"))
                
                rth2 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash"),smooth=True,)
                # #----------------------------------------------------------------------------------------------------------------grid 1
                rth1 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash1"),smooth=True,)

                prf_lb=Label(canvas, text="PROFIT AND LOSS",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                win_inv1 = canvas.create_window(0, 0, anchor="nw", window=prf_lb, tag=("prf_lb"))

                canvas.create_line(0, 0, 0, 0,fill="gray", tag=("prf_hr") )

                net_prf=Label(canvas, text="NET INCOME: ₹ 0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                win_inv1 = canvas.create_window(0, 0, anchor="nw", window=net_prf,tag=("net_prf"))

                figlast = plt.figure(figsize=(8, 4), dpi=50)

                x="Income"
                y=10 
                plt.barh(x,y, label="Undefined", color="blue") 
                plt.legend()
            
                plt.ylabel("")
                axes=plt.gca()
                axes.xaxis.grid()

                x="Expense"
                y=100
                plt.barh(x,y, color="red") 
                plt.legend()
            
                plt.ylabel("")
                axes=plt.gca()
                axes.xaxis.grid()
                        

                canvasbar = FigureCanvasTkAgg(figlast, master=canvas)
                canvasbar
                canvasbar.draw()
                canvasbar.get_tk_widget()
                win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph"))
                # #----------------------------------------------------------------------------------------------------------------grid 2
                rth2 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash2"),smooth=True,)

                exp_hd_lb=Label(canvas, text="EXPENSES: ₹ 0.0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                win_inv1 = canvas.create_window(0, 0, anchor="nw", window=exp_hd_lb, tag=("exp_hd_lb"))
                canvas.create_line(0, 0, 0, 0,fill="gray" ,tag=("exp_hr"))
                fig, ax = plt.subplots(figsize=(8, 4), dpi=50)

                size = 0.3
                vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

                cmap = plt.colormaps["tab20c"]
                outer_colors = cmap(np.arange(3)*4)
                # inner_colors = cmap([1, 2, 5, 6, 9, 10])

                ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
                    wedgeprops=dict(width=size, edgecolor='w'))

                # ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,
                #        wedgeprops=dict(width=size, edgecolor='w'))

                ax.set(aspect="equal", title='Pie plot with `ax.pie`')

                canvasbar = FigureCanvasTkAgg(fig, master=canvas)
                canvasbar
                canvasbar.draw()
                canvasbar.get_tk_widget()
                win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph_2"))

                # #----------------------------------------------------------------------------------------------------------------grid 3
                rth3 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash3"),smooth=True,)

                bnk_lb=Label(canvas, text="BANK ACCOUNTS",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                win_inv1 = canvas.create_window(0, 0, anchor="nw", window=bnk_lb,tag=("bnk_lb"))
                canvas.create_line(910, 195, 1290, 195,fill="gray",tag=("bank_hr"))
                # #----------------------------------------------------------------------------------------------------------------grid 4
                rth4 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash4"),smooth=True,)

                incom_lb=Label(canvas, text="INCOME: ₹ 0.0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                win_inv1 = canvas.create_window(0, 0, anchor="nw", window=incom_lb,tag=("incom_lb"))
                canvas.create_line(0, 0, 0, 0,fill="gray",tag=("incom_hr") )

                # Pie chart, where the slices will be ordered and plotted counter-clockwise:
                labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
                sizes = [15, 30, 45, 10]
                explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

                fig1, ax1 = plt.subplots(figsize=(8, 4), dpi=50)
                ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                        shadow=True, startangle=90)
                ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

                canvasbar = FigureCanvasTkAgg(fig1, master=canvas)
                canvasbar
                canvasbar.draw()
                canvasbar.get_tk_widget()
                win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph_4"))

                # #----------------------------------------------------------------------------------------------------------------grid 5
                rth5 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash5"),smooth=True,)
                inv_lb=Label(canvas, text="INVOICE",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                win_inv1 = canvas.create_window(0, 0, anchor="nw", window=inv_lb, tag=("inv_lb"))

                canvas.create_line(0, 0, 0, 0,fill="gray", tag=("invs_hr") )
                inv_lb2=Label(canvas, text="UNPAID:₹ 0.0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                win_inv1 = canvas.create_window(0, 0, anchor="nw", window=inv_lb2, tag=("inv_lb2"))
                inv_lb3=Label(canvas, text="PAID:₹ 0.0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                win_inv1 = canvas.create_window(0,0 , anchor="nw", window=inv_lb3, tag=("inv_lb3"))

                figlast = plt.figure(figsize=(8, 4), dpi=50)

                x="Unpaid"
                y=10 
                plt.barh(x,y, label="Undefined", color="blue") 
                plt.legend()
            
                plt.ylabel("")
                axes=plt.gca()
                axes.xaxis.grid()

                x="Paid"
                y=100
                plt.barh(x,y, color="red") 
                plt.legend()
            
                plt.ylabel("")
                axes=plt.gca()
                axes.xaxis.grid()
                        

                canvasbar = FigureCanvasTkAgg(figlast, master=canvas)
                canvasbar
                canvasbar.draw()
                canvasbar.get_tk_widget()
                win_inv1 = canvas.create_window(480, 780, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph_5"))
                #----------------------------------------------------------------------------------------------------------------grid 6
                rth6 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash6"),smooth=True,)
                sales_lb=Label(canvas, text="SALES $0.0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                win_inv1 = canvas.create_window(0, 0, anchor="nw", window=sales_lb, tag=("sales_lb"))

                canvas.create_line(0, 0, 0, 0,fill="gray", tag=("sales_hr") )
                
                
                fig, ax = plt.subplots(figsize=(8, 4), dpi=50)
                ax.plot(range(10))
                ax.set_yticks([2, 5, 7], labels=['really, really, really', 'long', 'labels'])
            

                canvasbar = FigureCanvasTkAgg(fig, master=canvas)
                canvasbar
                canvasbar.draw()
                canvasbar.get_tk_widget()
                win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("grapg_6"))
                
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
                    dcanvas.coords("combo2",dwidth/1.12,dheight/2.261)

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

                        r2 = 25
                        x11 = dwidth/63
                        x21 = dwidth/1.021
                        y11 = dheight/2.8
                        y21 = dheight/0.58


                        dcanvas.coords("poly5",x11 + r2,y11,
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
                            dcanvas.coords("label13",dwidth/9.8,dheight/0.94)
                            dcanvas.coords("label14",dwidth/3.7,dheight/0.94)
                            dcanvas.coords("label15",dwidth/2.12,dheight/0.94)
                            dcanvas.coords("label16",dwidth/1.56,dheight/0.94)
                            dcanvas.coords("label17",dwidth/1.245,dheight/0.94)
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
                            dcanvas.coords("entry8",dwidth/7.13,dheight/0.9)
                            dcanvas.coords("entry9",dwidth/3.15,dheight/0.9)
                            dcanvas.coords("entry10",dwidth/2.015,dheight/0.9)
                            dcanvas.coords("entry11",dwidth/1.48,dheight/0.9)
                            dcanvas.coords("entry12",dwidth/1.175,dheight/0.9)

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

                        dcanvas.coords("tree1",dwidth/15,dheight/0.79)
                        dcanvas.coords("combo13",dwidth/1.13,dheight/0.82)

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

                        cust_sql = "SELECT firstname,lastname FROM app1_customer"
                        fbcursor.execute(cust_sql,)
                        cust_data = fbcursor.fetchall()

                        cust_list = []
                        if not cust_data:
                            cust_list.append('Select Customer')
                        else:
                            for c in cust_data:
                                cust_list.append(c[0] + " " + c[1])
                            cust_list.insert(0,'Select Customer')

                        def fetch_custDetails(event):
                            cust_name = rp_custCombo.get()
                            cust_fname = cust_name.split(" ")[0]
                            cust_lname = cust_name.split(" ")[1]

                            user_sql = "SELECT id FROM auth_user WHERE username=%s"
                            user_val = (nm_ent.get(),)
                            fbcursor.execute(user_sql,user_val)
                            user_data = fbcursor.fetchone()

                            comp_sql = 'SELECT cid FROM app1_company WHERE id_id=%s'
                            comp_val = (user_data[0],)
                            fbcursor.execute(comp_sql,comp_val)
                            comp_data = fbcursor.fetchone()

                            cust_sql = "SELECT email FROM app1_customer WHERE firstname=%s and lastname=%s and cid_id=%s"
                            cust_val = (cust_fname,cust_lname,comp_data[0])
                            fbcursor.execute(cust_sql,cust_val)
                            cust_data = fbcursor.fetchone()

                            inv_sql = "SELECT * FROM app1_invoice WHERE customername=%s and cid_id=%s"
                            inv_val = (cust_name,comp_data[0])
                            fbcursor.execute(inv_sql,inv_val)
                            inv_data = fbcursor.fetchall()

                            if not cust_data:
                                pass
                            else:
                                rp_email.delete(0,END)
                                rp_email.insert(0,cust_data[0])

                            if not inv_data:
                                pass
                            else:
                                count = 1
                                for i in inv_data:
                                    rp_tree.insert(parent='',index='end',iid=i,text=count,values=(str(i[3]) + " " + i[5],i[6],i[17],i[41],0))
                                    count += 1

                        rp_custCombo = ttk.Combobox(sr_Canvas_1,width=15,font=('arial 15'))
                        rp_custCombo['values'] = cust_list
                        rp_custCombo.current(0)
                        rp_custCombo.bind("<<ComboboxSelected>>",fetch_custDetails)
                        sr_Canvas_1.create_window(0,0,anchor='nw',window=rp_custCombo,tags=("combo1"))

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
                            cust_title['values'] = ['Mr','Mrs','Miss','Ms',]
                            cust_title.current(0)
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

                            def select_GSTtype(event):
                                if cust_gtype.get() == 'GST unregistered' or cust_gtype.get() == 'Consumer' or cust_gtype.get() == 'Overseas':
                                    sr_Canvas_2.itemconfig("label9",state='hidden')
                                    sr_Canvas_2.itemconfig("entry6",state='hidden')
                                else:
                                    sr_Canvas_2.itemconfig("label9",state='normal')
                                    sr_Canvas_2.itemconfig("entry6",state='normal')

                            cust_gtype = ttk.Combobox(sr_Canvas_2,width=19,font=('arial 15'))
                            cust_gtype['values'] = ['Choose...','GST registered- Regular','GST registered- Composition','GST unregistered','Consumer','Overseas','SEZ',"Deemed exports - EOU's STP's EHTP's etc"]
                            cust_gtype.current(0)
                            cust_gtype.bind("<<ComboboxSelected>>",select_GSTtype)
                            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_gtype,tags=("combo2"))

                            cust_label9 = Label(sr_Canvas_2,width=20,height=1,text="GSTIN",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                            sr_Canvas_2.create_window(0,0,window=cust_label9,tags=('label9'))

                            gstinVar = StringVar()
                            cust_gin = Entry(sr_Canvas_2,textvariable=gstinVar,width=20,font=('arial 15'),background='#2f516f',foreground='grey')
                            cust_gin.insert(0,'29APPCK7465F1Z1')

                            def del_placeholder(event):
                                if cust_gin.get() == '29APPCK7465F1Z1':
                                    cust_gin.delete(0,END)
                                    cust_gin.config(fg="white")
                                else:
                                    pass

                            cust_gin.bind("<FocusIn>",del_placeholder)

                            def ret_placeholder(event):
                                if cust_gin.get() == '':
                                    cust_gin.insert(0,'29APPCK7465F1Z1')
                                    cust_gin.config(fg="grey")
                                else:
                                    pass
                            cust_gin.bind("<FocusOut>",ret_placeholder)
                            
                            def validate_gstin(value):
                                pattern = r'[0-9]{2}[a-zA-Z]{5}[0-9]{4}[a-zA-Z]{1}[1-9A-Za-z]{1}[a-zA-Z]{1}[0-9a-zA-Z]{1}'
                                if re.fullmatch(pattern,value) is None:
                                    return False
                                else:
                                    cust_gin.config(fg="white")
                                    return True

                            def invalid_gstin():
                                messagebox.showinfo("Fin sYs","Please provide a valid GST number")
                                cust_gin.config(fg="red")

                            valid_cmndGSTIN = (sr_Canvas_2.register(validate_gstin),'%P')
                            invalid_cmndGSTIN = (sr_Canvas_2.register(invalid_gstin),)
                            cust_gin.config(validate='focusout',validatecommand=valid_cmndGSTIN,invalidcommand=invalid_cmndGSTIN)
                            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_gin,tags=("entry6"))

                            cust_label10 = Label(sr_Canvas_2,width=20,height=1,text="PAN NO",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                            sr_Canvas_2.create_window(0,0,window=cust_label10,tags=('label10'))

                            panVar = StringVar()
                            cust_pan = Entry(sr_Canvas_2,width=20,textvariable=panVar,font=('arial 15'),background='#2f516f',foreground='grey')
                            cust_pan.insert(0,'APPCK7465F')

                            def del_placeholder(event):
                                if cust_pan.get() == 'APPCK7465F':
                                    cust_pan.delete(0,END)
                                    cust_pan.config(fg="white")
                                else:
                                    pass

                            cust_pan.bind("<FocusIn>",del_placeholder)

                            def ret_placeholder(event):
                                if cust_pan.get() == '':
                                    cust_pan.insert(0,'APPCK7465F')
                                    cust_pan.config(fg="grey")
                                else:
                                    pass
                            cust_pan.bind("<FocusOut>",ret_placeholder)

                            def validate_pan(value):
                                pattern = r'[a-zA-Z]{5}[0-9]{4}[a-zA-Z]{1}'
                                if re.fullmatch(pattern,value) is None:
                                    return False
                                else:
                                    cust_pan.config(fg="white")
                                    return True

                            def invalid_pan():
                                messagebox.showinfo("Fin sYs","Please provide a valid PAN number") 
                                cust_pan.config(fg="red")

                            valid_cmndPAN = (sr_Canvas_2.register(validate_pan),'%P')
                            invalid_cmndPAN = (sr_Canvas_2.register(invalid_pan),)
                            cust_pan.config(validate='focusout',validatecommand=valid_cmndPAN,invalidcommand=invalid_cmndPAN)
                            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_pan,tags=("entry7"))

                            cust_label11 = Label(sr_Canvas_2,width=20,height=1,text="Email",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                            sr_Canvas_2.create_window(0,0,window=cust_label11,tags=('label11'))

                            emailVar = StringVar()
                            cust_email = Entry(sr_Canvas_2,textvariable=emailVar,width=20,font=('arial 15'),background='#2f516f',foreground='white')

                            def validate_email(value):
                                pattern = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
                                if re.fullmatch(pattern,value) is None:
                                    return False
                                else:
                                    cust_email.config(fg="white")
                                    return True

                            def invalid_email():
                                messagebox.showinfo("Fin sYs","Please provide a valid Email address")
                                cust_email.config(fg="red")

                            valid_cmndEMAIL = (sr_Canvas_2.register(validate_email),'%P')
                            invalid_cmndEMAIL = (sr_Canvas_2.register(invalid_email),)
                            cust_email.config(validate='focusout',validatecommand=valid_cmndEMAIL,invalidcommand=invalid_cmndEMAIL)
                            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_email,tags=("entry8"))

                            cust_label12 = Label(sr_Canvas_2,width=20,height=1,text="Website",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                            sr_Canvas_2.create_window(0,0,window=cust_label12,tags=('label12'))

                            webVar = StringVar()
                            cust_web = Entry(sr_Canvas_2,textvariable=webVar,width=20,font=('arial 15'),background='#2f516f',foreground='white')

                            def validate_web(value):
                                pattern = r'www.+[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
                                if re.fullmatch(pattern,value) is None:
                                    return False
                                else:
                                    cust_web.config(fg="white")
                                    return True

                            def invalid_web():
                                messagebox.showinfo("Fin sYs","Please provide a valid Website address")
                                cust_web.config(fg="red")

                            valid_cmndWEB = (sr_Canvas_2.register(validate_web),'%P')
                            invalid_cmndWEB = (sr_Canvas_2.register(invalid_web),)
                            cust_web.config(validate='focusout',validatecommand=valid_cmndWEB,invalidcommand=invalid_cmndWEB)
                            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_web,tags=("entry9"))

                            cust_label13 = Label(sr_Canvas_2,width=20,height=1,text="Mobile",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                            sr_Canvas_2.create_window(0,0,window=cust_label13,tags=('label13'))

                            mobVar = StringVar()
                            cust_mob = Entry(sr_Canvas_2,textvariable=mobVar,width=20,font=('arial 15'),background='#2f516f',foreground='white')

                            def validate_mobile(value):
                                pattern = r'[7-9][0-9]{9}'
                                if re.fullmatch(pattern,value) is None:
                                    return False
                                else:
                                    cust_mob.config(fg="white")
                                    return True

                            def invalid_mobile():
                                messagebox.showinfo("Fin sYs","Please provide a valid Phone number")
                                cust_mob.config(fg="red")

                            valid_cmndMOB = (sr_Canvas_2.register(validate_mobile),'%P')
                            invalid_cmndMOB = (sr_Canvas_2.register(invalid_mobile),)
                            cust_mob.config(validate='focusout',validatecommand=valid_cmndMOB,invalidcommand=invalid_cmndMOB)
                            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_mob,tags=("entry10"))

                            cust_label14 = Label(sr_Canvas_2,width=20,height=1,text="Billing Address",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
                            sr_Canvas_2.create_window(0,0,window=cust_label14,tags=('label14'))

                            cust_label15 = Label(sr_Canvas_2,width=20,height=1,text="Street",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                            sr_Canvas_2.create_window(0,0,window=cust_label15,tags=('label15'))

                            cust_st1 = scrolledtext.ScrolledText(sr_Canvas_2,width=48,height=3,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_st1,tags=("entry11"))

                            cust_label17 = Label(sr_Canvas_2,width=20,height=1,text="Shipping Address",font=('arial 18 bold'),background='#1b3857',anchor="w",fg="white")
                            sr_Canvas_2.create_window(0,0,window=cust_label17,tags=('label17'))

                            cust_label16 = Label(sr_Canvas_2,width=20,height=1,text="Street",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                            sr_Canvas_2.create_window(0,0,window=cust_label16,tags=('label16'))

                            cust_st2 = scrolledtext.ScrolledText(sr_Canvas_2,width=48,height=3,font=('arial 15'),background='#2f516f',foreground='white')
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
                            cust_label22 = Label(sr_Canvas_2,width=20,height=1,text="Pin Code",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
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

                            def sameas_billaddress():
                                if sameasVar.get() == True:
                                    bill_address = cust_st1.get("1.0","end-1c")
                                    bill_city = cust_city.get()
                                    bill_state = cust_state.get()
                                    bill_pin = cust_pin.get()
                                    bill_country = cust_country.get()

                                    cust_st2.delete("1.0","end-1c")
                                    cust_st2.insert("1.0",bill_address)
                                    cust_city1.delete(0,END)
                                    cust_city1.insert(0,bill_city)
                                    cust_state1.delete(0,END)
                                    cust_state1.insert(0,bill_state)
                                    cust_pin1.delete(0,END)
                                    cust_pin1.insert(0,bill_pin)
                                    cust_country1.delete(0,END)
                                    cust_country1.insert(0,bill_country)
                                else:
                                    pass

                            sameasVar = BooleanVar()
                            cust_sameb = Checkbutton(sr_Canvas_2,variable=sameasVar,onvalue=1,offvalue=0,background='#1b3857',activebackground="#1b3857",command=sameas_billaddress)
                            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_sameb,tags=("check1"))

                            cust_label26 = Label(sr_Canvas_2,width=20,height=1,text="Same as billing address",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                            sr_Canvas_2.create_window(0,0,window=cust_label26,tags=('label26'))

                            termVar = BooleanVar()
                            cust_term = Checkbutton(sr_Canvas_2,variable=termVar,onvalue=1,offvalue=0,background='#1b3857',activebackground="#1b3857")
                            sr_Canvas_2.create_window(0,0,anchor='nw',window=cust_term,tags=("check2"))

                            cust_label27 = Label(sr_Canvas_2,width=25,height=1,text="Agree to terms and conditions",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                            sr_Canvas_2.create_window(0,0,window=cust_label27,tags=('label27'))

                            def sr_create_newCustomer():
                                title = cust_title.get()
                                firstname = cust_fname.get()
                                lastname = cust_lname.get()
                                company = cust_company.get()
                                location = cust_location.get()
                                gsttype = cust_gtype.get()
                                gstin = gstinVar.get()
                                panno = panVar.get()
                                email = emailVar.get()
                                website = webVar.get()
                                mobile = mobVar.get()
                                street = cust_st1.get("1.0","end-1c")
                                city = cust_city.get()
                                state = cust_state.get()
                                pincode = cust_pin.get()
                                country = cust_country.get()
                                shipstreet = cust_st2.get("1.0","end-1c")
                                shipcity = cust_city1.get()
                                shipstate = cust_state1.get()
                                shippincode = cust_pin1.get()
                                shipcountry = cust_country1.get()

                                
                                user_sql = "SELECT id FROM auth_user WHERE username=%s"
                                user_val = (nm_ent.get(),)
                                fbcursor.execute(user_sql,user_val)
                                user_data = fbcursor.fetchone()

                                comp_sql = 'SELECT cid FROM app1_company WHERE id_id=%s'
                                comp_val = (user_data[0],)
                                fbcursor.execute(comp_sql,comp_val)
                                comp_data = fbcursor.fetchone()
                                cid  = comp_data[0]

                                
                                
                                if gsttype == "GST unregistered" or gsttype == "Consumer" or gsttype == "Overseas":
                                    gstin = ''
                                    if validate_pan(panno) is False:
                                        pass 
                                    elif validate_email(email) is False: 
                                        pass
                                    elif validate_web(website) is False:
                                        pass 
                                    elif validate_mobile(mobile) is False:
                                        pass
                                    else:
                                        if termVar.get() == False:
                                            messagebox.showinfo("Fin sYs","You must agree before submitting")
                                        else:
                                            ins_cust_sql = "INSERT INTO app1_customer(title,firstname,lastname,company,location,gsttype,gstin,panno,email,website,mobile,street,city,state,pincode,country,shipstreet,shipcity,shipstate,shippincode,shipcountry,cid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
                                            ins_cust_val = (title,firstname,lastname,company,location,gsttype,gstin,panno,email,website,mobile,street,city,state,pincode,country,shipstreet,shipcity,shipstate,shippincode,shipcountry,cid,)
                                            fbcursor.execute(ins_cust_sql,ins_cust_val)
                                            finsysdb.commit()
                                            sr_Frame_2.destroy()
                                            cust_sql = "SELECT firstname,lastname FROM app1_customer"
                                            fbcursor.execute(cust_sql,)
                                            cust_data = fbcursor.fetchall()

                                            cust_list = []
                                            if not cust_data:
                                                cust_list.append('Select Customer')
                                            else:
                                                for c in cust_data:
                                                    cust_list.append(c[0] + " " + c[1])
                                                cust_list.insert(0,'Select Customer')
                                                rp_custCombo["values"] = cust_list
                                            sr_Frame_1.grid(row=0,column=0,sticky='nsew')
                                elif gstin == '29APPCK7465F1Z1' or panno == 'APPCK7465F':
                                    messagebox.showinfo("Fin sYs","Please provide valid inputs")
                                else:
                                    if validate_gstin(gstin) is False: 
                                        pass
                                    elif validate_pan(panno) is False:
                                        pass 
                                    elif validate_email(email) is False: 
                                        pass
                                    elif validate_web(website) is False:
                                        pass
                                    elif validate_mobile(mobile) is False:
                                        pass
                                    else:
                                        if termVar.get() == False:
                                            messagebox.showinfo("Fin sYs","You must agree before submitting")
                                        else:
                                            ins_cust_sql = "INSERT INTO app1_customer(title,firstname,lastname,company,location,gsttype,gstin,panno,email,website,mobile,street,city,state,pincode,country,shipstreet,shipcity,shipstate,shippincode,shipcountry,cid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
                                            ins_cust_val = (title,firstname,lastname,company,location,gsttype,gstin,panno,email,website,mobile,street,city,state,pincode,country,shipstreet,shipcity,shipstate,shippincode,shipcountry,cid,)
                                            fbcursor.execute(ins_cust_sql,ins_cust_val)
                                            finsysdb.commit()
                                            sr_Frame_2.destroy()
                                            cust_sql = "SELECT firstname,lastname FROM app1_customer"
                                            fbcursor.execute(cust_sql,)
                                            cust_data = fbcursor.fetchall()

                                            cust_list = []
                                            if not cust_data:
                                                cust_list.append('Select Customer')
                                            else:
                                                for c in cust_data:
                                                    cust_list.append(c[0] + " " + c[1])
                                                cust_list.insert(0,'Select Customer')
                                                rp_custCombo["values"] = cust_list
                                            sr_Frame_1.grid(row=0,column=0,sticky='nsew')
                            
                            cust_save = Button(sr_Canvas_2,text="Submit Form",font=('arial 12 bold'),width=40,height=2,background="#198fed",activebackground="#198fed",foreground="white",activeforeground="white",bd=0,command=lambda:sr_create_newCustomer())
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

                        def show_pmethod(event):
                            if rp_pmethod.get() == "Add new":
                                rp_newmeth.delete(0,END)
                                sr_Canvas_1.itemconfig("entry7",state='normal')
                            else:
                                sr_Canvas_1.itemconfig("entry7",state='hidden')

                        rp_pmethod = ttk.Combobox(sr_Canvas_1,font=('arial 15'),width=19,background='#2f516f')
                        pmethod_list = ['Add new',]
                        rp_pmethod['values'] = pmethod_list
                        rp_pmethod.current(0)
                        rp_pmethod.bind("<<ComboboxSelected>>",show_pmethod)
                        sr_Canvas_1.create_window(0,0,anchor='nw',window=rp_pmethod,tags=("entry3"))

                        def addnew_pmethod(event):
                            pmethod_list.insert(0,rp_newmeth.get())

                            rp_pmethod["values"] = pmethod_list

                        rp_newmeth = Entry(sr_Canvas_1,font=('arial 15'),width=20,background='#2f516f',foreground='white')
                        rp_newmeth.bind("<FocusOut>",addnew_pmethod)
                        sr_Canvas_1.create_window(0,0,anchor='nw',state=HIDDEN,window=rp_newmeth,tags=("entry7"))

                        rp_label7 = Label(sr_Canvas_1,width=20,height=1,text="Deposit to",font=('arial 12'),background='#1b3857',fg="white",anchor="nw")
                        sr_Canvas_1.create_window(0,0,window=rp_label7,tags=("label8"))

                        rp_depositto = ttk.Combobox(sr_Canvas_1,font=('arial 15'),width=15)
                        dep_list = ['Deferred CGST','Deferred GST Input Credit','Deferred IGST',
                        'Deferred Krishi Kalyan Cess Input Credit','Deferred SGST','Deferred Service Tax Input Credit',
                        'Deferred VAT Input Credit','GST Refund','Inventory Asset','Krishi Kalyan Cess Refund'
                        ,'Prepaid Insurance','Service Tax Refund','TDS Receivable','Uncategorised Asset','Undeposited Fund',]

                        user_sql = "SELECT id FROM auth_user WHERE username=%s"
                        user_val = (nm_ent.get(),)
                        fbcursor.execute(user_sql,user_val)
                        user_data = fbcursor.fetchone()

                        comp_sql = 'SELECT cid FROM app1_company WHERE id_id=%s'
                        comp_val = (user_data[0],)
                        fbcursor.execute(comp_sql,comp_val)
                        comp_data = fbcursor.fetchone()

                        dep_sql = "SELECT name FROM app1_accounts WHERE cid_id=%s"
                        dep_val = (comp_data[0],)
                        fbcursor.execute(dep_sql,dep_val)
                        dep_data = fbcursor.fetchall()

                        for d in dep_data:
                            dep_list.insert(0,d)
                        rp_depositto['values'] = dep_list
                        rp_depositto.current(0)
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

                            def fetch_detailType(event):
                                if dep_acctype.get() == "Bank":
                                    item_sql = "SELECT * FROM itemstable WHERE Pid=%s"
                                    item_val = (3,)
                                    fbcursor.execute(item_sql,item_val)
                                    item_data = fbcursor.fetchall()

                                    item_list = []
                                    for i in item_data:
                                        item_list.append(i[1])
                                    dep_dtype.configure(values=item_list)
                                else:
                                    item_sql = "SELECT * FROM itemstable WHERE Pid=%s"
                                    item_val = (2,)
                                    fbcursor.execute(item_sql,item_val)
                                    item_data = fbcursor.fetchall()

                                    item_list = []
                                    for i in item_data:
                                        item_list.append(i[1])
                                    dep_dtype.configure(values=item_list)

                            dep_acctype = ttk.Combobox(sr_Canvas_3,width=46,font=('arial 15'),background='#2f516f',foreground='black')
                            dep_acctype['values'] = ['Bank','Current Assets',]
                            dep_acctype.bind("<<ComboboxSelected>>",fetch_detailType)
                            sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_acctype,tags=("entry1"))

                            dep_label3 = Label(sr_Canvas_3,width=20,height=1,text="*Name",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
                            sr_Canvas_3.create_window(0,0,window=dep_label3,tags=("label3"))

                            dep_name = Entry(sr_Canvas_3,width=47,font=('arial 15'),background='#2f516f',foreground='white')
                            sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_name,tags=("entry2"))

                            dep_label4 = Label(sr_Canvas_3,width=20,height=1,text="*Detail Type",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
                            sr_Canvas_3.create_window(0,0,window=dep_label4,tags=("label4"))

                            dep_dtype = ttk.Combobox(sr_Canvas_3,width=46,font=('arial 15'),background='#2f516f',foreground='black')
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

                            dep_subacc = ttk.Combobox(sr_Canvas_3,width=46,font=('arial 15'),background='#2f516f',foreground='black',state=DISABLED)
                            dep_subacc['values'] = ['Deferred CGST','Deferred GST Input Credit','Deferred IGST',
                            'Deferred Krishi Kalyan Cess Input Credit','Deferred Service Tax Input Credit',
                            'Deferred SGST','Deferred VAT Input Credit','GST Refund','Inventory Asset','Paid Insurance',
                            'Service Tax Refund','TDS Receivable','Uncategorised Asset','Accumulated Depreciation',
                            'Buildings and Improvements','Furniture and Equipment','Land','Leasehold Improvements',
                            'CGST Payable','CST Payable','CST Suspense','GST Payable','GST Suspense','IGST Payable',
                            'Input CGST','Input CGST Tax RCM','Input IGST','Input IGST Tax RCM','Input Krishi Kalyan Cess',
                            'Input Krishi Kalyan Cess RCM','Input Service Tax','Input Service Tax RCM','Input SGST',
                            'Input SGST Tax RCM','Input VAT 14%','Input VAT 4%','Input VAT 5%','Krishi Kalyan Cess Payable',
                            'Krishi Kalyan Cess Suspense','Output CGST','Output CGST Tax RCM','Output CST 2%','Output IGST',
                            'Output IGST Tax RCM','Output Krishi Kalyan Cess','Output Krishi Kalyan Cess RCM','Output Service Tax',
                            'Output Service Tax RCM','Output SGST','Output SGST Tax RCM','Output VAT 14%','Output VAT 4%',
                            'Output VAT 5%','Service Tax Payable','Service Tax Suspense','SGST Payable','SGST Suspense',
                            'Swachh Bharat Cess Payable','Swachh Bharat Cess Suspense','TDS Payable','VAT Payable',
                            'VAT Suspense','Opening Balance','Equity',]
                            sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_subacc,tags=("entry6"))

                            dep_label7 = Label(sr_Canvas_3,width=20,height=1,text="Default Tax Code",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
                            sr_Canvas_3.create_window(0,0,window=dep_label7,tags=("label7"))

                            dep_dtaxcode = ttk.Combobox(sr_Canvas_3,width=46,font=('arial 15'),background='#2f516f',foreground='black')
                            dep_dtaxcode['values'] = ['18.0% IGST','14.00% ST','0% IGST','Out of Scope','0% GST','14.5% ST',
                            '14.0% VAT','6.0% IGST','28.0% IGST','15.0% ST','28.0% GST','12.0% GST','18.0% GST','3.0% GST',
                            '0.2% IGST','5.0% GST','6.0% GST','0.2% GST','Exempt IGST','3.0% IGS','4.0% VAT','5.0% IGST',
                            '12.36% ST','5.0% VAT','Exempt GST','12.0% IGST','2.0% CST',]
                            sr_Canvas_3.create_window(0,0,anchor='nw',window=dep_dtaxcode,tags=("entry7"))

                            def payment_createAccType():
                                acctype = dep_acctype.get()
                                detype = dep_dtype.get()
                                name = dep_name.get()
                                description = dep_desp.get()
                                gst = dep_subacc.get()
                                deftaxcode = dep_dtaxcode.get()
                                balance = 0
                                today = datetime.today()
                                asof = today.strftime("%Y-%m-%d")
                                balfordisp = 0
                               # ----company id
                                user_sql = "SELECT id FROM auth_user WHERE username=%s"
                                user_val = (nm_ent.get(),)
                                fbcursor.execute(user_sql,user_val)
                                user_data = fbcursor.fetchone()

                                comp_sql = 'SELECT cid FROM app1_company WHERE id_id=%s'
                                comp_val = (user_data[0],)
                                fbcursor.execute(comp_sql,comp_val)
                                comp_data = fbcursor.fetchone()
                                cid  = comp_data[0]
                                #----------------

                                #product id --------------
                                if acctype == "Bank":
                                    pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                    pro_val = (3,)
                                    fbcursor.execute(pro_sql,pro_val)
                                    product_data = fbcursor.fetchone()
                                else:
                                    product_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                    product_val = (2,)
                                    fbcursor.execute(product_sql,product_val)
                                    product_data = fbcursor.fetchone()
                                
                                productid = product_data[0]
                                #-----------------

                                acctype_sql = "SELECT accountname FROM app1_accountype WHERE accountname=%s"
                                acctype_val = (dep_dtype.get(),)
                                fbcursor.execute(acctype_sql,acctype_val)
                                acctype_data = fbcursor.fetchone()

                                acct_sql = "SELECT name,cid_id FROM app1_accounts WHERE name=%s AND cid_id=%s"
                                acct_val = (dep_name.get(),comp_data[0])
                                fbcursor.execute(acct_sql,acct_val)
                                acct_data = fbcursor.fetchone()

                                acct1_sql = "SELECT name,cid_id FROM app1_accounts1 WHERE name=%s AND cid_id=%s"
                                acct1_val = (dep_name.get(),comp_data[0])
                                fbcursor.execute(acct1_sql,acct1_val)
                                acct1_data = fbcursor.fetchone()
                                

                                if not acctype_data and not acct_data or not acct1_data:
                                    ins_acctype_sql = "INSERT INTO app1_accountype(cid_id,accountname,accountbal) VALUES(%s,%s,%s)"
                                    ins_acctype_val= (comp_data[0],detype,balance)
                                    fbcursor.execute(ins_acctype_sql,ins_acctype_val)
                                    finsysdb.commit()
                                    
                                    if acctype == "Bank":
                                        #pro id ------------
                                        pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                        pro_val = (3,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        pro_data = fbcursor.fetchone()
                                        #--------------------
                                        ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                        ins_accts_val = (3,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                        fbcursor.execute(ins_accts_sql,ins_accts_val)
                                        finsysdb.commit()
                                    else:
                                        #pro id ------------
                                        pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                        pro_val = (2,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        pro_data = fbcursor.fetchone()
                                        #--------------------

                                        ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                        ins_accts_val = (2,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                        fbcursor.execute(ins_accts_sql,ins_accts_val)
                                        finsysdb.commit()

                                    sel_accts1_sql = "SELECT * FROM app1_accounts1 WHERE cid_id=%s and name=%s"
                                    sel_accts1_val = (cid,'Opening Balance Equity',)
                                    fbcursor.execute(sel_accts1_sql,sel_accts1_val)
                                    sel_accts1_data = fbcursor.fetchone()

                                    bal = sel_accts1_data[7] + float(balance)
                                    upd_accts1_sql = "UPDATE app1_accounts1 SET balance=%s WHERE cid_id=%s and name=%s"
                                    upd_accts1_val = (bal,cid,'Opening Balance Equity',)
                                    fbcursor.execute(upd_accts1_sql,upd_accts1_val)
                                    finsysdb.commit()

                                    sr_Frame_3.destroy()
                                    sr_Frame_1.grid(row=0,column=0,sticky='nsew')

                                    deposit_sql = "SELECT name FROM app1_accounts WHERE cid_id=%s ORDER BY accountsid DESC LIMIT 1;"
                                    deposit_val = (comp_data[0],)
                                    fbcursor.execute(deposit_sql,deposit_val)
                                    deposit_data = fbcursor.fetchall()

                                    dep_list.insert(0,deposit_data)
                                    rp_depositto.config(values=dep_list)
                                    rp_depositto.current(0)
                                else:
                                    messagebox.showwarning("Fin sYs",f"Account with name {name} already exists. Please provide another name.")




                            dep_save = Button(sr_Canvas_3,text="Create",font=('arial 12 bold'),width=35,height=2,background="#198fed",activebackground="#198fed",foreground="white",activeforeground="white",bd=0,command=lambda:payment_createAccType())
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

                        def amount_receiving(event):
                            # try:
                            ramount = rp_amntre.get()
                            if ramount.isdigit():
                                if rp_tree.get_children() == '':
                                    pass
                                else:
                                    tree_list = []
                                    cash = float(ramount)
                                    for child in rp_tree.get_children():
                                        row = rp_tree.item(child,'values')
                                        if cash < float(row[3]):
                                            tree_list.append((row[0],row[1],row[2],row[3],cash))
                                            print(cash,float(row[3]))
                                            cash = float(row[3]) - cash
                                            print(cash)
                                        elif cash >= float(row[3]):
                                            tree_list.append((row[0],row[1],row[2],row[3],row[3]))
                                            cash -= (cash - float(row[3]))
                                        else:
                                            pass
                                    print(cash)

                                        # rp_tree.focus(child_id)
                                        # rp_tree.selection_set(child_id)
                                        # selected_row = rp_tree.selection()[0]
                                        # pay_indices = rp_tree.item(selected_row,'values')
                                        # rp_tree.item(selected_row,values=pay_indices)


                                        # payment = float(ramount) - float(pay_indices[])
                                        # if float(ramount) < float(child[3]):
                                        #     rp_tree.set(selected_row,"#5",ramount)
                                        # elif float(ramount) >= float(pay_indices[3]):
                                        #     rp_tree.set(selected_row,"#5",pay_indices[3])
                                        #     index = [rp_tree.index(id) for id in rp_tree.selection()]
                                        #     index[0] += 1
                                        # else:
                                        #     pass
                                        # rp_label10.config(text=str(ramount))
                            else:
                                rp_amntre.delete(0,END)
                                if ramount == '':
                                    rp_label10.config(text='0.00')
                                else:
                                    pass
                            # except:
                            #     pass

                        rp_amntre = Entry(sr_Canvas_1,font=('arial 15'),width=20,background='#2f516f',foreground='white')
                        rp_amntre.bind("<FocusOut>",amount_receiving)
                        sr_Canvas_1.create_window(0,0,anchor='nw',window=rp_amntre,tags=("entry4"))

                        rp_label9 = Label(sr_Canvas_1,width=20,height=1,text="AMOUNT RECIEVED",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
                        sr_Canvas_1.create_window(0,0,window=rp_label9,tags=("label10"))

                        rp_label10 = Label(sr_Canvas_1,width=20,height=1,text="0.00",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
                        sr_Canvas_1.create_window(0,0,window=rp_label10,tags=("label11"))

                        # sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("line1"))
                        # sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("line2"))
                        # sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("line3"))
                        # sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("line4"))
                        # sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("line5"))
                        # sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("line6"))
                        # sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("line7"))
                        # sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("line8"))
                        # sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("line9"))
                        # sr_Canvas_1.create_line(0,0,0,0,fill='gray',width=1,tags=("line16"))

                        # rpt_label1 = Label(sr_Canvas_1,width=5,height=1,text="#", font=('arial 10 bold'),background='#1b3857',fg="white") 
                        # sr_Canvas_1.create_window(0, 0, anchor="c", window=rpt_label1,tags=("label12"))

                        rpt_label2 = Label(sr_Canvas_1,width=15,height=1,text="DESCRIPTION", font=('arial 10 bold'),background='#1b3857',fg="white") 
                        sr_Canvas_1.create_window(0, 0, anchor="c",state=HIDDEN, window=rpt_label2,tags=("label13"))

                        rpt_label3 = Label(sr_Canvas_1,width=15,height=1,text="DUE DATE", font=('arial 10 bold'),background='#1b3857',fg="white") 
                        sr_Canvas_1.create_window(0, 0, anchor="c",state=HIDDEN, window=rpt_label3,tags=("label14"))

                        rpt_label4 = Label(sr_Canvas_1,width=15,height=1,text="ORIGINAL AMOUNT", font=('arial 10 bold'),background='#1b3857',fg="white") 
                        sr_Canvas_1.create_window(0, 0, anchor="c",state=HIDDEN, window=rpt_label4,tags=("label15"))

                        rpt_label5 = Label(sr_Canvas_1,width=15,height=1,text="OPEN BALANCE", font=('arial 10 bold'),background='#1b3857',fg="white") 
                        sr_Canvas_1.create_window(0, 0, anchor="c",state=HIDDEN, window=rpt_label5,tags=("label16"))

                        rpt_label6 = Label(sr_Canvas_1,width=15,height=1,text="PAYMENT", font=('arial 10 bold'),background='#1b3857',fg="white") 
                        sr_Canvas_1.create_window(0, 0, anchor="c",state=HIDDEN, window=rpt_label6,tags=("label17"))

                        rp_tree = ttk.Treeview(sr_Canvas_1,height=8)
                        rp_tree["columns"] = ["1","2","3","4","5"]
                        rp_tree.column("#0",width=35)
                        rp_tree.column("1",width=210,anchor=CENTER)
                        rp_tree.column("2",width=210,anchor=CENTER)
                        rp_tree.column("3",width=210,anchor=CENTER)
                        rp_tree.column("4",width=210,anchor=CENTER)
                        rp_tree.column("5",width=210,anchor=CENTER)
                        rp_tree.heading("#0",text="#")
                        rp_tree.heading("1",text="DESCRIPTION")
                        rp_tree.heading("2",text="DUE DATE")
                        rp_tree.heading("3",text="ORIGINAL AMOUNT")
                        rp_tree.heading("4",text="OPEN BALANCE")
                        rp_tree.heading("5",text="PAYMENT")
                        sr_Canvas_1.create_window(0,0,anchor='nw',window=rp_tree,tags=("tree1"))

                        # sr_Canvas_1.create_line(820,800,1260,800,fill='gray',width=1,tags=("line10"))
                        # sr_Canvas_1.create_line(820,850,1260,850,fill='gray',width=1,tags=("line11"))
                        # sr_Canvas_1.create_line(820,900,1260,900,fill='gray',width=1,tags=("line12"))
                        # sr_Canvas_1.create_line(820,800,820,900,fill='gray',width=1,tags=("line13"))
                        # sr_Canvas_1.create_line(1000,800,1000,900,fill='gray',width=1,tags=("line14"))
                        # sr_Canvas_1.create_line(1260,800,1260,900,fill='gray',width=1,tags=("line15"))

                        # rpt_label7 = Label(sr_Canvas_1,width=15,height=1,text="Amount to Apply", font=('arial 10 bold'),background='#1b3857',fg="white") 
                        # sr_Canvas_1.create_window(910, 825, anchor="c", window=rpt_label7,tags=("label18"))  

                        # rp_amnttoapply = Entry(sr_Canvas_1,font=('arial 15'),width=24,background='#2f516f',foreground='white')
                        # sr_Canvas_1.create_window(1130,825,anchor='c',window=rp_amnttoapply,tags=("entry5"))   

                        # rpt_label8 = Label(sr_Canvas_1,width=15,height=1,text="Amount to Credit", font=('arial 10 bold'),background='#1b3857',fg="white") 
                        # sr_Canvas_1.create_window(910, 875, anchor="c", window=rpt_label8,tags=("label19"))  

                        # rp_amnttocredit = Entry(sr_Canvas_1,font=('arial 15'),width=24,background='#2f516f',foreground='white')
                        # sr_Canvas_1.create_window(1130,875,anchor='c',window=rp_amnttocredit,tags=("entry6"))   

                        def sr_goBack():
                            sr_Frame_1.grid_forget()
                            sr_Frame.grid(row=0,column=0,sticky='nsew')

                        back_btn = Button(sr_Canvas_1,text='←  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:sr_goBack())
                        sr_Canvas_1.create_window(0,0,window=back_btn,tags=("button3")) 

                        # save_btn = Button(sr_Canvas_1,text='Save',width=20,height=2,font=('arial 10 bold'),background="#198fed",activebackground="#198fed",foreground="white",activeforeground="white",bd=0)
                        # sr_Canvas_1.create_window(0,0,window=save_btn,tags=("button4")) 

                        # rpt_label9 = Label(sr_Canvas_1,width=5,height=1,text="1",font=('arial 12'),background='#1b3857',fg="white",anchor="c")
                        # sr_Canvas_1.create_window(0,0,window=rpt_label9,tags=("label20"))

                        rpt_descp = Entry(sr_Canvas_1,font=('arial 15'),width=17,background='#2f516f',foreground='white')
                        sr_Canvas_1.create_window(0,0,anchor='c',state=HIDDEN,window=rpt_descp,tags=("entry8")) 

                        rpt_due = Entry(sr_Canvas_1,font=('arial 15'),width=17,background='#2f516f',foreground='white')
                        sr_Canvas_1.create_window(0,0,anchor='c',state=HIDDEN,window=rpt_due,tags=("entry9")) 

                        rpt_original = Entry(sr_Canvas_1,font=('arial 15'),width=17,background='#2f516f',foreground='white')
                        sr_Canvas_1.create_window(0,0,anchor='c',state=HIDDEN,window=rpt_original,tags=("entry10")) 

                        rpt_obal = Entry(sr_Canvas_1,font=('arial 15'),width=17,background='#2f516f',foreground='white')
                        sr_Canvas_1.create_window(0,0,anchor='c',state=HIDDEN,window=rpt_obal,tags=("entry11"))

                        rpt_payment = Entry(sr_Canvas_1,font=('arial 15'),width=17,background='#2f516f',foreground='white')
                        sr_Canvas_1.create_window(0,0,anchor='c',state=HIDDEN,window=rpt_payment,tags=("entry12")) 

                        def show_editEntry():
                            selected_item = rp_tree.selection()[0]
                            rpt_row = list(rp_tree.item(selected_item,'values'))
                            if len(rpt_row) == '':
                                pass
                            else:
                                sr_Canvas_1.itemconfig('label13',state='normal')
                                sr_Canvas_1.itemconfig('label14',state='normal')
                                sr_Canvas_1.itemconfig('label15',state='normal')
                                sr_Canvas_1.itemconfig('label16',state='normal')
                                sr_Canvas_1.itemconfig('label17',state='normal')

                                sr_Canvas_1.itemconfig('entry8',state='normal')
                                sr_Canvas_1.itemconfig('entry9',state='normal')
                                sr_Canvas_1.itemconfig('entry10',state='normal')
                                sr_Canvas_1.itemconfig('entry11',state='normal')
                                sr_Canvas_1.itemconfig('entry12',state='normal')

                                rpt_descp.delete(0,END)
                                rpt_descp.insert(0,rpt_row[0])
                                rpt_due.delete(0,END)
                                rpt_due.insert(0,rpt_row[1])
                                rpt_original.delete(0,END)
                                rpt_original.insert(0,rpt_row[2])
                                rpt_obal.delete(0,END)
                                rpt_obal.insert(0,rpt_row[3])
                                rpt_payment.delete(0,END)
                                rpt_payment.insert(0,rpt_row[4])

                                try:
                                    def assign_newvalue(event):
                                        rp_tree.item(selected_item,values=(rpt_descp.get(),rpt_due.get(),rpt_original.get(),rpt_obal.get(),rpt_payment.get()))

                                    rpt_descp.bind("<KeyRelease>",assign_newvalue)
                                    rpt_due.bind("<KeyRelease>",assign_newvalue)
                                    rpt_original.bind("<KeyRelease>",assign_newvalue)
                                    rpt_obal.bind("<KeyRelease>",assign_newvalue)
                                    rpt_payment.bind("<KeyRelease>",assign_newvalue)
                                except:
                                    pass


                        rpt_edit = Button(sr_Canvas_1,font=('arial 12'),text='edit',width=11,background='#1b3857',foreground='white',activebackground='#1b3857',activeforeground='white',command=lambda:show_editEntry())
                        sr_Canvas_1.create_window(0,0,anchor='c',window=rpt_edit,tags=("combo13")) 

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

                            def select_GSTtype(event):
                                if cust_gtype.get() == 'GST unregistered' or cust_gtype.get() == 'Consumer' or cust_gtype.get() == 'Overseas':
                                    sr_Canvas_2.itemconfig("label9",state='hidden')
                                    sr_Canvas_2.itemconfig("entry6",state='hidden')
                                else:
                                    sr_Canvas_2.itemconfig("label9",state='normal')
                                    sr_Canvas_2.itemconfig("entry6",state='normal')

                            cust_gtype = ttk.Combobox(sr_Canvas_2,width=19,font=('arial 15'))
                            cust_gtype['values'] = ['Choose...','GST registered- Regular','GST registered- Composition','GST unregistered','Consumer','Overseas','SEZ',"Deemed exports - EOU's STP's EHTP's etc"]
                            cust_gtype.current(0)
                            cust_gtype.bind("<<ComboboxSelected>>",select_GSTtype)
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

                            def select_GSTtype(event):
                                if cust_gtype.get() == 'GST unregistered' or cust_gtype.get() == 'Consumer' or cust_gtype.get() == 'Overseas':
                                    sr_Canvas_2.itemconfig("label9",state='hidden')
                                    sr_Canvas_2.itemconfig("entry6",state='hidden')
                                else:
                                    sr_Canvas_2.itemconfig("label9",state='normal')
                                    sr_Canvas_2.itemconfig("entry6",state='normal')

                            cust_gtype = ttk.Combobox(sr_Canvas_2,width=19,font=('arial 15'))
                            cust_gtype['values'] = ['Choose...','GST registered- Regular','GST registered- Composition','GST unregistered','Consumer','Overseas','SEZ',"Deemed exports - EOU's STP's EHTP's etc"]
                            cust_gtype.current(0)
                            cust_gtype.bind("<<ComboboxSelected>>",select_GSTtype)
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

                        cn_invperiod = ttk.Combobox(sr_Canvas_1,width=19,font=('arial 15'),background='#2f516f')
                        cn_invperiod['values'] = ['Add new',]
                        cn_invperiod.current(0)
                        sr_Canvas_1.create_window(0,0,anchor='nw',window=cn_invperiod,tags=("entry16"))

                        cn_label9 = Label(sr_Canvas_1,width=20,height=1,text="Invoice No.",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                        sr_Canvas_1.create_window(0,0,window=cn_label9,tags=('label27'))

                        cn_invoiceno = ttk.Combobox(sr_Canvas_1,width=19,font=('arial 15'),background='#2f516f',foreground='white')
                        sr_Canvas_1.create_window(0,0,anchor='nw',window=cn_invoiceno,tags=("entry17"))

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

                            def select_GSTtype(event):
                                if cust_gtype.get() == 'GST unregistered' or cust_gtype.get() == 'Consumer' or cust_gtype.get() == 'Overseas':
                                    sr_Canvas_2.itemconfig("label9",state='hidden')
                                    sr_Canvas_2.itemconfig("entry6",state='hidden')
                                else:
                                    sr_Canvas_2.itemconfig("label9",state='normal')
                                    sr_Canvas_2.itemconfig("entry6",state='normal')

                            cust_gtype = ttk.Combobox(sr_Canvas_2,width=19,font=('arial 15'))
                            cust_gtype['values'] = ['Choose...','GST registered- Regular','GST registered- Composition','GST unregistered','Consumer','Overseas','SEZ',"Deemed exports - EOU's STP's EHTP's etc"]
                            cust_gtype.current(0)
                            cust_gtype.bind("<<ComboboxSelected>>",select_GSTtype)
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

                        sr_Canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly5"))   

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

                            def select_GSTtype(event):
                                if cust_gtype.get() == 'GST unregistered' or cust_gtype.get() == 'Consumer' or cust_gtype.get() == 'Overseas':
                                    sr_Canvas_2.itemconfig("label9",state='hidden')
                                    sr_Canvas_2.itemconfig("entry6",state='hidden')
                                else:
                                    sr_Canvas_2.itemconfig("label9",state='normal')
                                    sr_Canvas_2.itemconfig("entry6",state='normal')

                            cust_gtype = ttk.Combobox(sr_Canvas_2,width=19,font=('arial 15'))
                            cust_gtype['values'] = ['Choose...','GST registered- Regular','GST registered- Composition','GST unregistered','Consumer','Overseas','SEZ',"Deemed exports - EOU's STP's EHTP's etc"]
                            cust_gtype.current(0)
                            cust_gtype.bind("<<ComboboxSelected>>",select_GSTtype)
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

                            def select_GSTtype(event):
                                if cust_gtype.get() == 'GST unregistered' or cust_gtype.get() == 'Consumer' or cust_gtype.get() == 'Overseas':
                                    sr_Canvas_2.itemconfig("label9",state='hidden')
                                    sr_Canvas_2.itemconfig("entry6",state='hidden')
                                else:
                                    sr_Canvas_2.itemconfig("label9",state='normal')
                                    sr_Canvas_2.itemconfig("entry6",state='normal')

                            cust_gtype = ttk.Combobox(sr_Canvas_2,width=19,font=('arial 15'))
                            cust_gtype['values'] = ['Choose...','GST registered- Regular','GST registered- Composition','GST unregistered','Consumer','Overseas','SEZ',"Deemed exports - EOU's STP's EHTP's etc"]
                            cust_gtype.current(0)
                            cust_gtype.bind("<<ComboboxSelected>>",select_GSTtype)
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
                        ta_billCombo.current(0)
                        ta_billCombo.bind("<<ComboboxSelected>>",ta_billable)
                        sr_Canvas_1.create_window(0,0,anchor='nw',window=ta_billCombo,tags=("combo11"))

                        ta_unknown = Entry(sr_Canvas_1,width=31,font=('arial 15'),background='#2f516f',foreground='white')
                        sr_Canvas_1.create_window(0,0,anchor='nw',window=ta_unknown,tags=("entry34"))

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
                        ta_startendCombo.current(0)
                        ta_startendCombo.bind("<<ComboboxSelected>>",ta_startend)
                        sr_Canvas_1.create_window(0,0,anchor='nw',window=ta_startendCombo,tags=("combo12"))

                        ta_label7 = Label(sr_Canvas_1,width=20,height=1,text="Start date",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
                        sr_Canvas_1.create_window(0,0,window=ta_label7,tags=("label60"))

                        ta_start = Entry(sr_Canvas_1,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                        sr_Canvas_1.create_window(0,0,anchor='nw',window=ta_start,tags=("entry35"))

                        ta_label8 = Label(sr_Canvas_1,width=20,height=1,text="End date",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
                        sr_Canvas_1.create_window(0,0,window=ta_label8,tags=("label61"))

                        ta_end = Entry(sr_Canvas_1,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                        sr_Canvas_1.create_window(0,0,anchor='nw',window=ta_end,tags=("entry36"))

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
                    


                sr_transCombo = ttk.Combobox(sr_Canvas,font=('arial 15'),width=14)
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
                        dcanvas.coords("hline1",dwidth/7.8,dheight/0.695,dwidth/1.15,dheight/0.695)
                        dcanvas.coords("hline1",dwidth/7.8,dheight/0.285,dwidth/1.15,dheight/0.285)

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


                        r2 = 25
                        x11 = dwidth/63
                        x21 = dwidth/1.021
                        y11 = dheight/2.8
                        y21 = dheight/0.27


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


                        x11 = dwidth/7.8
                        x21 = dwidth/1.15
                        y11 = dheight/2.1
                        y21 = dheight/0.28
                        dcanvas.coords("rect1",x11,y11,x21,y21)

                        x11 = dwidth/6.95
                        x21 = dwidth/1.17
                        y11 = dheight/0.67
                        y21 = dheight/0.64
                        dcanvas.coords("rect2",x11,y11,x21,y21)
                        

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

                            dcanvas.coords("label45",dwidth/4.22,dheight/1.7)
                            dcanvas.coords("label46",dwidth/6.32,dheight/1.4)
                            dcanvas.coords("label47",dwidth/3.55,dheight/1.16)
                            dcanvas.coords("label48",dwidth/5.18,dheight/1.06)
                            dcanvas.coords("label49",dwidth/4.22,dheight/1.01)
                            dcanvas.coords("label50",dwidth/6.36,dheight/0.902)
                            dcanvas.coords("label51",dwidth/2.18,dheight/1.06)
                            dcanvas.coords("label52",dwidth/1.995,dheight/1.01)
                            dcanvas.coords("label53",dwidth/2.371,dheight/0.902)
                            dcanvas.coords("label54",dwidth/1.45,dheight/1.04)
                            dcanvas.coords("label55",dwidth/1.25,dheight/1.04)
                            dcanvas.coords("label56",dwidth/1.45,dheight/0.98)
                            dcanvas.coords("label57",dwidth/1.25,dheight/0.98)
                            dcanvas.coords("label58",dwidth/4.6,dheight/0.77)
                            dcanvas.coords("label59",dwidth/2.9,dheight/0.77)
                            dcanvas.coords("label60",dwidth/4.95,dheight/0.73)
                            dcanvas.coords("label61",dwidth/3.1,dheight/0.73)
                            dcanvas.coords("label62",dwidth/4.2,dheight/0.655)
                            dcanvas.coords("label63",dwidth/2.8,dheight/0.655)
                            dcanvas.coords("label64",dwidth/2.3,dheight/0.655)
                            dcanvas.coords("label65",dwidth/1.86,dheight/0.655)
                            dcanvas.coords("label66",dwidth/1.47,dheight/0.655)
                            dcanvas.coords("label67",dwidth/1.25,dheight/0.655)
                            dcanvas.coords("label68",dwidth/4.2,dheight/0.62)
                            dcanvas.coords("label69",dwidth/2.8,dheight/0.62)
                            dcanvas.coords("label70",dwidth/2.3,dheight/0.62)
                            dcanvas.coords("label71",dwidth/1.86,dheight/0.62)
                            dcanvas.coords("label72",dwidth/1.47,dheight/0.62)
                            dcanvas.coords("label73",dwidth/1.25,dheight/0.62)
                            dcanvas.coords("label74",dwidth/6.5,dheight/0.62)

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
                            dcanvas.coords("button8",dwidth/1.18,dheight/8.24)
                            dcanvas.coords("button9",dwidth/1.08,dheight/8.24)
                            
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

                    sr_Canvas_4 = Canvas(sr_Frame_1,bg='#2f516f',scrollregion=(0,0,700,2000))

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
                        ed_label1 = Label(sr_Canvas_4,width=18,height=1,text="CASH MEMO NO.",font=('arial 25'),background='#1b3857',fg="white")
                        sr_Canvas_4.create_window(0,0,anchor="c",window=ed_label1,tags=("label1"))
                        sr_Canvas_4.create_line(0,0,0,0,fill='gray',width=1,tags=("hline"))

                        sr_Canvas_4.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly2"))

                        ed_label2 = Label(sr_Canvas_4,width=18,height=1,text="Fin sYs",font=('arial 25'),background='#1b3857',fg="white")
                        sr_Canvas_4.create_window(0,0,anchor="c",window=ed_label2,tags=("label2"))

                        ed_label3 = Label(sr_Canvas_4,width=10,height=1,text="Customer",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
                        sr_Canvas_4.create_window(0,0,window=ed_label3,tags=("label21"))

                        ed_custCombo = ttk.Combobox(sr_Canvas_4,width=19,font=('arial 15'))
                        sr_Canvas_4.create_window(0,0,anchor='nw',window=ed_custCombo,tags=("combo3"))

                        ed_label4 = Label(sr_Canvas_4,width=10,height=1,text="Email",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                        sr_Canvas_4.create_window(0,0,window=ed_label4,tags=('label22'))

                        ed_email = Entry(sr_Canvas_4,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                        sr_Canvas_4.create_window(0,0,anchor='nw',window=ed_email,tags=("entry13"))

                        ed_label5 = Label(sr_Canvas_4,width=20,height=1,text="Billing Address",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                        sr_Canvas_4.create_window(0,0,window=ed_label5,tags=('label23'))

                        ed_baddress = Text(sr_Canvas_4,width=20,font=('arial 15'),height=7,background='#2f516f',foreground='white')
                        sr_Canvas_4.create_window(0,0,anchor='nw',window=ed_baddress,tags=("entry14"))

                        ed_label7 = Label(sr_Canvas_4,width=20,height=1,text="Place of Supply",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                        sr_Canvas_4.create_window(0,0,window=ed_label7,tags=('label25'))

                        ed_pofsupply = ttk.Combobox(sr_Canvas_4,width=19,font=('arial 15'),background='#2f516f')
                        sr_Canvas_4.create_window(0,0,anchor='nw',window=ed_pofsupply,tags=("entry15"))

                        ed_label8 = Label(sr_Canvas_4,width=20,height=1,text="Payment Method",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                        sr_Canvas_4.create_window(0,0,window=ed_label8,tags=('label26'))

                        def addnew_pmethod_1(event):
                            if ed_pmethod.get() == "Add new":
                                sr_Canvas_4.itemconfig("entry26",state='normal')
                            else:
                                sr_Canvas_4.itemconfig("entry26",state='hidden')

                        ed_pmethod = ttk.Combobox(sr_Canvas_4,width=19,font=('arial 15'),background='#2f516f')
                        ed_pmethod['values'] = ['Add new',]
                        ed_pmethod.current(0)
                        ed_pmethod.bind("<<ComboboxSelected>>",addnew_pmethod_1)
                        sr_Canvas_4.create_window(0,0,anchor='nw',window=ed_pmethod,tags=("entry16"))

                        ed_newmeth = Entry(sr_Canvas_4,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                        sr_Canvas_4.create_window(115,755,anchor='nw',state=HIDDEN,window=ed_newmeth,tags=("entry26"))

                        ed_label9 = Label(sr_Canvas_4,width=20,height=1,text="Reference No:",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                        sr_Canvas_4.create_window(0,0,window=ed_label9,tags=('label27'))

                        ed_ref = Entry(sr_Canvas_4,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                        sr_Canvas_4.create_window(0,0,anchor='nw',window=ed_ref,tags=("entry17"))

                        ed_label10 = Label(sr_Canvas_4,width=20,height=1,text="Deposit to:",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                        sr_Canvas_4.create_window(0,0,window=ed_label10,tags=('label28'))

                        ed_depto = ttk.Combobox(sr_Canvas_4,width=19,font=('arial 15'),background='#2f516f')
                        sr_Canvas_4.create_window(0,0,anchor='nw',window=ed_depto,tags=("combo4"))

                        ed_label11 = Label(sr_Canvas_4,width=20,height=1,text="AMOUNT",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                        sr_Canvas_4.create_window(0,0,window=ed_label11,tags=('label29'))

                        ed_label12 = Label(sr_Canvas_4,width=20,height=1,text="0.00",font=('arial 14'),background='#1b3857',anchor="w",fg="white")
                        sr_Canvas_4.create_window(0,0,window=ed_label12,tags=('label30'))

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

                        ed_label13 = Label(sr_Canvas_4,width=3,height=1,text="#",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                        sr_Canvas_4.create_window(0,0,window=ed_label13,tags=('label31'))

                        ed_label14 = Label(sr_Canvas_4,width=3,height=1,text="1",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                        sr_Canvas_4.create_window(0,0,window=ed_label14,tags=('label32'))

                        ed_label18 = Label(sr_Canvas_4,width=15,height=1,text="Product / Service",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                        sr_Canvas_4.create_window(0,0,window=ed_label18,tags=('label33'))

                        ed_label19 = Label(sr_Canvas_4,width=14,height=1,text="HSN",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                        sr_Canvas_4.create_window(0,0,window=ed_label19,tags=('label34'))

                        ed_label20 = Label(sr_Canvas_4,width=18,height=1,text="Description",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                        sr_Canvas_4.create_window(0,0,window=ed_label20,tags=('label35'))

                        ed_label21 = Label(sr_Canvas_4,width=10,height=1,text="Qty",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                        sr_Canvas_4.create_window(0,0,window=ed_label21,tags=('label36'))

                        ed_label22 = Label(sr_Canvas_4,width=10,height=1,text="Price",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                        sr_Canvas_4.create_window(0,0,window=ed_label22,tags=('label37'))

                        ed_label23 = Label(sr_Canvas_4,width=10,height=1,text="Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                        sr_Canvas_4.create_window(0,0,window=ed_label23,tags=('label38'))

                        ed_label24 = Label(sr_Canvas_4,width=10,height=1,text="Tax (%)",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                        sr_Canvas_4.create_window(0,0,window=ed_label24,tags=('label39'))

                        edt_entry1 = ttk.Combobox(sr_Canvas_4,width=10,font=('arial 15'),background='#2f516f',foreground='white')
                        sr_Canvas_4.create_window(0,0,anchor='c',window=edt_entry1,tags=("combo5"))

                        edt_entry2 = Entry(sr_Canvas_4,width=11,font=('arial 15'),background='#2f516f',foreground='white')
                        sr_Canvas_4.create_window(0,0,anchor='nw',window=edt_entry2,tags=("entry18"))

                        edt_entry3 = Entry(sr_Canvas_4,width=17,font=('arial 15'),background='#2f516f',foreground='white')
                        sr_Canvas_4.create_window(0,0,anchor='nw',window=edt_entry3,tags=("entry19"))

                        edt_entry4 = Entry(sr_Canvas_4,width=10,font=('arial 15'),background='#2f516f',foreground='white')
                        sr_Canvas_4.create_window(0,0,anchor='nw',window=edt_entry4,tags=("entry20"))

                        edt_entry5 = Entry(sr_Canvas_4,width=14,font=('arial 15'),background='#2f516f',foreground='white')
                        sr_Canvas_4.create_window(0,0,anchor='nw',window=edt_entry5,tags=("entry21"))

                        edt_entry6 = Entry(sr_Canvas_4,width=13,font=('arial 15'),background='#2f516f',foreground='white')
                        sr_Canvas_4.create_window(0,0,anchor='nw',window=edt_entry6,tags=("entry22"))

                        edt_entry7 = ttk.Combobox(sr_Canvas_4,width=7,font=('arial 15'),background='#2f516f',foreground='white')
                        sr_Canvas_4.create_window(0,0,anchor='c',window=edt_entry7,tags=("combo6"))

                        ed_label25 = Label(sr_Canvas_4,width=10,height=1,text="Sub Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                        sr_Canvas_4.create_window(0,0,window=ed_label25,tags=('label40'))

                        ed_label26 = Label(sr_Canvas_4,width=10,height=1,text="Tax Amount",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                        sr_Canvas_4.create_window(0,0,window=ed_label26,tags=('label41'))

                        ed_label27 = Label(sr_Canvas_4,width=10,height=1,text="Grand Total",font=('arial 12'),background='#1b3857',anchor="c",fg="white")
                        sr_Canvas_4.create_window(0,0,window=ed_label27,tags=('label42'))

                        edt_entry8 = Entry(sr_Canvas_4,width=24,font=('arial 15'),background='#2f516f',foreground='white')
                        sr_Canvas_4.create_window(0,0,anchor='nw',window=edt_entry8,tags=("entry23"))

                        edt_entry9 = Entry(sr_Canvas_4,width=24,font=('arial 15'),background='#2f516f',foreground='white')
                        sr_Canvas_4.create_window(0,0,anchor='nw',window=edt_entry9,tags=("entry24"))

                        edt_entry10 = Entry(sr_Canvas_4,width=24,font=('arial 15'),background='#2f516f',foreground='white')
                        sr_Canvas_4.create_window(0,0,anchor='nw',window=edt_entry10,tags=("entry25"))

                        save_btn = Button(sr_Canvas_4,text='Save',width=20,height=2,font=('arial 10 bold'),background="#198fed",activebackground="#198fed",foreground="white",activeforeground="white",bd=0)
                        sr_Canvas_4.create_window(0,0,window=save_btn,tags=("button7")) 

                        ed_label7 = Label(sr_Canvas_4,width=20,height=1,text="Sales receipt No:",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                        sr_Canvas_4.create_window(0,0,window=ed_label7,tags=('label44'))

                        edt_entry11 = Entry(sr_Canvas_4,width=20,font=('arial 15'),background='#2f516f',foreground='white')
                        sr_Canvas_4.create_window(0,0,anchor='nw',window=edt_entry11,tags=("entry27"))

                        def sr_goBack():
                            sr_Frame_1.grid_forget()
                            sr_Frame.grid(row=0,column=0,sticky='nsew')

                        back_btn = Button(sr_Canvas_4,text='←  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:sr_goBack())
                        sr_Canvas_4.create_window(0,0,window=back_btn,tags=("button3"))
                        #--------------
                        ed_label6 = Label(sr_Canvas_4,width=20,height=1,text="Sales receipt date:",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
                        sr_Canvas_4.create_window(0,0,window=ed_label6,tags=('label24'))

                        cwidth = root.winfo_screenwidth()

                        ed_srdate = DateEntry(sr_Canvas_4,width=19,font=('arial 15'),background='#2f516f',foreground='white')
                        if cwidth > 1280:
                            sr_Canvas_4.create_window(495,442,anchor='nw',window=ed_srdate,tags=("date"))
                        elif cwidth <= 1024:
                            sr_Canvas_4.create_window(370,455,anchor='nw',window=ed_srdate,tags=("date"))
                        else:
                            sr_Canvas_4.create_window(465,407,anchor='nw',window=ed_srdate,tags=("date"))
                    elif srt_actionCombo.get() == 'View':
                        sr_Canvas_4.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly1"))
                        view_label1 = Label(sr_Canvas_4,width=18,height=1,text="SALES RECEIPT",font=('arial 25'),background='#1b3857',fg="white")
                        sr_Canvas_4.create_window(0,0,anchor="c",window=view_label1,tags=("label1"))

                        downloadPDF_btn = Button(sr_Canvas_4,text='Download PDF',font=('arial 10 bold'),bd=0,activebackground='#198fed',foreground='white',background='#198fed',padx=10,pady=5)
                        sr_Canvas_4.create_window(0,0,window=downloadPDF_btn,tags=("button8"))

                        print_btn = Button(sr_Canvas_4,text='Print',font=('arial 10 bold'),bd=0,activebackground='#198fed',foreground='white',background='#198fed',padx=10,pady=5)
                        sr_Canvas_4.create_window(0,0,window=print_btn,tags=("button9"))

                        sr_Canvas_4.create_line(0,0,0,0,fill='gray',width=1,tags=("hline"))

                        sr_Canvas_4.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("poly3"))
                        sr_Canvas_4.create_rectangle(0,0,0,0,fill="white",tags=("rect1"))

                        view_label2 = Label(sr_Canvas_4,width=20,height=1,text="Company Name",font=('arial 12 bold'),background="white",fg="black",anchor="w")
                        sr_Canvas_4.create_window(0,0,window=view_label2,tags=("label45"))

                        address_txt = "Company Address\nAddress1\nAddress2\nAddress3\nAddress4"

                        view_label3 = Text(sr_Canvas_4,width=25,height=5,font=('arial 12'),cursor='arrow',background="white",fg="black",bd=0)
                        view_label3.insert('1.0',address_txt)
                        view_label3.config(state=DISABLED)
                        sr_Canvas_4.create_window(0,0,window=view_label3,anchor="w",tags=("label46"))

                        view_label4 = Label(sr_Canvas_4,width=20,height=1,text="SALES RECEIPT",font=('arial 20'),background="white",fg="#198fed",anchor="w")
                        sr_Canvas_4.create_window(0,0,window=view_label4,tags=("label47"))

                        view_label5 = Label(sr_Canvas_4,width=10,height=1,text="Bill To:",font=('arial 13'),background="white",fg="black",anchor="w")
                        sr_Canvas_4.create_window(0,0,window=view_label5,tags=("label48"))

                        view_label6 = Label(sr_Canvas_4,width=20,height=1,text="Customer Name",font=('arial 12 bold'),background="white",fg="black",anchor="w")
                        sr_Canvas_4.create_window(0,0,window=view_label6,tags=("label49"))

                        address_txt1 = "Customer Address\nAddress1\nAddress2\nAddress3\nAddress4"

                        view_label7 = Text(sr_Canvas_4,width=25,height=5,font=('arial 12'),cursor='arrow',fg="black",bd=0)
                        view_label7.insert('1.0',address_txt1)
                        view_label7.config(state=DISABLED)
                        sr_Canvas_4.create_window(0,0,window=view_label7,anchor="w",tags=("label50"))

                        view_label5 = Label(sr_Canvas_4,width=10,height=1,text="Ship To:",font=('arial 13'),background="white",fg="black",anchor="w")
                        sr_Canvas_4.create_window(0,0,window=view_label5,tags=("label51"))

                        view_label6 = Label(sr_Canvas_4,width=20,height=1,text="Customer Name",font=('arial 12 bold'),background="white",fg="black",anchor="w")
                        sr_Canvas_4.create_window(0,0,window=view_label6,tags=("label52"))

                        address_txt1 = "Customer Address\nAddress1\nAddress2\nAddress3\nAddress4"

                        view_label7 = Text(sr_Canvas_4,width=25,height=5,font=('arial 12'),cursor='arrow',fg="black",bd=0)
                        view_label7.insert('1.0',address_txt1)
                        view_label7.config(state=DISABLED)
                        sr_Canvas_4.create_window(0,0,window=view_label7,anchor="w",tags=("label53"))

                        view_label8 = Label(sr_Canvas_4,width=20,height=1,text="Sales Receipt No      :",font=('arial 12 bold'),background="white",fg="black",anchor="w")
                        sr_Canvas_4.create_window(0,0,window=view_label8,tags=("label54"))

                        view_label9 = Label(sr_Canvas_4,width=15,height=1,text="1001",font=('arial 12'),background="white",fg="black",anchor="w")
                        sr_Canvas_4.create_window(0,0,window=view_label9,tags=("label55"))

                        view_label10 = Label(sr_Canvas_4,width=20,height=1,text="Sales Receipt Date   :",font=('arial 12 bold'),background="white",fg="black",anchor="w")
                        sr_Canvas_4.create_window(0,0,window=view_label10,tags=("label56"))

                        view_label11 = Label(sr_Canvas_4,width=15,height=1,text="02-08-2022",font=('arial 12'),background="white",fg="black",anchor="w")
                        sr_Canvas_4.create_window(0,0,window=view_label11,tags=("label57"))

                        view_label12 = Label(sr_Canvas_4,width=15,height=1,text="Place Of Supply   :",font=('arial 12 bold'),background="white",fg="black",anchor="w")
                        sr_Canvas_4.create_window(0,0,window=view_label12,tags=("label58"))

                        view_label13 = Label(sr_Canvas_4,width=20,height=1,text="Kerala",font=('arial 12'),background="white",fg="black",anchor="w")
                        sr_Canvas_4.create_window(0,0,window=view_label13,tags=("label59"))

                        view_label14 = Label(sr_Canvas_4,width=11,height=1,text="PMT Method   :",font=('arial 12 bold'),background="white",fg="black",anchor="w")
                        sr_Canvas_4.create_window(0,0,window=view_label14,tags=("label60"))

                        view_label15 = Label(sr_Canvas_4,width=20,height=1,text="Cheque",font=('arial 12'),background="white",fg="black",anchor="w")
                        sr_Canvas_4.create_window(0,0,window=view_label15,tags=("label61"))

                        sr_Canvas_4.create_line(0,0,0,0,fill='gray',width=1,tags=("hline1"))
                        sr_Canvas_4.create_rectangle(0,0,0,0,fill="#87ceeb",tags=("rect2"))

                        view_label16 = Label(sr_Canvas_4,width=18,height=1,text="PRODUCT/SERVICES",font=('arial 12'),background="#87ceeb",fg="black",anchor="c")
                        sr_Canvas_4.create_window(0,0,window=view_label16,tags=("label62"))

                        view_label17 = Label(sr_Canvas_4,width=4,height=1,text="HSN",font=('arial 12'),background="#87ceeb",fg="black",anchor="c")
                        sr_Canvas_4.create_window(0,0,window=view_label17,tags=("label63"))

                        view_label18 = Label(sr_Canvas_4,width=4,height=1,text="QTY",font=('arial 12'),background="#87ceeb",fg="black",anchor="c")
                        sr_Canvas_4.create_window(0,0,window=view_label18,tags=("label64"))

                        view_label19 = Label(sr_Canvas_4,width=6,height=1,text="PRICE",font=('arial 12'),background="#87ceeb",fg="black",anchor="c")
                        sr_Canvas_4.create_window(0,0,window=view_label19,tags=("label65"))

                        view_label20 = Label(sr_Canvas_4,width=6,height=1,text="TOTAL",font=('arial 12'),background="#87ceeb",fg="black",anchor="c")
                        sr_Canvas_4.create_window(0,0,window=view_label20,tags=("label66"))

                        view_label21 = Label(sr_Canvas_4,width=6,height=1,text="TAX(%)",font=('arial 12'),background="#87ceeb",fg="black",anchor="c")
                        sr_Canvas_4.create_window(0,0,window=view_label21,tags=("label67"))

                        view_label22 = Label(sr_Canvas_4,width=18,height=1,text="SHOES",font=('arial 12'),background="white",fg="black",anchor="c")
                        sr_Canvas_4.create_window(0,0,window=view_label22,tags=("label68"))

                        view_label23 = Label(sr_Canvas_4,width=4,height=1,text="AG79",font=('arial 12'),background="white",fg="black",anchor="c")
                        sr_Canvas_4.create_window(0,0,window=view_label23,tags=("label69"))

                        view_label24 = Label(sr_Canvas_4,width=4,height=1,text="1",font=('arial 12'),background="white",fg="black",anchor="c")
                        sr_Canvas_4.create_window(0,0,window=view_label24,tags=("label70"))

                        view_label25 = Label(sr_Canvas_4,width=6,height=1,text="1999",font=('arial 12'),background="white",fg="black",anchor="c")
                        sr_Canvas_4.create_window(0,0,window=view_label25,tags=("label71"))

                        view_label26 = Label(sr_Canvas_4,width=6,height=1,text="1999",font=('arial 12'),background="white",fg="black",anchor="c")
                        sr_Canvas_4.create_window(0,0,window=view_label26,tags=("label72"))

                        view_label27 = Label(sr_Canvas_4,width=6,height=1,text="4%" + "  GST",font=('arial 12'),background="white",fg="black",anchor="c")
                        sr_Canvas_4.create_window(0,0,window=view_label27,tags=("label73"))

                        view_label28 = Label(sr_Canvas_4,width=4,height=1,text="1",font=('arial 12'),background="white",fg="black",anchor="c")
                        sr_Canvas_4.create_window(0,0,window=view_label28,tags=("label74"))

                        sr_Canvas_4.create_line(0,0,0,0,fill='gray',width=1,tags=("hline3"))
                    else:
                        pass


                srt_actionCombo = ttk.Combobox(sr_Canvas,width=7,font=('arial 15'))
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
                
            else:
                messagebox.showerror("Login Failed","Invalid username or password")
                pass

#---------------------------------------------------------------------------------------------------------------Company Second Portion
def cmpny_crt2():
    

    cmp_name=cmp_nm.get()
    cmp_address=cmp_cmpn.get()
    cmp_ctys=cmp_cty.get()
    state=cmp_stat.get()
    cmp_pins=cmp_pin.get()
    cmp_emails=cmp_email.get()
    cmp_phs=cmp_ph.get()
    cmp_filess=cmp_files.get()
    if cmp_name is not None:
        sql_log_sql='select id from auth_user where username=%s'
        sql_log_sql_val=(sys_usr.get(),)
        
        fbcursor.execute(sql_log_sql,sql_log_sql_val,)
        id=fbcursor.fetchone()
        
        signup_cmp_sql="insert into app1_company(cname,caddress,city,state,pincode,cemail,phone,cimg,id_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
        signup_cmp_sql_val=(cmp_name,cmp_address,cmp_ctys,state,cmp_pins,cmp_emails,cmp_phs,cmp_filess,id[0])
        fbcursor.execute(signup_cmp_sql,signup_cmp_sql_val,)
        finsysdb.commit()
    else:
        messagebox.showerror("Company Creation Failed","Enter your company details")

    main_frame_cmpny.pack_forget()
    global main_frame_cmpny2,nm_nm2,industry_tp,cmp_type,bs_act_man,paid_typ
    main_frame_cmpny2=Frame(root, height=750,bg="#213b52")
    main_frame_cmpny2.pack(fill=X,)

    cmpny_dt_frm2=Frame(main_frame_cmpny2, height=650, width=500,bg="white")
    cmpny_dt_frm2.pack(pady=105)

    def responsive_wid_cmp2(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget
   

        dcanvas.coords("cmpny_hd1",dwidth/40,dheight/15)
        dcanvas.coords("nm_nm2",dwidth/6,dheight/5)
        dcanvas.coords("cmpny_cntry",dwidth/6,dheight/3.2)
        dcanvas.coords("cmpny_cntry2",dwidth/6,dheight/2.35)
        dcanvas.coords("r1",dwidth/2.2,dheight/1.8)
        dcanvas.coords("r2",dwidth/2.2,dheight/1.6)
        dcanvas.coords("cmpny_cntry3",dwidth/6,dheight/1.38)
        dcanvas.coords("button_cmp2",dwidth/4.3,dheight/1.2)
        dcanvas.coords("button_cmp3",dwidth/1.9,dheight/1.2)

        dcanvas.coords("cmp_lbl1",dwidth/6,dheight/3.8)
        dcanvas.coords("cmp_lbl2",dwidth/6,dheight/2.7)
        dcanvas.coords("cmp_lbl3",dwidth/6,dheight/2)
        dcanvas.coords("cmp_lbl4",dwidth/6,dheight/1.46)
        

    lf_cmpy2= Canvas(cmpny_dt_frm2,height=650, width=500)
    lf_cmpy2.bind("<Configure>", responsive_wid_cmp2)
    lf_cmpy2.pack(fill=X)

    def name_ent2(event):
        if nm_nm2.get()=="Legal Business Name":
            nm_nm2.delete(0,END)
        else:
            pass


    cmpny_hd1=Label(lf_cmpy2, text="Let's Start Building Your FinsYs",font=('Calibri 28 bold'), fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmpny_hd1, tag=("cmpny_hd1"))

    

    nm_nm2 = Entry(cmpny_dt_frm2, width=30, font=('Calibri 16'),borderwidth=2)
    nm_nm2.insert(0,"Legal Business Name")
    nm_nm2.bind("<Button-1>",name_ent2)
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=nm_nm2, tag=("nm_nm2"))

    cmp_lbl1=Label(cmpny_dt_frm2, text="Your Industry",font=('Calibri 12') ,fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmp_lbl1, tag=("cmp_lbl1"))

    industry_tp= StringVar()
    cmpny_cntry = ttk.Combobox(cmpny_dt_frm2,textvariable=industry_tp,width=29,font=('Calibri 16'))
    
    cmpny_cntry['values'] = ('Accounting Services','Consultants, doctors, Lawyers and similar','Information Tecnology','Manufacturing','Professional, Scientific and Technical Services','Restaurant/Bar and similar','Retail and Smilar','Other Finanacial Services')
   
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmpny_cntry, tag=("cmpny_cntry"))

    cmp_lbl2=Label(cmpny_dt_frm2, text="Company type",font=('Calibri 12') ,fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmp_lbl2, tag=("cmp_lbl2"))

    cmp_type = StringVar()
    cmpny_cntry2 = ttk.Combobox(cmpny_dt_frm2,textvariable=cmp_type,width=29,font=('Calibri 16'))
    
    cmpny_cntry['values'] = ('Private Limited Company','Public Limited Company','Joint-Venture Company','Partnership Firm Company','One Person Company','Branch Office Company','Non Government Organization')
    
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmpny_cntry2, tag=("cmpny_cntry2"))
    
    cmp_lbl3=Label(cmpny_dt_frm2, text="Do you have an Accountant, Bookkeeper or Tax Pro ?",font=('Calibri 12') ,fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmp_lbl3, tag=("cmp_lbl3"))

    bs_act_man=StringVar()
    r1=Radiobutton(cmpny_dt_frm2, text = "Yes", variable = bs_act_man, value ="Yes",font=('Calibri 16'))
    r1.select()
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=r1, tag=("r1"))

    r2=Radiobutton(cmpny_dt_frm2, text = "No", variable = bs_act_man, value ="No",font=('Calibri 16'))
    r2.select()
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=r2, tag=("r2"))


    cmp_lbl4=Label(cmpny_dt_frm2, text="How do you like to get paid?",font=('Calibri 12') ,fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmp_lbl4, tag=("cmp_lbl4"))
    
    paid_typ = StringVar()
    cmpny_cntry3 = ttk.Combobox(cmpny_dt_frm2,textvariable=paid_typ,width=29,font=('Calibri 16'))
    cmpny_cntry['values'] = ('Cash','Cheque','Credit card/Debit card','Bank Transfer','Paypal/Other service')
   
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmpny_cntry3, tag=("cmpny_cntry3"))

    button_cmp2 = customtkinter.CTkButton(master=cmpny_dt_frm2,command=cmpny_crt1,text="Previous",bg="#213b52")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=button_cmp2, tag=("button_cmp2"))
    button_cmp3 = customtkinter.CTkButton(master=cmpny_dt_frm2,command=fun_sign_in,text="Submit",bg="#213b52")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=button_cmp3, tag=("button_cmp3"))
#-------------------------------------------------------------------------------------------------------------------company creation

def cmpny_crt1():
    
    first_name=fst_nm.get()
    last_name=lst_nm.get()
    email=sys_em.get()
    username=sys_usr.get()
    password=sys_pass.get()
    con_password=sys_cf.get()
    join_dt=datetime.today()
    sql_signup='select * from auth_user'
    fbcursor.execute(sql_signup)
    check_none=fbcursor.fetchone()
    global main_frame_cmpny,cmp_nm,cmp_cmpn,cmp_cty,cmp_pin,cmp_email,cmp_ph,cmp_files,cmp_stat
    if check_none is not None:
        if check_none[4]!=username and check_none[1]!=password:
            
            if password==con_password and con_password==password :
                
                signup_sql="insert into auth_user(first_name,last_name,email,username,password,date_joined) VALUES(%s,%s,%s,%s,%s,%s)" #adding values into db
                signup_sql_val=(first_name,last_name,email,username,password,join_dt,)
                fbcursor.execute(signup_sql,signup_sql_val,)
                finsysdb.commit()
                try:
                    main_frame_cmpny2.pack_forget()
                except:
                    pass
                try:
                    main_frame_signup.pack_forget()
                except:
                    pass
                
                main_frame_cmpny=Frame(root, height=750,bg="#213b52")
                main_frame_cmpny.pack(fill=X,)

                cmpny_dt_frm=Frame(main_frame_cmpny, height=650, width=500,bg="white")
                cmpny_dt_frm.pack(pady=50)

                def name_ent(event):
                    if cmp_nm.get()=="Company Name":
                        cmp_nm.delete(0,END)
                    else:
                        pass

                def cmp_add(event):
                    if cmp_cmpn.get()=="Company Address":
                            cmp_cmpn.delete(0,END)
                    else:
                        pass
                def cty_ent(event):
                    if cmp_cty.get()=="City":
                        cmp_cty.delete(0,END)
                    else:
                        pass

                def em_ent(event):
                    if cmp_email.get()=="Email":
                            cmp_email.delete(0,END)
                    else:
                        pass
                def ph_ent(event):
                    if cmp_ph.get()=="Phone Number":
                        cmp_ph.delete(0,END)
                    else:
                        pass

                def fil_ent(event):
                    
                    cmp_logo = askopenfilename(filetypes=(("png file ",'.png'),('PDF', '*.pdf',),("jpg file", ".jpg"),  ("All files", "*.*"),))
                    logo_crp=cmp_logo.split('/',-1)
                    im1 = Image.open(r""+cmp_logo) 
                    im1 = im1.save("profilepic/propic.jpg")
                    
                    cmp_files.delete(0,END)
                    cmp_files.insert(0,logo_crp[-1])
                
                def responsive_wid_cmp1(event):
                    dwidth = event.width
                    dheight = event.height
                    dcanvas = event.widget
            

                    dcanvas.coords("cmpny_hd",dwidth/2,dheight/13)
                    dcanvas.coords("nm_nm",dwidth/2,dheight/5)
                    dcanvas.coords("cmp_cmpn",dwidth/2,dheight/3.5)
                    dcanvas.coords("cmp_cty",dwidth/2,dheight/2.7)
                    dcanvas.coords("cmpny_cntry",dwidth/2,dheight/2.2)
                    dcanvas.coords("cmp_pin",dwidth/2,dheight/1.85)
                    dcanvas.coords("cmp_email",dwidth/2,dheight/1.6)
                    dcanvas.coords("cmp_ph",dwidth/2,dheight/1.4)
                    dcanvas.coords("cmp_files",dwidth/2,dheight/1.25)
                    dcanvas.coords("button_cmp",dwidth/2,dheight/1.1)


                lf_cmpy1= Canvas(cmpny_dt_frm,height=650, width=500)
                lf_cmpy1.bind("<Configure>", responsive_wid_cmp1)
                lf_cmpy1.pack(fill=X)

                cmpny_hd=Label(lf_cmpy1, text="We're Happy you're Here!",font=('Calibri 30 bold'), fg="black")
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmpny_hd, tag=("cmpny_hd"))


                cmp_nm = Entry(cmpny_dt_frm, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_nm.insert(0,"Company Name")
                cmp_nm.bind("<Button-1>",name_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_nm, tag=("nm_nm"))

                cmp_cmpn = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_cmpn.insert(0,"Company Address")
                cmp_cmpn.bind("<Button-1>",cmp_add)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_cmpn, tag=("cmp_cmpn"))

                cmp_cty = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_cty.insert(0,"City")
                cmp_cty.bind("<Button-1>",cty_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_cty, tag=("cmp_cty"))

                cmp_stat = StringVar()
                cmpny_cntry = ttk.Combobox(lf_cmpy1,textvariable=cmp_stat,width=29,font=('Calibri 16'))
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmpny_cntry, tag=("cmpny_cntry"))
                cmpny_cntry['values'] = ('Default','Black','Maroon','Green','Olive','Navy','Purple','Teal','Gray','Silver','Red','Lime','Yellow','Blue','Fuchsia','Aqua','White','ScrollBar','Background','ActiveCaption','InactiveCaption','Menu','Window','WindowFrame','MenuText','WindowText','CaptionText','ActiveBorder','InactiveBorder','AppWorkSpace','Highlight','HighlightText','BtnFace','InactiveCaptionText','BtnHighlight','3DDkShadow','3DLight','InfoText','InfoBk','Custom')
                cmpny_cntry.current(0)

                cmp_pin = Spinbox(lf_cmpy1,from_=1,to=1000000,width=29, font=('Calibri 16'),borderwidth=2)
                cmp_pin.delete(0,END)
                cmp_pin.insert(0,"Pincode")
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_pin, tag=("cmp_pin"))

                def validateb211(value):
        
                        """
                        Validat the email entry
                        :param value:
                        :return:
                        """
                        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                        if re.fullmatch(pattern, value) is None:
                            
                            return False

                        cmp_email.config(fg="black")
                        return True

                def on_invalidb211():
                        cmp_email.config(fg="red")
                        

                cmp_email = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_email.insert(0,"Email")
                cmp_email.bind("<Button-1>",em_ent)
                vcmdb211 = (lf_cmpy1.register(validateb211), '%P')
                ivcmdb211 = (lf_cmpy1.register(on_invalidb211),)
                cmp_email.config(validate='focusout', validatecommand=vcmdb211, invalidcommand=ivcmdb211)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_email, tag=("cmp_email"))

                cmp_ph = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_ph.insert(0,"Phone Number")
                cmp_ph.bind("<Button-1>",ph_ent)
                def validate_telb51(value):
        
                        pattern = r'^[0-9]\d{9}$'
                        if re.fullmatch(pattern, value) is None:
                            
                            return False
                        cmp_ph.config(fg="black")
                        return True

                def on_invalid_telb51():
                        cmp_ph.config(fg="red")
                        
                v_tel_cmdb51 = (lf_cmpy1.register(validate_telb51), '%P')
                iv_tel_cmdb51 = (lf_cmpy1.register(on_invalid_telb51),)
                cmp_ph.config(validate='focusout', validatecommand=v_tel_cmdb51, invalidcommand=iv_tel_cmdb51)

                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_ph, tag=("cmp_ph"))

                cmp_files = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_files.insert(0,"No file Chosen")
                cmp_files.bind("<Button-1>",fil_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_files, tag=("cmp_files"))

                button_cmp = customtkinter.CTkButton(master=lf_cmpy1,command=cmpny_crt2,text="Next",bg="#213b52")
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=button_cmp, tag=("button_cmp"))
            else:
                messagebox.showerror("Sign Up Failed","password and conform password does not match")
        else:
            messagebox.showerror("Sign Up Failed","Username and password already exist")
    else:
        if password==con_password and con_password==password :
                
                signup_sql="insert into auth_user(first_name,last_name,email,username,password) VALUES(%s,%s,%s,%s,%s)" #adding values into db
                signup_sql_val=(first_name,last_name,email,username,password,)
                fbcursor.execute(signup_sql,signup_sql_val,)
                finsysdb.commit()
                try:
                    main_frame_cmpny2.pack_forget()
                except:
                    pass
                try:
                    main_frame_signup.pack_forget()
                except:
                    pass
                
                main_frame_cmpny=Frame(root, height=750,bg="#213b52")
                main_frame_cmpny.pack(fill=X,)

                cmpny_dt_frm=Frame(main_frame_cmpny, height=650, width=500,bg="white")
                cmpny_dt_frm.pack(pady=50)

                def name_ent(event):
                    if nm_nm.get()=="Company Name":
                        nm_nm.delete(0,END)
                    else:
                        pass

                def cmp_add(event):
                    if cmp_cmpn.get()=="Company Address":
                            cmp_cmpn.delete(0,END)
                    else:
                        pass
                def cty_ent(event):
                    if cmp_cty.get()=="City":
                        cmp_cty.delete(0,END)
                    else:
                        pass

                def em_ent(event):
                    if cmp_email.get()=="Email":
                            cmp_email.delete(0,END)
                    else:
                        pass
                def ph_ent(event):
                    if cmp_ph.get()=="Phone Number":
                        cmp_ph.delete(0,END)
                    else:
                        pass

                def fil_ent(event):
                    
                    cmp_logo = askopenfilename(filetypes=(("png file ",'.png'),('PDF', '*.pdf',),("jpg file", ".jpg"),  ("All files", "*.*"),))
                    logo_crp=cmp_logo.split('/',-1)
                    im1 = Image.open(r""+cmp_logo) 
                    im1 = im1.save("profilepic/propic.jpg")
                    
                    cmp_files.delete(0,END)
                    cmp_files.insert(0,logo_crp[-1])
                
                def responsive_wid_cmp1(event):
                    dwidth = event.width
                    dheight = event.height
                    dcanvas = event.widget
            

                    dcanvas.coords("cmpny_hd",dwidth/2,dheight/13)
                    dcanvas.coords("nm_nm",dwidth/2,dheight/5)
                    dcanvas.coords("cmp_cmpn",dwidth/2,dheight/3.5)
                    dcanvas.coords("cmp_cty",dwidth/2,dheight/2.7)
                    dcanvas.coords("cmpny_cntry",dwidth/2,dheight/2.2)
                    dcanvas.coords("cmp_pin",dwidth/2,dheight/1.85)
                    dcanvas.coords("cmp_email",dwidth/2,dheight/1.6)
                    dcanvas.coords("cmp_ph",dwidth/2,dheight/1.4)
                    dcanvas.coords("cmp_files",dwidth/2,dheight/1.25)
                    dcanvas.coords("button_cmp",dwidth/2,dheight/1.1)


                lf_cmpy1= Canvas(cmpny_dt_frm,height=650, width=500)
                lf_cmpy1.bind("<Configure>", responsive_wid_cmp1)
                lf_cmpy1.pack(fill=X)

                cmpny_hd=Label(lf_cmpy1, text="We're Happy you're Here!",font=('Calibri 30 bold'), fg="black")
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmpny_hd, tag=("cmpny_hd"))


                nm_nm = Entry(cmpny_dt_frm, width=30, font=('Calibri 16'),borderwidth=2)
                nm_nm.insert(0,"Company Name")
                nm_nm.bind("<Button-1>",name_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=nm_nm, tag=("nm_nm"))

                cmp_cmpn = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_cmpn.insert(0,"Company Address")
                cmp_cmpn.bind("<Button-1>",cmp_add)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_cmpn, tag=("cmp_cmpn"))

                cmp_cty = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_cty.insert(0,"City")
                cmp_cty.bind("<Button-1>",cty_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_cty, tag=("cmp_cty"))

                invset_bg_var = StringVar()
                cmpny_cntry = ttk.Combobox(lf_cmpy1,textvariable=invset_bg_var,width=29,font=('Calibri 16'))
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmpny_cntry, tag=("cmpny_cntry"))
                cmpny_cntry['values'] = ('Default','Black','Maroon','Green','Olive','Navy','Purple','Teal','Gray','Silver','Red','Lime','Yellow','Blue','Fuchsia','Aqua','White','ScrollBar','Background','ActiveCaption','InactiveCaption','Menu','Window','WindowFrame','MenuText','WindowText','CaptionText','ActiveBorder','InactiveBorder','AppWorkSpace','Highlight','HighlightText','BtnFace','InactiveCaptionText','BtnHighlight','3DDkShadow','3DLight','InfoText','InfoBk','Custom')
                cmpny_cntry.current(0)

                cmp_pin = Spinbox(lf_cmpy1,from_=1,to=1000000,width=29, font=('Calibri 16'),borderwidth=2)
                cmp_pin.delete(0,END)
                cmp_pin.insert(0,"Pincode")
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_pin, tag=("cmp_pin"))
            

                cmp_email = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_email.insert(0,"Email")
                cmp_email.bind("<Button-1>",em_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_email, tag=("cmp_email"))

                cmp_ph = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_ph.insert(0,"Phone Number")
                cmp_ph.bind("<Button-1>",ph_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_ph, tag=("cmp_ph"))

                cmp_files = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_files.insert(0,"No file Chosen")
                cmp_files.bind("<Button-1>",fil_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_files, tag=("cmp_files"))

                button_cmp = customtkinter.CTkButton(master=lf_cmpy1,command=cmpny_crt2,text="Next",bg="#213b52")
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=button_cmp, tag=("button_cmp"))
        else:
                messagebox.showerror("Sign Up Failed","password and conform password does not match")
  
#--------------------------------------------------------------------------------------------------------Sign in frame in signup section
def fun_sign_in():
    bs_nm=nm_nm2.get()
    ind_type=industry_tp.get()
    com_typ=cmp_type.get()
    acount_manage=bs_act_man.get()
    paid_type=paid_typ.get()

    sql_log_sql='select id from auth_user where username=%s'
    sql_log_sql_val=(sys_usr.get(),)
        
    fbcursor.execute(sql_log_sql,sql_log_sql_val,)
    id=fbcursor.fetchone()
    signup_cmp_sql="update app1_company set bname=%s,industry=%s,ctype=%s,abt=%s,paid=%s  where id_id=%s" #adding values into db
    signup_cmp_sql_val=(bs_nm,ind_type,com_typ,acount_manage,paid_type,id[0],)
    fbcursor.execute(signup_cmp_sql,signup_cmp_sql_val,)
    finsysdb.commit()


    try:
        main_frame_signup.pack_forget()
    except:
        pass
    try:
        main_frame_cmpny2.pack_forget()
    except:
        pass

    main_frame_signin.pack(fill=X,)
    
#---------------------------------------------------------------------------------------------------------------------Sign Up Section
def func_sign_up():
    
    global main_frame_signup,fst_nm,lst_nm,sys_em,sys_usr,sys_pass,sys_cf
    main_frame_signin.pack_forget()

    main_frame_signup=Frame(root, height=750)
    main_frame_signup.pack(fill=X,)

    def responsive_wid_signup(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget
   

        dcanvas.coords("round_signup",dwidth/2,-dheight/.5,dwidth/.7,dheight/.5)
        dcanvas.coords("sign_in_lb",dwidth/6,dheight/12)
        dcanvas.coords("fst_nm",dwidth/8.5,dheight/5)
        dcanvas.coords("lst_nm",dwidth/8.5,dheight/3.5)
        dcanvas.coords("sys_em",dwidth/8.5,dheight/2.7)
        dcanvas.coords("sys_usr",dwidth/8.5,dheight/2.2)
        dcanvas.coords("sys_pass",dwidth/8.5,dheight/1.85)
        dcanvas.coords("sys_cf",dwidth/8.5,dheight/1.6)
        dcanvas.coords("button_sign",dwidth/6,dheight/1.4)
        dcanvas.coords("lft_lab",dwidth/1.4,dheight/18)
        dcanvas.coords("lft_lab2",dwidth/1.52,dheight/10)
        dcanvas.coords("btn_signup2",dwidth/1.36,dheight/6.6)
        dcanvas.coords("label_img",dwidth/1.8,dheight/5)
        
        


    lf_signup= Canvas(main_frame_signup,width=1500, height=1500)
    lf_signup.bind("<Configure>", responsive_wid_signup)
    lf_signup.pack(fill=X)

    lf_signup.create_oval(0,0,0,0,fill="#213b52", tag=("round_signup"))

    # #--------------------------------------------------------------------------------sign up section
    sign_in_lb=Label(lf_signup, text="Sign Up",font=('Calibri 30 bold'), fg="black")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sign_in_lb, tag=("sign_in_lb"))

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
            messagebox.showerror("Password Format","The password length must be greater than or equal to 8 \n>The password must contain one or more uppercase characters\n>The password must contain one or more lowercase characters\n>The password must contain one or more numeric values\n>The password must contain one or more special characters")
        else:
            pass
    
    def nme5(event):
        if sys_cf.get()=="Confirm Password":
            sys_cf.delete(0,END)
        else:
            pass
    
    

    fst_nm = Entry(lf_signup, width=25, font=('Calibri 16'))
    fst_nm.insert(0,"Firstname")
    fst_nm.bind("<Button-1>",nme)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=fst_nm, tag=("fst_nm"))

    lst_nm = Entry(lf_signup,  width=25, font=('Calibri 16'))
    lst_nm.insert(0,"Lastname")
    lst_nm.bind("<Button-1>",nme1)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lst_nm, tag=("lst_nm"))

    
    sys_em = Entry(lf_signup, width=25, font=('Calibri 16'))
    sys_em.insert(0,"Email")
    sys_em.bind("<Button-1>",nme2)
    def validateb211(value):
        
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value) is None:
                            
            return False

        sys_em.config(fg="black")
        return True

    def on_invalidb211():
        
        sys_em.config(fg="red")

    vcmdb211 = (lf_signup.register(validateb211), '%P')
    ivcmdb211 = (lf_signup.register(on_invalidb211),)
    sys_em.config(validate='focusout', validatecommand=vcmdb211, invalidcommand=ivcmdb211)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sys_em, tag=("sys_em"))

    sys_usr = Entry(lf_signup, width=25, font=('Calibri 16'))
    sys_usr.insert(0,"Username")
    sys_usr.bind("<Button-1>",nme3)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sys_usr, tag=("sys_usr"))

    sys_pass = Entry(lf_signup, width=25, font=('Calibri 16'))
    sys_pass.insert(0,"Password")
    sys_pass.bind("<Button-1>",nme4)
    def pas_val_fun(value):
        
        pattern = r'(?=^.{8,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$'
        if re.fullmatch(pattern, value) is None:
                            
            return False

        sys_pass.config(fg="black")
        return True

    def pass_inval_fun():
        sys_pass.config(fg="red")

    pas_val = (lf_signup.register(pas_val_fun), '%P')
    pass_inval = (lf_signup.register(pass_inval_fun),)

    sys_pass.config(validate='focusout', validatecommand=pas_val, invalidcommand=pass_inval)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sys_pass, tag=("sys_pass"))

    sys_cf = Entry(lf_signup, width=25, font=('Calibri 16'))
    sys_cf.insert(0,"Confirm Password")
    sys_cf.bind("<Button-1>",nme5)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sys_cf, tag=("sys_cf"))

    button_sign = customtkinter.CTkButton(master=lf_signup, command=cmpny_crt1,text="Sign Up",bg="#213b52")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=button_sign, tag=("button_sign"))

    label_img = Label(lf_signup, image = sign_up,bg="#213b52", width=800,anchor="w")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=label_img, tag=("label_img"))
    
    

    lft_lab=Label(lf_signup, text="One of us ?",font=('Calibri 20 bold'), fg="white", bg="#213b52")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lft_lab, tag=("lft_lab"))
    lft_lab2=Label(lf_signup, text="click here for work with FinsYs.",font=('Calibri 16 bold'), fg="white", bg="#213b52")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lft_lab2, tag=("lft_lab2"))

    btn_signup2 = Button(lf_signup, text='Sign In', command=fun_sign_in, bg="white", fg="black",borderwidth = 3,height=1,width=10)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=btn_signup2, tag=("btn_signup2"))


main_frame_signin=Frame(root, height=750)
main_frame_signin.pack(fill=X,)


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


def responsive_wid_login(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget
   

        dcanvas.coords("sign_inlb",dwidth/1.4,dheight/4)

        dcanvas.coords("nm_ent",dwidth/1.5,dheight/2.7)
        dcanvas.coords("pass_ent",dwidth/1.5,dheight/2.2)
        dcanvas.coords("button",dwidth/1.4,dheight/1.8)
        dcanvas.coords("round_login",-dwidth/2,-dheight/.5,dwidth/2,dheight/.5)
        dcanvas.coords("lft_lab",dwidth/4,dheight/18)
        dcanvas.coords("lft_lab2",dwidth/6,dheight/10)
        dcanvas.coords("btn2",dwidth/3.7,dheight/6.6)
        dcanvas.coords("img",dwidth/16,dheight/5.5)
    

lf_signup= Canvas(main_frame_signin,width=1366,height=750)
lf_signup.bind("<Configure>", responsive_wid_login)
lf_signup.pack(fill=X)

sign_inlb=Label(lf_signup, text="Sign In",font=('Calibri 30 bold'), fg="black")
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sign_inlb, tag=("sign_inlb"))

nm_ent = Entry(lf_signup, width=25, font=('Calibri 16'))
nm_ent.insert(0,"Username")
nm_ent.bind("<Button-1>",sig_nm)
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=nm_ent, tag=("nm_ent"))

pass_ent = Entry(lf_signup, width=25, font=('Calibri 16'))
pass_ent.insert(0,"Password")
pass_ent.bind("<Button-1>",sig_pass)
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=pass_ent, tag=("pass_ent"))

button = customtkinter.CTkButton(master=main_frame_signin,command=main_sign_in,text="Log In",bg="#213b52")
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=button, tag=("button"))

# #------------------------------------------------------------------------------------------------------------------------left canvas

lf_signup.create_oval(0,0,0,0,fill="#213b52", tag=("round_login"))

img = Label(lf_signup, image = exprefreshIcon,bg="#213b52", width=500, justify=RIGHT)
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=img, tag=("img"))

lft_lab=Label(lf_signup, text="New here ?",font=('Calibri 20 bold'), fg="white", bg="#213b52")
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lft_lab, tag=("lft_lab"))
lft_lab2=Label(lf_signup, text="Join here to start a business with FinsYs!",font=('Calibri 16 bold'), fg="white", bg="#213b52")
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lft_lab2, tag=("lft_lab2"))

btn2 = Button(main_frame_signin, text = 'Sign Up', command = func_sign_up, bg="white", fg="black",borderwidth = 3,height=1,width=10)
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=btn2, tag=("btn2"))

root.mainloop()