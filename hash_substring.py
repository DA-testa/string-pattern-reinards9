def rabin_karp(text, pattern):
    t_len = len(text)
    p_len = len(pattern)
    p_hash = hash(pattern)
    t_hash = hash(text[:p_len])
    positions = []

    for i in range(t_len - p_len + 1):
        if p_hash == t_hash and pattern == text[i:i + p_len]:
            positions.append(str(i))

        if i < t_len - p_len:
            t_hash = hash(text[i + 1:i + p_len + 1])

    return " ".join(positions)


def main():
    pattern = input("Enter the pattern: ").strip()
    text = input("Enter the text: ").strip()
    positions = rabin_karp(text, pattern)
    print("Occurrences of the pattern at positions:", positions)


if __name__ == '__main__':
    main()


