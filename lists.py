N = int(input())
tea = []
for i in range(N):
    command = tea.append(input())
# print(tea)

tea2 = []
for j in tea:
    tea2.append(j.split())
# print(tea2)

output = []
for cmd in tea2:
    if cmd[0] == 'insert':
        output.insert(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == 'print':
        print(output)
    elif cmd[0] == 'remove':
        output.remove(int(cmd[1]))
    elif cmd[0] == 'append':
        output.append(int(cmd[1]))
    elif cmd[0] == 'sort':
        output.sort()
    elif cmd[0] == 'pop':
        output.pop()
    elif cmd[0] == 'reverse':
        output.reverse()
