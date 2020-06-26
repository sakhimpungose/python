import re
import tkinter as tk


window = tk.Tk() # creating window
window.geometry("354x460") # resizing window 
window.title("Calculator") # setting the title of the window
window.config(background='#eee') #setting the background colour of the window
window.resizable(False, False) # make window unresizable

display = tk.StringVar() # StringVar object to display output
    
result = "" # You find results here

def onClick(value):
    makeWhite()
    global result
    result += str(value)
    display.set(result)

def onAnswer():
    global result
    try:
        display.set(str(eval(result)))
    except:
        makeRed()
        display.set('')
    finally:
        result = ''    

def onClear():
    makeWhite()
    global result
    result = ''
    display.set(result)
    
def onClose():
    window.destroy()
        
def onInput(action, inText, preText, editedText):
    if action == '0' or action == '1':
        makeWhite()
    global result
    if result == '':
        display.set('')
    if action == '1':
        if re.search(r'[^0-9+-/ (*)]', inText) != None:
            return False
        else:
            result = editedText
    elif action == '0':        
        result = editedText

    return True
    
onInputCommand = window.register(onInput)
     
inputField = tk.Entry(window, font = ("Courier New", 12, 'bold'), textvar = display, width = 25, bd = 5, bg = 'white', justify ='right', validate='key', validatecommand=(onInputCommand, '%d', '%S', '%s', '%P'))
inputField.pack(pady = 10)

# makes inputField background red
def makeRed():
    inputField.config({'background':'#f00'})

# makes inputField background white
def makeWhite():
    inputField.config({'background':'#fff'})

# Button 7    
btn7 = tk.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:onClick(7),text="7",font=("Courier New",16,'bold'))
btn7.place(x = 10, y = 100)

# Buton 8
btn8=tk.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:onClick(8),text="8",font=("Courier New",16,'bold'))
btn8.place(x=75,y=100)

#Button 9
btn9=tk.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:onClick(9),text="9",font=("Courier New",16,'bold'))
btn9.place(x=140,y=100)

#Div button
btnDiv=tk.Button(window,padx=14,pady=14,bd=4,bg='white',text="/",command=lambda:onClick("/"),font=("Courier New",16,'bold'))
btnDiv.place(x=205,y=100)

# Button 4
btn4 = tk.Button(window, padx = 14, pady = 14, bd = 4, bg = 'white', command = lambda: onClick(4), text="4", font = ("Courier New",16,'bold'))
btn4.place(x = 10, y = 170)

# Button 5
btn5=tk.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:onClick(5),text="5",font=("Courier New",16,'bold'))
btn5.place(x=75,y=170)

# Button 6
btn6=tk.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:onClick(6),text="6",font=("Courier New",16,'bold'))
btn6.place(x=140,y=170)

# Mult button
btnMult=tk.Button(window,padx=14,pady=14,bd=4,bg='white',text="*",command=lambda:onClick("*"),font=("Courier New",16,'bold'))
btnMult.place(x=205,y=170)

# Button 1
btn1=tk.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:onClick(1),text="1",font=("Courier New",16,'bold'))
btn1.place(x=10,y=240)

# Button 2
btn2=tk.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:onClick(2),text="2",font=("Courier New",16,'bold'))
btn2.place(x=75,y=240)

# Button 3
btn3=tk.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:onClick(3),text="3",font=("Courier New",16,'bold'))
btn3.place(x=140,y=240)

# Sub button
btnSub=tk.Button(window,padx=14,pady=14,bd=4,bg='white',text="-",command=lambda:onClick("-"),font=("Courier New",16,'bold'))
btnSub.place(x=205,y=240)

# Zero button
btn0=tk.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:onClick(0),text="0",font=("Courier New",16,'bold'))
btn0.place(x=10,y=310)

# Dot button
btnDot=tk.Button(window,padx=47,pady=14,bd=4,bg='white',command=lambda:onClick("."),text=".",font=("Courier New",16,'bold'))
btnDot.place(x=75,y=310)

# Add button
btnAdd=tk.Button(window,padx=14,pady=14,bd=4,bg='white',text="+",command=lambda:onClick("+"),font=("Courier New",16,'bold'))
btnAdd.place(x=205,y=310)

# Clear button
btnClear = tk.Button(window,padx=14,pady=119,bd=4,bg='white', fg='#f00', text="CE",command=onClear,font=("Courier New",16,'bold'))
btnClear.place(x=270,y=100)

# Answer button
btnAnswer=tk.Button(window,padx=112,pady=14,bd=4,bg='white',command=onAnswer,text="=",font=("Courier New",16,'bold'))
btnAnswer.place(x=10,y=380)
# Close button
btnClose=tk.Button(window,padx=1,pady=14,bd=4,bg='#f00', fg='#fff',command=onClose,text="Exit",font=("Courier New",16,'bold'))
btnClose.place(x=270,y=380)

if __name__ == "__main__":
    window.mainloop()
