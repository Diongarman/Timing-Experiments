import random
import time

names = ["Ricky", "Joe", "Anna", "Serena", "Rachel", "Tom"]
subjects = ["Mathematics", "Engineering", "Physics", "Computer Science", "Philosophy"]


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {"id":i, "name": random.choice(names), "major": random.choice(subjects)}

        result.append(person)

    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {"id":i, "name": random.choice(names), "major": random.choice(subjects)}

        yield person


#The script below is a time comparison experiment between the function and generator.
#Uncomment the script calling each function or generator, testing one at a time.

#time_start = time.time()
#people = people_list(1000000)
#time_stop = time.time()


time_start = time.time()
people = people_generator(1000000)
time_stop = time.time()


print ("Test took %f Seconds" % (time_stop-time_start))


#Results: The generator test should be about 1.4 million times faster than the
#Function test here.


