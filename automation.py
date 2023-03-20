bits = True
while bits != False:
    x1input = int(input("X1: "))
    y1input = int(input("Y1: "))
    x2input = int(input("X2: "))
    y2input = int(input("Y2: "))
    xdiff = x2input - x1input
    ydiff = y2input - y1input
    print(f"Wall({x1input},{y1input},{xdiff},{ydiff},color)")
    done = input("(y/n): ").lower()
    if done == "n":
        bits = False