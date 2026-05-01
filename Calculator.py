#Calculator program


def add(x,y) :
    return x+y

def sub(x,y) :
    return x-y

def mul(x,y) :
    return x*y

def div(x,y) :
    return x/y

def calculate(num1,num2,op) :
    if op == "+" :
        a=add(num1,num2)
        print(f"The sum of {num1} and {num2} is {a:.2f}")
    elif op == "-" :
        b=sub(num1,num2)
        print(f"The difference of {num1} and {num2} is {b:.2f}")
    elif op == "*" :
        c= mul(num1,num2)
        print(f"The product of {num1} and {num2} is {c:.2f}")
    elif op == "/" :
        if num2 == 0 :
            print("Zero division error occurs, kindly recheck the values.")
        else :
            d=div(num1,num2)
            print(f"The division of {num1} and {num2} is {d:.2f}")


while True :
    num1=float(input("Enter number 1:"))
    num2=float(input("Enter number 2:"))
    op=input("Choose an operator (+-*/) :")
    while True :
        if op not in "+-*/" :
            print("Invalid operator..")
            op=input("Choose an operator (+-*/) :")
        else :
            break
    calculate(num1,num2,op)
    ch=input("Do you want to continue..? (y/n) :")
    if ch == "y" :
        continue
    else :
        print("Thank you...")
        break

