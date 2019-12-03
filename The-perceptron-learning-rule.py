# this is my first exercise
# importings
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import messagebox
from matplotlib import style
plt.style.use('ggplot')
# Beginning of train
points= [(1,1,0),(1,2,0),(2,3,0),(3,1,0),(2,2,0), # points in A
         (10,11,1),(11,12,1),(9,10,1),(11,8,1),(8,12,1)]    # points in B
# First 5 are A and Second 5 are B in format (x1,x2,t)
# t=0 for A and t=11 for B
# w0,w1,w2 = 0,0,0 at first of train
# x0 value is always one
# y is one when I is greater than zero
# I  equals to : summation of x_i*w_i
# ty : This is t-y
#evaluating I
################################
weights = []
def evaluate(A=points,len=10,w0=0,w1=0,w2=0,x0=1,y=0,I=0,ty=0):
    print('w0 w1 w2 x0 x1 x2 t I y ty')
    for K in range(0,20):
        for i in range(0,len):
            # calculating The new I
            I = (x0*w0 + A[i][0]*w1 + A[i][1]*w2)
            # calculating the new y
            if I>0:
                y=1
            else:
                y=0
            # calculating the new t - y
            ty = A[i][-1] - y # This is t - y
            print(w0,w1,w2,x0,A[i][0],A[i][1],A[i][-1],I,y,ty)
            # calculating new weights
            weights.append([w0,w1,w2])
            w0 += x0*ty
            w1 += A[i][0]*ty
            w2 += A[i][1]*ty
######################################################################################################
    x = np.linspace(-10,10,1000)
    line = plt.plot(x,(w0+w1*x)/(-w2))
    for i in range(0,len):
        for j in range(0,1):
            if A[i][-1]==0:
                plt.scatter(A[i][j],A[i][j+1],s=5,color='red')
            elif A[i][-1]==1:
                plt.scatter(A[i][j],A[i][j+1],s=5,color='blue')    
    plt.show()
    ################################################# testing part
    test = [] # for storing t-y values
    for i in range(0,len):
        # calculating The new I
        I = (x0*w0 + A[i][0]*w1 + A[i][1]*w2)
        # calculating the new y
        if I>0:
            y=1
        else:
            y=0
        # calculating the new t - y
        ty = A[i][-1] - y # This is t - y
        test.append(ty)
        # calculating new weights
        w0 += x0*ty
        w1 += A[i][0]*ty
        w2 += A[i][1]*ty
    for item in test:
        if item == 0:
            pass
        else:
            messagebox.showerror('Non_Sepratable')
            break    
######################################################################################################                
mst = Tk()
# canvas is the main window
canvas = tk.Canvas(mst,width=400,height=800)
canvas.pack()
# Label A
LabelA=tk.Label(text='Please Enter number of data in A :',justify='center')
canvas.create_window(200,100,window=LabelA)
# Entry A
EntryA=tk.Entry(justify='center')
canvas.create_window(200,140,window=EntryA)
# Label B
LabelB=tk.Label(text='Please Enter number of data in B :',justify='center')
canvas.create_window(200,180,window=LabelB)
# Entry B
EntryB=tk.Entry(justify='center')
canvas.create_window(200,220,window=EntryB)
# Label x1
Labelx1=tk.Label(text='Please Enter the Average of x1 :',justify='center')
canvas.create_window(200,260,window=Labelx1)
# Entry x1
Entryx1=tk.Entry(justify='center')
canvas.create_window(200,300,window=Entryx1)
# Label sd1
Labelsd1=tk.Label(text='Please Enter the Standard Deviation of x1 :',justify='center')
canvas.create_window(200,340,window=Labelsd1)
# Entry sd1
Entrysd1=tk.Entry(justify='center')
canvas.create_window(200,380,window=Entrysd1)
# Label x2
Labelx2=tk.Label(text='Please Enter the Average of x2 :',justify='center')
canvas.create_window(200,420,window=Labelx2)
# Entry x2
Entryx2=tk.Entry(justify='center')
canvas.create_window(200,460,window=Entryx2)
# Label sd2
Labelsd2=tk.Label(text='Please Enter the Standard Deviation of x2 :',justify='center')
canvas.create_window(200,500,window=Labelsd2)
# Entry sd2
Entrysd2=tk.Entry(justify='center')
canvas.create_window(200,540,window=Entrysd2)
# evaluation function
def evaluation():
    try:
        num_of_A = int(EntryA.get())
        num_of_B = int(EntryB.get())
        avgx1 = float(Entryx1.get())
        avgx2 = float(Entryx2.get())
        sdx1 = float(Entrysd1.get())
        sdx2 = float(Entrysd2.get())
        print(num_of_A,num_of_B,avgx1,avgx2,sdx1,sdx2)
    except:
        messagebox.showerror('Wrong input','Wrong or Empthy Input\nremember that all values must be numerical')
    A1 = np.random.normal(avgx1,sdx1,num_of_A)
    A2 = np.random.normal(avgx2,sdx2,num_of_A)
    A3 = [0]*num_of_A
    B1 = np.random.normal(avgx1,sdx1,num_of_B)
    B2 = np.random.normal(avgx2,sdx2,num_of_B)
    B3 = [1]*num_of_B
    A = list(zip(A1,A2,A3))
    B = list(zip(B1,B2,B3))
    C = list(A + B)
    evaluate(C,len(C))
# The Evaluation button
Start_Button = tk.Button(text='Start Evaluation',command=evaluation)
canvas.create_window(200,580,window=Start_Button)
# Evaluation eith default params
Start_Default_Button = tk.Button(text='Start evaluation with default Params',command=evaluate)
canvas.create_window (200,620,window=Start_Default_Button)
# setting the title
mst.title('Perceptron neuron')
# The main Loop
tk.mainloop()