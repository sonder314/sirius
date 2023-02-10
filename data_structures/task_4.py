#vlad
def download(stack, array, now):
    for i in range(len(array)):
        if array[i] == now:
            stack.append(array[i])
            return stack, array[i + 1::]
        else:
            stack.append(array[i])
    return stack, array[i + 1::]


def top(stack):
    if stack:
        return stack[-1]
    return 0

def delete(stack, array, now):
    while top(stack) == now:
        stack.pop()
        now += 1
    return stack, array, now


def f(array):
    stack = []
    now = 1
    while array:
        stack, array = download(stack, array, now)
        stack, array, now = delete(stack, array, now)
    if stack[::-1] == sorted(stack):
        return 'YES'
    return 'NO'


n = int(input())
array = list(map(int, input().split()))

print(f(array))

#internet
l = int(input())
s = list(map(int, input().split()))
 
tup = [0] # тупик
tr2 = [0] # путь 2
 
for i in range(l):
    while tup[-1] == tr2[-1] + 1:
        tr2.append(tup[-1])
        tup.pop()
    if s[i] == tr2[-1] + 1:
        tr2.append(s[i])
    else:
        tup.append(s[i])
 
while tup[-1] == tr2[-1] + 1:
    tr2.append(tup[-1])
    tup.pop()
 
if tr2[-1] == l:
    print('YES')
else:
    print('NO')