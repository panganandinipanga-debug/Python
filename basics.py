num1=10
num2=20
num3=35
num4=15
if num1>num2:
    if num1>num3:
        if num1>num4:
            print("num1 is highest")
        else:
            print("num4 is highest")
    else:
        if num3>num4:
            print("num3 is highes")
        else:
            print("num4 is highest")
else:
    if num2>num3:
        if num2>num4:
            print("num2 is highest")
        else:
            print("num4 is highest")

    else:
        if num3>num4:
            print("num3 is highest")
        else:
            print("num4 is highest")
