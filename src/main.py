import sys
from input_parser import input_parser
from solver import hvlcs_solver

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    filename = sys.argv[1]
    char_values, A, B = input_parser(filename)
    max_value, subsequence = hvlcs_solver(char_values, A, B)

    print(max_value)
    print(subsequence)

if __name__ == "__main__":
    main()
