import cv2
import dlib as db
import numpy as np
import tkinter as tk
root = tk.Tk()
root.title('年龄性别构成')
text1 = tk.StringVar()
text2 = tk.StringVar()
text3 = tk.StringVar()
text4 = tk.StringVar()
text5 = tk.StringVar()
text6 = tk.StringVar()
text7 = tk.StringVar()
text8 = tk.StringVar()
text9 = tk.StringVar()
text10 = tk.StringVar()
label1 = tk.Label(root,text='0-2岁：').grid(row=0, column=0)
label2 = tk.Label(root,text='2-4岁：').grid(row=1, column=0)
label3 = tk.Label(root,text='8-13岁：').grid(row=2, column=0)
label4 = tk.Label(root,text='15-20岁：').grid(row=3, column=0)
label5 = tk.Label(root,text='25-32岁：').grid(row=4, column=0)
label6 = tk.Label(root,text='38-43岁：').grid(row=5, column=0)
label7 = tk.Label(root,text='48-53岁：').grid(row=6, column=0)
label8 = tk.Label(root,text='60+岁：').grid(row=7, column=0)
label9 = tk.Label(root,text='男：').grid(row=8, column=0)
label10 = tk.Label(root,text='女：').grid(row=9, column=0)

label11 = tk.Label(root,textvariable=text1).grid(row=0, column=1)
label22 = tk.Label(root,textvariable=text2).grid(row=1, column=1)
label33 = tk.Label(root,textvariable=text3).grid(row=2, column=1)
label44 = tk.Label(root,textvariable=text4).grid(row=3, column=1)
label55 = tk.Label(root,textvariable=text5).grid(row=4, column=1)
label66 = tk.Label(root,textvariable=text6).grid(row=5, column=1)
label77 = tk.Label(root,textvariable=text7).grid(row=6, column=1)
label88 = tk.Label(root,textvariable=text8).grid(row=7, column=1)
label99 = tk.Label(root,textvariable=text9).grid(row=8, column=1)
label1010 = tk.Label(root,textvariable=text10).grid(row=9, column=1)
text1.set(0)
text2.set(0)
text3.set(0)
text4.set(1)
text5.set(6)
text6.set(1)
text7.set(0)
text8.set(0)
text9.set(7)
text10.set(1)
root.mainloop()