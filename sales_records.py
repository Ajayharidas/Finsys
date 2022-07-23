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

s = ttk.Style()
s.theme_use('clam')
s.configure('TCombobox',fieldbackground="#2f516f",background="#2f516f",foreground='white')


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


sr_Frame = Frame(root,)
sr_Frame.grid(row=0,column=0,sticky='nsew')
sr_Canvas = Canvas(sr_Frame,bg='#2f516f',scrollregion=(0,0,700,1200))

sr_Frame.grid_rowconfigure(0,weight=1)
sr_Frame.grid_columnconfigure(0,weight=1)

sr_Scroll = Scrollbar(sr_Frame,orient=VERTICAL)
sr_Scroll.grid(row=0,column=1,sticky='ns')
sr_Scroll.config(command=sr_Canvas.yview)
sr_Canvas.config(width=600,height=720)

sr_Canvas.config(yscrollcommand=sr_Scroll.set)
sr_Canvas.grid(row=0,column=0,sticky='nsew')

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



sr_rectangle1 = header_rectangle(20,50,1315,200,radius=20,fill="#1b3857")
sr_label = Label(sr_Canvas,width=15,height=1,text="SALES RECORDS",font=('arial 25'),background="#1b3857",fg="white")
sr_label_win = sr_Canvas.create_window(550,85,anchor="nw",window=sr_label)
sr_Canvas.create_line(60,150,1280,150,fill='gray',width=1)

sr_rectangle2 = header_rectangle(20,250,1315,600,radius=20,fill="#1b3857")

def close_canvas(event):
    sr_Frame.place_forget()
    sr_Frame_1 = Frame(root,)
    sr_Frame_1.grid(row=0,column=0,sticky='nsew')
    sr_Canvas_1 = Canvas(sr_Frame_1,bg='#2f516f',scrollregion=(0,0,700,1200))

    sr_Frame_1.grid_columnconfigure(0,weight=1)
    sr_Frame_1.grid_rowconfigure(0,weight=1)

    sr_Scroll_1 = Scrollbar(sr_Frame_1,orient=VERTICAL)
    sr_Scroll_1.grid(row=0,column=1,sticky='ns')
    sr_Scroll_1.config(command=sr_Canvas_1.yview)

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
            sr_Frame_1.place_forget()
            sr_Frame.place(x=2,y=0)

        back_btn = Button(sr_Canvas_1,text='←  Back',font=('arial 10 bold'),bd=0,activebackground='#2f516f',foreground='white',background='#2f516f',command=goBack)
        sr_Canvas_1.create_window(1260,130,window=back_btn) 
    else:
        pass
    


sr_transCombo = ttk.Combobox(sr_Canvas,)
sr_transCombo['values'] = ['New Transactios','Invoice','Payment','Sales Receipt','Credit Note','Estimate','Delayed Charge','Time Activity']
sr_transCombo.current(0)
sr_transCombo.bind('<<ComboboxSelected>>',close_canvas)
sr_transCombo_win = sr_Canvas.create_window(1220,310,window=sr_transCombo)


sr_Canvas.create_line(40, 350, 1295, 350, fill='gray',width=1)
sr_Canvas.create_line(40, 350, 40, 550, fill='gray',width=1)
sr_Canvas.create_line(40, 430, 1295, 430, fill='gray',width=1)
sr_Canvas.create_line(40, 470, 1295, 470, fill='gray',width=1)
sr_Canvas.create_line(40, 510, 1295, 510, fill='gray',width=1)
sr_Canvas.create_line(40, 550, 1295, 550, fill='gray',width=1)
sr_Canvas.create_line(160, 350, 160, 550, fill='gray',width=1)
sr_Canvas.create_line(310, 350, 310, 550, fill='gray',width=1)
sr_Canvas.create_line(430, 350, 430, 550, fill='gray',width=1)
sr_Canvas.create_line(590, 350, 590, 550, fill='gray',width=1)
sr_Canvas.create_line(710, 350, 710, 550, fill='gray',width=1)
sr_Canvas.create_line(840, 350, 840, 550, fill='gray',width=1)
sr_Canvas.create_line(970, 350, 970, 550, fill='gray',width=1)
sr_Canvas.create_line(1060, 350, 1060, 550, fill='gray',width=1)
sr_Canvas.create_line(1190, 350, 1190, 550, fill='gray',width=1)
sr_Canvas.create_line(1295, 350, 1295, 550, fill='gray',width=1)
sr_Canvas.create_line(40, 390, 1295, 390, fill='gray',width=1)

srt_dateLabel = Label(sr_Canvas,width=13,height=1,text="23-07-2022", font=('arial 10'),background="#1b3857",fg="white") 
sr_Canvas.create_window(100, 410, anchor="c", window=srt_dateLabel)

