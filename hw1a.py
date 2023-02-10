troom, tcond = list(map(int, input().split()))
mode = input()

if mode == 'heat':
    if tcond >= troom:
        print(tcond)
    else:
        print(troom)
elif mode == 'freeze':
    if tcond <= troom:
        print(tcond)
    else:
        print(troom)
elif mode == 'auto':
    print(tcond)
elif mode == 'fan':
    print(troom)
