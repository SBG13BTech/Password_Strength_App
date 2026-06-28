#This is a password strength checker app.

import tkinter as tk   #Tkinter Module for GUI 

root=tk.Tk() #Main window
root.title("Password Strength Checker")
root.geometry("400x600") #Size of the main window

L1=tk.Label(root,text="Welcome to the Password Strength Checker App")
L1.pack(pady=10)

L2=tk.Label(root,text="Enter Password below:")
L2.pack(padx=0,pady=10)

E1=tk.Entry(root)
E1.pack()

L3=tk.Label(root,text='')
L3.pack()

L4=tk.Label(root,text='')
L4.pack()

L5=tk.Label(root,text='')
L5.pack()

L6=tk.Label(root,text='')
L6.pack()

L7=tk.Label(root,text='')
L7.pack()

def reset():
    E1.delete(0,'end')
    L3.config(text='')
    L4.config(text='')
    L5.config(text='')
    L6.config(text='')
    L7.config(text='')


def common(p):
        with open("Common_Passwords.txt") as f:
            for line in f:
                if p==line.strip():  # strip() removes \n character from the end of every word
                    return True
            return False
    
    
def repeat(p):
    for i in range(0,len(p)-2):
        if p[i]==p[i+1]==p[i+2]:  #checks whether three consecutive characters are same
            return True
    return False
    
    
    
def sequence(p):
    for i in range(0,len(p)-3):
        if (ord(p[i].lower())+1==ord(p[i+1].lower())==ord(p[i+2].lower())-1==ord(p[i+3].lower())-2): #ord() function gives ASCII value of the character
            return True
    return False
    


def Checker(p):
        score=0 #scoring system out of 5
        uc=0
        lc=0
        numbers=0
        specialc=0

        if len(p)>=12:
            score+=1

        for i in p:
            
            if i.isupper():
                uc+=1
            
            elif i.islower():
                lc+=1
            
            elif i.isdigit():
                numbers+=1
            
            elif i in "!@#$%^&*()_+-{[]}':;?/>.<,~`":
                specialc+=1
            
        if uc>=3:
            score+=1
            
        if lc>=3:
            score+=1
            
        if numbers>=3:
            score+=1
            
        if specialc>=3:
            score+=1
            
        return score

def Check(p):
    
    
    
    if len(p)<12:
        L3.config(text="\nThe password is too short.\nIt should atleast be 12 characters long.")
    
    if common(p):
        L4.config(text=f"\nThe password '{p}' is a common password\nConsider changing it")
        L5.config(text="COMMON PASSWORD!!!\nScore will not be calculated\n")
    
    if repeat(p):
        L5.config(text="The password contains repeated characters\nAvoid repitition")
    
    if sequence(p):
        L6.config(text="Your password has sequence of characters\nAvoid Sequences\neg.abcd")

    if common(p)==False:
        result=Checker(p)
        score_dict={
                    0:"Very Weak",
                    1:"Weak",
                    2:"Slightly Weak",
                    3:"Slightly Strong",
                    4:"Strong",
                    5:"Very Strong"
                    }
        
        L7.config(text=f"Your password score out of 5 is {result}\n\nYour password is {score_dict[result]}")
        
        
    
    

b1=tk.Button(root,text="Check Strength",command=lambda:Check(E1.get()))
b1.pack(pady=15)
b2=tk.Button(root,text='Reset',command=reset)
b2.pack()
root.mainloop() #keeps the window open for user interactions