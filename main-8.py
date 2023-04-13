import sys

def rabin_karp(pattern, text):
    p_len = len(pattern)
    t_len = len(text)
    p_hash = hash(pattern)
    t_hashes = [hash(text[i:i+p_len]) for i in range(t_len - p_len + 1)]
    indices = [i for i, h in enumerate(t_hashes) if h == p_hash]
    return indices

if __name__ == '__main__':
    input_type = input("Enter input type (I for keyboard, F for file): ")
    if input_type == "I":
        pattern = input("Enter the pattern to search for: ")
        text = input("Enter the text to search in: ")
    elif input_type == "F":
        with open("test.txt") as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    else:
        print("Invalid input type!")
        sys.exit(1)
    indices = rabin_karp(pattern, text)
    for index in indices:
        print(index, end=" ")
    print()


