"""num=5
for line in range(num):
    for col in range(num):
        if line==0 or line==num-1 or col==0 or col==num-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()"""



num=5
line=0
while line!=num:
    col=0
    while col!=num:
        if line==0 or line==num-1 or col==0 or col==num-1:
            print("*", end="")
            col+=1
            break
        
        else:
            print(" ",end="")
    else:
        print()
        line+=1
       

        
    
