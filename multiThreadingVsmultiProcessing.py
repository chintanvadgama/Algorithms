import multiprocessing
import threading
import time

tests = ["test1", "test2", "test3"]

# simple execution
start = time.time()
for test in tests:
    print(test)
    time.sleep(5)
end = time.time()

print("Total Time Serial Execution = {}".format(end-start))


# Multi Threading
