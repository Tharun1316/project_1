from tkinter import *
root = Tk()
root.title("Calculator")
root.geometry("262x350+100+200")
root.resizable(width=False, height=False)
root.config(bg="#fff")

equation = ""


def show(value):
    global equation
    if len(equation) < 14:
        equation += value
        label_result.config(text=equation)
def clear():
    global equation
    equation = ""
    label_result.config(text=equation)


def calculate():
    global equation
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    label_result.config(text=result)


label_result = Label(root, width=20, height=1, text="", font=("arial", 25),anchor=W)
label_result.pack()

Button(root, text="C", width=3, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg= "#3697f5", command=lambda: clear()).place(x=5,y=50)
Button(root, text="X", width=3, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg= "#2a2d36", command=lambda: show('X')).place(x=70,y=50)
Button(root, text="%", width=3, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg= "#2a2d36", command=lambda: show('%')).place(x=135,y=50)
Button(root, text="*", width=3, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg= "#2a2d36", command=lambda: show('*')).place(x=200,y=50)

Button(root, text="7", width=3, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg= "#2a2d36", command=lambda: show('7')).place(x=5,y=110)
Button(root, text="8", width=3, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg= "#2a2d36", command=lambda: show('8')).place(x=70,y=110)
Button(root, text="9", width=3, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg= "#2a2d36", command=lambda: show('9')).place(x=135,y=110)
Button(root, text="+", width=3, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg= "#2a2d36", command=lambda: show('+')).place(x=200,y=110)

Button(root, text="4", width=3, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg= "#2a2d36", command=lambda: show('4')).place(x=5,y=170)
Button(root, text="5", width=3, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg= "#2a2d36", command=lambda: show('5')).place(x=70,y=170)
Button(root, text="6", width=3, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg= "#2a2d36", command=lambda: show('6')).place(x=135,y=170)
Button(root, text="-", width=3, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg= "#2a2d36", command=lambda: show('-')).place(x=200,y=170)

Button(root, text="1", width=3, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg= "#2a2d36", command=lambda: show('1')).place(x=5,y=230)
Button(root, text="2", width=3, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg= "#2a2d36", command=lambda: show('2')).place(x=70,y=230)
Button(root, text="3", width=3, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg= "#2a2d36", command=lambda: show('3')).place(x=135,y=230)

Button(root, text="0", width=7, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg= "#2a2d36", command=lambda: show('0')).place(x=5,y=290)
Button(root, text=".", width=3, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg= "#2a2d36", command=lambda: show('.')).place(x=135,y=290)
Button(root, text="=", width=3, height=3, font=("arial", 20, "bold"), bd=1, fg="#fff", bg= "#fe9037", command=lambda: calculate()).place(x=200,y=230)

root.mainloop()
