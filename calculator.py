first = float(input("enter the first value =  "))
dec = float(input("enter the sec value = "))
ope = str (input("enter the operation (+,-,*,/)"))

if ope == '+':
    total = first + dec
elif ope == '-':
    total = first - dec
elif ope == '*':
    total = first * dec
elif ope == '/':
    total = first / dec
elif ope == '%':
    total = first % dec
else:
    print ("wrong operation please enter the crt operator  ")

print (total)