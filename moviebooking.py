def singleton(arg):
    L=[]
    def inner():
        if len(L)==0:
            obj = arg()
            L.append(obj)
        return L(0)
    return inner
@singleton
class movie1():
    def __init__(self):
        self.seats = 200
    def booking(self):
        print(f'available seats:{self.seats}')
        tickets=int(input('enter the no. of  tickets'))
        if 0 < tickets <= 200:
            self.seats -= tickets
            print('tickets booked successfully')
        else:
            print('invalid tickets')
@singleton
class movie2():
    def __init__(self):
        self.seats = 250
    def booking(self):
        print(f'available seats:{self.seats}')
        tickets=int(input('enter the no. of  tickets'))
        if 0 < tickets <= 200:
            self.seats -= tickets
            print('tickets booked successfully')
        else:
            print('invalid tickets')
@singleton
class movie3():
    def __init__(self):
        self.seats = 200
    def booking(self):
        print(f'available seats:{self.seats}')
        tickets=int(input('enter the no. of  tickets'))
        if 0 < tickets <= 200:
            self.seats -= tickets
            print('tickets booked successfully')
        else:
            print('invalid tickets')
def BmyS():
    print('1)movie1 \n2)movie2 \n3)movie3')
    selection = int(input('select the movie name to watch'))
    if selection == 1:
        user = movie1()
        user.booking()
    elif selection == 2: 
        user=movie2()
        user.booking()
    elif selection == 3:
        user = movie3()
        user3.booking()
    else:
        print('invalid option')
def paytm():
    print('1)movie1 \n2)movie2 \n3)movie3')
    selection = int(input('select the movie name to watch:'))
    if selection == 1:
        user = movie1()
        user.booking()
    elif selection == 2: 
        user=movie2()
        user.booking()
    elif selection == 3:
        user = movie3()
        user3.booking()
    else:
        print('invalid option')
cus1 = paytm()
print('-----------')
cus2 = BmyS()
print('-----------')
cus3 = paytm()
print('-----------')
