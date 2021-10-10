# Link for the problem 👇
# https://www.codechef.com/OCT21C/problems/MIXTURE

try:
    t = int(input())
    while t:
        a,b = map(int, input().split())
        if a>0 and b>0:
            print("Solution")
        elif b == 0:
            print("Solid")
        elif a == 0:
            print("Liquid")
        t -= 1
except Exception as e:
    pass