import time
import os
import matplotlib.pyplot as plt
from input_parser import input_parser
from solver import hvlcs_solver

def runtime_timer(char_values, A, B, runs=3):
    total = 0
    for _ in range(runs):
        start = time.perf_counter()
        hvlcs_solver(char_values, A, B)
        end = time.perf_counter()
        total += (end - start)
    return total/runs

def main():
    data_dir = "data"

    files = sorted(
        [f for f in os.listdir(data_dir) if f.endswith(".in")],
        key = lambda x: int(x.replace("test", "").replace(".in", "")))
    
    lengths = []
    runtimes = []

    print(f"{'File':<15} {'Length':<10} {'Runtime (s)':<15}")
    print("-" * 45)

    for filename in files:
        filepath = os.path.join(data_dir, filename)
        char_values, A, B = input_parser(filepath)
        length = len(A)

        runtime = runtime_timer(char_values, A, B)

        lengths.append(length)
        runtimes.append(runtime)

        print(f"{filename:<15} {length:<10} {runtime:<15.6f}")

    #plot/make graph
    plt.figure()
    plt.plot(lengths, runtimes, marker='o')
    plt.xlabel("Input String Length")
    plt.ylabel("Runtime (seconds)")
    plt.title("HVLCS Runtime vs Input Size")
    plt.grid()
    plt.savefig("runtime_graph.png")
    plt.show()

if __name__ == "__main__":
    main()