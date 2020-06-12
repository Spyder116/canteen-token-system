from tkinter import*
import time
import random

root=Tk()
root.geometry("1600x700+0+0")
root.title("CANTEEN TOKEN SYSTEM")

top=Frame(root,bg="white",width=1600,height=50,relief=SUNKEN)
top.pack(side=TOP)

f1=Frame(root,width=900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

#-------Time-------#
localtime=time.asctime(time.localtime(time.time()))
#-------top--------#
h1=Label(top,font=('aria',30,'bold'),text="CANTEEN TOKEN SYSTEM",fg="steel blue",bd=10,anchor='w')
h1.grid(row=0,column=0)
h2=Label(top,font=('aria',20,),text=localtime,fg="steel blue",anchor="w")
h2.grid(row=1,column=0)
#--------------------------------------------
def Ref():
    x=random.randint(12980,50876)
    randomRef=str(x)
    rand.set(randomRef)

    coi=float(idli.get())
    cod=float(dosa.get())
    cop=float(poori.get())
    com=float(meals.get())
    copp=float(parota.get())
    coe=float(eggrice.get())
    cov=float(vegrice.get())
    codr=float(drinks.get())

    costofidli=coi*30
    costofdosa=cod*30
    costofpoori=cop*30
    costofmeals=com*50
    costofparota=copp*40
    costofeggrice=coe*45
    costofvegrice=cov*40
    costofdrinks=codr*20

    cost=(costofidli+costofdosa+costofpoori+costofmeals+costofparota+costofeggrice+costofvegrice+costofdrinks)

    totalcost.set(cost)
def reset():
    rand.set("")
    idli.set("")
    dosa.set("")
    poori.set("")
    meals.set("")
    parota.set("")
    eggrice.set("")
    vegrice.set("")
    drinks.set("")
    totalcost.set("")

def qexit():
    root.destroy()

        
    

#--------------------------------------------
rand=StringVar()
idli=StringVar()
dosa=StringVar()
poori=StringVar()
meals=StringVar()
parota=StringVar()
eggrice=StringVar()
vegrice=StringVar()
drinks=StringVar()
totalcost=StringVar()


lbltoken=Label(f1,font=('aria',16,'bold'),text="token no.",fg="steel blue",bd=10,anchor='w')
lbltoken.grid(row=0,column=0)
txttoken=Entry(f1,font=('ariel',16,'bold'),textvariable=rand,bd=6,insertwidth=4,bg="powder blue",justify='right')
txttoken.grid(row=0,column=1)

lblidli=Label(f1,font=('aria',16,'bold'),text="Idli",fg="steel blue",bd=10,anchor='w')
lblidli.grid(row=1,column=0)
txtidli=Entry(f1,font=('ariel',16,'bold'),textvariable=idli,bd=6,insertwidth=4,bg="powder blue",justify='right')
txtidli.grid(row=1,column=1)

lbldosa=Label(f1,font=('aria',16,'bold'),text="Dosa",fg="steel blue",bd=10,anchor='w')
lbldosa.grid(row=2,column=0)
txtdosa=Entry(f1,font=('ariel',16,'bold'),textvariable=dosa,bd=6,insertwidth=4,bg="powder blue",justify='right')
txtdosa.grid(row=2,column=1)

lblpoori=Label(f1,font=('aria',16,'bold'),text="Poori",fg="steel blue",bd=10,anchor='w')
lblpoori.grid(row=3,column=0)
txtpoori=Entry(f1,font=('ariel',16,'bold'),textvariable=poori,bd=6,insertwidth=4,bg="powder blue",justify='right')
txtpoori.grid(row=3,column=1)

lblmeals=Label(f1,font=('aria',16,'bold'),text="Meals",fg="steel blue",bd=10,anchor='w')
lblmeals.grid(row=4,column=0)
txtmeals=Entry(f1,font=('ariel',16,'bold'),textvariable=meals,bd=6,insertwidth=4,bg="powder blue",justify='right')
txtmeals.grid(row=4,column=1)

#-----------------------------------------------------

lblparota=Label(f1,font=('aria',16,'bold'),text="Parota",fg="steel blue",bd=10,anchor='w')
lblparota.grid(row=0,column=2)
txtparota=Entry(f1,font=('ariel',16,'bold'),textvariable=parota,bd=6,insertwidth=4,bg="powder blue",justify='right')
txtparota.grid(row=0,column=3)

lbleggrice=Label(f1,font=('aria',16,'bold'),text="Eggrice",fg="steel blue",bd=10,anchor='w')
lbleggrice.grid(row=1,column=2)
txteggrice=Entry(f1,font=('ariel',16,'bold'),textvariable=eggrice,bd=6,insertwidth=4,bg="powder blue",justify='right')
txteggrice.grid(row=1,column=3)

lblvegrice=Label(f1,font=('aria',16,'bold'),text="Vegrice",fg="steel blue",bd=10,anchor='w')
lblvegrice.grid(row=2,column=2)
txtvegrice=Entry(f1,font=('ariel',16,'bold'),textvariable=vegrice,bd=6,insertwidth=4,bg="powder blue",justify='right')
txtvegrice.grid(row=2,column=3)

lbldrinks=Label(f1,font=('aria',16,'bold'),text="Drink",fg="steel blue",bd=10,anchor='w')
lbldrinks.grid(row=3,column=2)
txtdrinks=Entry(f1,font=('ariel',16,'bold'),textvariable=drinks,bd=6,insertwidth=4,bg="powder blue",justify='right')
txtdrinks.grid(row=3,column=3)

lbltotal=Label(f1,font=('aria',16,'bold'),text="Totalcost",fg="steel blue",bd=10,anchor='w')
lbltotal.grid(row=4,column=2)
txttotal=Entry(f1,font=('ariel',16,'bold'),textvariable=totalcost,bd=6,insertwidth=4,bg="powder blue",justify='right')
txttotal.grid(row=4,column=3)
#-----------------buttons----------------
btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="powder blue",command=Ref)
btnTotal.grid(row=7, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="powder blue",command=reset)
btnreset.grid(row=7, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="powder blue",command=qexit)
btnexit.grid(row=7, column=3)

name=Label(f1,font=('aria',30,'bold'),text="-by Saiteja Damaraju",fg="black",bd=10,anchor="w")
name.grid(row=8,columnspan=2)


def price():
    roo = Tk()
    roo.geometry("600x400+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="idli", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="RS.30/-", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="dosa", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Rs.30/-", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="poori", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Rs.30/-", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="meals", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Rs.50/-", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="parota", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Rs.40/-", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="eggrice", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Rs.45/-", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="vegrice", fg="steel blue", anchor=W)
    lblinfo.grid(row=7, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Rs.40/-", fg="steel blue", anchor=W)
    lblinfo.grid(row=7, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="drinks", fg="steel blue", anchor=W)
    lblinfo.grid(row=8, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Rs.20/-", fg="steel blue", anchor=W)
    lblinfo.grid(row=8, column=3)

    roo.mainloop()
btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="powder blue",command=price)
btnprice.grid(row=7, column=0)

root.mainloop()










