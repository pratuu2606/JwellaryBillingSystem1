from tkinter import *
import MySQLdb

from tkcalendar import DateEntry
from tkinter import ttk
from tkinter .messagebox import *
import random
root=Tk()
root.title("Raviraj Jwellers Bill")
img=PhotoImage(file='D:\jwellary billing system\Bill Mini Project\Bill.png')
lblimg=Label(root,image=img)
lblimg.pack()
root.geometry("2000x1800")
def insert():
    conn=MySQLdb.connect(host="localhost",user="root",database="billdb",password="manager")
    cur=conn.cursor()
    cur.execute("use billdb")
    query=f"insert into jbill (name,bill_no,date,address,jwellery_type,item,quantity,method,amount)values('{e1.get()}','{e2.get()}','{cal.get()}','{e4.get()}','{s.get()}','{s1.get()}','{s2.get()}','{sal2.get()}','{b6.get()}');"
    cur.execute(query)
    conn.commit()
    showinfo("record","record added successfully..")
#function for entering same value in two entries amount entries
def same(*args):    
    amt2_var.set(amt1.get())
#function for two entris gross wt and net wt
def update(*args):   
    en2_var.set(en1.get())

f1=Frame(root,borderwidth=4,relief=SUNKEN,bg="pink",padx=400,pady=400)
f1.pack(fill=X)
l1=Label(root,text="JWELLERY SALES",fg="black",bg="white",font=("times new roman",20,"bold"))
l1.pack()
l2=Label(root,text="Name  :",fg="black",font=("vardana",10,"bold"))
l2.place(x=40,y=200)
e1=Entry(root,font=("vardana",10,"bold"),fg="black")
e1.place(x=100,y=200)
l4=Label(root,text="No  : ",fg="black",font=("vardana",10,"bold"))
l4.place(x=900,y=180)
e2=Entry(root,fg="black",font=("vardana",10,"bold"))
e2.place(x=950,y=180)
#
def generate_random_bill_number():
        # Generate a random bill number
        random_bill_number = random.randint(100000, 999999)  # Adjust range as needed
        # Update the entry box
        e2.delete(0,END)  # Clear the current entry
        e2.insert(0, str(random_bill_number))  # Insert the new bill number

generate_button = Button(root, text="Generate Bill Number",fg="black",font=("vardana",10,"") ,command=generate_random_bill_number)
generate_button.place(x=1100,y=180)


l6=Label(root,text="Date  :",fg="black",font=("vardana",10,"bold"))
l6.place(x=900,y=205)
#adding a calendar 
cal = DateEntry(root, date_pattern="dd-mm-yyyy")
cal.place(x=950,y=205)
selected_date = cal.get()
print(f"Selected date: {selected_date}")
l8=Label(root,text="Address  : ",fg="black",font=("vardana",10,"bold"))
l8.place(x=40,y=230)
e4=Entry(root,fg="black",font=("vardana",10,"bold"))
e4.place(x=120,y=230)
l10=Label(root,text="pure rate : ",fg="black",font=("vardana",10,"bold"))
l10.place(x=900,y=230)
e5=Entry(root,fg="black",font=("vardana",10,"bold"))
e5.place(x=965,y=230)
c1=Canvas(root,height=450,width=450)
c1.pack()
c1.create_line(10,10,1500,10,width=1)
c1.pack(fill=X,expand=TRUE)
la1=Label(c1,text="Particulars",font=("vardana",13,"bold"))
la1.place(x=20,y=15)
la2=Label(c1,text="Pcs.",font=("vardana",13,"bold"))
la2.place(x=220,y=15)
la3=Label(c1,text="Gross wt.",font=("vardana",13,"bold"))
la3.place(x=330,y=15)
la4=Label(c1,text="Net wt.",font=("vardana",13,"bold"))
la4.place(x=460,y=15)
la5=Label(c1,text="Rate",font=("vardana",13,"bold"))
la5.place(x=580,y=15)
la6=Label(c1,text="Amount",font=("vardana",13,"bold"))
la6.place(x=700,y=15)
c1.create_line(10,40,1500,40,width=1)
c1.pack(fill=X,expand=TRUE)
#
siz=["Gold","Silver","Diamond","Pearl"]
s=ttk.Combobox(root,value=siz)
s.place(x=5,y=340)
size=["Payal","Chokar","Bracelet","Necklace","Ring","Earings"]
s1=ttk.Combobox(root,value=size)
s1.place(x=10,y=370)
size1=[1,2,3,4,5,6,7,8,9,10]
s2=ttk.Combobox(root,value=size1)
s2.place(x=165,y=340)
#code for entering same value in net wt. and gross wt. columns
en1_var=StringVar()
en2_var=StringVar()
en1=Entry(c1,fg="black",textvariable=en1_var,font=("vardana",10,""))
en1.place(x=330,y=45)
en2=Entry(c1,fg="black",textvariable=en2_var,font=("vardana",10,""))
en2.place(x=470,y=45)
#binding the two entries
en1_var.trace_add("write", update)
en3=Entry(c1,fg="black",font=("vardana",10,""))
en3.place(x=580,y=45)
c1.create_line(10,140,1500,140,width=1)
c1.pack(fill=X,expand=TRUE)
#function to calculate gst on a perticular amount
def calculate_gst(*args):
    try:
        amount = float(amount_var.get())
        gst_rate = float(gst_rate_var.get())
        gst_amount = amount * (gst_rate / 100)
        total_amount = amount + gst_amount       
        gst_var.set(f"{gst_amount:.2f}")
        total_var.set(f"{total_amount:.2f}")
    except ValueError:
        gst_var.set("Invalid input")
        total_var.set("Invalid input")
