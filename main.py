#This is a password strength checker app.

import tkinter as tk

root=tk.Tk()
root.title("Password Strength Checker")
root.geometry("600x400")
L1=tk.Label(root,text="Welcome to the Password Strength Checker App",anchor='center')
L1.pack(pady=10)
L2=tk.Label(root,text="Enter Password below:")
L2.pack(padx=0,pady=10)
E1=tk.Entry(root)
E1.pack()
L3=tk.Label(root,text="")
L3.pack()
L4=tk.Label(root,text="")
L4.pack(padx=10,pady=5)
def reset():
    E1.delete(0,'end')
    L3.config(text='')
    L4.config(text='')
def Check(p):
    def common(p):
            with open("Common_Passwords.txt") as f:
                for line in f:
                    if p==line.strip():
                        
                        L3.config(text=f"The password '{p}' is a common password\n\nConsider changing it")
                        return True
                return False


    def Checker(p):
            score=0
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
    C_pswd=common(p)
    if C_pswd == False:
        result=Checker(p)
        score_dict={0:"Very Weak",1:"Weak",2:"Slightly Weak",3:"Slightly Strong",4:"Strong",5:"Very Strong"}
        
        L4.config(text=f"Your password score is {result}\n\nYour password is {score_dict[result]}")
        
        
    
    

b1=tk.Button(root,text="Check Strength",command=lambda:Check(E1.get()))
b1.pack(pady=5)
b2=tk.Button(root,text='Reset',command=reset)
b2.pack(padx=30,pady=60)
root.mainloop()

