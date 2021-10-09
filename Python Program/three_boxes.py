try:
    t = int(input())
    while t:
        a,b,c,d = map(int, input().split())
        if (a+b+c <= d):
            print("1")
        elif (a+b <= d) or (b+c <= d) or (a+c <= d):
            print("2")
        elif ((a == d) or (b == d) or (c == d)) and ((a+b <= d) or (b+c <= d) or (a+c <= d)):
            print("2")
        else:
            print("3")
        t -= 1
except Exception as e:
    pass