# def format_name(first,second):
#     print(first.title())
#     print(second.title())
# format_name("tilak","datla")
#


def sum(a,b):
    print(a,"+",b,"=",a+b)
def sub(a,b):
    print(a, "-", b, "=", a - b)
def mult(a,b):
    print(a, "*", b, "=", a * b)
def dev(a,b):
    print(a, "/", b, "=", a / b)

while True:
    a=float(input("What's the first number?:"))
    s=input("+ - / *\n")
    if s=="+":
        b=float(input("what's second number: "))
        sum(a,b)
    elif s=="-":
        b = float(input("what's second number: "))
        sub(a,b)
    elif s=="*":
        b = float(input("what's second number: "))
        mult(a,b)
    elif s=="/":
        b = float(input("what's second number"))
        dev(a,b)
    else:
        print("enter valide choice")

    type=input("Type 'y' to continue and 'n' for stop").lower()
    if type=="y":
        pass
    elif type=="n":
        break
    else:
        print("enter valide choice")

















































