from timeit import Timer


#Timing experiment that shows pop(0) is of O(n) order and pop() is of O(1)

popzero = Timer("x.pop(0)",
                "from __main__ import x")
popend = Timer("x.pop()",
               "from __main__ import x")
print("pop(0)   pop()")
for i in range(1000000,100000001,1000000):
    x = list(range(i))
    pt = popend.timeit(number=1000)
    x = list(range(i))
    pz = popzero.timeit(number=1000)
    print("%7.5f, %7.5f" %(pz,pt))
