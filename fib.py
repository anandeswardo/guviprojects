#anand
num = int(input())
 first = 0
second = 1
print(first, second, end=" ")
for i in range(2, num):
    next = first + second
    print(next, end=" ")
    first = second
    second = next
