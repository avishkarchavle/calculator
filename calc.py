import tkinter
from tkinter import*
from tkinter import messagebox


val=""
A=0
operator=""
# numbers
def btn1isclicked():
    global val
    val=val+"1"
    data.set(val)

def btn2isclicked():
    global val
    val=val+"2"
    data.set(val)

def btn3isclicked():
    global val
    val=val+"3"
    data.set(val)

def btn4isclicked():
    global val
    val=val+"4"
    data.set(val)

def btn5isclicked():
    global val
    val=val+"5"
    data.set(val)

def btn6isclicked():
    global val
    val=val+"6"
    data.set(val)

def btn7isclicked():
    global val
    val=val+"7"
    data.set(val)

def btn8isclicked():
    global val
    val=val+"8"
    data.set(val)

def btn9isclicked():
    global val
    val=val+"9"
    data.set(val)

def btn0isclicked():
    global val
    val=val+"0"
    data.set(val)



def btnplusclicked():
    global A
    global operator
    global val
    A=int(val)
    operator="+"
    val=val + "+"
    data.set(val)

def btnminusclicked():
    global A
    global operator
    global val
    A=int(val)
    operator="-"
    val=val + "-"
    data.set(val)

def btnmulclicked():
    global A
    global operator
    global val
    A=int(val)
    operator="*"
    val=val + "*"
    data.set(val)

def btndivsclicked():
    global A
    global operator
    global val
    A=int(val)
    operator="/"
    val=val + "/"
    data.set(val)

def cisclicked():
    global A
    global operator
    global val
    val=""
    A=0
    operator=""
    data.set(val),
    command=cisclicked,


def result():
    global A
    global operator
    global val
    val2=val
    if operator == "+":
        x=int((val2.split("+")[1]))
        C=A+x
        data.set(C)
        val=str(C)
    elif operator=="-":
        x=int((val2.split("-")[1]))
        C=A-x
        data.set(C)
        val=str(C)
    elif operator=="*":
        x=int((val2.split("*")[1]))
        C=A*x
        data.set(C)
        val=str(C)
    elif operator=="/":
        x=int((val2.split("/")[1]))
        if x==0:
            messagebox.showerror("ERROR,devision by 0 not allowed")
            A=""
            val=""
            data.set(val)
        else:
            C=int(A/x)
            data.set(C)
            val=str(C)




root=tkinter.Tk()
root.geometry("250x400+300+300")
# root.resizable(0,0)
root.title("CALCULATOR")


data=StringVar()

lbl=Label(
    root,
    text="label",
    anchor=SE,
    font=("verdana",20),
    textvariable=data,
    background="#ffffff",
    fg="#000000"
)
lbl.pack(expand=True,fill="both")

btnrow1=Frame(root,bg="#000000")
btnrow1.pack(expand = True,fill = "both",)


btnrow2=Frame(root)
btnrow2.pack(expand=True,fill="both")

btnrow3=Frame(root)
btnrow3.pack(expand=True,fill="both")

btnrow4=Frame(root)
btnrow4.pack(expand=True,fill="both")
# row1
btn1 =Button(
    btnrow1,
    text="1",
    font=("verdana",22),
    relief=GROOVE,
    border=0,
    command=btn1isclicked,
)
btn1.pack(side=LEFT,expand=True,fill="both",)

btn2 =Button(
    btnrow1,
    text="2",
    font=("verdana",22),
    relief=GROOVE,
    border=0,
    command=btn2isclicked,
)
btn2.pack(side=LEFT,expand=True,fill="both",)

btn3 =Button(
    btnrow1,
    text="3",
    font=("verdana",22),
    relief=GROOVE,
    border=0,
    command=btn3isclicked,
)
btn3.pack(side=LEFT,expand=True,fill="both",)

btnplus =Button(
    btnrow1,
    text="+",
    font=("verdana",22),
    relief=GROOVE,
    border=0,
    command= btnplusclicked,
    
)
btnplus.pack(side=LEFT,expand=True,fill="both",)

# row2

btn4 =Button(
    btnrow2,
    text="4",
    font=("verdana",22),
    relief=GROOVE,
    border=0,
    command=btn4isclicked,
)
btn4.pack(side=LEFT,expand=True,fill="both",)

btn5 =Button(
    btnrow2,
    text="5",
    font=("verdana",22),
    relief=GROOVE,
    border=0,
    command=btn5isclicked,
)
btn5.pack(side=LEFT,expand=True,fill="both",)

btn6 =Button(
    btnrow2,
    text="6",
    font=("verdana",22),
    relief=GROOVE,
    border=0,
    command=btn6isclicked,
)
btn6.pack(side=LEFT,expand=True,fill="both",)

btnminus =Button(
    btnrow2,
    text="-",
    font=("verdana",22),
    relief=GROOVE,
    border=0,
    command=btnminusclicked,
)
btnminus.pack(side=LEFT,expand=True,fill="both",)
# row3

btn7 =Button(
    btnrow3,
    text="7",
    font=("verdana",22),
    relief=GROOVE,
    border=0,
    command=btn7isclicked,
)
btn7.pack(side=LEFT,expand=True,fill="both",)

btn8 =Button(
    btnrow3,
    text="8",
    font=("verdana",22),
    relief=GROOVE,
    border=0,
    command=btn8isclicked,
)
btn8.pack(side=LEFT,expand=True,fill="both",)

btn9 =Button(
    btnrow3,
    text="9",
    font=("verdana",22),
    relief=GROOVE,
    border=0,
    command=btn9isclicked,
)
btn9.pack(side=LEFT,expand=True,fill="both",)

btnmul =Button(
    btnrow3,
    text="*",
    font=("verdana",22),
    relief=GROOVE,
    border=0,
    command=btnmulclicked,
)
btnmul.pack(side=LEFT,expand=True,fill="both",)

# btn4

btnc =Button(
    btnrow4,
    text="C",
    font=("verdana",22),
    relief=GROOVE,
    border=0,
     command=cisclicked,
)
btnc.pack(side=LEFT,expand=True,fill="both",)

btn0 =Button(
    btnrow4,
    text="0",
    font=("verdana",22),
    relief=GROOVE,
    border=0,
    command=btn0isclicked,
)
btn0.pack(side=LEFT,expand=True,fill="both",)

btneq =Button(
    btnrow4,
    text="=",
    font=("verdana",22),
    relief=GROOVE,
    border=0,
    command=result,
    
)
btneq.pack(side=LEFT,expand=True,fill="both",)

btndiv =Button(
    btnrow4,
    text="/",
    font=("verdana",22),
    relief=GROOVE,
    border=0,
    command=btndivsclicked,
)
btndiv.pack(side=LEFT,expand=True,fill="both",)


# for running
root.mainloop()