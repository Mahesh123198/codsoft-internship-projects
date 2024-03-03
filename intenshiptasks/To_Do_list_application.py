from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self,  root):
        self.root=root
        self.root.title("To do LIst")

        self.label=Label(self.root, text="To-DO-LIST-APP", font="ariel, 25 bold", width=18, bd=5, bg="pink", fg="black")
        self.label.pack(side='top',fill=BOTH)
        self.label2=Label(self.root, text="Add task", font="ariel, 18 bold", width=18, bd=5, bg="pink", fg="black")
        self.label2.place(x=40,y=70)

        self.label3=Label(self.root, text="Task", font="arial, 18 bold", width=18, bd=5, bg="pink", fg="black")
        self.label3.place(x=800,y=70)

        self.main_text=Listbox(self.root, height=9, width=60, bd=5, font="ariel, 20 italic bold")
        self.main_text.place(x=500,y=120)

        self.text=Text(self.root,bd=5, height=2, width=50, font="ariel, 10 bold")
        self.text.place(x=25,y=140)

        # =============add tesk===========
        def add():
            content=self.text.get(1.0, END)
            self.main_text.insert(END, content)
            with open("data.txt","a") as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0, END)
        def delete():
            delete_=self.main_text.curselection()
            look=self.main_text.get(delete_)
            with open("data.txt", "r+") as f:
                new_f=f.readlines()
                f.seek(0)
                for line in new_f:
                    item= str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)

        with open("data.txt", "r") as file:
            read=file.readlines()
            for i in read:
                ready=i.split
                self.main_text.insert(END,ready)
            file.close()

            self.button= Button(self.root, text="Add", bg="pink", bd=5, font="serif 18 bold", fg="black", command=add, width=10)
            self.button.place(x=50,y=400)
            self.button= Button(self.root, text="Delete", bg="pink", bd=5, font="serif 18 bold", fg="black", command=delete, width=10)
            self.button.place(x=50,y=500)
def main():
    root=Tk()
    ui=todo(root)
    root.mainloop()
if __name__=="__main__":
    main()