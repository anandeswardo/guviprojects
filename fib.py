#anand
num = int(input())
first = 0
second = 1
print(second, end=" ")
for i in range(2, num+1):
    next = first + second
    print(next, end=" ")
    first = second
    second = next