# creating instances for calculating gst 
amount_var = StringVar()
gst_rate_var = StringVar()
gst_var = StringVar()
total_var = StringVar()
# Binding to call calculate_gst
amount_var.trace("w", calculate_gst)
gst_rate_var.trace("w", calculate_gst)
labe2=Label(c1,text="Amount :",font=("vardana",10,""))
labe2.place(x=590,y=145)
labe3=Entry(c1, textvariable=amount_var,font=("vardana",10,""))
labe3.place(x=700,y=145)
g1=Label(c1,text="Payment Method :",font=("vardana",10,""))
g1.place(x=20,y=150)
sa2=["By Cash","By Cheque","By Card","By Online Method",]
sal2=ttk.Combobox(c1,value=sa2)
sal2.place(x=140,y=150)
a2=Label(c1,text="GST Rate (%) : ",font=("vardana",10,""))
a2.place(x=590,y=170)
am=Entry(c1,textvariable=gst_rate_var,font=("vardana",10,""))
am.place(x=700,y=170)
b3=Label(c1,text="GST Amount :",font=("vardana",10,""))
b3.place(x=590,y=210)
b4=Entry(c1,textvariable=gst_var,font=("vardana",10,""))
b4.place(x=700,y=210)
b5=Label(c1,text="Total Amount:",font=("vardana",10,""))
b5.place(x=590,y=240)
b6=Entry(c1,textvariable=total_var,font=("vardana",10,"bold"))
b6.place(x=700,y=240)
#code to enter same amount in 2 entries
amt1_var = StringVar()
amt2_var = StringVar()
amt1=Entry(c1,fg="black",textvariable=amt1_var,font=("vardana",10,""))
amt1.place(x=710,y=45)
amt2=Entry(c1,textvariable=amt2_var,font=("vardana",10,""))
amt2.place(x=20,y=210)
# Bind the same function with amt entries
amt1_var.trace_add("write", same)
c1.create_line(10,300,1500,300,width=1)
c1.pack(fill=X,expand=TRUE)
b7=Label(c1,text="SATURDAY CLOSE ",fg="maroon",font=("vardana",10,"bold"))
b7.place(x=330,y=310)
b8=Label(c1,text="CUSTOMER'S SIGN ",fg="maroon",font=("vardana",10,"bold"))
b8.place(x=510,y=310)
b9=Label(c1,text="FOR RAVIRAJ JWELLERS ",fg="maroon",font=("vardana",10,"bold"))
b9.place(x=700,y=310)
c1.create_line(10,360,1500,360,width=1,fill="maroon")
c1.pack(fill=X,expand=TRUE)
b10=Label(c1,text= "THANK YOU FOR VISITING US !",fg="red",font=("vardana",10,"bold"))
b10.place(x=460,y=380)
btn1=Button(root,text="Save & Print",bg="pink",fg="black",font=("vardana",12,"bold"),command=insert)
btn1.place(x=680,y=680)
root.mainloop()