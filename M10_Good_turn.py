t = int(input())

i = 0
while i < t:
    x, y = map(int, input().split())
    
    if x + y > 6:
        print("YES")
    else:
        print("NO")
        
    i += 1
