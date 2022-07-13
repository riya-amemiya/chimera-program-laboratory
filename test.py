import random
import subprocess
import time


def average(numbers):
    return sum(numbers) / len(numbers)


results = {
    "py_c_factorial.py": {
        "averageTimes": [],
        "totalTimes": [],
    },
    "py_c_rs_call_zig_factorial.py": {
        "averageTimes": [],
        "totalTimes": [],
    },
    "py_c_rs_factorial.py": {
        "averageTimes": [],
        "totalTimes": [],
    },
    "py_cython_factorial.py": {
        "averageTimes": [],
        "totalTimes": [],
    },
    "py_factorial.py": {
        "averageTimes": [],
        "totalTimes": [],
    },
    "py_rs_factorial.py": {
        "averageTimes": [],
        "totalTimes": [],
    },
    "py_rs_call_zig_factorial.py": {
        "averageTimes": [],
        "totalTimes": [],
    },
    "./target/release/factorial": {
        "averageTimes": [],
        "totalTimes": [],
    },
    "./lib/go/factorial": {
        "averageTimes": [],
        "totalTimes": [],
    },
    "./lib/cpp/a.out": {
        "averageTimes": [],
        "totalTimes": [],
    },
    "./lib/test/zig-out/bin/lib": {
        "averageTimes": [],
        "totalTimes": [],
    },
}


def main():
    global results
    l = [
        "py_c_factorial.py",
        # "py_c_rs_call_golang_factorial.py",
        "py_c_rs_factorial.py",
        "py_cython_factorial.py",
        "py_factorial.py",
        # "py_go.py",
        "py_rs_factorial.py",
        "py_rs_call_zig_factorial.py",
        "py_c_rs_call_zig_factorial.py",
    ]

    random.shuffle(l)
    score = {}
    count = 0
    for i in l:
        resultTime = []
        for _ in range(10):
            startTime = time.time()
            _ = subprocess.check_output(["python", i])
            endTime = time.time() - startTime
            resultTime.append(endTime)
        averageTime = average(resultTime)
        totalTime = sum(resultTime)
        count += 1
        results[i]["averageTimes"].append(averageTime)
        results[i]["totalTimes"].append(totalTime)

    l = [
        "./target/release/factorial",
        "./lib/go/factorial",
        "./lib/cpp/a.out",
        "./lib/test/zig-out/bin/lib"
    ]

    random.shuffle(l)

    for i in l:
        resultTime = []
        for _ in range(10):
            startTime = time.time()
            _ = subprocess.check_output([i])
            endTime = time.time() - startTime
            resultTime.append(endTime)
        averageTime = average(resultTime)
        totalTime = sum(resultTime)
        count += 1
        results[i]["averageTimes"].append(averageTime)
        results[i]["totalTimes"].append(totalTime)

    # try:
    #     with open("./score.csv", mode="x") as f:
    #         f.write("name,averageTime,totalTime,count\n")
    # except:
    #     pass


if __name__ == '__main__':
    for i in range(10):
        main()
    for k in sorted(results, key=lambda x: results[x]["averageTimes"][0]):
        print("----------------------------------------------------")
        print("Name: " + k)
        print("Average time: " + str(average(results[k]["averageTimes"])))
        print("Total time: " + str(average(results[k]["totalTimes"])))
        print("----------------------------------------------------")
