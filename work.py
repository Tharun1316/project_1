# e = Entry(root, width=35, borderwidth=7, font=('Arial',10))
# e.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
# def button_click(number):
#     current = e.get()
#     e.delete(0, END)
#     e.insert(0, str(current) + str(number))
#     return
# def button_add():
#     first_number = e.get()
#     global f_num
#     global math
#     math = "addition"
#     f_num = int(first_number)
#     e.delete(0, END)
#     return
# def button_subtract():
#     first_number = e.get()
#     global f_num
#     global math
#     math = "subtraction"
#     f_num = int(first_number)
#     e.delete(0, END)
#     return
# def button_multiplication():
#     first_number = e.get()
#     global f_num
#     global math
#     math = "multiplication"
#     f_num = int(first_number)
#     e.delete(0, END)
#     return
# def button_division():
#     first_number = e.get()
#     global f_num
#     global math
#     math = "division"
#     f_num = int(first_number)
#     e.delete(0, END)
#     return
# def button_equal():
#     second_number = e.get()
#     e.delete(0, END)
#     if math == "addition":
#         e.insert(0, f_num + int(second_number))
#     elif math == "subtraction":
#         e.insert(0, f_num - int(second_number))
#     elif math == "multiplication":
#         e.insert(0, f_num * int(second_number))
#     elif math == "division":
#         e.insert(0, f_num / int(second_number))
# def button_clear():
#     e.delete(0, FIRST)
#     return
#
#
# button_1 = Button(root, text="1", font=("arial",11,"bold"), width=5, height=2, padx=19, bd=3, background="#FFFFFF", command=lambda: button_click(1))
# button_2 = Button(root, text="2", font=("arial",11,"bold"), width=5, height=2, padx=19, bd=3, background="#FFFFFF", command=lambda: button_click(2))
# button_3 = Button(root, text="3", font=("arial",11,"bold"), width=5, height=2, padx=18, bd=3, background="#FFFFFF", command=lambda: button_click(3))
# button_4 = Button(root, text="4", font=("arial",11,"bold"), width=5, height=2, padx=19, bd=3, background="#FFFFFF", command=lambda: button_click(4))
# button_5 = Button(root, text="5", font=("arial",11,"bold"), width=5, height=2, padx=19, bd=3, background="#FFFFFF", command=lambda: button_click(5))
# button_6 = Button(root, text="6", font=("arial",11,"bold"), width=5, height=2, padx=18, bd=3, background="#FFFFFF", command=lambda: button_click(6))
# button_7 = Button(root, text="7", font=("arial",11,"bold"), width=5, height=2, padx=19, bd=3, background="#FFFFFF", command=lambda: button_click(7))
# button_8 = Button(root, text="8", font=("arial",11,"bold"), width=5, height=2, padx=19, bd=3, background="#FFFFFF", command=lambda: button_click(8))
# button_9 = Button(root, text="9", font=("arial",11,"bold"), width=5, height=2, padx=18, bd=3, background="#FFFFFF", command=lambda: button_click(9))
# button_0 = Button(root, text="0", font=("arial",11,"bold"), width=5, height=2, padx=19, bd=3, background="#FFFFFF", command=lambda: button_click(0))
# button_subtract = Button(root, text="-", font=("arial",11,"bold"), width=5, height=2, padx=19, bd=3, background="#FFFFFF", command=button_subtract)
# button_divide = Button(root, text="/", font=("arial",11,"bold"), width=5, height=2, padx=18, bd=3, background="#FFFFFF", command=button_division)
# button_mul = Button(root, text="X", font=("arial",11,"bold"), width=5, height=2, padx=19, bd=3, background="#FFFFFF", command=button_multiplication)
# button_add = Button(root, text="+", font=("arial",11,"bold"), width=15, height=2, padx=21, bd=3, background="#FFFFFF", command=button_add)
# button_clear = Button(root, text="Clear", font=("arial",11,"bold"), width=5, height=2, padx=19, bd=3, background="#FFFFFF", command=button_clear)
# button_equal = Button(root, text="=", font=("arial",11,"bold"), width=15, height=2, padx=21, bd=3, background="#FFFFFF", command=button_equal)
#
#
# button_1.grid(row=3, column=0)
# button_2.grid(row=3, column=1)
# button_3.grid(row=3, column=2)
#
# button_4.grid(row=2, column=0)
# button_5.grid(row=2, column=1)
# button_6.grid(row=2, column=2)
#
# button_7.grid(row=1, column=0)
# button_8.grid(row=1, column=1)
# button_9.grid(row=1, column=2)
#
# button_0.grid(row=4, column=0)
# button_subtract.grid(row=4, column=1)
# button_divide.grid(row=4, column=2)
#
# button_mul.grid(row=5, column=0)
# button_add.grid(row=5, column=1, columnspan=2)
#
# button_clear.grid(row=6, column=0)
# button_equal.grid(row=6, column=1, columnspan=2)

