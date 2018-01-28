from math import *
from tkinter import *
from tkinter import font
class calculator:
    def __init__(self):

        # constructor function
        self.root=Tk()
        self.root.title("Calculator")
        self.root.maxsize(width=290,height=345)
        self.root.minsize(width=290, height=345)
        myfont = font.Font(family='Arial', size=12, weight=font.BOLD)
        myfontsmall = font.Font(family='MS Sans Serif', size=12, weight=font.BOLD)
        self.flag=0
        self.expresion=""
        self.result = Label(self.root, text="", width="27", height="2", bg="azure",anchor=E,relief=RIDGE,bd=8,font=myfontsmall)
        self.result.grid(columnspan=5)

        #creating the buttons
        self.btnfact = Button(self.root, font=myfont, text="n!", bd=6, relief=RAISED, width="4", height="1", bg="slategray4",fg="white", command=lambda: self.append("fact(")).grid(row=1, column=1)
        self.btnsqrt = Button(self.root, font=myfont, text="√", bd=6, relief=RAISED, width="4", height="1", bg="slategray4",fg="white", command=lambda: self.append("sqrt(")).grid(row=1, column=0)
        self.btnlog = Button(self.root, font=myfont, text="log\u2081\u2080", bd=6, relief=RAISED, width="4", height="1",bg="slategray4", fg="white", command=lambda: self.append("log10(")).grid(row=1, column=2)
        self.btnln = Button(self.root, font=myfont, text="ln", bd=6, relief=RAISED, width="4", height="1",bg="slategray4", fg="white", command=lambda: self.append("log(")).grid(row=1, column=3)
        self.btne = Button(self.root, font=myfont, text="e", bd=6, relief=RAISED, width="4", height="1", bg="slategray4",fg="white", command=lambda: self.append("e")).grid(row=1, column=4)
        self.btnsin = Button(self.root, font=myfont, text="sin", bd=6, relief=RAISED, width="4", height="1", bg="slategray4",fg="white", command=lambda: self.append("sin(")).grid(row=2, column=0)
        self.btncos = Button(self.root, font=myfont, text="cos", bd=6, relief=RAISED, width="4", height="1", bg="slategray4",fg="white", command=lambda: self.append("cos(")).grid(row=2, column=1)
        self.btntan = Button(self.root, font=myfont, text="tan", bd=6, relief=RAISED, width="4", height="1", bg="slategray4",fg="white", command=lambda: self.append("tan(")).grid(row=2, column=2)
        self.btnrad = Button(self.root, font=myfont, text="rad", bd=6, relief=RAISED, width="4", height="1", bg="slategray4",fg="white", command=lambda: self.append("radians(")).grid(row=2, column=3)
        self.btnpi = Button(self.root, font=myfont, text="pi", bd=6, relief=RAISED, width="4", height="1",bg="slategray4", fg="white", command=lambda: self.append("pi")).grid(row=2, column=4)
        self.btnasin = Button(self.root, font=myfont, text="sin\u207B\u00B9", bd=6, relief=RAISED, width="4", height="1", bg="slategray4",fg="white", command=lambda: self.append("asinh(")).grid(row=3, column=0)
        self.btnacos = Button(self.root, font=myfont, text="cos\u207B\u00B9", bd=6, relief=RAISED, width="4", height="1", bg="slategray4",fg="white", command=lambda: self.append("acosh(")).grid(row=3, column=1)
        self.btnatan = Button(self.root, font=myfont, text="tan\u207B\u00B9", bd=6, relief=RAISED, width="4", height="1", bg="slategray4",fg="white", command=lambda: self.append("atanh(")).grid(row=3, column=2)
        self.btnpow = Button(self.root, font=myfont, text="pow", bd=6, relief=RAISED, width="4", height="1", bg="slategray4",fg="white", command=lambda: self.append("pow(")).grid(row=3, column=3)
        self.btncomma = Button(self.root, font=myfont, text=",", bd=6, relief=RAISED, width="4", height="1", bg="slategray4",fg="white", command=lambda: self.append(",")).grid(row=3, column=4)
        self.btn7 = Button(self.root, font=myfont, text="7", bd=6, relief=RAISED, width="4", height="1", bg="black",fg="white", command=lambda: self.append("7")).grid(row=6, column=0)
        self.btn8 = Button(self.root, font=myfont, text="8", bd=6, relief=RAISED, width="4", height="1", bg="black",fg="white", command=lambda: self.append("8")).grid(row=6, column=1)
        self.btn9 = Button(self.root, font=myfont, text="9", bd=6, relief=RAISED, width="4", height="1", bg="black",fg="white", command=lambda: self.append("9")).grid(row=6, column=2)
        self.btnDel = Button(self.root, font=myfont, text="DEL", bd=6, relief=RAISED, width="4", height="1", bg="red2",fg="white", command=lambda: self.delete()).grid(row=6, column=3)
        self.btnClr = Button(self.root,font=myfont, text="AC", bd=6,relief=RAISED, width="4", height="1", bg="red2",fg="white", command=lambda: self.clear()).grid(row=6, column=4)
        self.btn4 = Button(self.root, font=myfont, text="4", bd=6, relief=RAISED, width="4", height="1", bg="black",fg="white", command=lambda: self.append("4")).grid(row=7, column=0)
        self.btn5 = Button(self.root, font=myfont, text="5", bd=6, relief=RAISED, width="4", height="1", bg="black",fg="white", command=lambda: self.append("5")).grid(row=7, column=1)
        self.btn6 = Button(self.root, font=myfont, text="6", bd=6, relief=RAISED, width="4", height="1", bg="black",fg="white", command=lambda: self.append("6")).grid(row=7, column=2)
        self.btnMul = Button(self.root,font=myfont, text="x", bd=6,relief=RAISED, width="4", height="1", bg="gray14",fg="white", command=lambda: self.append("*")).grid(row=7,column=3)
        self.btnDiv = Button(self.root,font=myfont, text="/", bd=6,relief=RAISED, width="4", height="1", bg="gray14",fg="white", command=lambda: self.append("/")).grid(row=7,column=4)
        self.btn1 = Button(self.root,font=myfont, text="1",bd=6,relief=RAISED, width="4", height="1", bg="black",fg="white", command=lambda: self.append("1")).grid(row=8,column=0)
        self.btn2 = Button(self.root,font=myfont, text="2",bd=6,relief=RAISED, width="4", height="1", bg="black",fg="white", command=lambda: self.append("2")).grid(row=8,column=1)
        self.btn3 = Button(self.root,font=myfont, text="3",bd=6,relief=RAISED, width="4", height="1", bg="black",fg="white", command=lambda: self.append("3")).grid(row=8,column=2)
        self.btnPlus = Button(self.root,font=myfont, text="+", bd=6,relief=RAISED, width="4", height="1", bg="gray14",fg="white", command=lambda: self.append("+")).grid(row=8,column=3)
        self.btnSub = Button(self.root,font=myfont, text="-",bd=6,relief=RAISED, width="4", height="1",bg="gray14",fg="white", command=lambda: self.append("-")).grid(row=8,column=4)
        self.btnfbrac = Button(self.root,font=myfont, text="(",bd=6,relief=RAISED, width="4", height="1", bg="gray14",fg="white", command=lambda: self.append("(")).grid(row=10,column=0)
        self.btn0 = Button(self.root,font=myfont, text="0",bd=6,relief=RAISED, width="4", height="1", bg="black",fg="white", command=lambda: self.append("0")).grid(row=10,column=1)
        self.btndot = Button(self.root,font=myfont, text=".",bd=6,relief=RAISED, width="4", height="1", bg="black",fg="white", command=lambda: self.append(".")).grid(row=10,column=2)
        self.btnebrac = Button(self.root,font=myfont, text=")",bd=6,relief=RAISED, width="4", height="1", bg="gray14",fg="white", command=lambda: self.append(")")).grid(row=10,column=3)
        self.btnEquals = Button(self.root,font=myfont, text="=",bd=6,relief=RAISED, width="4", height="1", bg="gray14",fg="white", command=lambda: self.publish()).grid(row=10, column=4)

        #keyboard shortcuts
        self.root.bind("<e>",self.appende)
        self.root.bind("<p>",self.appendpi)
        self.root.bind("1",self.append1)
        self.root.bind("2",self.append2)
        self.root.bind("3",self.append3)
        self.root.bind("4",self.append4)
        self.root.bind("5",self.append5)
        self.root.bind("6",self.append6)
        self.root.bind("7",self.append7)
        self.root.bind("8",self.append8)
        self.root.bind("9",self.append9)
        self.root.bind("0",self.append0)
        self.root.bind(".",self.appenddot)
        self.root.bind("+",self.appendadd)
        self.root.bind("-",self.appendsub)
        self.root.bind("*",self.appendmul)
        self.root.bind("/",self.appenddiv)
        self.root.bind("(",self.appendbracf)
        self.root.bind(")",self.appendbrace)
        self.root.bind("<Return>",self.publish)
        self.root.bind("<BackSpace>", self.delete)
        self.root.bind("<Delete>", self.clear)

        self.root.mainloop()

    #keyboard shortcut functions

    def appende(self,event=NONE):
        self.expresion+="e"
        self.result.configure(text=self.expresion)

    def appendpi(self,event=NONE):
        self.expresion+="pi"
        self.result.configure(text=self.expresion)

    def append1(self,event=NONE):
        self.expresion+="1"
        self.result.configure(text=self.expresion)

    def append2(self,event=NONE):
        self.expresion+="2"
        self.result.configure(text=self.expresion)

    def append3(self,event=NONE):
        self.expresion+="3"
        self.result.configure(text=self.expresion)

    def append4(self,event=NONE):
        self.expresion+="4"
        self.result.configure(text=self.expresion)

    def append5(self,event=NONE):
        self.expresion+="5"
        self.result.configure(text=self.expresion)

    def append6(self,event=NONE):
        self.expresion+="6"
        self.result.configure(text=self.expresion)

    def append7(self,event=NONE):
        self.expresion+="7"
        self.result.configure(text=self.expresion)

    def append8(self,event=NONE):
        self.expresion+="8"
        self.result.configure(text=self.expresion)

    def append9(self,event=NONE):
        self.expresion+="9"
        self.result.configure(text=self.expresion)

    def append0(self,event=NONE):
        self.expresion+="0"
        self.result.configure(text=self.expresion)

    def appenddot(self,event=NONE):
        self.expresion+="."
        self.result.configure(text=self.expresion)

    def appendbracf(self,event=NONE):
        self.expresion+="("
        self.result.configure(text=self.expresion)

    def appendbrace(self,event=NONE):
        self.expresion+=")"
        self.result.configure(text=self.expresion)

    def appendadd(self,event=NONE):
        self.expresion+="+"
        self.result.configure(text=self.expresion)

    def appendsub(self,event=NONE):
        self.expresion+="-"
        self.result.configure(text=self.expresion)

    def appendmul(self,event=NONE):
        self.expresion+="*"
        self.result.configure(text=self.expresion)

    def appenddiv(self,event=NONE):
        self.expresion+="/"
        self.result.configure(text=self.expresion)

    #function to add numbers or symbols to the calculator screen

    def append(self,exp,event=NONE):
        self.expresion+=exp
        self.result.configure(text=self.expresion)

    #function to delete the most recent number or symbol

    def delete(self,event=NONE):

        testlist = list(self.expresion)
        self.expresion = ''.join(testlist[:-1])
        self.result.configure(text=self.expresion)

    #funtion to evaluate the result

    def publish(self,event=NONE):
        #error handling
        try:
            self.expresion=str(eval(self.expresion))
            self.result.configure(text=self.expresion)
        except ZeroDivisionError:
            self.expresion = ""
            self.result.configure(text="Undefined!")
        except SyntaxError:
            self.expresion = ""
            self.result.configure(text="Syntax error!")
        except ValueError:
            self.expresion = ""
            self.result.configure(text="Math error!")
        except NameError:
            self.expresion = ""
            self.result.configure(text="Syntax error!")

    #funtion to clear the calculator screen

    def clear(self,event=NONE):
        self.expresion=""
        self.result.configure(text=self.expresion)

#creating the object of class calculator

obj1=calculator()