srt_typeLabel = Label(sr_Canvas,width=15,height=1,text="Payment", font=('arial 10'),background="#1b3857",fg="white") 
sr_Canvas.create_window(235, 410, anchor="c", window=srt_typeLabel)

srt_noLabel = Label(sr_Canvas,width=13,height=1,text="1010", font=('arial 10'),background="#1b3857",fg="white") 
sr_Canvas.create_window(370, 410, anchor="c", window=srt_noLabel)

srt_custLabel = Label(sr_Canvas,width=18,height=1,text="Nithin", font=('arial 10'),background="#1b3857",fg="white") 
sr_Canvas.create_window(510, 410, anchor="c", window=srt_custLabel)

srt_dueLabel = Label(sr_Canvas,width=13,height=1,text="30-07-2022", font=('arial 10'),background="#1b3857",fg="white") 
sr_Canvas.create_window(650, 410, anchor="c", window=srt_dueLabel)

srt_balLabel = Label(sr_Canvas,width=14,height=1,text="1000", font=('arial 10'),background="#1b3857",fg="white") 
sr_Canvas.create_window(775, 410, anchor="c", window=srt_balLabel)

srt_totbLabel = Label(sr_Canvas,width=14,height=1,text="1500", font=('arial 10'),background="#1b3857",fg="white") 
sr_Canvas.create_window(905, 410, anchor="c", window=srt_totbLabel)

srt_taxLabel = Label(sr_Canvas,width=9,height=1,text="100", font=('arial 10'),background="#1b3857",fg="white") 
sr_Canvas.create_window(1015, 410, anchor="c", window=srt_taxLabel)

srt_totLabel = Label(sr_Canvas,width=14,height=1,text="1000", font=('arial 10'),background="#1b3857",fg="white") 
sr_Canvas.create_window(1125, 410, anchor="c", window=srt_totLabel)

srt_actionCombo = ttk.Combobox(sr_Canvas,width=10)
srt_actionCombo['values'] = ['Actions','Edit','Delete','View']
srt_actionCombo.current(0)
sr_Canvas.create_window(1243,410,window=srt_actionCombo)

srt_label1 = Label(sr_Canvas,width=10,height=1,text="DATE", font=('arial 10 bold'),background="#1b3857",fg="white") 
srt_winlabel1 = sr_Canvas.create_window(100, 370, anchor="c", window=srt_label1)
srt_label2 = Label(sr_Canvas,width=11,height=1,text="TYPE", font=('arial 10 bold'),background="#1b3857",fg="white") 
srt_winlabel2 = sr_Canvas.create_window(235, 370, anchor="c", window=srt_label2)
srt_label3 = Label(sr_Canvas,width=11,height=1,text="NO.", font=('arial 10 bold'),background="#1b3857",fg="white") 
srt_winlabel3 = sr_Canvas.create_window(370, 370, anchor="c", window=srt_label3)
srt_label4 = Label(sr_Canvas,width=11,height=1,text="CUSTOMER", font=('arial 10 bold'),background="#1b3857",fg="white") 
srt_winlabel4 = sr_Canvas.create_window(510, 370, anchor="c", window=srt_label4)
srt_label5 = Label(sr_Canvas,width=11,height=1,text="DUE DATE", font=('arial 10 bold'),background="#1b3857",fg="white") 
srt_winlabel5 = sr_Canvas.create_window(650, 370, anchor="c", window=srt_label5)
srt_label6 = Label(sr_Canvas,width=11,height=1,text="BALANCE", font=('arial 10 bold'),background="#1b3857",fg="white") 
srt_winlabel6 = sr_Canvas.create_window(775, 370, anchor="c", window=srt_label6)
srt_label7 = Label(sr_Canvas,width=12,height=1,text="TOTAL BEFORE", font=('arial 10 bold'),background="#1b3857",fg="white") 
srt_winlabel7 = sr_Canvas.create_window(905, 370, anchor="c", window=srt_label7)
srt_label8 = Label(sr_Canvas,width=10,height=1,text="TAX", font=('arial 10 bold'),background="#1b3857",fg="white") 
srt_winlabel8 = sr_Canvas.create_window(1015, 370, anchor="c", window=srt_label8)
srt_label9 = Label(sr_Canvas,width=11,height=1,text="TOTAL", font=('arial 10 bold'),background="#1b3857",fg="white") 
srt_winlabel9 = sr_Canvas.create_window(1125, 370, anchor="c", window=srt_label9)
srt_label10 = Label(sr_Canvas,width=10,height=1,text="ACTION", font=('arial 10 bold'),background="#1b3857",fg="white") 
srt_winlabel10 = sr_Canvas.create_window(1242, 370, anchor="c", window=srt_label10)


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