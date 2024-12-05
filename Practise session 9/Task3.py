class counter:
    count=0
    def __init__(self):
        counter.count+=1
        print(counter.count)

obj1=counter()
obj2=counter()
obj3=counter()