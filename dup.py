l=[1,2,3,1]
l1=[]
for ele in l:
    if ele not in l1:
        l1+=[ele]
        return True
    return False
        
        
