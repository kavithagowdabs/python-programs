try:
    num=int(input("enter the value of num\n"))
    den=int(input("enter the value of den\n"))
    result=num/den
    print("result=",result)
except(ZeroDivisionError):
    den=int(input("pls,enter a new num value\n"))
    result=num/den
    print("result=",result)
