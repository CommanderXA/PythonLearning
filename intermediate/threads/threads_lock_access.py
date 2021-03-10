import threading
import time

semaphore = threading.BoundedSemaphore(value=5) # allow only 5 accesses

def access(thread_number):
    print(f"{thread_number} is trying to access.")
    semaphore.acquire()
    print(f"{thread_number} was granted access.")
    time.sleep(5)
    print(f"{thread_number} is now releasing.")
    semaphore.release()

for thread_number in range(10):
    t = threading.Thread(target=access, args=(thread_number,))
    t.start()
    time.sleep(1)
