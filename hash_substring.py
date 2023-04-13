def read_input():
   
    input_type = input().rstrip()
    if input_type == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == 'F':
        with open('input.txt', 'r') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    else:
        raise ValueError('Invalid input type')
    return pattern, text


def print_occurrences(output):
    
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):

    p = len(pattern)
    t = len(text)
    p_hash = sum(ord(pattern[i]) * pow(10, p - i - 1) for i in range(p))
    t_hash = sum(ord(text[i]) * pow(10, p - i - 1) for i in range(p))
    occurrences = []
    for i in range(t - p + 1):
        if p_hash == t_hash:
            if pattern == text[i:i+p]:
                occurrences.append(i)
        if i < t - p:
            t_hash = (t_hash - ord(text[i]) * pow(10, p - 1)) * 10 + ord(text[i+p])
    return occurrences


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

