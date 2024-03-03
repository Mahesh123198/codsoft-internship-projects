from tkinter import *
import math

def click(value):
    ex=entryfield.get()
    # answer=''
    try:
        if value=="C":
            ex=ex[0:len(ex)-1]#delete the only one number for single click..
            entryfield.delete(0,END)
            entryfield.insert(0,ex)
            return
        elif value=="CE":
            entryfield.delete(0,END)# here click onec delete the all the values.
        elif value=="√":
            answer=math.sqrt(eval(ex))
        elif value=="π":
            answer=math.pi
        elif value=="cosΘ":
            answer=math.cos(math.radians(eval(ex)))
        elif value=="tanΘ":
            answer=math.tan(math.radians(eval(ex)))
        elif value=="sinΘ":
            answer=math.sin(math.radians(eval(ex)))
        elif value=="2π":
            answer=2*math.pi
        elif value=="cosh":
            answer=math.cosh(eval(ex))
        elif value=="tanh":
            answer=math.tanh(eval(ex))
        elif value=="sinh":
            answer=math.sinh(eval(ex))
        elif value==chr(8731):
            answer=eval(ex)**(1/3)
        elif value=="x\u02b8":
            entryfield.insert(END,"**")
            return
        elif value=="x\u00b3":
            answer=eval(ex)**3
        elif value=="x\u00b2":
            answer=eval(ex)**2
        elif value=="ln":
            answer=math.log2(eval(ex))
        elif value=="deg":
            answer=math.degrees(eval(ex))
        elif value=="rad":
            answer=math.radians(eval(ex))
        elif value=="e":
            answer=math.e
        elif value=="log10":
            answer=math.log10(eval(ex))
        elif value=="x!":
            answer=math.factorial(eval(ex))
        elif value==chr(247):#7/2=3.5
            entryfield.insert(END,"/")
            return
        elif value=="=":
            answer=eval(ex)
        else:
            entryfield.insert(END,value)
            return

        entryfield.delete(0,END)
        entryfield.insert(0,answer)
    except SyntaxError:
        pass       

root=Tk()
root.title("caluculator")
root.geometry("680x500+100+100")
root.config(bg="lightblue")

logoimage=PhotoImage(file='calculator.png')
label=Label(root,image=logoimage,bg="lightblue")
label.grid(row=0,column=0)

entryfield=Entry(root,font=('arial',20,'bold'), bg="lightblue", bd=10, relief=SUNKEN, width=30, fg="white")
entryfield.grid(row=0,column=0,columnspan=8)

micphone=PhotoImage(file='microphone.png')
button=Button(root,image=micphone,bg="lightblue",activebackground="lightblue")
button.grid(row=0,column=7)
rowvalue=1
columnvalue=0

button_text_list=["C","CE","√","+","π","cosΘ","tanΘ","sinΘ",
                  "1","2","3","-","2π","cosh","tanh","sinh",
                  "4","5","6","*",chr(8731),"x\u02b8","x\u00b3","x\u00b2",
                  "7","8","9",chr(247),"ln","deg","rad","e",
                  "0",".","%","=","log10","(",")","x!"]

for i in button_text_list:
    button=Button(root,width=5,height=2,bd=2,text=i,bg="lightblue",font=('arial',18,'bold'),fg='white',relief=SUNKEN,
                  activebackground='lightblue', command=lambda button=i:click(button))
    button.grid(row=1,column=0)
    button.grid(row=rowvalue,column=columnvalue)
    columnvalue+=1
    if columnvalue>7:
        rowvalue+=1
        columnvalue=0

mainloop()


