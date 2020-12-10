import tkinter as tk

num = ""
oper = ""
dots = 1
operators = ["+", "-", "x", u"\u00F7"]
nums = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]

def numer(x):
  global num, oper, dots, nums, operators
  permitido = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "x", u"\u00F7", ".", "(", ")"]
  z = pantalla.cget("text")
  y = list(z)
  ya = len(y)-1
  if y[ya] not in permitido:
    pass
  else:
      if x == "*" or x == "/":
        dots = 1
        if x == "*":
            y="x"
            num = num+y
            oper=oper+x
            pantalla.config(text=num)
        else:
            y= u"\u00F7"
            num = num+y
            oper=oper+x
            pantalla.config(text=num)
      else:  
          if x == "+" or x == "-":
              dots = 1
              num = num+x
              oper = oper+x
              pantalla.config(text=num)
              
          elif x == "(" or x == ")":
              if x == "(":
                  if y[ya] == "." or y[ya] in nums:
                      pass
                  else:
                      num = num+x
                      oper = oper+x
                      pantalla.config(text=num)
              elif x == ")":
                  if y[ya] == "." or y[ya] in operators:
                      pass
                  else:
                      num = num+x
                      oper = oper+x
                      pantalla.config(text=num)
              else:
                  num = num+x
                  oper = oper+x
                  pantalla.config(text=num)
          else:
                  num = num+x
                  oper = oper+x
                  pantalla.config(text=num)
              
          

def equal():
    global num, oper, dots
    x = eval(oper)
    num = str(x)
    pantalla.config(text=num)
    oper = num
    dots = 1
    z = list(num)
    for i in z:
        if i == ".":
            dots = 0

def DOT():
    global num, oper, dots
    permitido = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
    num = pantalla.cget("text")
    x = list(num)
    xa = len(x)-1
    if x[xa] in permitido and dots == 1:
        num = num+"."
        oper = oper+"."
        pantalla.config(text=num)
        dots = 0

        

def clean():
    global num, oper, dots
    x = list(num)
    y=list(oper)
    xa = len(x)-1
    ya = len(y)-1
    if x[xa] == ".":
        dots = 1
    x.remove(x[xa])
    y.remove(y[ya])
    x = "".join(x)
    y = "".join(y)
    num=x
    oper = y
    if len(x) == 0:
        num = ""
        oper = ""
        pantalla.config(text="0")
    else:    
        pantalla.config(text=num)
    
    

def cleaner():
    global num, oper, dots
    num = ""
    oper = ""
    pantalla.config(text="0")
    dots = 1

def pi():
    global num, oper, dots
    if dots == 1:
        dots = 0
        num = num + "3.1415926"
        oper = oper+ "3.1415926"
        pantalla.config(text=num)

        
root = tk.Tk()
root.resizable(False, False)
root.geometry("347x619+770+228")
root.title("Calculadora Científica")

##########################PANTALLA############################

pantalla = tk.Label(root, text="0", font=("Calibri", 25), bg="light blue", width=18, justify="right")
pantalla.place(x=20, y=20)

###################LINEA1##########################

button1 = tk.Button(root, text="1", bg="light blue", font=("Calibri", 13), width=10, command=lambda:numer("1"))
button1.place(x=10, y=100)

button2 = tk.Button(root, text="2", bg="light blue", font=("Calibri", 13), width=10, command=lambda:numer("2"))
button2.place(x=120, y=100)

button3 = tk.Button(root, text="3", bg="light blue", font=("Calibri", 13), width=10, command=lambda:numer("3"))
button3.place(x=230, y=100)

#################LINEA2###############################

button4 = tk.Button(root, text="4", bg="light blue", font=("Calibri", 13), width=10, command=lambda:numer("4"))
button4.place(x=10, y=170)

button5 = tk.Button(root, text="5", bg="light blue", font=("Calibri", 13), width=10, command=lambda:numer("5"))
button5.place(x=120, y=170)

button6 = tk.Button(root, text="6", bg="light blue", font=("Calibri", 13), width=10, command=lambda:numer("6"))
button6.place(x=230, y=170)

#################LINEA·#####################

button7 = tk.Button(root, text="7", bg="light blue", font=("Calibri", 13), width=10, command=lambda:numer("7"))
button7.place(x=10, y=250)

button8 = tk.Button(root, text="8", bg="light blue", font=("Calibri", 13), width=10, command=lambda:numer("8"))
button8.place(x=120, y=250)

button9 = tk.Button(root, text="9", bg="light blue", font=("Calibri", 13), width=10, command=lambda:numer("9"))
button9.place(x=230, y=250)

button0 = tk.Button(root, text="0", bg="light blue", font=("Calibri", 13), width=10, command=lambda:numer("0"))
button0.place(x=120, y=410)

buttonPlus = tk.Button(root, text="+", bg="light blue", font=("Calibri", 13), width=10, command=lambda: numer("+"))
buttonPlus.place(x=10, y=330)

buttonMinus = tk.Button(root, text="-", bg="light blue", font=("Calibri", 13), width=10, command=lambda: numer("-"))
buttonMinus.place(x=120, y=330)

buttonDivid = tk.Button(root, text=u"\u00F7", bg="light blue", font=("Calibri", 13), width=10, command=lambda: numer("/"))
buttonDivid.place(x=10, y=410)

buttonDuplo = tk.Button(root, text="x", bg="light blue", font=("Calibri", 13), width=10, command=lambda: numer("*"))
buttonDuplo.place(x=230, y=330)

buttonEqual = tk.Button(root, text="=", bg="light blue", font=("Calibri", 13), width=10, command=equal)
buttonEqual.place(x=120, y=490)

buttonDOT = tk.Button(root, text=".", bg="light blue", font=("Calibri", 13), width=10, command=DOT)
buttonDOT.place(x=230, y=410)

buttonCE = tk.Button(root, text="CE", bg="light blue", font=("Calibri", 13), width=10, command=cleaner)
buttonCE.place(x=230, y=490)

buttonC = tk.Button(root, text="C", bg="light blue", font=("Calibri", 13), width=10, command=clean)
buttonC.place(x=10, y=490)

buttonPi = tk.Button(root, text="PI", bg="light blue", font=("Calibri", 13), width=10, command=pi)
buttonPi.place(x=10, y=570)

buttonOpen = tk.Button(root, text="(", bg="light blue", font=("Calibri", 13), width=10, command=lambda: numer("("))
buttonOpen.place(x=120, y=570)

buttonClose = tk.Button(root, text=")", bg="light blue", font=("Calibri", 13), width=10, command=lambda: numer(")"))
buttonClose.place(x=230, y=570)

root.mainloop()
