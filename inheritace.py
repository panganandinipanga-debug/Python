class wv1:
    a=10
    b=20

class wv2:
    c=20

class wv3(wv1,wv2):
    d=15
obj=wv3()
print(wv3.a)
