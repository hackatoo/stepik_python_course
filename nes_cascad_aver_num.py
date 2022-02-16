a,b,c= int(input()), int(input()), int(input())
if (a < b and b < c) or (a > b and b > c):
    print(b)
elif (a > b and a < c) or (a < b and a > c): 
    print(a)
else: 
    print(c)
