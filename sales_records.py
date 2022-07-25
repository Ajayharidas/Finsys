from msilib.schema import ComboBox
from tkinter import *
import tkinter as tk
from tkinter import ttk
from turtle import width,color
from matplotlib import style
from tkcalendar import Calendar
from tkcalendar import DateEntry



root = Tk()
root.title('Finsys - Sales Records')
# root_width = root.winfo_screenwidth()
# root_height = root.winfo_screenheight()
root.geometry("1360x730")

root.grid_columnconfigure(0,weight=1)
root.grid_rowconfigure(0,weight=1)

plus = PhotoImage(file="images/plus.png")
backward = PhotoImage(file="images/back.png")

# Sales Record---------------------
s = ttk.Style()
s.theme_use('clam')
s.configure('TCombobox',fieldbackground="#2f516f",background="#2f516f",foreground='white')


sr_Frame = Frame(root,)
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

    x1 = dwidth/63
    x2 = dwidth/1.021
    y1 = dheight/14 
    y2 = dheight/3.505
    x1pr = dwidth/28.15
    x2mr = dwidth/1.0514
    y1pr = dheight/9.34
    y2mr = dheight/4

    dcanvas.coords("poly1",x1pr,y1,
    x1pr,y1,
    x2mr,y1,
    x2mr,y1,     
    x2,y1,     
    #--------------------
    x2,y1pr,     
    x2,y1pr,     
    x2,y2mr,     
    x2,y2mr,     
    x2,y2,
    #--------------------
    x2mr,y2,     
    x2mr,y2,     
    x1pr,y2,
    x1pr,y2,
    x1,y2,
    #--------------------
    x1,y2mr,
    x1,y2mr,
    x1,y1pr,
    x1,y1pr,
    x1,y1,
    )

    dcanvas.coords("hline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

    x11 = dwidth/63
    x21 = dwidth/1.021
    y11 = dheight/2.8
    y21 = dheight/1.168
    x11pr = dwidth/28.15
    x21mr = dwidth/1.0514
    y11pr = dheight/2.549
    y21mr = dheight/1.219


    dcanvas.coords("poly2",x11pr,y11,
    x11pr,y11,
    x21mr,y11,
    x21mr,y11,     
    x21,y11,     
    #--------------------
    x21,y11pr,     
    x21,y11pr,     
    x21,y21mr,     
    x21,y21mr,     
    x21,y21,
    #--------------------
    x21mr,y21,     
    x21mr,y21,     
    x11pr,y21,
    x11pr,y21,
    x11,y21,
    #--------------------
    x11,y21mr,
    x11,y21mr,
    x11,y11pr,
    x11,y11pr,
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

def close_canvas(event):
    sr_Frame.grid_forget()
    sr_Frame_1 = Frame(root,)
    sr_Frame_1.grid(row=0,column=0,sticky='nsew')

    def responsive_widgets1(event):
        dwidth1 = event.width
        dheight1 = event.height
        dcanvas1 = event.widget

    sr_Canvas_1 = Canvas(sr_Frame_1,bg='#2f516f',scrollregion=(0,0,700,1200))

    sr_Frame_1.grid_columnconfigure(0,weight=1)
    sr_Frame_1.grid_rowconfigure(0,weight=1)

    sr_Scroll_1 = Scrollbar(sr_Frame_1,orient=VERTICAL)
    sr_Scroll_1.grid(row=0,column=1,sticky='ns')
    sr_Scroll_1.config(command=sr_Canvas_1.yview)
    sr_Canvas_1.bind("<Configure>", responsive_widgets1)
    sr_Canvas_1.config(yscrollcommand=sr_Scroll_1.set)
    sr_Canvas_1.grid(row=0,column=0,sticky='nsew')

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
        return sr_Canvas_1.create_polygon(points,**kwargs,smooth=True)


    if sr_transCombo.get() == 'Payment':
        rp_rectangle1 = header_rectangle(20,150,1315,260,radius=20,fill="#1b3857")
        rp_label = Label(sr_Canvas_1,width=18,height=1,text="RECIEVE PAYMENT",font=('arial 25'),background='#1b3857',fg="white")
        sr_Canvas_1.create_window(660,190,anchor="c",window=rp_label)
        sr_Canvas_1.create_line(60,220,1280,220,fill='gray',width=1)

        rp_rectangle2 = header_rectangle(20,320,1315,970,radius=20,fill="#1b3857")

        rp_label1 = Label(sr_Canvas_1,width=18,height=1,text="Fin sYs",font=('arial 25'),background='#1b3857',fg="white")
        sr_Canvas_1.create_window(650,350,anchor="c",window=rp_label1)

        rp_label2 = Label(sr_Canvas_1,width=10,height=1,text="Customer",font=('arial 12'),background='#1b3857',fg="white",anchor='w')

        rp_custCombo = ttk.Combobox(sr_Canvas_1,width=28)
        sr_Canvas_1.create_window(135,432,anchor='nw',window=rp_custCombo)

        rp_plus = Button(sr_Canvas_1,text='',bd=0,image=plus,activebackground='#1b3857',background='#1b3857')
        sr_Canvas_1.create_window(340,442,window=rp_plus)

        rp_label3 = Label(sr_Canvas_1,width=10,height=1,text="Email",font=('arial 12'),background='#1b3857',anchor="w",fg="white")
        sr_Canvas_1.create_window(602,415,window=rp_label3)

        rp_email = Entry(sr_Canvas_1,width=35,background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(555,430,anchor='nw',window=rp_email)

        rp_label4 = Label(sr_Canvas_1,width=20,height=1,text="Find by invoice number",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
        sr_Canvas_1.create_window(1057,415,window=rp_label4)

        rp_invnum = Entry(sr_Canvas_1,width=35,background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(965,430,anchor='nw',window=rp_invnum)

        rp_label5 = Label(sr_Canvas_1,width=20,height=1,text="Payment date",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
        sr_Canvas_1.create_window(228,475,window=rp_label5)

        rp_pdate = DateEntry(sr_Canvas_1,width=33,background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(135,490,anchor='nw',window=rp_pdate)

        rp_label6 = Label(sr_Canvas_1,width=20,height=1,text="Payment method",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
        sr_Canvas_1.create_window(228,535,window=rp_label6)

        rp_pmethod = Entry(sr_Canvas_1,width=35,background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(135,550,anchor='nw',window=rp_pmethod)

        rp_label7 = Label(sr_Canvas_1,width=20,height=1,text="Deposit to",font=('arial 12'),background='#1b3857',fg="white",anchor="nw")
        sr_Canvas_1.create_window(1058,535,window=rp_label7)

        rp_depositto = ttk.Combobox(sr_Canvas_1,width=28)
        sr_Canvas_1.create_window(965,550,anchor='nw',window=rp_depositto)

        rp_plus1 = Button(sr_Canvas_1,text='',bd=0,image=plus,activebackground='#1b3857',background='#1b3857')
        sr_Canvas_1.create_window(1170,560,window=rp_plus1)

        rp_label8 = Label(sr_Canvas_1,width=20,height=1,text="Amount recieved",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
        sr_Canvas_1.create_window(1058,595,window=rp_label8)

        rp_amntre = Entry(sr_Canvas_1,width=35,background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(965,610,anchor='nw',window=rp_amntre)

        rp_label9 = Label(sr_Canvas_1,width=20,height=1,text="AMOUNT RECIEVED",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
        sr_Canvas_1.create_window(1058,655,window=rp_label9)

        rp_label10 = Label(sr_Canvas_1,width=20,height=1,text="0.00",font=('arial 12'),background='#1b3857',fg="white",anchor="w")
        sr_Canvas_1.create_window(1058,685,window=rp_label10)

        sr_Canvas_1.create_line(60,730,1260,730,fill='gray',width=1)
        sr_Canvas_1.create_line(60,770,1260,770,fill='gray',width=1)
        sr_Canvas_1.create_line(60,730,60,770,fill='gray',width=1)
        sr_Canvas_1.create_line(1260,730,1260,770,fill='gray',width=1)
        sr_Canvas_1.create_line(120,730,120,770,fill='gray',width=1)
        sr_Canvas_1.create_line(350,730,350,770,fill='gray',width=1)
        sr_Canvas_1.create_line(520,730,520,770,fill='gray',width=1)
        sr_Canvas_1.create_line(820,730,820,770,fill='gray',width=1)
        sr_Canvas_1.create_line(1070,730,1070,770,fill='gray',width=1)

        rpt_label1 = Label(sr_Canvas_1,width=5,height=1,text="#", font=('arial 10 bold'),background='#1b3857',fg="white") 
        sr_Canvas_1.create_window(90, 750, anchor="c", window=rpt_label1)

        rpt_label2 = Label(sr_Canvas_1,width=15,height=1,text="DESCRIPTION", font=('arial 10 bold'),background='#1b3857',fg="white") 
        sr_Canvas_1.create_window(235, 750, anchor="c", window=rpt_label2)

        rpt_label3 = Label(sr_Canvas_1,width=15,height=1,text="DUE DATE", font=('arial 10 bold'),background='#1b3857',fg="white") 
        sr_Canvas_1.create_window(435, 750, anchor="c", window=rpt_label3)

        rpt_label4 = Label(sr_Canvas_1,width=15,height=1,text="ORIGINAL AMOUNT", font=('arial 10 bold'),background='#1b3857',fg="white") 
        sr_Canvas_1.create_window(670, 750, anchor="c", window=rpt_label4)

        rpt_label5 = Label(sr_Canvas_1,width=15,height=1,text="OPEN BALANCE", font=('arial 10 bold'),background='#1b3857',fg="white") 
        sr_Canvas_1.create_window(945, 750, anchor="c", window=rpt_label5)

        rpt_label6 = Label(sr_Canvas_1,width=15,height=1,text="PAYMENT", font=('arial 10 bold'),background='#1b3857',fg="white") 
        sr_Canvas_1.create_window(1165, 750, anchor="c", window=rpt_label6)

        sr_Canvas_1.create_line(820,800,1260,800,fill='gray',width=1)
        sr_Canvas_1.create_line(820,850,1260,850,fill='gray',width=1)
        sr_Canvas_1.create_line(820,900,1260,900,fill='gray',width=1)
        sr_Canvas_1.create_line(820,800,820,900,fill='gray',width=1)
        sr_Canvas_1.create_line(1000,800,1000,900,fill='gray',width=1)
        sr_Canvas_1.create_line(1260,800,1260,900,fill='gray',width=1)

        rpt_label7 = Label(sr_Canvas_1,width=15,height=1,text="Amount to Apply", font=('arial 10 bold'),background='#1b3857',fg="white") 
        sr_Canvas_1.create_window(910, 825, anchor="c", window=rpt_label7)  

        rp_amnttoapply = Entry(sr_Canvas_1,width=35,background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(1130,825,anchor='c',window=rp_amnttoapply)   

        rpt_label8 = Label(sr_Canvas_1,width=15,height=1,text="Amount to Credit", font=('arial 10 bold'),background='#1b3857',fg="white") 
        sr_Canvas_1.create_window(910, 875, anchor="c", window=rpt_label8)  

        rp_amnttocredit = Entry(sr_Canvas_1,width=35,background='#2f516f',foreground='white')
        sr_Canvas_1.create_window(1130,875,anchor='c',window=rp_amnttocredit)   

        def goBack():
            sr_Frame_1.grid_forget()
            sr_Frame.grid(row=0,column=0,sticky='nsew')

        back_btn = Button(sr_Canvas_1,text='←  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=lambda:goBack())
        sr_Canvas_1.create_window(1260,130,window=back_btn) 
    else:
        pass
    


sr_transCombo = ttk.Combobox(sr_Canvas,)
sr_transCombo['values'] = ['New Transactios','Invoice','Payment','Sales Receipt','Credit Note','Estimate','Delayed Charge','Time Activity']
sr_transCombo.current(0)
sr_transCombo.bind('<<ComboboxSelected>>',close_canvas)
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
srt_label3 = Label(sr_Canvas,width=11,height=1,text="NO.", font=('arial 10 bold'),background="#1b3857",fg="white") 
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

# data_list = [('02-07-2022','phone',1,'Mahesh','07-07-2022','10000','20000','400','10400'),
# ('02-07-2022','phone',1,'Mahesh','07-07-2022','10000','20000','400','10400')]

# a = 0
# for i in data_list:
#     for j in range(len(i)):
#         T_label = Label(sr_Canvas,width=8,fg='white',background='#1b3857',text=i[j],relief='ridge',anchor='w')
#         T_label.grid(row=a,column=j)
# a += 1
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