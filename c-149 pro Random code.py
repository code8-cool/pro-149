# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 20:32:21 2024

@author: occup
"""

from tkinter import *
import random
root = Tk()
root.title("Lucky tickets")
root.geometry("750x500")


label1 = Label(root)


alpha_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "w", "x", "y", "z" ]
def determine_winners():
    random_no1 = random.randint(1,26)
    random_no2 = random.randint(1,26)
    random_no3 = random.randint(1,26)
    random_no4 = random.randint(1,26)
    random_no5 = random.randint(1,26)
    random_alpha1 = str(alpha_list[random_no1])
    random_alpha2 = str(alpha_list[random_no2])
    random_alpha3 = str(alpha_list[random_no3])
    random_alpha4 = str(alpha_list[random_no4])
    random_alpha5 = str(alpha_list[random_no5])
    label1["text"] = "Your Lucky code is " +  str((random_alpha1)) + str((random_alpha2)) + str((random_alpha3)) + str((random_alpha4)) + str((random_alpha5))


 
btn = Button(root, text = "Show winning codes", command = determine_winners)


btn.place(relx = 0.5, rely = 0.35, anchor = CENTER)
label1.place(relx = 0.5, rely = 0.4, anchor = CENTER)


root.mainloop()
