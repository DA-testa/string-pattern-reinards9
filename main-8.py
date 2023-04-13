import sys

def rolling_hash(s, p):
    d = 256  # number of possible characters
    q = 101  # prime modulus
    h = pow(d, p-1, q)  # h = d^(p-1) mod q
    t = 0
    p_hash = sum(ord(p[i]) * pow(d, p-1-i, q) for i in range(p))
    for i in range(p):
        t = (d*t + ord(s[i])) % q
    indices = []
    for i in range(len(s)-p+1):
        if p_hash == t and s[i:i+p] == p:
            indices.append(i)
        if i < len(s)-p:
            t = (d*(t-ord(s[i])*h) + ord(s[i+p])) % q
    return indices

def rabin_karp(pattern, text):
    return rolling_hash(text, pattern)

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


