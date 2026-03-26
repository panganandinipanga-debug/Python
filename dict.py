num=4
spaces=num-1
stars=1
for line in range(1,num+1):
    for sp in range(spaces):
        print('',end='')
        for st in range(stars):
            print('*',end='')
    print()
    spaces=spaces-1
    stars+=2
