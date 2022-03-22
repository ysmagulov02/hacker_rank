# if __name__ == '__main__':
n = int(input())
arr = map(int, input().split())
biggest = next_biggest = -101

arr_sorted = sorted(arr, reverse = True)

tea = []
for i in arr_sorted:
    if i != max(arr_sorted):
        tea.append(i)
    continue

print(tea[0])

