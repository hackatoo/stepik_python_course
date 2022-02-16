i=int(input())
a = i // 1000
b = (i % 1000) // 100
c = i % 100 // 10
d = i % 10

if (a + d) == (b - c):
    print('ДА')
else:
    print('НЕТ')
