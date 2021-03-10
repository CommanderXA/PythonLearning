'''

    Using Threads you can execute two functions 
    at the same time. THey will work parallel.

'''

import threading

def function1():
    for _ in range(10):
        print("ONE")

def function2():
    for _ in range(10):
        print("TWO")

t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)

t1.start()
t1.join() # Doesn't allow to execute other code. It will wait until function1 will be executed

t2.start()

print("test")