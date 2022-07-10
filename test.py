import random
import subprocess
import time


def average(numbers):
    return sum(numbers) / len(numbers)


l = [
    "py_c_factorial.py",
    "py_c_rs_call_golang_factorial.py",
    "py_c_rs_factorial.py",
    "py_cython_factorial.py",
    "py_factorial.py",
    "py_go.py",
    "py_rs_factorial.py",
]

random.shuffle(l)

for i in l:
    resultTime = []
    print("----------------------------------------------------")
    print("Testing: " + i)
    for _ in range(10):
        startTime = time.time()
        _ = subprocess.check_output(["python", i])
        endTime = time.time() - startTime
        resultTime.append(endTime)
    print("Average time: " + str(average(resultTime)))
    print("Total time: " + str(sum(resultTime)))
    print("----------------------------------------------------")
