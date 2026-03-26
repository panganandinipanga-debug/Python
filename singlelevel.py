class v1:
    def __init__(self,num1):
        self.num1=num1
class v2(v1):
    def __method__(self,num1):
        super().__init__(num1)
obj=v1(10)
print(obj.num1)
