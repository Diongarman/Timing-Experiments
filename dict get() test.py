import timeit
import random

"""a timing experiment that demonstrates
    the dictionary method get() is of O(1) order"""

print("Timing Experiment\n")
print("|size|      |O(1)|\n")

for i in range(10000, 1000001, 20000):
    t = timeit.Timer("x.get(random.randrange(%d))"%i,
                     "from __main__ import random,x")
   

    x = {j: None for j in range(i)}
    get_time = t.timeit(number = 1000)
    print("%d, %10.3f" %(i, get_time))

    
