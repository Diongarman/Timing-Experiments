	
import timeit
import random


#Test experiment that displays the "in" method speed in a list is O(n) vs the
#Same method in a dictionary that is O(1)

print("Timing Experiment: 'in' method of list vs dict\n")
print("|size|   |O(n)|     |O(1)|\n")

for i in range(10000,1000001,20000):
    t = timeit.Timer("random.randrange(%d) in x"%i,
                     "from __main__ import random,x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j:None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))
