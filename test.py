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
    # "py_c_rs_call_golang_factorial.py": {
    #     "averageTimes": [],
    #     "totalTimes": [],
    # },
    # "py_go.py": {
    #     "averageTimes": [],
    #     "totalTimes": [],
    # },
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
    "./lib/js/a.out": {
        "averageTimes": [],
        "totalTimes": [],
    },
    "lib/js/factorial.js": {
        "averageTimes": [],
        "totalTimes": [],
    },
    "lib/ruby/index.rb": {
        "averageTimes": [],
        "totalTimes": [],
    }
}


def main():
    global results
    count = 0
    l = {
        "python": [
            "py_c_factorial.py",
            # "py_c_rs_call_golang_factorial.py",
            "py_c_rs_factorial.py",
            "py_cython_factorial.py",
            "py_factorial.py",
            # "py_go.py",
            "py_rs_factorial.py",
            "py_rs_call_zig_factorial.py",
            "py_c_rs_call_zig_factorial.py",
        ],
        "node": [
            "lib/js/factorial.js"
        ],
        "ruby": [
            "lib/ruby/index.rb"
        ]
    }
    # score = {}
    for i in l:
        lists = l[i]
        random.shuffle(lists)
        for j in lists:
            resultTime = []
            for _ in range(10):
                startTime = time.time()
                _ = subprocess.check_output([i, j])
                endTime = time.time() - startTime
                resultTime.append(endTime)
            averageTime = average(resultTime)
            totalTime = sum(resultTime)
            count += 1
            results[j]["averageTimes"].append(averageTime)
            results[j]["totalTimes"].append(totalTime)

    l = [
        "./target/release/factorial",
        "./lib/go/factorial",
        "./lib/test/cpp/factorial",
        "./lib/test/zig/zig-out/bin/factorial",
        "./lib/js/a.out"
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


if __name__ == '__main__':
    for i in range(1):
        main()
    for k in sorted(results, key=lambda x: results[x]["averageTimes"][0]):
        print("----------------------------------------------------")
        print("Name: " + k)
        print(
            "Average time: " + str(average(results[k]["averageTimes"])) + "s")
        print("Total time: " + str(average(results[k]["totalTimes"])) + "s")
        print("----------------------------------------------------")
