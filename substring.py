def count_substring(string, sub_string):
    count = sum(1 for i in range(len(string)) 
         if string.startswith(sub_string, i))
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)