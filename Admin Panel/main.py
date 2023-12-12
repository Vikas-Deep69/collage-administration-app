from tkinter import *
from tkinter import ttk

main = Tk()
main.geometry('516x305')
main.resizable(False,False)
main.title("Calculator")

theValue = StringVar()

style = ttk.Style()
styleTwo = ttk.Style()

style.configure('big.TButton', font=(None, 12, 'bold'))

def onClick(num):
    etInput.insert(100, num)

def clr():
    etInput.delete(0,100)

def operation():
    theString = etInput.get()
    etInput.delete(0,100)
    etInput.insert(0, eval(theString))

inputFrame = Frame(main, bg = '#39E75F')
etInput = Entry(inputFrame, width=30, font=('Areal', 16, 'bold'), bd=5, fg='black',bg='white', textvariable=theValue, justify=RIGHT)
theFrame = Frame(main, bg='#F94449')
secondFrame = Frame(main, bg = "#92DFF3")

btnSeven = ttk.Button(theFrame, text = "7", style="big.TButton", command = lambda: onClick(7))
btnEight = ttk.Button(theFrame, text = "8", style="big.TButton", command = lambda: onClick(8))
btnNine = ttk.Button(theFrame, text = "9", style="big.TButton", command = lambda: onClick(9))

btnFour = ttk.Button(theFrame, text = "4",style="big.TButton", command = lambda: onClick(4))
btnFive = ttk.Button(theFrame, text = "5",style="big.TButton", command = lambda: onClick(5))
btnSix = ttk.Button(theFrame, text = "6",style="big.TButton", command = lambda: onClick(6))

btnOne = ttk.Button(theFrame, text = "1", style="big.TButton", command = lambda: onClick(1))
btnTwo = ttk.Button(theFrame, text = "2",style="big.TButton", command = lambda: onClick(2))
btnThree = ttk.Button(theFrame, text = "3", style="big.TButton", command = lambda: onClick(3))

btnDot = ttk.Button(theFrame, text = ".",style="big.TButton", command = lambda: onClick('.'))
btnZero = ttk.Button(theFrame, text = "0", style="big.TButton", command = lambda: onClick(0))
btnClr = ttk.Button(theFrame, text = "AC", style="big.TButton", command=clr)

btnEqual = ttk.Button(secondFrame, text = "=", style="big.TButton", command=lambda: operation())
btnPlus = ttk.Button(secondFrame, text = "+", style="big.TButton", command = lambda: onClick('+'))
btnMinus = ttk.Button(secondFrame, text = "-", style="big.TButton", command = lambda: onClick('-'))
btnMultiplication = ttk.Button(secondFrame, text = "x", style="big.TButton", command = lambda: onClick('*'))
btnDivide = ttk.Button(secondFrame, text = "/", style="big.TButton", command = lambda: onClick('/'))



inputFrame.grid(row=0,column=0, columnspan=3)
etInput.grid(row = 0, column = 0, columnspan = 3, pady=5, ipadx=2, ipady=5, padx=5)
theFrame.grid(row = 1, column = 0, rowspan = 4, columnspan = 3)
secondFrame.grid(row=0, column=3, rowspan=4)

btnSeven.grid(row=1, column=0, pady=10, padx=10, ipady = 6)
btnEight.grid(row=1, column=1, pady=10, padx=10, ipady = 6)
btnNine.grid(row=1, column=2, pady=10, padx=10, ipady = 6)

btnFour.grid(row=2, column=0, pady=10, padx=10, ipady = 6)
btnFive.grid(row=2, column=1, pady=10, padx=10, ipady = 6)
btnSix.grid(row=2, column=2, pady=10, padx=10, ipady = 6)

btnOne.grid(row=3, column=0, pady=10, padx=10, ipady = 6)
btnTwo.grid(row=3, column=1, pady=10, padx=10, ipady = 6)
btnThree.grid(row=3, column=2, pady=10, padx=10, ipady = 6)

btnDot.grid(row=4, column=0, pady=10, padx=10, ipady = 6)
btnZero.grid(row=4, column=1, pady=10, padx=10, ipady = 6)
btnClr.grid(row=4, column=2, pady=10, padx=10, ipady = 6)

btnEqual.grid(row = 0, column = 3, pady=10, padx=10, ipady=6)
btnPlus.grid(row = 1, column = 3, pady=10, padx=10, ipady=6)
btnMinus.grid(row = 2, column = 3, pady=10, padx=10, ipady=6)
btnMultiplication.grid(row = 3, column = 3, pady=10, padx=10, ipady=6)
btnDivide.grid(row = 4, column = 3, pady=10, padx=10, ipady=6)
main.mainloop()