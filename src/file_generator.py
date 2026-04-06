import os
import random
import string

def generate_input_files(filename, k ,length_a, length_b, max_value=20):
    #alphabet size
    k = min(k, 26)

    #choose k unique characters
    alphabet = random.sample(string.ascii_lowercase, k)

    #assign values
    char_values = {c: random.randint(1, max_value) for c in alphabet}

    #generate strings
    A = ''.join(random.choice(alphabet) for _ in range(length_a))
    B = ''.join(random.choice(alphabet) for _ in range(length_b))

    with open(filename, 'w') as f:
        f.write(f"{k}\n")
        for c, v in char_values.items():
            f.write(f"{c} {v}\n")
        f.write(A + "\n")
        f.write(B + "\n")

if __name__ == "__main__":
    #make sure data folder exists
    os.makedirs("data", exist_ok=True)

    #generate 10 files
    for i in range (1, 11):
        length = 25 * i
        filename = f"data/test{i}.in"

        generate_input_files(
            filename=filename,
            k = 5,
            length_a=length,
            length_b=length,
            max_value=20
        )