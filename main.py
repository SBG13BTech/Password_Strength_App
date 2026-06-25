#This is a password strength checker app.

print("Hello!\nWelcome to my console based password strength checking app.")


def common(p):
        with open("Common_Passwords.txt") as f:
            for line in f:
                if p==line.strip():
                    print("The password \"",p,"\" is a common password.\nTry some other password")
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

opt='y'
while opt=='y':
    
    pswd=input("Enter your password:")
    c_pswd=common(pswd)
    if c_pswd==False:
        result=Checker(pswd)
        print("Your password strength score out of 5 is ",result)
        score_dict={0:"Very Weak",1:"Weak",2:"Slightly Weak",3:"Slightly Strong",4:"Strong",5:"Very Strong"}
        print("Your password is ",score_dict.get(result))
    
    opt=input("Do you want to check another password? [y/n]").strip()
print("Thank you")