def swap_case(s):
    new_str = ""
    for i in range(0, len(s)):
        if s[i].islower():
            new_str += s[i].upper()
        elif s[i].isupper():
            new_str += s[i].lower()
        else:
            new_str += s[i]
    return new_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)