def rabin_karp(pattern, text):
    p_len = len(pattern)
    t_len = len(text)
    p_hash = hash(pattern)
    t_hashes = [hash(text[i:i+p_len]) for i in range(t_len - p_len + 1)]
    indices = [i for i, h in enumerate(t_hashes) if h == p_hash and text[i:i+p_len] == pattern]
    return indices

if __name__ == '__main__':
    pattern = input().strip()
    text = input().strip()
    indices = rabin_karp(pattern, text)
    for index in indices:
        print(index, end=' ')



