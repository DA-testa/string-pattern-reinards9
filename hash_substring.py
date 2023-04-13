def read_input():
    # this function needs to acquire input from keyboard
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    return input().rstrip(), input().rstrip()

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurrences using Rabin Karp algorithm
    p = 1000000007
    x = 1
    result = []
    pattern_hash = poly_hash(pattern, p, x)
    n = len(text)
    m = len(pattern)
    h = [0] * (n - m + 1)
    s = text[n-m:]
    h[n-m] = poly_hash(s, p, x)
    y = pow(x, m, p)
    for i in range(n-m-1, -1, -1):
        h[i] = (x * h[i+1] + ord(text[i]) - y * ord(text[i+m])) % p
    for i in range(n - m + 1):
        if pattern_hash != h[i]:
            continue
        if text[i:i+m] == pattern:
            result.append(i)
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))


