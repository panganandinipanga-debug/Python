"""digits=[9]
s=''
l=[]
out=0
num=''
for ele in digits:
    s+=str(ele)
out+=int(s)+1
num=str(out)
for ele in num:
    l+=[int(ele)]
print(l)"""



#------------check strings are equivalent or not---------


"""word=["ab","c"]
word1=["ab","bc"]
if ''.join(word)==''.join(word1):
    print(True)
else:
    print(False)"""


#------------increment large increment by one---------
"""digits=[1,2,3]
s=''
l=[]
out=0
num=''
for ele in digits:
    s+=str(ele)
out=int(s)+1
num=str(out)
for ele in num:
    l+=[int(ele)]
print(l)"""


#------------------pallindrome------------
"""num=121
sum=0
temp=num
while num!=0:
    ld=num%10
    sum=sum*10+ld
    num//=10
if sum==temp:
    print("pallindrome")
else:
    print("not pallindrome")"""


#---------------prime number--------------
"""num=23
val=1
count=0
for val in range(1,num+1):
    if num%val==0:
        count+=1
if count==2:
    print("prime number")
else:
    print("not a prime number")"""

     #-----using for loop----------
"""num=25
count=0
for val in range(1,num+1):
    if num%val==0:
        count+=1

if count==2:
    print("prime number")
else:
    print("not a prime number")"""

#------------perfect square---------------
"""num=25
val=1
while val!=num+1:
    if val*val==num:
        print("perfect square")
        break
    val+=1
else:
    print("not a perfect square")"""

#-------------dissarum number-------------
"""num=125
sum=0
temp=num
length=len(str(num))
while num!=0:
    ld=num%10
    sum+=ld**length
    length-=1
    num//=10
if sum==temp:
    print("dissarum number")
else:
    print("not a dissarum number")"""

#--------------armstrong-----------------
'''num=153
sum=0
length=len(str(num))
temp=num
while num!=0:
    ld=num%10
    sum=sum+ld**length
    num//=10
if sum==temp:
    print("armstrong")
else:
    print("not armstrong")'''


#-----------fascinating number------------
"""num=192
res=str(num*1)+str(num*2)+str(num*3)
for val in range(1,10):
    if str(val) not in res:
        print("not fascinating number")
        break
else:
    print("fascinating number")"""


#------------EMIRP number-------------------
num=13
sum=0

temp=num
while num!=0:
    ld=num%10
    sum=sum*10+ld
    num//=10
if sum!=temp:
    count=0
    val=1
    while val!=temp+1:
        if temp%val==0:
            count+=1
        val+=1
    if count==2:
        count=0
        val=1
        while val!=temp+1:
            if temp%val==0:
                count+=1
            val+=1
        if count==2:
            print("EMIRP number")
        else:
            print("not EMIRP number")

    else:
        print("not EMIRP number")
else:
    print("not EMIRP number")
            

        
    
    






