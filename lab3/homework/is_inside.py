def is_inside(a, b):
    if b[0] + b[2] >= a[0] >= b[0] and b[1] + b[3] >= a[1] >= b[1]:
        return(True)
    else:
        return(False)

s = 50

if is_inside([200, 120], [140, 60, 100, 200]):
    print(s)



